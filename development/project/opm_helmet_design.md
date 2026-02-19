---
title: OPM helmet design
---

{% include /shared/development/warning.md %}

## Introduction

Measuring MEG with OPMs allow for flexible sensor placement. This is a significant departure from the rigidity of traditional SQUID-based systems, which confine participants within a fixed sensor array. With OPMs, researchers can now tailor the magnetometer configuration to an individual's unique head shape and size, a benefit that is particularly impactful when studying children or patient populations. The flexible placement allows positioning the sensors close to the scalp and to brain regions expected to be activated.

The flexible OPM sensor placement opens the door for a range of novel experimental paradigms, as subjects are no longer tethered to a single, bulky dewar; they can potentially move, interact, and perform tasks in a much more naturalistic environment, thereby capturing brain activity that is more representative of real-world cognition. It should be noted, however, that OPMs in a helmet or cap that moves along with the participant will pick up considerable artifacts due to the OPMs moving and/or rotating through the residual magnetic field in the MSR. Extra shielding of the MSR with 3 instead of 2 layers of mu metal, and/or the use of nulling coils can reduce, but completely eliminate these movement-related artifacts. Although denoising algorithms like HFC and AMM can help to clean the data from the artifacts caused by the movements, it should also always be considered whether the measurement is not better done with a head-fixed setup.

This tutorial aims for designing OPM arrays with relatively uniform whole whole-head coverage. It does not include forward simulations of how a hypothetical dipole in the brain is visible on the OPM sensor array, and also does not cover how to place (a limited set of) OPMs to specifically target activity in a particular brain area. Furthermore, this tutorial will not discuss how OPM recordings are processed.

## Background

OPMs differ in size, depending on the manufacturer, but in general can be conceived as a rectangular box with a cable attached. For the FieldLine system, for example, the individual sensors are 13x15x35 mm. The OPMs are placed in holders which can in principle be mounted on a flexible cap just like EEG electrodes, but this comes with the potential disadvantage that the sensor orientations are not fixed and might vary depending on the head orientation and movements. With a fixed/rigid helmet as demonstrated in this tutorial, the position _and_ orientation of all sensors is well-defined.

The tutorial demonstrates the placement of FieldLine sensors, but is equally applicable to the sensors from QuSpin, Mag4health, or other companies. The OPM sensors and the holders are modeled (outside of MATLAB) as STL files; these sensors and holders are then distributed over the shell that forms the helmet. Furtermore, additional geometrical objects can be modeled as STL files and can be used as "tools" in the fabrication process to make holes in the helmet, or to add a small rim to facilitate glueing the sensor holder to the shell.

## Procedure

In this tutorial we separate the design of the complete OPM helmet into two parts: the shell, i.e. the basic helmet-shaped outline that fits around the head, and the sensor holders that are printed seperately and that are glued into place. We will cover the process of designing custom OPM helmets for well defined geometries (like a sphere), for individual participants, and to accomodate specific populations. Furthermore, it demonstrates how a given number of OPM sensors can be distributed over the helmet and how sensor orientations/rotations can be optimized. Finally it discusses how the STL design files can be combined to make a model that can be 3D printed.

In part 1 we use different approaches to make the overall helmet shape.

- from a regular geometrical shape, like a sphere
- from an individual anatomical MRI
- from an individual 3D scan
- from a large sample of MRIs to make a population-optimized helmet

In part 2 we demonstrate different procedures to distribute the OPM sensors over the helmet:

- based on the 10-20 placement scheme for EEG electrodes
- based on an equidistant sensor distribution
- by interactively clicking to specify the sensor positions

In part 3 we look at the sensor orientation, i.e., how the sensors are rorated around their own axes. This is not too relevant for mono-axial and tri-axial sensors, but is highly relevant for bi-axial OPMs like the FieldLine v3 and Mag4Health sensors.

In part 4 we will discuss how the STL design files that have been generated are combined into a complete helmet design that can be 3D printed.

{% include markup/yellow %}
In the following we will be using [Autodesk Fusion](https://www.autodesk.com/products/fusion-360/). You can sign up as a student or educator and get an educational license for free, or you can sign up for a free personal license. Alternatively, you could also [SolidWorks](https://www.solidworks.com), [FreeCAD](https://www.freecad.org), [Blender](https://www.blender.org), or other 3D design software.
{% include markup/end %}

## Part 1 - different helmet shapes

### Spherical helmet

For this helmet design we start with a sphere designed in Fusion. The center of the sphere is at the origin, and the radius is 100 mm. Furthermore, we have created a hemisphere shell that has an inner radius of 100 mm and a thickness of 10 mm. The sphere represents the head and the hemisphere shell that fits exactly around it acts as the helmet.

The figure below shows the sphere/head (red) with the hemisphere/helmet (grey), with a cut-out cross section so that you can see that they perfectly align. 

{% include image src="/assets/img/tutorial/opm_helmet_design/figure1.png" width="600" %}

The STL file of the spherical head and hemisphere shell are available from our [download server](https://download.fieldtriptoolbox/org/tutorial/opm_helmet_design).

We read the two STL files into MATLAB and plot them together with the axes of the coordinate system. For this we use **[ft_read_headshape](/reference/fileio/ft_read_headshape)** which is a general function to read meshes, point clouds, 3D scans, etcetera.

    headshape = ft_read_headshape('spherical-head.stl')
    helmet = ft_read_headshape('spherical-helmet.stl')

    figure
    ft_plot_mesh(headshape, 'facecolor', 'skin_light', 'axes', true)
    ft_plot_mesh(helmet, 'facecolor', [0.7 0.7 0.7]) % grey
    ft_headlight % or lighting phong; camlight

The units of the geometrical objects are correctly recognized as 'mm'. We can also specify in which [head coordinate system](/faq/coordsys) they are specified, which will ensure the correct labels along the axes.

    % the CTF coordinate system has X towards the nose and Y towards the left
    headshape.coordsys = 'ctf'; 
    helmet.coordsys = 'ctf'; 

We proceed with determining the sensor positions. In part 2 of this tutorial we will explore different placement schemes, but for now we will distribute the OPM sensors following the (extended) 10-20 electrode placement scheme. See the 2001 paper by Oostenveld & Praamstra [The five percent electrode system for high-resolution EEG and ERP measurements](https://doi.org/10.1016/s1388-2457(00)00527-7) for details.

For the automatic placement we have to define positions on the headshape surface. Here the head is a sphere with 100 mm radius, so that is easy.

    nas = [+100 0 0];
    ini = [-100 0 0];
    lpa = [0 +100 0];
    rpa = [0 -100 0];

We can add the anatomical landmarks (often referred to as fiducials) to the headshape structure, and use **[ft_plot_headshape](/reference/ft_plot_headshape)** instead of **[ft_plot_mesh](/reference/ft_plot_mesh)**. The two functions are very similar, but the first automatically plots the fiducials (if present), whereas the second has more low-level options to optimize the figure.

    headshape.fid.pos = [
        nas
        ini
        lpa
        rpa
    ];

    headshape.fid.label = {
        'nas'
        'ini'
        'lpa'
        'rpa'
    };

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin_light', 'axes', true)
    alpha 0.5 % slightly transparent
    ft_headlight

Subsequently we call **[ft_electrodeplacement](/reference/ft_electrodeplacement)** to automatically determine the electrode positions.

    % this places a lot of electrodes, see https://doi.org/10.1016/s1388-2457(00)00527-7
    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = '1020';
    cfg.feedback = 'yes';
    elec = ft_electrodeplacement(cfg, headshape);

In the next step, we use **[ft_sensorplacement](/reference/ft_sensorplacement)** which reads the STL models for the sensor, the sensor holder, and for a "cutting tool" that will be used to make a hole in the helmet on the location where the sensor holder needs to be glued. The ft_sensorplacement will translate the STL objects to each of the selected electrode locations on the head shape, rotate the STL object such that it is perpendicular to the surface, and then move it outward a little bit.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 5; % in mm

    cfg.template = 'fieldline_sensor.stl';
    sensor = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    holder = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_cuttingtool.stl';
    cuttingtool = ft_sensorplacement(cfg, headshape);

This returns a cell-array for each of the objects which we can plot in MATLAB:

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', true);
    ft_plot_mesh(helmet, 'facecolor', 'lightgray')

    for i=1:numel(sensor)
        ft_plot_headshape(sensor(i), 'facecolor', 'r', 'facealpha', 1);
        ft_plot_headshape(holder(i), 'facecolor', 'g', 'facealpha', 1);
        ft_plot_headshape(cuttingtool(i), 'facecolor', 'b', 'facealpha', 0.5);
    end
    ft_headlight

Subsequently we export the translated and rotated objects to STL files, so that we can combine them with the shell to make the 3D model of the complete helmet.

    for i=1:numel(sensor)
        disp(chansel{i});
        filename = sprintf('spherical-sensor-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('spherical-holder-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('spherical-cuttingtool-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
    end

This results in 19 channels times 3 files, so 57 STL files on disk. In principle you only need the cuttingtool files, since the sensors don't need to be printed (these are basically only dummies for visualisation purposes), and multiple sensor holders can be 3D printed from the original sensor STL file without translatiopns and rotations.

In the 3rd secction of this tutorial we will explain how to combine the shell and the cuttingtool for the final helmet design.

### Flattened spherical helmet

This is again a helmet that starts with a design in Fusion (or your 3D design software of choice). It consists of a sphere, that to the bottom is extended with a cylinder and subsequently flattened on the left and right hemisphere. As before, there is a STL model for the headshape and an STL model for the shell that forms the helmet.  

{% include image src="/assets/img/tutorial/opm_helmet_design/figure2.png" width="600" %}

    headshape = ft_read_headshape('flattenedspherical-head.stl')
    helmet = ft_read_headshape('flattenedspherical-helmet.stl')

In the previous spherical helmet design , we had a hemisphere and hence the lowest sensors on the plane spanned by FPz-T7-T8-Oz needed to be _above_ the mid-plane of the sphere. Now the head and helmet extend further down, so we can also place the anatomical landmarks a bit lower. You could also design the helmet such that it is tilted, i.e. higher up at the front and further down at the back, and place the anatomical landmarks correspondingly. But here we continue with a straight helmet with the anatomical landmarks in the same plane with z = -10.

    nas = [+100 0 -10];
    ini = [-100 0 -10];
    lpa = [ 0 +80 -10];
    rpa = [ 0 -80 -10];

    headshape.fid.pos = [
        nas
        ini
        lpa
        rpa
    ];

    headshape.fid.label = {
        'nas'
        'ini'
        'lpa'
        'rpa'
    };

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin_light', 'axes', true)
    alpha 0.5 % slightly transparent
    ft_headlight

You should check that the LPA and RPA landmarks are on the flat pieces that represent the temples, as it is easy to get it wrong and have them 90 degrees rotated relative to the model. Furthermore, you can see in the image that the landmarks are now slightly _below_ the axes. That is in general not what we want, since the axes of the coordinate system pass through the fiducials. We could use **[ft_transform_geometry](/reference/ft_transform_geometry)** to move the head (and helmet) 10 mm up, and then give the fiducials a z-coordinate of 0 instead of -10. However, since it does not significantly affect the following steps, we will leave it like this and continue.

    % specify the XYZ coordinate system as ALS, i.e. anterior-left-superior
    % it is not CTF, since the axes don't go through the nasion and ears
    headshape.coordsys = 'als';
    helmet.coordsys = 'als';

Again we can distribute the electrode positions over the head surface.

    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = '1020';
    cfg.feedback = 'yes';
    elec = ft_electrodeplacement(cfg, headshape);

We make the same selection of 19 positions and use those to place the OPM sensors.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 5; % in mm

    cfg.template = 'fieldline_sensor.stl';
    sensor = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    holder = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_cuttingtool.stl';
    cuttingtool = ft_sensorplacement(cfg, headshape);

{% include markup/blue %}
#### Exercise

Use the same for-loop as before to plot the headshape, helmet, sensor holders and sensors. The template STL file for the individual OPM sensor not only consists of a 13x15x35 mm rectangular block, but also has a small off-center protrusion that represents where the cable is attached. The biaxial FieldLine v3 sensors have the laser pointing in the x-direction and can record the field along the y- and z-axis, which are the intermediate (15 mm) and long axes (35 mm). It is obvious that you will place the sensor with the cable pointing outward, but along the x- and y-direction in principle it fits in two ways, rotated 180 degrees.

What is the consequence on the signals that you record if you were to rotate the sensor 180 degrees?

What is the advantage (or disadvantage) of rotating some sensor holders by 90 degrees in the helmet design?
{% include markup/end %}

Again we write the translated and rotated sensor positions to STL files.

    for i=1:numel(sensor)
        disp(chansel{i});
        filename = sprintf('flattenedspherical-sensor-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('flattenedspherical-holder-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('flattenedspherical-cuttingtool-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
    end

### Individualized based on MRI

    mri = ft_read_mri('/Users/roboos/data/Subject01.mri');

    ft_determine_coordsys(mri, 'interactive', 'no')
    rotate3d

%%

    % disp(mri.fid.label)
    %     {'nas'}
    %     {'lpa'}
    %     {'rpa'}
    % 
    % disp(mri.fid.pos)
    %   116.0061   -0.0000   -0.0000
    %    -1.2560   71.9129    0.0000
    %     1.2560  -71.9129   -0.0000

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    cfg.flip = 'no';  % to determine the voxel indices
    ft_sourceplot(cfg, mri);

%%

    % cfg = [];
    % cfg.method = 'interactive';
    % cfg.viewmode = 'surface'; % or ortho
    % mri_realigned = ft_volumerealign(cfg, mri)

    % the original CTF coregistration was done with vitamine E markers in the ear canal
    % at the same position of the MEG head localizer coils 
    left_fid  = [ 29 145 155];
    right_fid = [144 142 158];

    % we now want to use the pre-auricular points rather than the ear canal
    % these are given as voxel indices, ranging from [1 1 1] to [256 256 256]
    nas_vox = [  87   60  116 ];
    lpa_vox = [  29  130  158 ];
    rpa_vox = [ 144  127  158 ];
    ini_vox = [  88  214  155 ];

    cfg = [];
    cfg.method = 'fiducial';
    cfg.fiducial.nas = nas_vox;
    cfg.fiducial.lpa = lpa_vox;
    cfg.fiducial.rpa = rpa_vox;
    cfg.coordsys = 'ctf';
    mri_realigned = ft_volumerealign(cfg, mri);

%%

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    cfg.flip = 'yes';
    ft_sourceplot(cfg, mri_realigned);

%%

    cfg = [];
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri_resliced);

    disp(mri_resliced.cfg)

%%

    cfg = [];
    cfg.xrange = [ -97.5000 157.5000] - 20;
    cfg.yrange = [-127.5000 127.5000];
    cfg.zrange = [ -87.5000 167.5000] - 10;
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri_resliced);

%%

    nas = ft_warp_apply(mri_realigned.transform, nas_vox)
    lpa = ft_warp_apply(mri_realigned.transform, lpa_vox)
    rpa = ft_warp_apply(mri_realigned.transform, rpa_vox)
    ini = ft_warp_apply(mri_realigned.transform, ini_vox)

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = ini; % also try nas, lpa, rpa
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri_resliced);

%%

    ft_determine_coordsys(mri_resliced, 'interactive', 'no')
    rotate3d

%%

    cfg = [];
    cfg.output = 'scalp';
    mri_segmented = ft_volumesegment(cfg, mri_resliced);

%%

    cfg = [];
    cfg.method = 'projectmesh';
    cfg.numvertices = 4000;
    headshape = ft_prepare_mesh(cfg, mri_segmented);

%%

    headshape.fid.pos = [
        nas
        lpa
        rpa
        ini
    ];

    headshape.fid.label = {
        'nas'
        'lpa'
        'rpa'
        'ini'
    };

    fidcolor = 'k';

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.5, 'fidmarker', '.', 'fidcolor', fidcolor, 'fidlabel', true, 'fidsize', 24)
    ft_headlight

%%

    cfg = [];
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_segmented)

%%

    mri_segmented.scalp(:,:,1:50) = 0;
    mri_segmented.airgap = imdilate(mri_segmented.scalp,  strel('sphere', 3));
    mri_segmented.helmet = imdilate(mri_segmented.airgap, strel('sphere', 7));

    mri_indexed = ft_checkdata(mri_segmented, 'segmentationstyle', 'indexed');

    cfg = [];
    cfg.funparameter = 'tissue';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    cfg.atlas = mri_indexed;
    ft_sourceplot(cfg, mri_indexed)

%%

    cfg = [];
    cfg.method = 'isosurface';
    cfg.numvertices = inf;
    cfg.tissue = 'airgap'; % this makes a surface from the outside of the "airgap" part
    inner = ft_prepare_mesh(cfg, mri_segmented);
    cfg.tissue = 'helmet';
    outer = ft_prepare_mesh(cfg, mri_segmented);

%%

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(inner, 'facecolor', 'r', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight
    rotate3d

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(outer, 'facecolor', 'g', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight
    rotate3d

%%

    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = '1020';
    elec = ft_electrodeplacement(cfg, headshape);

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 10;

    cfg.template = 'fieldline_sensor.stl';
    sensor = ft_sensorplacement(cfg, headshape);
    cfg.template = 'fieldline_holder.stl';
    holder = ft_sensorplacement(cfg, headshape);
    cfg.template = 'fieldline_cuttingtool.stl';
    cuttingtool = ft_sensorplacement(cfg, headshape);

%%

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(outer, 'facecolor', 'lightgray', 'facealpha', 0.5);

    for i=1:numel(sensor)
        ft_plot_headshape(sensor(i), 'facecolor', 'r', 'facealpha', 1);
        ft_plot_headshape(holder(i), 'facecolor', 'g', 'facealpha', 1);
        ft_plot_headshape(cuttingtool(i), 'facecolor', 'b', 'facealpha', 0.5);
        end
    ft_headlight

%%

    mkdir individualized

    for i=1:numel(sensor)
        disp(chansel{i});
        filename = sprintf('individualized/sensor-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('individualized/holder-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('individualized/cuttingtool-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
    end

### Individualized based on 3D scan

To be done, for this we need another subject that can be 3D scanned with a swimming cap on.

### Adapted to percentile of population

    mri = {};
    fiducial = {};

    for i=1:nsubj
        fprintf('------------------------------- %d -------------------------------\n', i);
        mrifile = sprintf('population/subject%03d.nii', i);
        fidfile = sprintf('population/fiducial%03d.mat', i);
        mri{i} = ft_read_mri(mrifile);
        mri{i}.coordsys = 'ctf';
        fiducial{i} = load(fidfile);
    end

%%

    ft_determine_coordsys(mri{3}, 'interactive', 'no')

%%

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = fiducial{3}.nas;
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri{3});

%%

    mri_resliced = {};
    mri_segmented = {};

    for i=1:nsubj
        fprintf('------------------------------- %d -------------------------------\n', i);
        cfg = [];
        cfg = [];
        cfg.xrange = [ -97.5000 157.5000] - 20;
        cfg.yrange = [-127.5000 127.5000];
        cfg.zrange = [ -87.5000 167.5000] - 10;
        mri_resliced{i} = ft_volumereslice(cfg, mri{i});

        cfg = [];
        cfg.output = 'scalp';
        mri_segmented{i} = ft_volumesegment(cfg, mri_resliced{i});
    end

%%

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = fiducial{4}.nas;
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_segmented{4});

%%

    mri_averaged = rmfield(mri_segmented{1}, 'cfg');
    for i=2:nsubj
        mri_averaged.scalp = mri_averaged.scalp + mri_segmented{i}.scalp;
    end
    mri_averaged.scalp = mri_averaged.scalp/nsubj;

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_averaged);

%%

    mri_90percentile       = mri_averaged;
    mri_90percentile.scalp = mri_averaged.scalp>=0.9;

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_90percentile);

%%

    mri_segmented = mri_90percentile;

    % we now do the same as with the individual MRI

    mri_segmented.scalp(:,:,1:50) = 0;
    mri_segmented.airgap = imdilate(mri_segmented.scalp,  strel('sphere', 3));
    mri_segmented.helmet = imdilate(mri_segmented.airgap, strel('sphere', 7));

    mri_indexed = ft_checkdata(mri_segmented, 'segmentationstyle', 'indexed');

    cfg = [];
    cfg.funparameter = 'tissue';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    cfg.atlas = mri_indexed;
    ft_sourceplot(cfg, mri_indexed)

    % from here on it continues as with the individual segmented MRI

## Part 2 - sensor distributions

### 10-20 distribution

### Equidistant

### From a template

### Interactive manual specification

## Part 3 - sensor orientations

## Part 4 - putting it together

Throughout this tutorial we are using [Autodesk Fusion](https://www.autodesk.com/products/fusion-360/), which is the software we are most familar with. You can sign up as a student or educator and get an educational license for free, or you can sign up for a free personal license. However, you can also [SolidWorks](https://www.solidworks.com), [FreeCAD](https://www.freecad.org), [Blender](https://www.blender.org), or other 3D design software. The required characteristics of the software are that it should be able to read and write STL files, and that it should be able to combine different geometries by means of (Boolean) addition and subtraction. For example, we have the STL file of the basic helmet shape from an MRI and the software should be able to cut off the lower part to accomodate the face, ears and neck. Furthermore, it should be able to remove material from the helmet shell based on the cutting tool "holes" that are defined as STL files.

## Summary and conclusion

What has been covered?

What has not been covered but is relevant in the context of the tutorial?

Provide links to suggested further reading, related FAQs and example scripts.
