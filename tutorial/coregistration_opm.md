---
title: Coregistration of Optically Pumped Magnetometer (OPM) data
tags: [tutorial, opm, coordsys]
---

# Coregistration of Optically Pumped Magnetometer (OPM) data

## Introduction

Optically Pumped Magnetometers (OPMs) are magnetic field sensors that can be used for MEG. Conventionally SQUID sensors are used for MEG; SQUIDs are superconductive sensors that require cryocooling, and hence need to be placed as an array in a fixed helmet-shaped dewar. OPMs do not require cryocooling and can be placed individually.

Due to their small size and flexibility, different strategies are used to place OPM sensors on the head. Some labs use flexible caps, like EEG and fNIRS caps. These flexible caps don't constrain the orientation of the sensors very well, which means that the sensor orientation relative to the head can change during the experiment depending on the head orientation and that the sensors can wobble due to movement. Since the magnetic field measured with MEG is a vector, the measurement is sensitive to these orientation differences.

To ensure a well-defined sensor placement, we often use helmets that place the OPM sensors relative to the head. These helmets can be designed and 3-D printed to fit optimally to the individual head, or can be designed as standard helmets to fit multiple participants (with different sized helmets for children and adults). For a good interpretation of the MEG signals recorded with the OPM sensors over the head, it is important to coregister the OPM sensors (location and orientation) with the head. Also for source reconstruction it is required to coregister the sensors with the anatomical MRI, the volume conduction model, and the source model. As a side note, for conventional SQUID-based MEG coregistration is also relevant, but here the coregistration procedure is more easily standardized.

This tutorial demonstrates four different methods for coregistering OPM sensors that are placed in a standard helmet to the subjects head. It demonstrates each of the methods, including data that you can download to carry out all steps yourself. Furthermore, it discusses the advantages and disadvantages of each method. The data for this tutorial can be downloaded [here](https://download.fieldtriptoolbox.org/tutorial/coregistration_opm/) from our download server.
In this tutorial we will _not_ consider the coregistration of OPM sensors in flexible EEG-like caps. We will also _not_ discuss the coregistration of individually designed 3D printed helmets, as for those the coregistration is usually part of the design process and the helmet will fit only one way on the participant's head. Finally, this tutorial will also not cover the processing of the MEG signals recorded from the participants brain, this is covered in the [preprocessing_opm](/tutorial/preprocessing_opm) tutorial.

## Background

The common aim of the three coregistration methods that we explore in this tutorial is to align geometrical objects - i.e. 'things' that have a position and orientation in 3D-space - with respect to one another. Ultimately, we want know the location  of the OPM MEG sensors relative to the participant's head. In the examples below, the OPM MEG sensors are expressed relative to a coordinate system that is defined by the Fieldline smart helmet, which leaves some freedom in the exact position of the head. For reasons outlined below (inspired by arguments that facilitate the downstream analysis of the MEG signals, e.g. for group level analysis), it is custom to start from (or end up with) a coordinate system that is defined based on anatomical landmarks on the participant's head. Some basic background about coordinate systems, and the exact definition of some widely used coordinate systems is given in this [FAQ](/faq/coordsys). 

## Procedure

Procedural outlines of the examples are provided in detail below. This tutorial describes four different ways to achieve coregistration:
- Using geometric information from a Polhemus tracker, matching two sets of points that are known to match one-to-one.
- Using head localization coils, where the location of the coils on the head is known, and the location of the coils relative to the sensors is calculated.
- Using a 3D model from a 3D scanner of the head and helmet, and aligning this model with more detailed anatomical and sensor information.
- Using sensor depth information from the Fieldline smart helmet as a proxy for the head surface.  


## Coregistration using a Polhemus tracker

{% include markup/info %}
The Polhemus device consists of an electromagnetic transmitter (the large knob) and one or multiple receivers. When the OPMs are placed in the same magnetically shielded room (MSR) as a SQUID MEG system, the SQUID sensors can be disturbed by the rather strong electromagnetic fields. Depending on the sensitivity of the SQUID system and local procedures, the Polhemus-based method might therefore not be optimal or available.

Other 3D pointing devices such as the Optotrak (optical) and the Zebris (acoustical) might be more appropriate to localize the OPMs that are operated in the MSR room together with the SQUID MEG system.
{% include markup/end %}

The following example is based on a Polhemus recording, which - besides a description of the participant's head surface - contains a set of digitized points which correspond to 8 fixed locations on the Fieldline smart helmet. These 8 fixed locations are also defined in the fieldlinebeta2 template helmet, but expressed in a different coordinate system than the equivalent locations in the Polhemus file.  

This part consists of the following steps:
- Read in the headshape and change the coordinate system, using **[ft_read_headshape](/reference/ft_read_headshape)** and **[ft_convert_coordsys](/reference/ft_convert_coordsys)**. for visualisation we use **[ft_plot_headshape](/reference/ft_plot_headshape)** and **[ft_plot_axes](/reference/ft_plot_axes)**.
- Identification of the reference points
- Calculation of the transformation parameters, using **[ft_electroderealign](/reference/ft_electroderealign)**.
- Apply the transformation parameters to the sensors, using **[ft_transform_geometry](/reference/ft_transform_geometry)**, and **[ft_plot_sens](/reference/ft_plot_sens)** for visualisation.

 
### Read the Polhemus file and impose a head-based coordinate system

This Polhemus measurement has been obtained with the (too bulky) plastic security glasses and the reference sensor around the neck, which is not realistic. A real measurement should have the ref sensor taped to the forehead, just so that it does not limit the participant moving into the helmet. Note, that the file used here was created using software that used the CTF convention for the definition of the X/Y/Z axes of the coordinate system (i.e. ALS). For consistency with the other examples in this tutorial, we will first convert the head-based coordinate system to be RAS. 

    %% read in the data and enforce the units to be in 'mm'
    headshape = ft_read_headshape('example1_head_markers.pos');
    headshape = ft_convert_units(headshape, 'mm');

    %% visualisation, coordinate axes are ALS
    figure
    ft_plot_headshape(headshape)
    ft_plot_axes(headshape)
    view([-27 20]) 

{% include image src="/assets/img/tutorial/coregistration_opm/headshape_upsideup_ctf.png" width="400" %}
_Figure: recorded headshape has the coordinate axes according to the CTF-convention, with the X-axis pointing towards the nose._



    headshape.coordsys = 'ctf';
    headshape = ft_convert_coordsys(headshape, 'neuromag');
    
    %% visualisation, coordinate axes are now RAS
    figure
    ft_plot_headshape(headshape)
    ft_plot_axes(headshape)
    view([114 20])

{% include image src="/assets/img/tutorial/coregistration_opm/headshape_upsideup.png" width="400" %}
_Figure: adjusted headshape with new coordinate system._

    
### Identification of reference points

The Polhemus file contains a specification of the helmet reference points, the exact identity of those points were not stored in the file, so the order of the points was noted during the Polhemus collection. Here, the last 8 points recorded in the file coincide with those reference points, which on the Fieldline helmet are indicated with labels A1-A8. The order of the points were recorded in the order:  left, front-to-back, then right front-to-back: 'A5', 'A6', 'A7', 'A8', 'A1', 'A2', 'A3', 'A4'. The idea is now to calculate the transformation parameters that are needed to move the set of points as defined in the helmet coordinate system, to the coordinate system that is defined within the Polhemus measurement. To this end, we will use a function from FieldTrip that was originally written to align a set of electrode positions to a head surface. As it turns out, this code can also be used to align - more generically - two sets of points.

    %% definition of the set of target positions, here defined in head coordinates 
    fid_measured = [];
    fid_measured.pos(1,:) = headshape.pos(end-7,:);
    fid_measured.pos(2,:) = headshape.pos(end-6,:);
    fid_measured.pos(3,:) = headshape.pos(end-5,:);
    fid_measured.pos(4,:) = headshape.pos(end-4,:);
    fid_measured.pos(5,:) = headshape.pos(end-3,:);
    fid_measured.pos(6,:) = headshape.pos(end-2,:);
    fid_measured.pos(7,:) = headshape.pos(end-1,:);
    fid_measured.pos(8,:) = headshape.pos(end-0,:);
    fid_measured.label = {'A5', 'A6', 'A7', 'A8', 'A1', 'A2', 'A3', 'A4'};

    %% definition of the corresponding set of source positions, here obtained from the template fieldlinebeta2 helmet
    load fieldlinebeta2;
    fieldlinebeta2 = ft_convert_units(fieldlinebeta2, 'mm');
    fid_helmet     = fieldlinebeta2.fid;

    %% show the misalignment
    headshape2     = headshape;
    headshape2.fid = fid_measured; % replace the original fit, for plotting purposes
    
    figure
    ft_plot_headshape(headshape2)
    ft_plot_axes(headshape2)
    ft_plot_sens(fieldlinebeta2)
    view([102 5]);

{% include image src="/assets/img/tutorial/coregistration_opm/coreg_polhemus_before.png" width="400" %}
_Figure: OPM sensor locations are not in register with the Polhemus headshape._

### Calculation of the transformation parameters

The alignment parameters can now be estimated, using the ```template``` method in ```ft_electroderealign```. Since we want to express the sensors' coordinates in the head coordinate system, the measured positions will be used as the target.

    %% estimate the alignment parameters
    cfg         = [];
    cfg.method  = 'template';
    cfg.target  = fid_measured;
    cfg.elec    = fid_helmet;
    fid_aligned = ft_electroderealign(cfg);


### Apply the transformation parameters to the sensors 

    %% now, we can apply the transformation parameters to the sensors, and evaluate the outcome
    fieldlinebeta2_head = ft_transform_geometry(fid_aligned.rigidbody, fieldlinebeta2, 'rigidbody');

    figure
    ft_plot_headshape(headshape)
    ft_plot_axes(headshape)
    ft_plot_sens(fieldlinebeta2_head)
    view([102 5]);

{% include image src="/assets/img/tutorial/coregistration_opm/coreg_polhemus_after.png" width="400" %}
_Figure: OPM sensor locations are in register with the Polhemus headshape._

## Coregistration using head localizer coils

Conventional SQUID MEG systems commonly head localization coils, which are also known as head position indicator (HPI) coils. All SQUID systems are based on certain number of sensors (e.g., 275 or 306) that are placed in a fixed-size helmet to accomodate most participants. Unless when using [custom headcasts](Barnes paper), the SQUID MEG helmet gives the subject a few cm of space around the head. The heads of different participants are therefore not in the same position, and also for an individual participant the position of the head in the helmet will differ between sessions, and can even vary a bit within a session.

To localize the head relative to the SQUID MEG helmet, HPI coils are placed on the head - often on well-defined [anatomical landmarks](/faq/xxx) - and the coils are energized to create small magnetic dipoles at the start of the recording session. Sometimes the localization is repeated at the end of the recording session, and sometimes the localization is done continuously. These magnetic dipoles can be localized, thereby determining the position of the sensors relative to the anatomical landmarks. All commercial SQUID MEG systems have a standard procedure for this that is well-integrated in the acquisition protocol and software, consequently the MEG recordings stored by the acquisition software include the sensor positions in [head coordinates](/faq/coordsys).

OPM sensors allow for individual placement and use variable-sized helmets. Furthermore, labs that operate an OPM MEG system will not all have the same number of sensors; some labs have as few as 8 sensors, whereas other labs might have up to 128 sensors.

{% include markup/info %}
To localize the HPI coils you need sufficient coverage of the spatial distribution of the magnetic dipole that is generated by the coil. Both the position (3 parameters) and the orientation (2 angles) need to be estimated, and if the magnetic dipole moment of the coil is not calibrated, also the strength needs to be estimated.

To estimate 6 magnetic dipole parameters, a minimum of 6 OPM channels are needed. A reliable estimation requires more channels. Coregistration using head localizer coils is therefore less suited for OPM systems with fewer channels.
{% include markup/end %}

The dataset used here is a 32-channel dataset, with the OPM-sensors distributed across the 144-slot fieldlinebeta2 helmet. The CTF magnetic phantom - with the HPI coils attached at fixed (and known) locations on the phantom - was positioned quite high into the helmet, to maximize the coverage of the coils. We will analyse an ~1 minute segment of data, during which the 3 HPI coils were energized with 3 sinusoidal signals, at 8 ('nasion' coil), 11 ('right ear'), and 14 ('left ear') Hz. These signals can be considered to be temporally orthogonal, and when the measured data is filtered appropriately, this filtered data will reflect purely the signal that is generated by the respective coil. Here, we will fit dipoles to the first principal component spatial topography of bandpass-filtered data.

This part exists of the following steps:
- Processing of the data to highlight the contribution of the individual HPI coils to the measured signals, using **[ft_preprocessing](/reference/ft_preprocessing)**, and **[ft_selectdata](/reference/ft_selectdata)**. To evaluate the spectrum of the signals, we will use **[ft_freqanalysis](/reference/ft_freqanalysis)**.
- Fitting of dipoles to the topographies of the first principal components of the bandpass filtered data, using **[ft_componentanalysis](/reference/ft_componentanalysis)**, and **[ft_dipolefitting](/reference/ft_dipolefitting)**. For visualization of the spatial topogrphies, we use **[ft_topoplotIC](/reference/ft_topoplotic)**, and for the dipole fit we start with a grid search, and we use **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** to create the search grid.  
- Calculation of the transformation matrix that moves the sensors to the head-based coordinate system, using **[ft_headcoordinates](/reference/ft_headcoordinates)**.
- Apply the transformation matrix to the sensors, using **[ft_transform_geometry](/reference/ft_transform_geometry)**.

### Processing of the data to capture the signal of the HPI coils

    % load in the data
    cfg              = [];
    cfg.dataset      = 'example2_magneticphantom_HPIplusdipoleset6_raw.fif';
    cfg.coilaccuracy = 0;
    data_all         = ft_preprocessing(cfg);

Now we cut out the relevant time segment, and exclude channels for which the positions were incorrectly stored in the file. Both selection criteria are specific to the file we use here. 

    cfg         = [];
    cfg.latency = [2 60-1./data_all.fsample];
    cfg.channel = {'all' '-L212_bz' '-R212_bz'}; % exclude channels which have wrong position/orientation information in the file (this is specific to the example data used)
    data        = ft_selectdata(cfg, data_all);
    
We can now compute the powerspectrum the MEG, to verify the presence of spectral peaks (and their harmonics) at 8/11/14 Hz. 

    cfg1        = [];
    cfg1.method = 'mtmfft';
    cfg1.foilim = [0 40];
    cfg1.taper  = 'dpss';
    cfg1.tapsmofrq = 0.2;
    cfg1.pad    = 10;
    cfg2        = [];
    cfg2.length = 10;
    cfg2.overlap = 0.8;
    freq        = ft_freqanalysis(cfg1, ft_redefinetrial(cfg2, data));

    figure; plot(freq.freq, log10(mean(freq.powspctrm)));

{% include image src="/assets/img/tutorial/coregistration_opm/powerspectrum_hpi.png" width="400" %}
_Figure: Powerspectrum from a measurement containing strong signals at 8, 11 and 14 Hz, and harmonics._

In order to focus on the signals of the specific HPI-coils, we next bandpass filter the data in three different frequency bands, and cut off the edges for any potential edge artifacts.

    cfg            = [];
    cfg.bpfilter   = 'yes';
    cfg.bpfilttype = 'firws';
    cfg.usefftfilt = 'yes';
    cfg.bpfreq     = [7 9];
    data08         = ft_preprocessing(cfg, data); % nas
    cfg.bpfreq     = [10 12];
    data11         = ft_preprocessing(cfg, data); % rpa
    cfg.bpfreq     = [13 15];
    data14         = ft_preprocessing(cfg, data); % lpa
    
    cfg            = [];
    cfg.latency    = [6 56-1./data.fsample];
    data08         = ft_selectdata(cfg, data08);
    data11         = ft_selectdata(cfg, data11);
    data14         = ft_selectdata(cfg, data14);
    
    %% look at the data 
    figure;plot(data08.time{1}, data08.trial{1});
    xlim([10 12]);
    xlabel('time (s)');
    ylabel('magnetic field strength (T)');

{% include image src="/assets/img/tutorial/coregistration_opm/hpi_8hz.png" width="400" %}
_Figure: Two seconds of data of the measurement, band-pass filtered for 8 Hz._


### Fit dipoles to the sensor topographies

We proceed by performing a principal component analysis (PCA) on the recorded signals. The idea is that - given that the signals on the coils are the strongest signal components in the measurement, and given that we have pre bandpass filtered the time series - the strongest principal components will be the 'spatial fingerprints' of the coils impacting the sensors. Those fingerprints will be used to perform a dipole fit, i.e. find the parameters of a dipole that optimally explain those principal components.

    cfg            = [];
    cfg.method     = 'pca';
    cfg.updatesens = 'no';
    comp08 = ft_componentanalysis(cfg, data08);
    comp11 = ft_componentanalysis(cfg, data11);
    comp14 = ft_componentanalysis(cfg, data14);

    %% look at the topographies
    load fieldlinebeta2bz_helmet.mat
    cfg              = [];
    cfg.component    = 1;
    cfg.layout       = layout;
    cfg.gridscale    = 150;
    cfg.interplimits = 'electrodes';
    cfg.figure       = subplot('position',[0 0 1/3 1]);
    ft_topoplotIC(cfg, comp08);
    cfg.figure       = subplot('position',[1/3 0 1/3 1]);
    ft_topoplotIC(cfg, comp11);
    cfg.figure       = subplot('position',[2/3 0 1/3 1]);
    ft_topoplotIC(cfg, comp14);

{% include image src="/assets/img/tutorial/coregistration_opm/hpi_topo.png" width="700" %}
_Figure: Spatial topographies of the signals generated by the 3 HPI coils._

For the dipolefit, we will use a gridsearch based initial scan, followed by a non-linear optimization step to find the final set of parameters. The gridsearch is motivated by the fact that a non-linear search of the whole parameter space (i.e. volume of space covered by the helmet) might result in convergence to a local minimum. The following creates a source grid that will be used for the initial grid search.

    %% create a scanning grid, that is bounded by the helmet
    load fieldlinebeta2

    % this is the volume conductor model
    headmodel = ft_headmodel_infinite();
    
    % this is a definition of the boundary points
    hs      = [];
    hs.pos  = fieldlinebeta2.coilpos;
    hs.unit = 'm';

    % this creates a mesh, with positions on the mesh, which is not what we need, 
    % but which is a necessary step to create the boundary of the mesh
    cfg           = [];
    cfg.headshape = hs;
    cfg.grad      = fieldlinebeta2;
    hs            = ft_prepare_sourcemodel(cfg); 
    
    % creates a boundary out of the points, that is to be interpreted 
    % as the in/out boundary
    hm = ft_headmodel_singleshell(hs); 

    %% create the grid
    cfg            = [];
    cfg.headmodel  = hm;
    cfg.resolution = 0.0075;
    sourcemodel    = ft_prepare_sourcemodel(cfg);

Now we can perform the dipole fits.

    cfg             = [];
    cfg.headmodel   = headmodel;
    cfg.component   = 1;
    cfg.gridsearch  = 'yes';
    cfg.sourcemodel = sourcemodel;
    dip08 = ft_dipolefitting(cfg, comp08);
    dip11 = ft_dipolefitting(cfg, comp11);
    dip14 = ft_dipolefitting(cfg, comp14);

The data in this example was obtained using the CTF magnetic phantom, with the HPI coils placed on well-defined locations (with respect to one another), i.e. located on 12 (Nas) 3 and 9 o'clock (Rpa/Lpa) of a 7.5 cm radius circle. Accounting for the thickness of the coils, the expected distances between the localizer coils on the phantom are as follows:
- L-R: 0.1532
- N-R/N-L: 0.1083

We can verify the reconstructed distances as follows. Note that for a real measurement, one would need to measure the distance between the fiducials first (e.g. with a Polhemus scanner, see above) in order to be able to make such a comparison. 

    % for verification
    p     = [dip08.dip.pos; dip14.dip.pos; dip11.dip.pos];
    delta = pdist(p);
    disp(delta);


### Definition of the head-based coordinate system

Now, we can use the identified location, to compute the coregistration matrix, that transforms the sensor positions from 'helmet' coordinates to the head coordinate system, as defined by the positions of the fiducial locations. Here, we use the neuromag convention.

    % sensor coordinates into head coordinates (RAS)
    transform_sens2head = ft_headcoordinates(dip08.dip.pos, dip14.dip.pos, dip11.dip.pos, 'neuromag');

### Apply the transformation matrix to the sensors

load fieldlinebeta2;
fieldlinebeta2_hpi = ft_transform_geometry(transform_sens2head, fieldlinebeta2);


## Coregistration using a 3D scanner

{% include markup/info %}
Note that if you are using 3D scanner based on an iPhone or iPad, such as the [Structure Sensor](ref), and if you have the OPMs in the same MSR as a SQUID MEG system, you will want to turn the iPhone or iPad to airplane mode prior to taking it into the MSR. Otherwise the electromagnetic fields of the cellular and/or wifi radio can cause problems with the SQUIDs.
{% include markup/end %}

The idea here is to make a sufficiently high quality 3D-model that captures the participant's facial features in register with the the helmet, such that the facial features can be used for coregistration with a surface image obtained from an anatomical MRI. From the image of the helmet, the position of the sensors can be deduced. Thus, the 3D-model serves as an intermediary to link the anatomy with the sensors. 

This part consists of the following steps:
- Read the anatomical MRI, and assign a head-based coordinate system, using **[ft_read_mri](/reference/ft_read_mri)**, and **[ft_volumerealign](/reference/ft_volumerealign)**.
- Read in the 3D model, assign a meaningful coordinate system, and erase the irrelevant parts, using **[ft_read_headshape](/reference/ft_read_headshape)**, **[ft_meshrealign](/reference/ft_meshrealign)**, and **[ft_defacemesh](/reference/ft_defacemesh)**.
- Interactive alignment of the face - extracted from the 3D model -  with the MRI-extracted scalp surface, using **[ft_volumesegment](/reference/ft_volumesegment)**, **[ft_prepare_mesh](/reference/ft_prepare_mesh)**, and **[ft_meshrealign](/reference/ft_meshrealign)**.
- Interactive alignment of the helmet with the reference sensors/helmet, using **[ft_meshrealign](/reference/ft_meshrealign)**.
- Combination of the obtained alignment parameters into a single transformation matrix
- Application of the resulting transformation to the sensor array, using **[ft_transform_geometry](/reference/ft_transform_geometry)**. 

### Definition of the head-based coordinate system

Here, we read in the anatomical MRI of the participant, and define the coordinate system based on the conventions that are typically used for SQUID-based MEG. That is, using anatomical landmarks on the surface of the head, a coordinate system is defined, that can also be defined using a Polhemus tracker (as in coregistration strategy 1, see above). Note that alternatively the coordinate system can be defined based on anatomical structures in the brain (cf. the anterior and posterior commissures), which facilitates spatial alignment/normalisation across participants.

    % read in the anatomical MRI
    mri   = ft_read_mri('example3_anatomical.nii.gz');
    ft_determine_coordsys(mri);

{% include image src="/assets/img/tutorial/coregistration_opm/mri_notaligned.png" width="400" %}
_Figure: anatomical MRI image with an underdefined coordinate system._

After reading in the MRI, you can check the coordinate system with ```ft_determine_coordsys```. As the above figure shows, the axes are labelled as 'unknown', but it seems that they are oriented according to the RAS convention, while the origin of the coordinate system is ill-defined. For this reason, we will explicitly impose an anatomical landmark based coordinate system next, which requires interactive identification of the relevant landmarks (nasion, left/right pre auricular points).

    % define a head based coordinate system
    cfg          = [];
    cfg.coordsys = 'neuromag';
    mri          = ft_volumerealign(cfg, mri);
    ft_determine_coordsys(mri);

{% include image src="/assets/img/tutorial/coregistration_opm/mri_aligned.png" width="400" %}
_Figure: anatomical MRI image with a 'neuromag' coordinate system._

### Cleaning of the structure sensor scan

Here, we read in the 3D-model from the structure scan, and define a coordinate system that has its axes pointing into more or less canonical directions (relative to the participant). The next steps remove irrelevant parts of the image (e.g. the back of a chair etc), and here we also choose to separate the 'face' part from the 'helmet' part, to facilitate the alignment. Strictly speaking this separation is not necessary.

    scan      = ft_read_headshape('example3_face_helmet.obj');
    scan.unit = 'm';
    
    figure;hold on;
    ft_plot_headshape(scan);
    ft_plot_axes(scan);
    lighting gouraud; material dull; h=light;

{% include image src="/assets/img/tutorial/coregistration_opm/scan_notaligned.png" width="400" %}
_Figure: 3D-model with an underdefined coordinate system._

In the example model, the coordinate axes' orientations relative to the participant more or less are well-behaved, i.e. the axes are pointing approximately along the left/right, anterior/posterior, and superior inferior directions, but the order of the axes is not conventional. As a first step we might want to assign a better defined coordinate system to the model. Note that the exact coordinate system does not matter too much. Here we define the coordinate system such that the X/Y/Z axes are pointing into the same direction as the head  coordinate system defined in the MRI image, i.e. R(ight)A(nterior)S(uperior). We use ```cfg.coordsys='neuromag'``` because this method allows us to approximately indicate the N(asion)/L(eft preauricular point), and R(ight) preauricular point. Note that in the below procedure, the ears are not visible in the model, instead we will use the protruding points on the helmet's rim to define 'l' and 'r'.

    % approximately align the mesh to a RAS coordinate system,
    % by clicking on 'dummy' nas/lpa/rpa
    cfg          = [];
    cfg.method   = 'fiducial';
    cfg.coordsys = 'neuromag';
    scan         = ft_meshrealign(cfg, scan);
    
    figure;hold on;
    ft_plot_headshape(scan);
    ft_plot_axes(scan);
    view([125 10]);
    lighting gouraud; material dull; h=light;

{% include image src="/assets/img/tutorial/coregistration_opm/scan_sosoaligned.png" width="400" %}
_Figure: 3D-model with a coordinate system relating to the head and helmet._

In the example model, a large part of the body of the participant is also present, we remove it, in order to facilitate the alignment. The below code uses ```ft_defacemesh``` with ```cfg.method='plane'```. This particular method throws away data points that are on one side of the plane, which is indicated by the direction of the stick that is sticking out from the middle of the plane. Here, good results were obtained, by setting the viewpoint in the interactive window to 'right', and then using the following numbers to define the cutting plane: rotate [-40 0 0], translate [0 0 -140]. Note that the viewpoint does not have a consequence for the points to be excluded.

    % cut off the irrelevant parts, this might require a few iterations
    cfg        = [];
    cfg.method = 'plane';
    scan         = ft_defacemesh(cfg, scan);
    
    figure;hold on;
    ft_plot_headshape(scan);
    ft_plot_axes(scan);
    view([125 10]);
    lighting gouraud; material dull; h=light;

{% include image src="/assets/img/tutorial/coregistration_opm/scan_facehelmet.png" width="400" %}
_Figure: 3D-model with only the face and helmet._

In the following, we separate the 'helmet' part of the model from the 'face' part of the model, because this facilitates the alignment performed below. Note that we need to ensure that any change in the coordinates of one of these objects should be reflected in the other object as well. Clearly, this is needed because this model of the two objects is the crucial link that links the anatomy with the sensors.

    % separate the face from the helmet, it's easier to keep the face at first
    % instance, and then go back to the original mesh to get the helmet
    scan_face    = scan;
    scan_face    = ft_defacemesh(cfg, scan_face); % viewpoint: front, rotate: [0 -90 0], translate: [85 0 20].
    scan_face    = ft_defacemesh(cfg, scan_face); % viewpoint: front, rotate: [0  90 0], translate: [-67 0 20].
    scan_face    = ft_defacemesh(cfg, scan_face); % viewpoint: left,  rotate: [140 0 0], translate: [0 0 55];
    
    figure;hold on;
    ft_plot_headshape(scan_face);
    ft_plot_axes(scan_face);
    view([125 10]);
    lighting gouraud; material dull; h=light;    
    
{% include image src="/assets/img/tutorial/coregistration_opm/scan_face.png" width="400" %}
_Figure: 3D-model with only the face._

The helmet mesh will be extracted by removing the face vertices from the model. This is a bit less straightforward with normal FieldTrip functions, and we need to do a little bit of coding, and use a function which is located in a private folder.

    % get the helmet by excluding the face nodes from the model
    scan_helmet  = scan;
    
    % this requires a temporary change into a private folder
    [ftver, ftdir] = ft_version;
    pdir = fullfile(ftdir, 'private');
    cd(pdir);
    
    % the intersect(a,b,'rows') does not give the full intersection because of duplicate points
    pos1 = scan_face.pos;
    pos2 = scan_helmet.pos;
    mindist = nan(size(pos1,1),1);
    indx    = nan(size(pos1,1),1);
    sel     = cell(size(pos1,1),1);
    for k = 1:size(pos1,1)
      delta = sqrt(sum((pos2 - pos1(k,:)).^2,2));
      [mindist(k), indx(k)] = min(delta);
      sel{k} = find(delta==mindist(k));
    end
    sel = unique(cat(1,sel{:}));
    [scan_helmet.pos, scan_helmet.tri] = remove_vertices(scan_helmet.pos, scan_helmet.tri, sel);

    figure;hold on;
    ft_plot_headshape(scan_helmet);
    ft_plot_axes(scan_helmet);
    view([125 10]);
    lighting gouraud; material dull; h=light;

{% include image src="/assets/img/tutorial/coregistration_opm/scan_helmet.png" width="400" %}
_Figure: 3D-model with only the helmet._
    
### Interactive alignment of the face with the MRI-based scalp surface

Now we will extract the scalp surface from the anatomical MRI, and interactively align this with the face extracted from the 3D model. In theory, an automatic algorithm, such as the iterative closest point (ICP) algorithm could be used, but the quality of the results highly depends on the number of points, and the quality of the initial alignment. In this example, we stick to a manual alignment. To achieve a reasonably good alignment, the following values can be specified for the rotation (without clicking the 'apply' button in between): [13.5 0.2 -4], and for the translation: [-0.003 0.0825 -0.0083]. (Note that the metric units are now expressed in 'm'.

    % segment the scalp 
    cfg          = [];
    cfg.output   = 'scalp';
    seg          = ft_volumesegment(cfg, mri);
    
    % create a mesh for the scalp
    cfg             = [];
    cfg.tissue      = 'scalp';
    cfg.numvertices = 10000;
    mri_face        = ft_prepare_mesh(cfg, seg);
    mri_face        = ft_convert_units(mri_face, 'm');
    
    % align the 3D model's face to the face extracted from the anatomical image
    cfg             = [];
    cfg.headshape   = mri_face;
    cfg.meshstyle   = {'edgecolor','k','facecolor','skin'};
    scan_face_aligned = ft_meshrealign(cfg, scan_face);

    figure;hold on;
    ft_plot_headshape(mri_face,'facealpha',0.4);
    ft_plot_mesh(scan_face_aligned, 'facecolor','skin');    
    view([125 10]);
    lighting gouraud; material dull; h = light;

{% include image src="/assets/img/tutorial/coregistration_opm/face_aligned.png" width="400" %}
_Figure: 3D-model of the face aligned with MRI-derived face surface._

### Interactive alignment of the helmet with the reference sensors/helmet

We can also attempt to interactively align the helmet model with the template helmet. Here, we could use the following values for the rotation: [24 0 -3], and  for the translation: [-0.009 0.07 -0.05]. 

    load fieldlinebeta2
    fieldlinebeta2.coordsys = 'ras';

    cfg = [];
    cfg.grad = fieldlinebeta2;
    cfg.meshstyle = {'edgecolor','k','facecolor','skin'};
    scan_helmet_aligned = ft_meshrealign(cfg, scan_helmet);

    figure;hold on;
    ft_plot_sens(fieldlinebeta2);
    ft_plot_mesh(scan_helmet_aligned, 'facecolor', [0.5 0.5 1], 'facealpha', 0.4, 'edgecolor', 'none');
    view([125 10]);
    lighting gouraud; material dull; h = light;

{% include image src="/assets/img/tutorial/coregistration_opm/helmet_aligned.png" width="400" %}
_Figure: 3D-model of the helmet aligned with Fieldline helmet._

### Calculation of the transformation matrix

Now we can use the transformations that align the 3D scan's face with the MRI-derived facial surface, and that align the 3D scan's helmet with the sensor positions to calculate the transformation that aligns the sensors with the anatomy. 

    transform_scan2helmet = scan_helmet_aligned.cfg.transform;
    transform_scan2face   = scan_face_aligned.cfg.transform;
    transform_helmet2face = transform_scan2face/transform_scan2helmet;
    
### Apply the transformation matrix to the sensors

The transformation matrix ```transform_helmet2face``` can now be used to update the sensor definition, which aligns the sensors with head-based coordinate system .

    % align the sensors to the head
    fieldlinebeta2_head = ft_transform_geometry(transform_helmet2face, fieldlinebeta2);
    
    figure;hold on;
    ft_plot_sens(fieldlinebeta2_head);
    ft_plot_headshape(mri_face, 'facecolor', [0.5 0.5 1], 'facealpha', 0.4, 'edgecolor', 'none');
    view([125 10]);
    lighting gouraud; material dull; h = light;

{% include image src="/assets/img/tutorial/coregistration_opm/sensors_face_aligned.png" width="400" %}
_Figure: sensors aligned with the anatomical MRI._

Note that in this particular example, the participant was not positioned very high in the Fieldline helmet.


## Coregistration using the sensors following the head shape

_This is specific for the FieldLine smart helmet._

More info to follow: stay tuned!

## Summary and suggested further reading

This tutorial gave an introduction on the coregistration of OPM data, specifically dealing with OPM data that has been collected with the sensors positioned in in a known helmet configuration.  

You may want to continue with the more general [tutorials](/tutorial/) on processing MEG (and EEG) data, or have a look at the [system specific details](/getting_started) for the OPM data that you are working with. Also, you may want to proceed with the [opm preprocessing tutorial](/tutorial/preprocessing_opm).

Furthermore, you can explore other pages that deal with OPMs:

{% include seealso tag1="opm" %}
