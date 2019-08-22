---
title: Virtual channel analysis of epilepsy MEG data - Case 1
tags: [tutorial, meg-epilepsy]
---

### Analysis of the CTF dataset

#### Coregistration of the anatomical MRI

The original MRI that is provided for this patient has been partially processed with the CTF software and MRIcro, and is stored in NIFTI format. Read the MRI and check the coregistration.

    mri_orig = ft_read_mri('case1.mri');

    headshape = ft_read_headshape('case1.pos');
    headshape = ft_convert_units(headshape, 'mm');

    ft_determine_coordsys(mri_orig, 'interactive', 'no')
    ft_plot_headshape(headshape);

In this case the coregistration is already nearly perfect.

{% include image src="/assets/img/tutorial/epilepsy/case1a-coreg.png" width="400" %}

Usually you would start with an anatomical MRI (e.g. stored as a stack of DICOM files) that is not yet coregistered with the MEG. We will improve the coregistration a bit, using the same procedure you could use to coregister from scratch.

The coregistration procedure starts with a coarse manual coregistration, followed by an automatic fine coregistration in which the skin surface from the MRI is fitted to the headshape points.

    cfg = [];
    cfg.method = 'headshape';
    cfg.headshape.interactive = 'yes';
    cfg.headshape.icp = 'yes';
    cfg.headshape.headshape = headshape;
    cfg.coordsys = 'ctf';
    mri_realigned = ft_volumerealign(cfg, mri_orig);

{% include image src="/assets/img/tutorial/epilepsy/case1a-coreg-manual.png" width="400" %}

The headshape not only covers the scalp, but also the face and nose. Hence the coregistration needs to be done prior to defacing from the anatomical MRI. The translate, rotate and scale parameters specified here were determined experimentally in the graphical user interface of the **[ft_defacevolume](/reference/ft_defacevolume)** function.

    cfg = [];
    cfg.translate = [100 0 -60];
    cfg.rotate = [-4 30 0];
    cfg.scale = [75 150 120];
    mri_defaced = ft_defacevolume(cfg, mri_realigned);

    save mri_defaced.mat mri_defaced  % save the data for sharing

{% include image src="/assets/img/tutorial/epilepsy/case1a-deface.png" width="400" %}

{% include image src="/assets/img/tutorial/epilepsy/case1a-deface_result.png" width="400" %}

    cfg = [];
    mri_resliced = ft_volumereslice(cfg, mri_defaced);

    save mri_resliced.mat mri_resliced  % save the data for sharing

Finally we should do a visual inspection of the realigned, defaced and resliced MRI.

    cfg = [];
    ft_sourceplot(cfg, mri_resliced)

{% include image src="/assets/img/tutorial/epilepsy/case1a-resliced.png" width="400" %}

Note that the patients head is tilted to the right relative to the coordinate axes. Apparently the anatomical landmarks at the left and right ear were not clicked symmetrically with the Polhemus. This is not a problem for further processing, as long as we remember that results are expressed in head coordinates relative to the anatomical landmark of this specific recording.

#### Importing and filtering the channel level data

    dataset = 'case1.ds';

    cfg = [];
    cfg.dataset   = dataset;
    cfg.hpfilter  = 'yes';
    cfg.hpfreq    = 10;
    cfg.lpfilter  = 'yes';
    cfg.lpfreq    = 70;
    cfg.channel   = 'MEG';
    cfg.coilaccuracy = 1; % ensure that sensors are expressed in SI units
    data = ft_preprocessing(cfg);

#### Construction of the volume conduction model of the head

We will use the defaced MRI, which has been realigned with the CTF system and resliced.

    mri = ft_read_mri('mri_defaced.mat');

Segment the brain compartment from the anatomical MRI and make the volume conduction model. If you want, you could save the head model to disk.

    cfg = [];
    cfg.tissue = 'brain';
    seg = ft_volumesegment(cfg, mri);

    % save seg seg

    cfg = [];
    cfg.tissue = 'brain';
    brain = ft_prepare_mesh(cfg, seg);

    cfg = [];
    cfg.unit = 'm'; % ensure that the headmodel is expressed n SI units
    cfg.method = 'singleshell';
    headmodel = ft_prepare_headmodel(cfg, brain);

    % save headmodel headmodel

#### Construction of the source model

To save time we have chosen to use a 7 mm grid for the source model here, but in a real clinical scenario a grid of 5 mm or smaller would typically be used.

    cfg = [];
    cfg.resolution = 0.007;
    cfg.unit = 'm'; % ensure that the sourcemodel is expressed n SI units
    cfg.headmodel = headmodel;
    cfg.grad = data.grad; % this being needed here is a silly historical artifact
    sourcemodel_grid = ft_prepare_sourcemodel(cfg);

Finally we plot everything out and check that it is all aligned correctly.

    figure
    ft_plot_headmodel(headmodel, 'unit', 'mm');
    ft_plot_sens(data.grad, 'unit', 'mm', 'coilsize', 10, 'chantype', 'meggrad');
    ft_plot_mesh(sourcemodel_grid.pos, 'unit', 'mm');
    ft_plot_ortho(mri_resliced.anatomy, 'transform', mri_resliced.transform, 'style', 'intersect', 'unit', 'mm');
    alpha 0.5

{% include image src="/assets/img/tutorial/epilepsy/case1a_head.png" width="400" %}

In the following stage, we compute the data covariance matrix for the beamformer source reconstruction. We use the **[ft_timelockanalysis](/reference/ft_sourceanalysis)** function (more commonly used elsewhere to compute an average), and because we have not defined individual trials within the data it will produce the covariance matrix for the whole time period of the data.

    cfg = [];
    cfg.channel = 'MEG';
    cfg.covariance = 'yes';
    cov_matrix = ft_timelockanalysis(cfg, data);

Next we precompute the leadfields, which is not obligatory, but speeds up the subsequent step.

    cfg = [];
    cfg.channel = 'MEG';
    cfg.headmodel  = headmodel;
    cfg.sourcemodel = sourcemodel_grid;
    cfg.normalize = 'yes';  % normalization avoids power bias towards centre of head
    leadfield = ft_prepare_leadfield(cfg, cov_matrix);

Now we compute the LCMV beamformer and reconstruct the time series at each of the locations specified in the source model grid. By projecting the vector dipole moment (for x, y, and z direction) in the direction of maximal power, the source time series becomes a simple vector. The **[ft_sourceanalysis](/reference/ft_sourceanalysis)** function can compute the kurtosis of this time series.

    cfg = [];
    cfg.headmodel  = headmodel;
    cfg.sourcemodel = leadfield;
    cfg.method = 'lcmv';
    cfg.lcmv.projectmom = 'yes';  % project dipole time series for each dipole in direction of maximal power (see below)
    cfg.lcmv.kurtosis = 'yes';    % compute kurtosis at each location
    source = ft_sourceanalysis(cfg, cov_matrix);

#### Explore the outputs

We are ready to explore the results visually, starting with the volumetric images. First of all we need to interpolate the kurtosis on the resliced MRI, then we can plot the images.

    cfg = [];
    cfg.parameter = 'kurtosis';
    source_interp = ft_sourceinterpolate(cfg, source, mri_resliced);

    cfg = [];
    cfg.funparameter = 'kurtosis';
    cfg.method = 'ortho'; % orthogonal slices with crosshairs at peak (default anyway if not specified)
    ft_sourceplot(cfg, source_interp);

    cfg = [];
    cfg.funparameter = 'kurtosis';
    cfg.method = 'slice';  % plot a series of slices
    ft_sourceplot(cfg, source_interp);

    {% include image src="/assets/img/tutorial/epilepsy/case1a_result.png" width="400" %}
    {% include image src="/assets/img/tutorial/epilepsy/case1a_slices.png" width="400" %}

At this stage, we can also write out our images (i.e., the resliced MRI and the kurtosis image that we just made) into NIFTI format so they can be imported into other software that may be more prevalent in clinical settings and merged with other clinical information.

    cfg = [];
    cfg.filename = 'Case1_resliced_anatomy.nii'
    cfg.parameter = 'anatomy';
    cfg.format = 'nifti';
    ft_volumewrite(cfg, mri_resliced);

    cfg = [];
    cfg.filename = 'Case1_kurtosis.nii';
    cfg.parameter = 'kurtosis';
    cfg.format = 'nifti';
    ft_volumewrite(cfg, source);

Returning to our images in FieldTrip, we can scroll through the slices to see where the areas of high kurtosis fall. But to be more objective, it is useful to identify each discrete peak location in the kurtosis data. This can be done using the [imregionalmax](https://nl.mathworks.com/help/images/ref/imregionalmax.html) function from the Image Processing toolbox. An alternative is to use a 3rd party function called [findpeaksn.m](https://github.com/vigente/gerardus/blob/master/matlab/PointsToolbox/findpeaksn.m) which needs to be downloaded separately and added to the MATLAB path. The Aston clinical team would typically examine every single peak but for simplicity we will just look at the top few. We display the co-ordinates and plot some images.

    % we need to input a 3d array instead of a 1 x n voxels array.
    % ispeak = findpeaksn(reshape(source.avg.kurtosis, source.dim));
    ispeak = imregionalmax(reshape(source.avg.kurtosis, source.dim), 6); % use 6 neighbours in 3-D, instead of the default 26

    j = find(ispeak(:));
    [m, i] = sort(-source.avg.kurtosis(j));  % sort on the basis of kurtosis value
    peaks = j(i);
    disp(source.pos(peaks(1:20),:));  % output the positions of the top 20 peaks

    % plot out the top 5 sources
    for i = 1:5,
        cfg = [];
        cfg.funparameter = 'kurtosis';
        cfg.location = source.pos(peaks(i),:);
        ft_sourceplot(cfg, source_interp);
    end

(In this complicated case study, the peak that falls near the glioma is quite far down the list, shown in this image)
{% include image src="/assets/img/tutorial/epilepsy/case1a_nearlesion.png" width="400" %}

#### Visualize the beamformer time series in AnyWave

It is also clinically important to visualize the spikes that are contributing to the kurtosis images, not least to screen out any spurious sources which may be elicited by artifacts. To do this, it is useful to have the original sensor data visible alongside the source time series. Marking the timepoints at which spikes occur at the sources can help the clinician scroll more easily through the data. We will write the data to a format that can be read by the open-source package [AnyWave](http://meg.univ-amu.fr/wiki/AnyWave), which is well-suited to this purpose.

When we read in the data earlier, we filtered it, but here it is more useful to have the unfiltered data. So we import that to FieldTrip and then append source time series data, adding header information for this, before writing the whole lot to the AnyWave ADES file format.

    cfg = [];
    cfg.dataset = dataset;
    cfg.channel = 'MEG';
    data = ft_preprocessing(cfg);
    dat = ft_fetch_data(data);
    hdr = ft_fetch_header(data);

    % then append the source hdr and data to the channel hdr and data.
    nsources = 10;  % for simplicity here we just append the top 10 source time series.
    for i = 1:nsources
        dat(size(dat,1)+1,:)= source.avg.mom{peaks(i),:}*10e5; % see note below about scaling
        hdr.label{end+1}= ['S' num2str(i)];
        hdr.chantype{end+1} = 'source';
        hdr.chanunit{end+1} = ''; % see note below about scaling
    end
    hdr.nChans = hdr.nChans+nsources;

    % write to files
    ft_write_data('Case1_timeseries', dat, 'header', hdr, 'dataformat', 'anywave_ades');

Finally we can automatically mark potential spikes in the source time series data and create labels in AnyWave marker file format. We use the convention (from the original CTF SAMg2 software) of placing a marker wherever the source time series exceeds 6 standard deviations of its mean. In our marker file, there is one label for each source, so events on the marker labelled 'S1' correspond to spikes on the time series from peak number 1 in the image. Marker 'S2' indicates events occurring at peak number 2, etc., etc.

    fid = fopen('Case1_timeseries.mrk', 'w');
    fprintf(fid,'%s\r\n','// AnyWave Marker File ');
    % loop through sources and times
    k = 1;
    for i = 1:nsources
        dat = source.avg.mom{peaks(i),:};
        sd = std(dat);
        tr = zeros(1,length(dat));
        tr(dat>6*sd)=1;
        [tmp,mrksample] = findpeaks(tr, 'MinPeakDistance', 300); % peaks have to be separated by 300 sample points to be treated as separate

        for j = 1:length(mrksample)
            fprintf(fid, '%d\t', k);                          % marker name (just a number)
            fprintf(fid, '%d\t', dat(mrksample(j)));          % marker value
            fprintf(fid, '%d\t',source.time(mrksample(j)) );  % marker time
            fprintf(fid, '%d\t', 0);                          % marker duration
            fprintf(fid, 'S%d\r\n', i);                       % marker channel
            k = k + 1;
        end
    end
    fclose(fid);

The data can now be opened in AnyWave. Once the file is opened, to see sources alongside source data, click 'Add View' in the top/middle toolbar. Then use the eyeball icon to set each view so that one has 'MEG' and one has 'SOURCE' data. Set the timescale to be 0.3 sec/cm (close to the clinical standard 3cm/sec) and scale the amplitudes appropritely. Use the menu to import the marker file that we just created.

The ABC clinicians examined the source data alongside other information including anatomical imaging of the lesion in the left parietal lobe, and seizure semiology, and their observations were followed up by the surgical with corticography in the zone surrounding the lesion. Surgery in the area surrounding the lesion resulted in a significant reduction in seizures for the patient. The data are several years old and nowadays SEEG would be the normal follow-up procedure subsequent to neuroimaging.

### Analysis of the MEGIN dataset

The MEGIN (formerly 'Elekta' or 'Neuromag') dataset was collected from the same patient on the same day as the CTF dataset described above. So, we expect the results to be very similar to those yielded by the CTF data.

Generally the analysis of MEGIN data is almost identical to the analysis of CTF data. So this part of the tutorial has fewer comments than above. However there is one important difference, related to the processing of Maxfiltered data, which is addressed in more detail in the relevant tutorial sections below. Maxfilter is MEGIN's proprietary pre-processing system which offers some improvements in signal-to-noise ratio and artifact handling, and potential for head movement correction. Importantly it is obligatory in datasets where active shielding ('MaxShield') was used during data collection and indeed the epilepsy data used here required preprocessing with Maxfilter for this reason. But Maxfilter has effects on the data covariance which can cause problems in accurately computing the beamformer source model. Some ways to optimise the beamformer calculations to avoid these problems are demonstrated below.

#### Coregistering the data

For patient confidentiality we only include here the MRI which has already been coregistered with the data, defaced, and resliced to align it to the data head co-ordinate system. The process for coregistration is identical to the one described above, except that in the MEGIN file system the polhemus head shape points are stored in the raw data file. When we reslice this MRI, it becomes aligned with the MEGIN co-ordinate system (RAS) which means that slice images are shown in a different set of orientations to the CTF data that has been aligned to its own co-ordinate system (see the following [tutorial](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined/) for more details).

    load mri_coreg_resliced.mat
    cfg = [];
    ft_sourceplot(cfg, mri_resliced)

#### Importing and filtering the sensor level data

MEGIN MEG data has two channel types, but we are only going to import the gradiometer data for now. We apply the same 10-70 Hz bandpass filter as for the CTF analysis. In this dataset, the head coils are switched on after 20 seconds of recording, which causes a filter artifact, so we omit the first 20 seconds of data by specifying a single 'trial' from 21 seconds until the end of the recording.

    dataset = 'case1_cHPI_raw_trans_sss.fif'
    cfg = [];
    cfg.dataset   = dataset;
    cfg.hpfilter  = 'yes';
    cfg.hpfreq    = 10;
    cfg.lpfilter  = 'yes';
    cfg.lpfreq    = 70;
    cfg.channel   = 'meggrad';
    cfg.trl = [21*2000 255000 0];  % omit the first 20 seconds (numbers based on pre-screening of data)
    data = ft_preprocessing(cfg);

    data.grad   = ft_convert_units(data.grad, 'm');

#### Construction of the volume conduction model of the head

This is exactly the same as for the CTF data.

    mri = ft_read_mri('mri_coreg_resliced.mat');

    % segment the brain from the mri
    cfg = [];
    cfg.tissue = 'brain';
    seg = ft_volumesegment(cfg, mri);

    % extract surface mesh of the brain for the headmodel
    cfg = [];
    cfg.tissue = 'brain';
    brain_mesh = ft_prepare_mesh(cfg, seg);

    % turn this into a headmodel
    cfg = [];
    cfg.method = 'singleshell';
    headmodel = ft_prepare_headmodel(cfg, brain_mesh);

#### Construction of the source model

This step is identical to the method for the CTF data, up until the very last stage where the LCMV beamformer is computed.

    cfg = [];
    cfg.resolution = 7;  % clinical work would typically use a grid which <5mm
    cfg.unit = 'mm';
    cfg.headmodel = headmodel;
    cfg.grad = data.grad;
    sourcemodel_grid = ft_prepare_sourcemodel(cfg);

    % align the voxel axes with the head co-ordinate axes.
    cfg.xrange = [min(sourcemodel_grid.pos(:,1))-30 max(sourcemodel_grid.pos(:,1))+30];
    cfg.yrange = [min(sourcemodel_grid.pos(:,2))-30 max(sourcemodel_grid.pos(:,2))+30];
    cfg.zrange = [min(sourcemodel_grid.pos(:,3))-30 max(sourcemodel_grid.pos(:,3))+30];
    mri_coreg_resliced = ft_volumereslice(cfg, mri);

    %% plot all geometrical data to check their alignment
    figure
    ft_plot_headmodel(headmodel, 'unit', 'mm');  % this is the brain shaped head model volume
    ft_plot_sens(data.grad, 'unit', 'mm', 'coilsize', 10);  % the sensor locations
    ft_plot_mesh(sourcemodel_grid.pos); % the source model is a cubic grid of points
    ft_plot_ortho(mri.anatomy, 'transform', mri.transform, 'style', 'intersect');
    alpha 0.5 % make the anatomical MRI slices a bit transparent

{% include image src="/assets/img/tutorial/epilepsy/case1b_head.png" width="400" %}

    cfg = [];
    cfg.channel = 'MEG';
    cfg.covariance = 'yes';
    cov_matrix = ft_timelockanalysis(cfg, data);

    %% Precompute the leadfields, which speeds up the source reconstructions (but this is not obligatory)
    cfg = [];
    cfg.channel = 'MEG';
    cfg.headmodel  = headmodel;
    cfg.sourcemodel = sourcemodel_grid;
    cfg.normalize = 'yes';  % normalisation avoids power bias towards centre of head
    leadfield = ft_prepare_leadfield(cfg, cov_matrix);

At this point the analysis deviates from the CTF analysis because we need to account for differences in the covariance matrix that result from Maxfilter. First, we perform a singular value decomposition of the covariance matrix and plot the singular values, 's'. These are plotted in descending order, and the discontinuity that occurs after the 68th value reflects the effects of Maxfilter, which has reconstructed the data based on (typically) about 80 components.

    [u,s,v] = svd(cov_matrix.cov);
    figure;semilogy(diag(s),'o-');

{% include image src="/assets/img/tutorial/epilepsy/case1b_gradsonlysvd.png" width="400" %}

As we compute the LCMV beamformer below, we can use the information from the SVD to help regularize the covariance matrix using a truncation parameter called kappa. We set this at a value before the big 'cliff' in the singular values. We also set a parameter called lambda which can be considered a weighting factor for the regularization.

    cfg                  = [];
    cfg.method           = 'lcmv';
    cfg.sourcemodel      = leadfield;
    cfg.headmodel        = headmodel;
    cfg.lcmv.keepfilter  = 'yes';
    cfg.lcmv.fixedori    = 'yes'; % project on axis of most variance using SVD
    cfg.lcmv.reducerank  = 2;
    cfg.lcmv.lambda      = '5%';
    cfg.lcmv.kappa       = 65;
    cfg.lcmv.projectmom = 'yes';  % project dipole time series for each dipole in direction of maximal power (see below)
    cfg.lcmv.kurtosis = 'yes';
    source = ft_sourceanalysis(cfg, cov_matrix);

The remainder of the analysis is identical to the CTF analysis - we run the LCMV beamformer, compute the images and explore the time series.

Plotting the images:

    source.kurtosis = source.avg.kurtosis(source.inside) % get rid of NaNs which fall outside head
    source.kurtosisdimord = 'pos';
    cfg = [];
    cfg.parameter = 'kurtosis';
    source_interp = ft_sourceinterpolate(cfg, source, mri);

    cfg = [];
    cfg.funparameter = 'kurtosis';
    cfg.method = 'ortho'; % orthogonal slices with crosshairs at peak (default anyway if not specified)
    ft_sourceplot(cfg, source_interp);

    cfg = [];
    cfg.funparameter = 'kurtosis';
    cfg.method = 'slice';  % plot slices
    ft_sourceplot(cfg, source_interp);

{% include image src="/assets/img/tutorial/epilepsy/case1b_result.png" width="400" %}

{% include image src="/assets/img/tutorial/epilepsy/case1b_slices.png" width="400" %}

We can see here that the results are similar, but not identical to the results from the CTF data. Both analyses reveal an area of relatively high kurtosis adjacent to the lesion, a glioma in the right parietal area. This was the area followed up by the surgical team, based on the kurtosis data (originally analysed in CTF software) interpreted in the context of seizure semiology and neuroanatomy. Both analyses also yielded a strong peak in the left frontal cortex, which is also thought to be clinically significant (the peak indicated by the crosshairs in the image above).

In contrast with the CTF data, this analysis of the MEGIN data did not show an activation in the right frontal cortex, perhaps because of differences in the patterns of spiking activity in the different recordings, or alternatively perhaps because the patient's head was located further from these sensors in this recording (see note below about this). The deeper activity that can be seen in the slice images appears to be located in white matter, but is potentially leakage from activity propagated to deeper areas e.g. insula cortex.

Writing the images to NIFTI:

    cfg = [];
    cfg.filename = 'Case1_resliced_anatomy.nii'
    cfg.parameter = 'anatomy';
    cfg.format = 'nifti';
    ft_volumewrite(cfg, mri_resliced);

    cfg = [];
    cfg.filename = 'Case1_kurtosis.nii';
    cfg.parameter = 'kurtosis';
    cfg.format = 'nifti';
    ft_volumewrite(cfg, source);

Identifying the peaks in the image:

    [ispeak] = findpeaksn(reshape(source.avg.kurtosis, source.dim));
    j = find(ispeak(:));
    [m, i] = sort(-source.avg.kurtosis(j));  % sort on the basis of kurtosis value
    peaks = j(i);
    disp(source.pos(peaks(1:10),:));  % output their positions

    for i = 1:5,
        cfg = [];
        cfg.funparameter = 'kurtosis';
        cfg.location = source.pos(peaks(i),:);
        ft_sourceplot(cfg, source_interp);
    end

Output the time series to AnyWave format:

    % dataset = 'case1_cHPI_raw_trans_sss.fif'  % our original data file
    cfg = [];
    cfg.dataset   = dataset;
    cfg.channel   = 'MEG';
    data = ft_preprocessing(cfg);
    dat = ft_fetch_data(data);
    hdr = ft_fetch_header(data);

    nsources = 5;
    for i = 1:nsources,
        dat(size(dat,1)+1,:)= source.avg.mom{peaks(i),:}*10e5; % see comment below about scaling
        hdr.label{end+1}= ['S' num2str(i)];
        hdr.chantype{end+1} = 'source';
        hdr.chanunit{end+1} = ''  ; % see note below about scaling
    end;
    hdr.nChans = hdr.nChans+nsources;

    ft_write_data(filename, dat, 'header', hdr, 'dataformat', 'anywave_ades');

Create a marker file:

    fid = fopen([filename,'.mrk'], 'w+');
    fprintf(fid,'%s\r\n','// AnyWave Marker File ');
    % loop through sources and times
    for i = 1:nsources
        dat = source.avg.mom{peaks(i),:};
        sd = std(dat);
        tr = zeros(1,length(dat));
        tr(dat>6*sd)=1;
        [tmp,mrksample] = findpeaks(tr, 'MinPeakDistance', 300); % peaks have to be separated by 300 sample points to be treated as separate

        for j = 1:length(mrksample)
            fprintf(fid, '%d\t', i);  %marker name (just a number)
            fprintf(fid, '%d\t', i); %marker value (same number)
            fprintf(fid, '%d\t',source.time(mrksample(j)) ); %marker time
            fprintf(fid, '%s\t', '0'); %marker duration
            fprintf(fid, 'SOURCE%d\r\n', 'i'); %marker channel
        end
    end
    fclose(fid);

{% include image src="/assets/img/tutorial/epilepsy/case1b_anywave.png" width="600" %}

#### Head position during the recording

The flexibility of analysis in FieldTrip can offer additional information to support data interpretation. For example, the step above where the MRI, sensors, head model and mesh are plotted together, can be used to examine positioning within the MEG helmet. This can be particularly important for clinical analysis with children because, with smaller heads, they can potential move quite far from the sensors. In the Maxfiltering process for the Neuromag data above, the continuous head position monitoring allowed the sensor time series to be realigned to a 'standard' position in the centre of the MEG helmet so this effect is not observed. However if the head position is plotted for a version of the data where this head position correction was not done, the original positioning of the brain in relation to the sensors can be seen. In this case, the patient's head was not centrally located during the recording. This might explain the lack of activation in the right temporal lobe for this dataset and underlines the need for MEG systems which better serve pediatric recordings.

{% include image src="/assets/img/tutorial/epilepsy/case1b_headpos.png" width="400" %}
