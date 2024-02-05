---
title: Coregistration of Optically Pumped Magnetometer (OPM) data
tags: [tutorial, opm, coordsys]
---

# Coregistration of Optically Pumped Magnetometer (OPM) data

## Introduction

_Introduction to the tutorial and dataset. This should include

- What will you learn from this tutorial?
- What does this tutorial expect as background understanding or skills?
- Which topics are not covered in this tutorial?_

Optically Pumped Magnetometers (OPMs) are magnetic field sensors that can be used for MEG. Conventionally SQUID sensors are used for MEG; SQUIDs are superconductive sensors that require cryocooling, and hence need to be placed as an array in a fixed helmet-shaped dewar. OPMs do not require cryocooling and can be placed individually.

Due to their small size and flexibility, different strategies are used to place OPM sensors on the head. Some labs use flexible caps, like EEG and fNIRS caps. These flexible caps don't constrain the orientation of the sensors very well, which means that the sensor orientation relative to the head can change during the experiment depending on the head orientation and that the sensors can wobble due to movement. Since the magnetic field measured with MEG is a vector, the measurement is sensitive to these orientation differences.

To ensure a well-defined sensor orientation, we often use helmets that place the OPM sensors relative to the head. These helmets can be designed and 3-D printed to fit optimally to the individual head, or can be designed as standard helmets to fit multiple participants (with different sized helmets for children and adults).

For a good interpretation of the MEG signals recorded with the OPM sensors over the head, it is important to coregister the OPM sensors (location and orientation) with the head. Also for source reconstruction it is required to coregister the sensors with the anatomical MRI, the volume conduction model, and the source model. As a side note, for conventional SQUID-based MEG coregistration is also relevant, but here the coregistration procedure is more easily standardized.

This tutorial demonstrates three different methods for coregistering OPM sensors that are placed in a standard helmet to the subjects head. It demonstrates each of the methods, including data that you can download to carry out all steps yourself. Furthermore, it discusses the advantages and disadvantages of each method.

In this tutorial we will _not_ consider the coregistration of OPM sensors in flexible EEG-like caps. We will also _not_ discuss the coregistration of individually designed 3D printed helmets, as for those the coregistration is usually part of the design process and the helmet will fit only one way on the participant's head.

Furthermore, this tutorial will also not cover the processing of the MEG signals recorded from the participants brain.

## Background

The common aim of the three coregistration methods that we explore in this tutorial is to align geometrical objects - i.e. 'things' that have a position in 3D-space - with respect to one another. Ultimately, we want know the location  of the OPM MEG sensors relative to the participant's head. In the examples below, the OPM MEG sensors are expressed relative to a coordinate system that is defined by the fieldlinebeta2 helmet, which leaves some freedom in the exact position of the head. For reasons outlined below (inspired by arguments that facilitate the downstream analysis of the signals), it is custom to start from (or end up with) a coordinate system that is defined based on anatomical landmarks on the participant's head.  o this end, we need to compute  with In order to achieve this, we need to first ensure that the 3D coordinate system, in which the spatial coordinates are expressed, is the same for the objects that are used for the coregistration.  one first needs to decide on the target coordinate system in which the  

## Procedure

_summarize which analysis steps are performed in the tutorial. This should include a picture of the analysis protocol._

## Coregistration using a Polhemus tracker

{% include markup/info %}
The Polhemus device consists of an electromagnetic transmitter (the large knob) and one or multiple receivers. When the OPMs are placed in the same magnetically shielded room (MSR) as a SQUID MEG system, the SQUID sensors can be disturbed by the rather strong electromagnetic fields. Depending on the sensitivity of the SQUID system and local procedures, the Polhemus-based method might therefore not be optimal or available.

Other 3D pointing devices such as the Optotrak (optical) and the Zebris (acoustical) might be more appropriate to localize the OPMs that are operated in the MSR room together with the SQUID MEG system.
{% include markup/end %}

The following example is based on a Polhemus recording, which - besides a description of the coordinate system based on the fiducials placed on the participant's head - contains a set of digitized points which correspond to 8 fixed locations on the Fieldline smart helmet.
 
### Step 1.1: fixing the Polhemus recording error to obtain a correct head-based coordinate system

The following example is a bit ugly, because we mixed up LPA and RPA in the Polhemus recording. This caused the scan to be upside down. This should be fixed (and can be done so here by swapping the LPA and RPA by hand, after reading them in into MATLAB). Also, this Polhemus measurement has been obtained with the (too bulky) plastic security glasses and the reference sensor around the neck, which is not realistic. A real measurement should have the ref sensor taped to the forehead, just so that it does not limit the participant moving into the helmet.  

    %% read in the data and enforce the units to be in 'mm'
    filename  = '20231119_hedscan3.pos';
    headshape = ft_read_headshape(filename);
    headshape = ft_convert_units(headshape, 'mm');

    %% visualisation, head is upside-down
    figure
    ft_plot_headshape(headshape)
    ft_plot_axes(headshape)
    view([-27 20]) 

{% include image src="/assets/img/tutorial/coregistration_opm/headshape_upsidedown.png" width="400" %}
_Figure: recorded headshape is upside-down, also note the labels of the axes._

    %% fix the swapped LPA/RPA during the recording
    lpa = headshape.fid.pos(3,:);
    nas = headshape.fid.pos(2,:);
    rpa = headshape.fid.pos(1,:);

    % this is the transformation matrix that will put the head upside-up
    transform = ft_headcoordinates(nas, lpa, rpa, [], 'neuromag');

    headshape = ft_transform_geometry(transform, headshape);
    headshape.fid.label = {'rpa', 'nas', 'lpa'};
    headshape.coordsys  = 'neuromag';
    
    %% visualisation, head is upside-up again
    figure
    ft_plot_headshape(headshape)
    ft_plot_axes(headshape)
    view([114 20])

{% include image src="/assets/img/tutorial/coregistration_opm/headshape_upsideup.png" width="400" %}
_Figure: adjusted headshape is upside-up, also note the labels of the axes, thanks to the manual addition of the coordsys._
    
### Step 1.2: identification of reference points, and calculation of the transformation parameters

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
    headshape2 = headshape;
    headshape2.fid = fid_measured; % replace the original fit, for plotting purposes
    
    figure
    ft_plot_headshape(headshape2)
    ft_plot_axes(headshape2)
    ft_plot_sens(fieldlinebeta2)
    view([102 5]);

{% include image src="/assets/img/tutorial/coregistration_opm/coreg_polhemus_before.png" width="400" %}
_Figure: OPM sensor locations are not in register with the Polhemus headshape._

The alignment parameters can now be estimated, using the ```template``` method in ```ft_electroderealign```. Since we want to express the sensors' coordinates in the head coordinate system, the measured positions will be used as the target.

    %% estimate the alignment parameters
    cfg         = [];
    cfg.method  = 'template';
    cfg.target  = fid_measured;
    cfg.elec    = fid_helmet;
    fid_aligned = ft_electroderealign(cfg);

    %% now, we can apply the transformation parameters to the sensor, and evaluate the outcome
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

### Step 2.1, processing of the data to capture the signal of the HPI coils

    % load in the data
    datadir = '/project/3055060.01/202311xx_opm_installation/20231121_opm_sub-magneticphantom/sub-Magneticphantom';
    
    cfg = [];
    cfg.dataset = fullfile(datadir, '20231121_143558_sub-Magneticphantom_file- HPIplusdipoleset6_raw.fif');
    cfg.coilaccuracy = 0;
    data_all = ft_preprocessing(cfg);

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

### Step 2.2, fit dipoles to the sensor topographies

We proceed by performing a principal component analysis (PCA) on the recorded signals. The idea is that - given that the signals on the coils are the strongest signal components in the measurement, and given that we have pre bandpass filtered the time series - the strongest principal components will be the 'spatial fingerprints' of the coils impacting the sensors. Those fingerprints will be used to perform a dipole fit, i.e. find the parameters of a dipole that optimally explain those principal components.

    cfg = [];
    cfg.method = 'pca';
    cfg.updatesens = 'no';
    comp08 = ft_componentanalysis(cfg, data08);
    comp11 = ft_componentanalysis(cfg, data11);
    comp14 = ft_componentanalysis(cfg, data14);

    %% look at the topographies
    load fieldlinebeta2bz_helmet.mat
    cfg           = [];
    cfg.component = 1;
    cfg.layout    = layout;
    cfg.gridscale = 150;
    cfg.interplimits = 'electrodes';
    cfg.figure = subplot('position',[0 0 1/3 1]);
    ft_topoplotIC(cfg, comp08);
    cfg.figure = subplot('position',[1/3 0 1/3 1]);
    ft_topoplotIC(cfg, comp11);
    cfg.figure = subplot('position',[2/3 0 1/3 1]);
    ft_topoplotIC(cfg, comp14);

{% include image src="/assets/img/tutorial/coregistration_opm/hpi_topo.png" width="700" %}
_Figure: Spatial topographies of the signals generated by the 3 HPI coils._

For the dipolefit, we will use a gridsearch based initial scan, followed by a non-linear optimization step to find the final set of parameters. The gridsearch is motivated by the fact that a non-linear search of the whole parameter space (i.e. volume of space covered by the helmet) might result in convergence to a local minimum. The following creates a source grid that will be used for the initial grid search.

    %% create a scanning grid, that is bounded by the helmet
    load fieldlinebeta2

    % this is the volume conductor model
    headmodel = ft_headmodel_infinite();
    
    % this is a definition of the boundary points
    hs = [];
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
    p = [dip08.dip.pos; dip14.dip.pos; dip11.dip.pos];
    delta = pdist(p);
    disp(delta);



### Step 2.3, definition of the head-based coordinate system

Now, we can use the identified location, to compute the coregistration matrix, that transforms the sensor positions from 'helmet' coordinates to the head coordinate system, as defined by the positions of the fiducial locations. Here, we use the neuromag convention.

    % dewar coordinates into head coordinates (RAS)
    T = ft_headcoordinates(dip08.dip.pos, dip14.dip.pos, dip11.dip.pos, 'neuromag');


## Coregistration using a 3D scanner

{% include markup/info %}
Note that if you are using 3D scanner based on an iPhone or iPad, such as the [Structure Sensor](ref), and if you have the OPMs in the same MSR as a SQUID MEG system, you will want to turn the iPhone or iPad to airplane mode prior to taking it into the MSR. Otherwise the electromagnetic fields of the cellular and/or wifi radio can cause problems with the SQUIDs.
{% include markup/end %}

The idea here is to make a sufficiently high quality 3D-model that captures the participant's facial features in register with the the helmet, such that the facial features can be used for coregistration with a surface image obtained from an anatomical MRI. From the image of the helmet, the position of the sensors can be deduced. 

### Step 3.1, definition of the head-based coordinate system

Here, we read in the anatomical MRI of the participant, and define the coordinate system based on the conventions that are typically used for SQUID-based MEG. That is, using anatomical landmarks on the surface of the head, a coordinate system is defined, that can also be defined using a Polhemus tracker (as in coregistration strategy 1, see above). Note that alternatively the coordinate system can be defined based on anatomical structures in the brain (cf. the anterior and posterior commissures), which facilitates spatial alignment/normalisation across participants.

    % read in the anatomical MRI
    datadir = '/project/3055060.01/jansch_sandbox/scans/structuresensor_helmet_jm';
    fname = fullfile(datadir, 'anatomical.nii.gz');
    mri   = ft_read_mri(fname);

    % define a head based coordinate system
    cfg          = [];
    cfg.coordsys = 'neuromag';
    mri          = ft_volumerealign(cfg, mri);


### Step 3.2, cleaning of the structure sensor scan

Here, we read in the 3D-model from the structure scan, and define a coordinate system that has its axes pointing into more or less canonical directions (relative to the participant). The next steps remove irrelevant parts of the image (e.g. the back of a chair etc), and here we also choose to separate the 'face' part from the 'helmet' part, to facilitate the alignment. Strictly speaking this separation is not necessary.

    % this file is a depth-only image
    datadir = '/project/3055060.01/jansch_sandbox/scans/structuresensor_helmet_jm/';
    fname   = fullfile(datadir, 'Model5.obj');
     
    jm      = ft_read_headshape(fname);
    jm.unit = 'm';
    
    figure;hold on;
    ft_plot_headshape(jm);
    ft_plot_axes(jm);
    lighting gouraud; material dull; h=light;

In the example model, the coordinate axes' orientations relative to the participant are well-behaved, i.e. the axes are pointing approximately along the left/right, anterior/posterior, and superior inferior directions. This is not a given in general, so as a first step we might to assign a known coordinate system to the model, before we proceed. Note that the exact coordinate system does not matter too much. Here we define the coordinate system such that the X/Y/Z axes are pointing into the same direction as the head  coordinate system defined in the MRI image, i.e. R(ight)A(nterior)S(uperior). We use ```cfg.coordsys='neuromag'``` because this method allows us to indicate the N(asion)/L(eft preauricular point), and R(ight) preauricular point.

    % approximately align the mesh to a RAS coordinate system,
    % by clicking on 'dummy' nas/lpa/rpa
    cfg          = [];
    cfg.method   = 'fiducial';
    cfg.coordsys = 'neuromag';
    jm           = ft_meshrealign(cfg, jm);
    
    figure;hold on;
    ft_plot_headshape(jm);
    ft_plot_axes(jm);
    lighting gouraud; material dull; h=light;

In the example model, a large part of the body of the participant is also present, we remove it, in order to facilitate the alignment. The below code uses ```ft_defacemesh``` with ```cfg.method='plane'```. This particular method throws away data points that are on one side of the plane, which is indicated by the direction of the stick that is sticking out from the middle of the plane.

    % cut off the irrelevant parts, this might require a few iterations
    cfg        = [];
    cfg.method = 'plane';
    jm         = ft_defacemesh(cfg, jm);
    
    figure;hold on;
    ft_plot_headshape(jm);
    ft_plot_axes(jm);
    lighting gouraud; material dull; h=light;

In the following, we separate the 'helmet' part of the model from the 'face' part of the model, because this facilitates the alignment performed below. Note that we need to ensure that any change in the coordinates of one of these objects should be reflected in the other object as well. Clearly, this is needed because this model of the two objects is the crucial link that links the anatomy with the sensors.

    % separate the face from the helmet, it's easier to keep the face at first
    % instance, and then go back to the original mesh to get the helmet
    jm_face    = jm;
    jm_face    = ft_defacemesh(cfg, jm_face);
    jm_face    = ft_defacemesh(cfg, jm_face);
    jm_face    = ft_defacemesh(cfg, jm_face);
    
    figure;hold on;
    ft_plot_headshape(jm_face);
    ft_plot_axes(jm_face);
    lighting gouraud; material dull; h=light;    
    
    % get the helmet by excluding the face nodes from the model
    jm_helmet  = jm;
    
    [ftver, ftdir] = ft_version;
    pdir = fullfile(ftdir, 'private');
    cd(pdir);
    
    % the intersect(a,b,'rows') does not seem to give the full
    % intersection because of duplicate points
    pos1 = jm_face.pos;
    pos2 = jm_helmet.pos;
    mindist = nan(size(pos1,1),1);
    indx    = nan(size(pos1,1),1);
    sel     = cell(size(pos1,1),1);
    for k = 1:size(pos1,1)
      delta = sqrt(sum((pos2 - pos1(k,:)).^2,2));
      [mindist(k), indx(k)] = min(delta);
      sel{k} = find(delta==mindist(k));
    end
    sel = unique(cat(1,sel{:}));
    [jm_helmet.pos, jm_helmet.tri] = remove_vertices(jm_helmet.pos, jm_helmet.tri, sel);
    
### Step 3.3, alignment of the face with the MRI-based scalp surface

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
    jm_face_aligned = ft_meshrealign(cfg, jm_face);

### Step 3.4, alignment of the helmet with the reference sensors/helmet

    load fieldlinebeta2
    fieldlinebeta2.coordsys = 'ras';

    cfg = [];
    cfg.grad = fieldlinebeta2;
    cfg.meshstyle = {'edgecolor','k','facecolor','skin'};
    jm_helmet_aligned = ft_meshrealign(cfg, jm_helmet);


### Step 3.5, putting everything together


## Coregistration using the sensors following the head shape

_This is specific for the FieldLine smart helmet._

### Step 4.1

### Step 4.2


## Summary and conclusion:

- What has been covered?
- What has not been covered but is relevant in the context of the tutorial?
- Provide links to suggested further reading, related FAQs and example scripts.
