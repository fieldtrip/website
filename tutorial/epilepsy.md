---
title: Virtual channel analysis of epilepsy MEG data
layout: default
tags: [tutorial, MEG-epilepsy]
---

# Table of contents
{:.no_toc}

* this is a markdown unordered list which will be replaced with the ToC, excluding the "Contents header" from above
{:toc}

#  Virtual channel analysis of epilepsy MEG data

{:.alert-info}
This documentation is under development and hence incomplete and perhaps incorrect.

{{page>:tutorial/shared/disclaimer}}

The data for this tutorial can be downloaded from [our ftp server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/epilepsy)

## Case 1

*Male, age 9.  Right parietal Glioma with parietal extended lesionectomy. Corticography also showed interictal discharges in the frontal lobe, though seizures were of parietal origin. Following the MEG, was operated and is now seizure free and off medication.*

MEG data was recorded at [Aston Brain Centre](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/) (ABC) using both a 275-channel CTF system and using an Elekta 306-channel system. This case report and the data are kindly provided by Professor [Stefano Seri](https://research.aston.ac.uk/portal/en/persons/stefano-seri(448f2383-5cc6-48b7-ae19-f599c6e69c58).html). The data has been clinically analysed by the staff of ABC using the software accompanying the MEG system. The FieldTrip analysis demonstrated here is only for educational purposes.

### Analysis of the CTF dataset

####  Coregistration of the anatomical MRI

The original MRI that is provided for this patient has been partially processed in the CTF software and is stored in CTF .mri format. This MRI is *not shared* for privacy reasons. Nevertheless, here we will show how it was processed in FieldTrip.

    mri_orig = ft_read_mri('case1.mri');

The dataset also includes a Polhemus recording of the head surface, which can be used to coregister the MRI to the CTF system.

    headshape = ft_read_headshape('case1.pos');
    headshape = ft_convert_units(headshape, 'mm');

Check the coregistration of the Polhemus headshape and the anatomical MRI. In the CTF coordinate system the x-axis should be pointing to the nose and the y-axis to the left ear.

    ft_determine_coordsys(mri_orig, 'interactive', 'no')
    ft_plot_headshape(headshape);

In this case the coregistration is already nearly perfect.

![image](/static/img/tutorial/case1a-coreg.png@400)

Usually you would start with an anatomical MRI (e.g. stored as a stack of DICOM files) that is not yet coregistered with the MEG. We will improve the coregistration a bit, using the same procedure you could use to coregister from scratch.

The coregistration procedure starts with a coarse manual coregistration, followed by an automatic fine coregistration in which the skin surface from the MRI is fitted to the headshape points.

    cfg = [];
    cfg.method = 'headshape';
    cfg.headshape.interactive = 'yes';
    cfg.headshape.icp = 'yes';
    cfg.headshape.headshape = headshape;
    cfg.coordsys = 'ctf';
    mri_realigned = ft_volumerealign(cfg, mri_orig);

![image](/static/img/tutorial/case1a-coreg-manual.png@400)

The headshape not only covers the scalp, but also the face and nose. Hence the coregistration needs to be done prior to defacing from the anatomical MRI. The translate, rotate and scale parameters specified here were determined experimentally in the graphical user interface of the **[/reference/ft_defacevolume](/reference/ft_defacevolume)** function.

    cfg = [];
    cfg.translate = [100 0 -60];
    cfg.rotate = [-4 30 0];
    cfg.scale = [75 150 120];
    mri_defaced = ft_defacevolume(cfg, mri_realigned);

![image](/static/img/tutorial/case1a-deface.png@400)

![image](/static/img/tutorial/case1a-deface_result.png@400)

For convenience in later plotting, we reslice the MRI so that the axes of the volume are aligned with the axes of the coordinate system.

    cfg = [];
    mri_resliced = ft_volumereslice(cfg, mri_defaced);

Finally we should do a visual inspection of the realigned, defaced and replaced MRI.

    cfg = [];
    ft_sourceplot(cfg, mri_resliced)

![image](/static/img/tutorial/case1a-resliced.png@400)

Note that the patients head is tilted to the right. Apparently the anatomical landmarks at the left and right ear were not clicked symmetrically with the Polhemus. This is not a problem for further processing, as long as we remember that results are expressed in head coordinates relative to the anatomical landmark of this specific recording.

#### Processing the channel level data

    dataset = 'case1.ds';

    cfg = [];
    cfg.dataset   = dataset;
    cfg.hpfilter  = 'yes';
    cfg.hpfreq    = 10;
    cfg.lpfilter  = 'yes';
    cfg.lpfreq    = 70;
    cfg.channel   = 'MEG';
    data = ft_preprocessing(cfg);

    %% visualize the preprocessed data

    cfg = [];
    cfg.viewmode = 'vertical';
    cfg.channel  = 'MEG';
    cfg.layout   = 'CTF275.lay';
    cfg.event    = ft_read_event(dataset);
    ft_databrowser(cfg, data);

    %% compute channel-level kurtosis

    datak = [];
    datak.label    = data.label;
    datak.dimord   = 'chan';
    datak.kurtosis = kurtosis(data.trial{1}')';

    cfg = [];
    cfg.comment = 'computed channel-level kurtosis';
    datak = ft_annotate(cfg, datak);

    cfg = [];
    cfg.layout    = 'CTF275.lay';
    cfg.parameter = 'kurtosis';
    ft_topoplotER(cfg, datak);

    % caxis([0 40])

#### Construction of the volume conduction model of the head

    % we will use the defaced MRI, which has been realigned with the CTF system and resliced

    mri = ft_read_mri('mri_defaced.mat');

    %% segment the brain compartment from the anatomical MRI and make the volume conduction model

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

    cfg = [];
    cfg.grid.resolution = 7;
    cfg.grid.unit = 'mm';
    cfg.vol = headmodel;
    cfg.grad = data.grad; % this being needed here is a silly historical artifact
    sourcemodel = ft_prepare_sourcemodel(cfg);

    %%
    cfg = [];
    cfg.xrange = [min(sourcemodel.pos(:,1))-30 max(sourcemodel.pos(:,1))+30];
    cfg.yrange = [min(sourcemodel.pos(:,2))-30 max(sourcemodel.pos(:,2))+30];
    cfg.zrange = [min(sourcemodel.pos(:,3))-30 max(sourcemodel.pos(:,3))+30];
    mri_resliced = ft_volumereslice(cfg, mri_defaced);

    % save mri_resliced mri_resliced

    figure
    ft_plot_vol(headmodel, 'unit', 'mm');
    ft_plot_sens(data.grad, 'unit', 'mm', 'coildiameter', 10);
    ft_plot_mesh(sourcemodel.pos);
    ft_plot_ortho(mri_resliced.anatomy, 'transform', mri_resliced, 'style', 'intersect');

    %% compute data covariance for source reconstruction

    cfg = [];
    cfg.channel = 'MEG';
    cfg.covariance = 'yes';
    timelock = ft_timelockanalysis(cfg, data);

    %% this is not required, but speeds up repeated source reconstructions

    cfg = [];
    cfg.channel = 'MEG';
    cfg.vol  = headmodel;
    cfg.grid = sourcemodel;
    cfg.normalize = 'yes';
    sourcemodel = ft_prepare_leadfield(cfg, timelock);

    % save sourcemodel sourcemodel

    cfg = [];
    cfg.vol  = headmodel;
    cfg.grid = sourcemodel;
    cfg.method = 'lcmv';
    cfg.lcmv.projectmom = 'yes';
    sourcep = ft_sourceanalysis(cfg, timelock);

    sourcep.kurtosis = nan(size(sourcep.pos,1),1);
    sourcep.kurtosisdimord = 'pos';
    sel = find(sourcep.inside(:));
    for i=1:length(sel)
    disp(i);
    sourcep.kurtosis(sel(i)) = kurtosis(sourcep.avg.mom{sel(i)});
    end

    cfg = [];
    cfg.comment = 'computed source-level kurtosis';
    sourcep = ft_annotate(cfg, sourcep);

    %% explore the results

    cfg = [];
    cfg.parameter = 'kurtosis';
    sourcepi = ft_sourceinterpolate(cfg, sourcep, mrir);

    %%

    % cfg = [];
    % cfg.funparameter = 'mom';
    % ft_sourceplot(cfg, sourcep);

    %%

    cfg = [];
    cfg.funparameter = 'kurtosis';
    ft_sourceplot(cfg, sourcep);

    %%

    cfg = [];
    cfg.funparameter = 'kurtosis';
    ft_sourceplot(cfg, sourcepi);

    %% find peaks and plot timecourse

    ispeak = findpeaksn(sourcep.kurtosis);
    j = find(ispeak(:));
    [m, i] = sort(-sourcep.kurtosis(j));
    peaks = j(i);
    disp(sourcep.pos(peaks(1:20),:));

    % peak 1 is left frontal
    % peak 4 is right frontal

    s1 = sourcep.avg.mom{peaks(1)};
    s4 = sourcep.avg.mom{peaks(4)};
    shift = 1.1*(max(s1) - min(s4));

    figure;
    plot(sourcep.time, s1, 'r');
    hold on
    plot(sourcep.time, s4 + shift, 'm');
    legend({'area 1', 'area 4'})

    datas = [];
    datas.time = {sourcep.time};
    datas.trial = {[s1; s4]};
    datas.label = {'area 1', 'area 4'}';

    cfg = [];
    cfg.comment = 'constructed virtual-channel raw data structure';
    datas = ft_annotate(cfg, datas);

    %%

    cfg = [];
    cfg.funparameter = 'kurtosis';
    cfg.location = sourcep.pos(peaks(1),:);
    ft_sourceplot(cfg, sourcepi);
    cfg.location = sourcep.pos(peaks(4),:);
    ft_sourceplot(cfg, sourcepi);

    %% find maxima in virtual channel time series based on 6 SDs

    sd1 = std(s1);
    sd4 = std(s4);

    tr = abs(s1)>6*sd1 & abs(s4)>6*sd4;
    % tr = conv(double(tr), ones(1,60), 'same');
    tr = tr>0;
    begsample = find(diff([tr 0]==1));
    endsample = find(diff([tr 0]==1));

    %%

    cfg = [];
    datac = ft_appenddata(cfg, data, datas);

    cfg = [];
    cfg.artfctdef.interictal.artifact = [begsample(:) endsample(:)];
    cfg.viewmode = 'vertical';
    cfg.channel = 'MEG';
    cfg.layout = 'CTF275.lay';
    % cfg.event = ft_read_event(dataset);
    ft_databrowser(cfg, datac);

    %% show the provenance of the analysis pipeline

    cfg = [];
    cfg.filename = 'sourcepi';
    cfg.filetype = 'html';
    ft_analysispipeline(cfg, sourcepi);

    !open sourcepi.html

### Analysis of the Elekta dataset

FIXME

## Case 2

*Female, age 14. Epilepsy. Referral for MEG because EEG did not allow laterlisation or localisation of discharges, though clinically they appeared to come from the left hemisphere. Functional neuroimaging in the form of a PET scan showed a right area of hypo metabolism. Surgical follow-up information about this patient is not available.*

MEG data was recorded at [Aston Brain Centre](http://www.aston.ac.uk/lhs/research/centres-facilities/brain-centre/) (ABC) using both a 275-channel CTF system and using an Elekta 306-channel system. This case report and the data are kindly provided by Professor [Stefano Seri](https://research.aston.ac.uk/portal/en/persons/stefano-seri(448f2383-5cc6-48b7-ae19-f599c6e69c58).html). The data has been clinically analysed by the staff of ABC using the software accompanying the MEG system. The FieldTrip analysis demonstrated here is only for educational purposes.

### Analysis of the CTF dataset

FIXME

### Analysis of the Elekta dataset

FIXME
