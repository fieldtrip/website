---
title: Virtual channel analysis of epilepsy MEG data
tags: [tutorial, meg-epilepsy]
---

{% include markup/info %}
This documentation is under development and hence incomplete and perhaps incorrect.
{% include markup/end %}

# Virtual channel analysis of epilepsy MEG data

{% include markup/danger %}
The FieldTrip toolbox is designed for research purposes only. The FieldTrip project and development team make no representation that FieldTrip is a clinically approved medical device, and users understand and accept that any result or its display presented in whatever form obtained using FieldTrip must not be used for any purpose other than research.

FieldTrip is released under the [GNU General Public License](http://www.gnu.org/copyleft/gpl.html) and you should review its terms and conditions.
{% include markup/end %}

The data for this tutorial can be downloaded from [our ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/epilepsy/)

All MEG data were recorded at [Aston Brain Centre](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/) (ABC) using both a 275-channel CTF system and using an Elekta 306-channel system. This case report and the data are kindly provided by Professor [Stefano Seri](<https://research.aston.ac.uk/portal/en/persons/stefano-seri(448f2383-5cc6-48b7-ae19-f599c6e69c58).html>). The data has been clinically analysed by the staff of ABC using the software accompanying the MEG system. The FieldTrip analysis demonstrated here is only for educational purposes.

The kurtosis beamformer method described here, for identifying the source(s) of epileptiform activity, was originally published by [Kirsch et al (2006)](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5953276/).

The ABC clinical staff would typically use the following sequence of analysis steps for epilepsy data:
1. Screen the data visually for spikes and also to identify physiological or external recording artefacts.
2. Choose relatively artefact-free data, that appears to contain spikes, for further analysis (bearing in mind that data quality can vary widely in patient recordings, especially children)
3. Run the kurtosis beamformer analysis to yield candidate sources in volumetric images, which can be examined alongside other information e.g. lesions visible in anatomical images.
4. Examine source timeseries from the candidate sources to verify the presence of spikes. Usually source timeseries would be visualised alongside the original raw data. Candidate spikes can be automatically marked in the timeseries based on their amplitude.
5. Before reporting back to the surgical team, candidate sources are typically confirmed by dipole-fitting of key spikes identified by the pipeline outlined above.  

Because of the importance to clinical work of visually screening data and marking spikes, we have also incorporated here (with brief instructions) the use of [AnyWave software](http://meg.univ-amu.fr/wiki/AnyWave), an open-source package for visualising MEG and EEG data which lends itself well to the interpretation of the outputs from this analysis. 

There are some small differences in the parameters for the beamformer source analysis depending on whether the analysis is for CTF or Elekta data, so analyses for each data type are presented here separately.



## Case 1

_Male, age 9. Right parietal Glioma with parietal extended lesionectomy. Corticography also showed interictal discharges in the frontal lobe, though seizures were of parietal origin. Following the MEG, was operated and is now seizure free and off medication._

MEG data were recorded at [Aston Brain Centre](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/) (ABC) using both a 275-channel CTF system and using an Elekta 306-channel system. This case report and the data are kindly provided by Professor [Stefano Seri](<https://research.aston.ac.uk/portal/en/persons/stefano-seri(448f2383-5cc6-48b7-ae19-f599c6e69c58).html>). The data has been clinically analysed by the staff of ABC using the software accompanying the MEG system. The FieldTrip analysis demonstrated here is only for educational purposes.

### Analysis of the CTF dataset

#### Coregistration of the anatomical MRI

The original MRI that is provided for this patient has been partially processed in the CTF software and is stored in CTF .mri format. This MRI is _not shared_ for privacy reasons. Nevertheless, here we will show how it was processed in FieldTrip.

    mri_orig = ft_read_mri('case1.mri');

The dataset also includes a Polhemus recording of the head surface, which can be used to coregister the MRI to the CTF system.

    headshape = ft_read_headshape('case1.pos');
    headshape = ft_convert_units(headshape, 'mm');

Check the coregistration of the Polhemus headshape and the anatomical MRI. In the CTF coordinate system the x-axis should be pointing to the nose and the y-axis to the left ear.

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

{% include image src="/assets/img/tutorial/epilepsy/case1a-deface.png" width="400" %}

{% include image src="/assets/img/tutorial/epilepsy/case1a-deface_result.png" width="400" %}

For convenience in later plotting, we reslice the MRI so that the axes of the volume are aligned with the axes of the coordinate system.

    cfg = [];
    mri_resliced = ft_volumereslice(cfg, mri_defaced);

Finally we should do a visual inspection of the realigned, defaced and replaced MRI.

    cfg = [];
    ft_sourceplot(cfg, mri_resliced)

{% include image src="/assets/img/tutorial/epilepsy/case1a-resliced.png" width="400" %}

Note that the patients head is tilted to the right. Apparently the anatomical landmarks at the left and right ear were not clicked symmetrically with the Polhemus. This is not a problem for further processing, as long as we remember that results are expressed in head coordinates relative to the anatomical landmark of this specific recording.

#### Importing and filtering the channel level data

    dataset = 'case1.ds';

    cfg = [];
    cfg.dataset   = dataset;
    cfg.hpfilter  = 'yes';
    cfg.hpfreq    = 10;
    cfg.lpfilter  = 'yes';
    cfg.lpfreq    = 70;
    cfg.channel   = 'MEG';
    data = ft_preprocessing(cfg);
    
The kurtosis beamformer is typically run within a bandpass filter (here 10-70 Hz) which excludes some physiological artefacts such as eyeblinks or EMG that might affect the analysis, while preserving as much energy from the spikes as possible.  

    %% visualize the preprocessed data

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.channel  = 'MEG';
    cfg.layout   = 'CTF275.lay';
    cfg.event    = ft_read_event(dataset);
    ft_databrowser(cfg, data);


#### Construction of the volume conduction model of the head

We will use the defaced MRI, which has been realigned with the CTF system and resliced

    mri = ft_read_mri('mri_defaced.mat');

Segment the brain compartment from the anatomical MRI and make the volume conduction model

    cfg = [];
    cfg.tissue = 'brain';
    seg = ft_volumesegment(cfg, mri);

    % save seg seg

    cfg = [];
    cfg.tissue = 'brain';
    brain = ft_prepare_mesh(cfg, seg);

    cfg = [];
    cfg.method = 'singleshell';
    headmodel = ft_prepare_headmodel(cfg, brain);

    % save headmodel headmodel

#### Construction of the source model

To save time we have chosen to use a 7 mm grid for the source model here, but in a real clincal scenario a grid of 5 mm or smaller would typically be used. 

    cfg = [];
    cfg.grid.resolution = 7;
    cfg.grid.unit = 'mm';
    cfg.headmodel = headmodel;
    cfg.grad = data.grad; % this being needed here is a silly historical artifact
    sourcemodel_grid = ft_prepare_sourcemodel(cfg);

 Finally we align the voxel axes with the head co-ordinate axes and reslice the MRI
 
    cfg.xrange = [min(sourcemodel_grid.pos(:,1))-30 max(sourcemodel_grid.pos(:,1))+30];
    cfg.yrange = [min(sourcemodel_grid.pos(:,2))-30 max(sourcemodel_grid.pos(:,2))+30];
    cfg.zrange = [min(sourcemodel_grid.pos(:,3))-30 max(sourcemodel_grid.pos(:,3))+30];
    mri_resliced = ft_volumereslice(cfg, mri);   
    save mri_resliced mri_resliced;
  
Plot everything out and check that everything is aligned correctly.     

    figure
    ft_plot_vol(headmodel, 'unit', 'mm');
    ft_plot_sens(data.grad, 'unit', 'mm', 'coildiameter', 10);
    ft_plot_mesh(sourcemodel_grid.pos);
    ft_plot_ortho(mri_resliced.anatomy, 'transform', mri_resliced, 'style', 'intersect');

In the following stage, we compute the data covariance matrix for the beamformer source reconstruction.  We use the **[ft_timelockanalysis](/reference/ft_sourceanalysis)** function (more commonly used elsewhere to compute an average), and because we have not defined individual trials within the data it will produce the covariance matrix for the whole time period of the data.  

    cfg = [];
    cfg.channel = 'MEG';
    cfg.covariance = 'yes';
    cov_matrix = ft_timelockanalysis(cfg, data);
    
Next we precompute the leadfields, which is not obligatory but speeds up the following steps.
    
    cfg = [];
    cfg.channel = 'MEG';
    cfg.headmodel  = headmodel;
    cfg.grid = sourcemodel_grid;
    cfg.normalize = 'yes';  % normalisation avoids power bias towards centre of head
    leadfield = ft_prepare_leadfield(cfg, cov_matrix);  

Now we compute the LCMV beamformer and reconstruct the timeseries at each of the locations specified in the source model grid.  **[ft_sourceanalysis](/reference/ft_sourceanalysis)** can also automatically compute the kurtosis of each timeseries.

    cfg = [];
    cfg.headmodel  = headmodel; 
    cfg.grid = leadfield;  
    cfg.method = 'lcmv';
    cfg.lcmv.projectmom = 'yes';  %project dipole timeseries for each dipole in direction of maximal power (see below)
    cfg.lcmv.kurtosis = 'yes'; % compute kurtosis at each location
    source = ft_sourceanalysis(cfg, cov_matrix);

#### Explore the outputs
We are ready to explore the results visually, starting with the volumetric images.  First of all we need to interpolate the kurtosis information with the resliced MRI, then we can plot the images.

    source.kurtosis = source.avg.kurtosis(source.inside) % get rid of NaNs which fall outside head
    source.kurtosisdimord = 'pos';  
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


Returning to our images in FieldTrip, we can scroll through the slices to see where the areas of high kurtosis fall. But to be more objective it is useful to identify each discrete peak location in the kurtosis data. Here we use a 3rd party function called [findpeaksn.m](https://github.com/vigente/gerardus/blob/master/matlab/PointsToolbox/findpeaksn.m) which needs to be downloaded separately and added to the matlab path. The Aston clinical team would typically examine every single peak but for simplicity we will just look at the top few. We plot the co-ordinates and some images. 

    [ispeak] = findpeaksn(reshape(source.avg.kurtosis, source.dim)); % We need to input a 3d array instead of a 1 x n voxels array.
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

#### Visualise the beamformer timeseries in AnyWave
It is also clinically important to visualise the spikes that are contributing to the kurtosis images, not least to screen out any spurious sources which may be elicited by artefacts.  To do this, it is useful to have the original sensor data visible alongside the source timeseries. Marking the timepoints at which spikes occur at the sources can help the clinician scroll more easily through the data. We will write the data to a format that can be read by the open-source package [AnyWave](http://meg.univ-amu.fr/wiki/AnyWave), which is well-suited to this purpose.

When we read in the data earlier, we filtered it, but here it is more useful to have the unfiltered data.  So we import that to Fieldtrip and then append source timeseries data, adding header information for this, before writing the whole lot to the Anywave ADES file format. 

    % dataset = 'case1_sss_hpi.fif'  % our original data file
    cfg = [];
    cfg.dataset   = dataset;
    cfg.channel   = 'MEG';
    data = ft_preprocessing(cfg);
    dat = ft_fetch_data(data);  
    hdr = ft_fetch_header(data);


    % then append the source hdr and data to the channel hdr and data. 
    nsources = 10;  % for simplicity here we just append the top 10 source timeseries.
    for i = 1:nsources, 
        dat(size(dat,1)+1,:)= source.avg.mom{peaks(i),:}*10e5; %see comment below about scaling
        hdr.label{end+1}= ['S' num2str(i)];
        hdr.chantype{end+1} = 'source';
        hdr.chanunit{end+1} = ''  ; % see note below about scaling
    end; 
    hdr.nChans = hdr.nChans+nsources;

    % write to files
    ft_write_data(filename, dat, 'header', hdr, 'dataformat', 'anywave_ades');

_(Notes:  At the time of writing, units for the source timeseries in Anywave are abitrary. Also, it is currently advisable to write all data to file at the same time rather than attempting to append source timeseries to an existing data file)._

Finally we can automatically mark potential spikes in the source timeseries data and create labels in AnyWave marker file format.  We use the convention (from the original CTF SAMg2 software) of placing a marker wherever the source timeseries exceeds 6 standard deviations of its mean.  

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



The data can now be opened in AnyWave.  Once the file is opened, to see sources alongside source data, click 'Add View' in the top/middle toolbar. Then use the eyeball icon to set each view so that one has 'MEG' and one has 'SOURCE' data.  Set the timescale to be
0.3 sec/cm (close to the clinical standard 3cm/sec) and scale the amplitudes appropritely. Use the menu to import the marker file that we just created.







### Analysis of the Elekta dataset

FIXME

## Case 2

_Female, age 14. Epilepsy. Referral for MEG because EEG did not allow laterlisation or localisation of discharges, though clinically they appeared to come from the left hemisphere. Functional neuroimaging in the form of a PET scan showed a right area of hypo metabolism. Surgical follow-up information about this patient is not available._

MEG data was recorded at [Aston Brain Centre](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/) (ABC) using both a 275-channel CTF system and using an Elekta 306-channel system. This case report and the data are kindly provided by Professor [Stefano Seri](<https://research.aston.ac.uk/portal/en/persons/stefano-seri(448f2383-5cc6-48b7-ae19-f599c6e69c58).html>). The data has been clinically analysed by the staff of ABC using the software accompanying the MEG system. The FieldTrip analysis demonstrated here is only for educational purposes.

### Analysis of the CTF dataset

FIXME

### Analysis of the Elekta dataset

FIXME
