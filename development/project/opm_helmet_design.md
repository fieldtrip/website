---
title: OPM helmet design
---

{% include /shared/development/warning.md %}

## Introduction

Measuring MEG with OPMs allows for flexible sensor placement. This is a significant departure from the rigidity of traditional SQUID-based systems, which confine participants within a fixed sensor array. With OPMs, researchers can now tailor the magnetometer configuration to an individual's unique head shape and size, a benefit that is particularly impactful when studying children or patient populations. The flexible placement allows sensors to be positioned close to the scalp and to brain regions expected to be activated.

The flexible OPM sensor placement opens the door for a range of novel experimental paradigms, as subjects are no longer tethered to a single, bulky dewar; they can potentially move, interact, and perform tasks in a much more naturalistic environment, thereby capturing brain activity that is more representative of real-world cognition. It should be noted, however, that OPMs in a helmet or cap that moves along with the participant will pick up considerable artifacts due to the OPMs moving and/or rotating through the residual magnetic field in the MSR. Extra shielding of the MSR with 3 instead of 2 layers of mu metal, and/or the use of nulling coils can reduce, but not completely eliminate these movement-related artifacts. Although denoising algorithms like HFC and AMM can help to clean the data from the artifacts caused by the movements, it should also always be considered whether the measurement is not better done with a head-fixed setup.

This tutorial aims to design OPM arrays with relatively uniform whole-head coverage. It does not include forward simulations of how a hypothetical dipole in the brain is visible on the OPM sensor array, and also does not cover how to place (a limited set of) OPMs to specifically target activity in a particular brain area. Furthermore, this tutorial will not discuss how OPM recordings are processed.

## Background

OPMs differ in size, depending on the manufacturer, but in general can be conceived as a rectangular box with a cable attached. For the FieldLine system, for example, the individual sensors are 13x15x35 mm. The OPMs are placed in holders which can in principle be mounted on a flexible cap just like EEG electrodes, but this comes with the potential disadvantage that the sensor orientations are not fixed and might vary depending on the head orientation and movements. With a fixed/rigid helmet as demonstrated in this tutorial, the position _and_ orientation of all sensors is well-defined.

The tutorial demonstrates the placement of FieldLine sensors, but is equally applicable to the sensors from QuSpin, Mag4health, or other companies. The OPM sensors and the holders are modeled (outside of MATLAB) as STL files; these sensors and holders are then distributed over the shell that forms the helmet. Furthermore, additional geometrical objects can be modeled as STL files and can be used as "tools" in the fabrication process to make holes in the helmet, or to add a small rim to facilitate gluing the sensor holder to the shell.

## Procedure

In this tutorial we separate the design of the complete OPM helmet into two parts: the shell, i.e. the basic helmet-shaped outline that fits around the head, and the sensor holders that are printed separately and that are glued into place. We will cover the process of designing custom OPM helmets for well-defined geometries (like a sphere), for individual participants, and to accommodate specific populations. Furthermore, it demonstrates how a given number of OPM sensors can be distributed over the helmet and how sensor orientations/rotations can be optimized. Finally, it discusses how the STL design files can be combined to make a model that can be 3D printed.

In part 1 we use different approaches to make the overall helmet shape.

- from a regular geometrical shape, like a sphere
- from an individual anatomical MRI
- from an individual 3D scan
- from a large sample of MRIs to make a population-optimized helmet

In part 2 we demonstrate different procedures to distribute the OPM sensors over the helmet:

- based on the 10-20 placement scheme for EEG electrodes
- based on an equidistant sensor distribution
- by interactively clicking to specify the sensor positions

In part 3 we look at the sensor orientation, i.e., how the sensors are rotated around their own axes. This is not too relevant for mono-axial and tri-axial sensors, but is highly relevant for bi-axial OPMs like the FieldLine v3 and Mag4Health sensors.

In part 4 we will discuss how the STL design files that have been generated are combined into a complete helmet design that can be 3D printed.

{% include markup/yellow %}
In the following we will be using [Autodesk Fusion](https://www.autodesk.com/products/fusion-360/). You can sign up as a student or educator and get an educational license for free, or you can sign up for a free personal license. Alternatively, you could also use [SolidWorks](https://www.solidworks.com), [FreeCAD](https://www.freecad.org), [Blender](https://www.blender.org), or other 3D design software.
{% include markup/end %}

## Part 1 - different helmet shapes

### Spherical helmet

For this helmet design we start with a sphere designed in Fusion. The center of the sphere is at the origin, and the radius is 100 mm. Furthermore, we have created a hemisphere shell that has an inner radius of 100 mm and a thickness of 10 mm. The sphere represents the head and the hemisphere shell that fits exactly around it acts as the helmet.

The figure below shows the sphere/head (red) with the hemisphere/helmet (grey), with a cut-out cross section so that you can see that they perfectly align.

{% include image src="/assets/img/tutorial/opm_helmet_design/figure1.png" width="600" %}

The STL file of the spherical head and hemisphere shell are available from our [download server](https://download.fieldtriptoolbox.org/tutorial/opm_helmet_design).

We read the two STL files into MATLAB and plot them together with the axes of the coordinate system. For this we use **[ft_read_headshape](/reference/fileio/ft_read_headshape)** which is a general function to read meshes, point clouds, 3D scans, etcetera.

    headshape = ft_read_headshape('spherical-head.stl')
    helmet = ft_read_headshape('spherical-helmet.stl')

    figure
    ft_plot_mesh(headshape, 'facecolor', 'skin_light', 'axes', true)
    ft_plot_mesh(helmet, 'facecolor', [0.7 0.7 0.7]) % grey
    ft_headlight % or lighting phong; camlight

{% include image src="/assets/img/tutorial/opm_helmet_design/spherical1.png" width="600" %}

The units of the geometrical objects are correctly recognized as 'mm'. We can also specify in which [head coordinate system](/faq/source/coordsys) they are specified, which will ensure the correct labels along the axes.

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

{% include image src="/assets/img/tutorial/opm_helmet_design/spherical2.png" width="600" %}

Subsequently, we call **[ft_electrodeplacement](/reference/ft_electrodeplacement)** to automatically determine the electrode positions.

    % this places a lot of electrodes, see https://doi.org/10.1016/s1388-2457(00)00527-7
    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = '1020';
    cfg.feedback = 'yes';
    elec = ft_electrodeplacement(cfg, headshape);

{% include image src="/assets/img/tutorial/opm_helmet_design/spherical3.png" width="600" %}

Note that the head is now rotated about 90 degrees around the z-axis and that it is looking towards the left of the screen, whereas previously we had rotated it so that the x-axis (going through the nose) was pointing towards the right.

In the next step, we use **[ft_sensorplacement](/reference/ft_sensorplacement)**, which reads the STL models for the sensor, the sensor holder, and for a "cutting tool" that will be used to make a hole in the helmet on the location where the sensor holder needs to be glued. The `ft_sensorplacement` function will translate the STL objects to each of the selected electrode locations on the head shape, rotate the STL object such that it is perpendicular to the surface, and then move it outward a little bit.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 5; % in mm

    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    [tmpcfg, holder] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_hole.stl';
    [tmpcfg, hole] = ft_sensorplacement(cfg, headshape);

This returns a cell-array for each of the objects, which we can plot in MATLAB:

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', true);
    ft_plot_mesh(helmet, 'facecolor', 'lightgray', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_plot_mesh(holder, 'facecolor', 'g', 'facealpha', 1, 'edgecolor', 'none');
    % ft_plot_mesh(hole, 'facecolor', 'b', 'facealpha', 0.5, 'edgecolor', 'none');
    % ft_plot_mesh(padding, 'facecolor', 'm', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight

{% include image src="/assets/img/tutorial/opm_helmet_design/spherical4.png" width="600" %}

Subsequently we export the translated and rotated objects to STL files, so that we can combine them with the shell to make the 3D model of the complete helmet.

    mkdir spherical

    for i=1:numel(sensor)
        disp(chansel{i});
        filename = sprintf('spherical/sensor-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('spherical/holder-%s.stl', chansel{i});
        ft_write_headshape(filename, holder(i), 'fileformat', 'stl');
        filename = sprintf('spherical/hole-%s.stl', chansel{i});
        ft_write_headshape(filename, hole(i), 'fileformat', 'stl');
        filename = sprintf('spherical/padding-%s.stl', chansel{i});
        ft_write_headshape(filename, padding(i), 'fileformat', 'stl');
    end

This results in 19 channels times 4 files, so 76 STL files on disk. In principle you only need the hole files, since the sensors don't need to be printed (these are basically only dummies for visualisation purposes), and multiple sensor holders can be 3D printed from the original sensor STL file without translations and rotations.

In part 4 of this tutorial we will explain how to combine the different STL files into the final helmet design.

### Flattened spherical helmet

This is again a helmet that starts with a design in Fusion (or your 3D design software of choice). It consists of a sphere, that to the bottom is extended with a cylinder and subsequently flattened on the left and right hemisphere. As before, there is a STL model for the headshape and an STL model for the shell that forms the helmet.  

{% include image src="/assets/img/tutorial/opm_helmet_design/figure2.png" width="600" %}

The STL files are again available from our [download server](https://download.fieldtriptoolbox.org/tutorial/opm_helmet_design).

    headshape = ft_read_headshape('flattenedspherical-head.stl')
    helmet = ft_read_headshape('flattenedspherical-helmet.stl')

In the previous spherical helmet design, we had a hemisphere and hence the lowest sensors on the plane spanned by FPz-T7-T8-Oz needed to be _above_ the mid-plane of the sphere. Now the head and helmet extend further down, so we can also place the anatomical landmarks a bit lower. You could also design the helmet such that it is tilted, i.e. higher up at the front and further down at the back, and place the anatomical landmarks correspondingly. But here we continue with a straight helmet, with the anatomical landmarks in the same plane with z = -10.

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

{% include image src="/assets/img/tutorial/opm_helmet_design/flattenedspherical1.png" width="600" %}

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

{% include image src="/assets/img/tutorial/opm_helmet_design/flattenedspherical2.png" width="600" %}

We make the same selection of 19 positions and use those to place the OPM sensors.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 5; % in mm

    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    [tmpcfg, holder] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_hole.stl';
    [tmpcfg, hole] = ft_sensorplacement(cfg, headshape);

We use the same code as before to plot the headshape, helmet and sensors.

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.5, 'axes', 1);
    ft_plot_mesh(helmet, 'facecolor', 'lightgray', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_plot_mesh(holder, 'facecolor', 'g', 'facealpha', 1, 'edgecolor', 'none');
    % ft_plot_mesh(hole, 'facecolor', 'b', 'facealpha', 0.5, 'edgecolor', 'none');
    % ft_plot_mesh(padding, 'facecolor', 'm', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight

{% include image src="/assets/img/tutorial/opm_helmet_design/flattenedspherical3.png" width="600" %}

{% include markup/blue %}
#### Exercise

The template STL file for the individual OPM sensor not only consists of a 13x15x35 mm rectangular block, but also has a small off-center protrusion that represents where the cable is attached. The biaxial FieldLine v3 sensors have the laser pointing in the x-direction and can record the field along the y- and z-axis, which are the intermediate (15 mm) and long axes (35 mm). It is obvious that you will place the sensor with the cable pointing outward, but the sensor in principle fits in two ways, rotated 180 degrees around its own z-axis.

What is the consequence on the signals that you record if you were to rotate the sensor 180 degrees?

What is the advantage (or disadvantage) of rotating some sensor holders by 90 degrees in the helmet design?
{% include markup/end %}

Again we write the translated and rotated sensor positions to STL files.

    for i=1:numel(sensor)
        disp(chansel{i});
        filename = sprintf('flattenedspherical-sensor-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('flattenedspherical-holder-%s.stl', chansel{i});
        ft_write_headshape(filename, holder(i), 'fileformat', 'stl');
        filename = sprintf('flattenedspherical-hole-%s.stl', chansel{i});
        ft_write_headshape(filename, hole(i), 'fileformat', 'stl');
    end

In part 4 of this tutorial we will explain how to combine the different STL files into the final helmet design.

### Individualized based on MRI

We start by reading the individual anatomical MRI, either from a NIFTI file or from DICOM files. With **[ft_determine_coordsys](/reference/ft_determine_coordsys)** we can see that - although the axes are indicated as "unknown" - the x-axis goes through the nasion and the y-axis goes through the pre-auricular points, consistent with the [CTF coordinate system](/faq/coordsys).

    mri = ft_read_mri('individual.nii');

    ft_determine_coordsys(mri, 'interactive', 'no')
    rotate3d

{% include image src="/assets/img/tutorial/opm_helmet_design/individual1.png" width="600" %}

In the next step we have to determine the location of the anatomical landmarks. We will use the nasion and left and right pre-auricular points to align the MRI with the desired coordinate system (which is not strictly needed here, as it already appears to be aligned), but we need the anatomical landmarks and also the inion for the sensor placement.

By clicking in the image, we can see the voxel indices which we write down and store in the script.

    cfg = [];
    cfg.method = 'ortho';
    cfg.flip = 'no'; % important for identifying voxel indices
    ft_sourceplot(cfg, mri);

    nas_vox = [ 102 217 123 ];
    ini_vox = [ 90   18 104 ];
    lpa_vox = [ 20  135 103 ];
    rpa_vox = [ 173 121  95 ];

{% include image src="/assets/img/tutorial/opm_helmet_design/individual2.png" width="600" %}

Although the MRI already seemed to be aligned with the CTF coordinate system, we use three of the anatomical landmarks anyway to ensure that it is properly aligned.

    cfg = [];
    cfg.method = 'fiducial';
    cfg.coordsys = 'ctf';
    cfg.fiducial.nas = nas_vox;
    cfg.fiducial.lpa = lpa_vox;
    cfg.fiducial.rpa = rpa_vox;
    mri_realigned = ft_volumerealign(cfg, mri);

We also want to know what the positions of the four landmarks are in head coordinates. We can check the position of each of the anatomical landmarks by using `cfg.location` in **[ft_sourceplot](/reference/ft_sourceplot)**, where `cfg.locationcoordinates` allows us to specify whether the three numbers are to be interpreted as (x, y, z) in head coordinates, or as (i, j, k) in voxel coordinates. The function **[ft_transform_geometry](/reference/utilities/ft_transform_geometry)** allows us to apply a geometrical transformation on a Nx3 set of points or on a geometrical object like a mesh.

    nas = ft_transform_geometry(mri.transform, nas_vox);
    ini = ft_transform_geometry(mri.transform, ini_vox);
    lpa = ft_transform_geometry(mri.transform, lpa_vox);
    rpa = ft_transform_geometry(mri.transform, rpa_vox);

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = nas; % nas, ini, lpa, rpa
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri_realigned);

{% include image src="/assets/img/tutorial/opm_helmet_design/individual3.png" width="600" %}

The axes of the coordinate system are not aligned with the voxels in the MRI volume. Furthermore, we don't know for sure that the voxels are isotropic, i.e., uniform in size. For the subsequent image processing we want the voxels to be exactly 1x1x1 mm hence we reslice the MRI.

    cfg = [];
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri_resliced);

{% include image src="/assets/img/tutorial/opm_helmet_design/individual4.png" width="600" %}

Looking at the resliced image, we see that the head does not fit so well within the "box" that was automatically fitted around it. The `cfg` structure in the output of the function usually contains the details used in the computation, so we can take that as starting point. We can modify the range and shift the box to the back (and hence the head to the front).

    disp(mri_resliced.cfg)

    cfg = [];
    cfg.xrange = [ -97.5000 157.5000] - 30;
    cfg.yrange = [-127.5000 127.5000];
    cfg.zrange = [ -87.5000 167.5000] - 5;
    mri_resliced = ft_volumereslice(cfg, mri_realigned);

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri_resliced);

We plot it again, and repeat it until we are happy with what we see.

{% include image src="/assets/img/tutorial/opm_helmet_design/individual5.png" width="600" %}

Subsequently, we proceed by segmenting the scalp and by creating a mesh that describes the outline of the scalp.

    cfg = [];
    cfg.output = 'scalp';
    mri_segmented = ft_volumesegment(cfg, mri_resliced);

    cfg = [];
    cfg.method = 'projectmesh';
    cfg.numvertices = 4000;
    headshape = ft_prepare_mesh(cfg, mri_segmented);

If we add the previously determined anatomical landmarks to the headshape structure, the **[ft_plot_headshape](/reference/ft_plot_headshape)** function will add those to the figure.

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

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.7, 'fidmarker', 'o', 'fidcolor', 'k', 'fidlabel', true, 'fidsize', 24)
    ft_headlight

{% include image src="/assets/img/tutorial/opm_helmet_design/individual6.png" width="600" %}

The segmented scalp is represented as a binary array, which when plotted shows as a black-and-white image. We can use tools from the MATLAB Image Processing Toolbox to adjust the segmentation.

    cfg = [];
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_segmented)

{% include image src="/assets/img/tutorial/opm_helmet_design/individual7.png" width="600" %}

We need a helmet around the head that gives a little bit of space, so we will "inflate" the scalp segmentation by one voxel (which is 1 mm) to make an airgap. Furthermore, we "inflate" the airgap again with 5 voxels to make a 5 mm thick shell all around the head.

Since we don't need the helmet shell to go all the way down, we mark the lowest 50 slices of the MRI as "not-scalp". Then we use the MATLAB **[imdilate](https://nl.mathworks.com/help/images/ref/imdilate.html)** function to dilate or inflate the binary image.

    mri_segmented.scalp(:,:,1:50) = 0;
    mri_segmented.airgap = imdilate(mri_segmented.scalp,  strel('sphere', 1));
    mri_segmented.helmet = imdilate(mri_segmented.airgap, strel('sphere', 5));

The `mri_segmented` structure now contains three binary volumes that largely overlap. For visualisation purposes we can change those into a single one with an indexed representation, i.e. where the tissues are not binary, but marked as 1, 2, 3. See **[ft_datatype_segmentation](/reference/ft_datatype_segmentation)** for details.

    mri_indexed = ft_checkdata(mri_segmented, 'segmentationstyle', 'indexed');

    cfg = [];
    cfg.funparameter = 'tissue';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    cfg.atlas = mri_indexed;
    ft_sourceplot(cfg, mri_indexed)

{% include image src="/assets/img/tutorial/opm_helmet_design/individual8.png" width="600" %}

From the segmented airgap and helmet, we construct surface meshes that describe the inside of the helmet (i.e. the outside of the airgap volume) and the outside of the helmet.

    cfg = [];
    cfg.method = 'projectmesh';
    cfg.numvertices = 4000;

    cfg.tissue = 'airgap'; % this makes a surface from the outside of the "airgap" part
    tmp = removefields(mri_segmented, {'scalp', 'helmet'}); % FIXME this is a hack that should be resolved
    inside = ft_prepare_mesh(cfg, tmp);

    cfg.tissue = 'helmet';
    tmp = removefields(mri_segmented, {'scalp', 'airgap'}); % FIXME this is a hack that should be resolved
    outside = ft_prepare_mesh(cfg, tmp);

We can plot the meshes that describe the inside and outside of the helmet. 

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(inside, 'facecolor', 'r', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight
    rotate3d

{% include image src="/assets/img/tutorial/opm_helmet_design/individual9.png" width="600" %}

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(outside, 'facecolor', 'g', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight
    rotate3d

{% include image src="/assets/img/tutorial/opm_helmet_design/individual10.png" width="600" %}

You can see that they extend all the way to the nose, and that the bottom is closed; that is something we will fix later by editing the mesh in Fusion.

The next step is to determine the desired position of the sensors. As before, we will here use the 10-20 EEG electrode placement scheme.

    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = '1020';
    elec = ft_electrodeplacement(cfg, headshape);

{% include image src="/assets/img/tutorial/opm_helmet_design/individual11.png" width="600" %}

We take a subset of 19 electrode positions and use those to position the STL model of the sensors, the sensor holders, and the holes relative to the headshape and helmet.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 10;

    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    [tmpcfg, holder] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_hole.stl';
    [tmpcfg, hole] = ft_sensorplacement(cfg, headshape);

We can plot the head with the outside of the helmet and all STL objects in one figure to check their spatial alignment.

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(outside, 'facecolor', 'lightgray', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_plot_mesh(holder, 'facecolor', 'g', 'facealpha', 1, 'edgecolor', 'none');
    % ft_plot_mesh(hole, 'facecolor', 'b', 'facealpha', 0.5, 'edgecolor', 'none');
    % ft_plot_mesh(padding, 'facecolor', 'm', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight

{% include image src="/assets/img/tutorial/opm_helmet_design/individual12.png" width="600" %}

If we are happy with the sensor distribution, we can export all geometrical objects to STL files for postprocessing (see part 4).

    mkdir individual

    ft_write_headshape('individual/helmet-inside.stl', inside, 'fileformat', 'stl');
    ft_write_headshape('individual/helmet-outside.stl', outside, 'fileformat', 'stl');

    for i=1:numel(sensor)
    disp(chansel{i});
        filename = sprintf('individual/sensor-%s.stl', chansel{i});
        ft_write_headshape(filename, sensor(i), 'fileformat', 'stl');
        filename = sprintf('individual/holder-%s.stl', chansel{i});
        ft_write_headshape(filename, holder(i), 'fileformat', 'stl');
        filename = sprintf('individual/hole-%s.stl', chansel{i});
        ft_write_headshape(filename, hole(i), 'fileformat', 'stl');
        filename = sprintf('individual/padding-%s.stl', chansel{i});
        ft_write_headshape(filename, padding(i), 'fileformat', 'stl');
    end

In part 4 of this tutorial we will explain how to combine the different STL files into the final helmet design.

### Individualized based on 3D scan

FIXME for this we need another subject that can be 3D scanned while wearing a swimming cap

### Adapted to percentile of population

Rather than making an individualized helmet for each subject, you can also make a helmet that fits your whole population, or a large fraction of your population. This is of course what the OPM companies try to achieve with their helmets, but if you are working with a specific population, for example 4-year-olds, then the OPM companies might not have the right size helmet for you. The following section shows how a series of anatomical MRIs can be processed and combined to make a helmet that will fit a certain percentile of your population - in this case 90%.

This approach does assume that you have imaging data available for your population. If you don't have the scans for your specific subjects (which is quite likely, especially if they are babies or kids), then you may be able to use an existing database with age-matched anatomical MRI data, for example the [Neurodevelopmental MRI Database](https://jerlab.sc.edu/projects/neurodevelopmental-mri-database/) from John E. Richards.

In this case we are not going to use a large database with MRIs, but rather a small set to demonstrate the principle. This set of MRIs was constructed by taking an individual subject's MRI and scaling, rotating and translating that, to create some variability in the head size and in the position relative to the MRI scanner field-of-view.

As before, the data is available from our [download server](https://download.fieldtriptoolbox.org/tutorial/opm_helmet_design).

We have prepared 10 different anatomical MRIs:

    >> ls population/*.nii
    population/subject001.nii
    population/subject002.nii
    ...
    population/subject010.nii

Since they all need to be aligned to each other, we have also prepared 10 corresponding files that contain the anatomical landmarks:

    >> ls population/*.mat
    population/fiducial001.mat
    population/fiducial002.mat
    ...
    population/fiducial010.mat

The anatomical MRIs are not that large, so we start by reading them all in memory.

    nsubj = 10;

    mri = cell(1,nsubj);
    fiducial = cell(1,nsubj);

    for i=1:nsubj
        fprintf('------------------------------- %d -------------------------------\n', i);
        mrifile = sprintf('population/subject%03d.nii', i);
        fidfile = sprintf('population/fiducial%03d.mat', i);
        mri{i} = ft_read_mri(mrifile);
        mri{i}.coordsys = 'ctf';
        fiducial{i} = load(fidfile);
    end

There are two cell-arrays, one with the MRIs and the other with the anatomical landmarks.

The individual subjects' MRIs have all been aligned to the CTF coordinate system with the x-axis going through the nose. We can confirm this with ft_determine_coordsys.

    ft_determine_coordsys(mri{1}, 'interactive', 'no')

Note however that the fiducial locations are not identical, since some heads are smaller than others.

    >> fiducial{2}
    struct with fields:
        ini: [-94.3201 1.0090 29.7481]
        lpa: [2.9110 68.1849 -1.4211e-14]
        nas: [82.8648 -2.8422e-14 0]
        rpa: [-2.9110 -68.1849 -7.1054e-15]

    >> fiducial{2}
    struct with fields:
        ini: [-91.2260 1.1314 32.6141]
        lpa: [2.2625 75.9092 2.1316e-14]
        nas: [80.3743 2.8422e-14 1.4211e-14]
        rpa: [-2.2625 -75.9092 7.1054e-15]

The nasion point is in both cases along the x-axis since the y- and z-value are zero (up to some numerical precision error).

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

## Part 3 - sensor orientation and rotation

Besides determining _where_ to place the sensors on the head or helmet, we also need to decide how the sensors should be oriented. By default `ft_sensorplacement` will orient the sensors (and sensor holders, etc.) perpendicular to the headshape surface. This defines two of the three rotations, but still leaves the rotation around the (radial) axis to be determined.

In general the orientation and rotation are determined by a rotation around the z-axis, followed by a rotation around the y- and x-axis. Since rotations are not [commutative](https://en.wikipedia.org/wiki/Commutative_property), the order in which they are applied matters. These rotations can be specified as `cfg.rotz`, `cfg.roty` and `cfg.rotx`, respectively. Note that `ft_sensorplacement` also returns the `cfg` structure as it was used in the placement, so if you did not explicitly specify the rotations in the input `cfg`, the output `cfg` will have the rotations, which allows you to change them and re-run the placement.

### Sensor orientation relative to the head

By default the sensor is oriented perpendicular to the headshape, and no explicit rotation around its z-axis is done. 

    headshape = ft_read_headshape('spherical-head.stl')

    nas = [+100 0 0];
    ini = [-100 0 0];
    lpa = [0 +100 0];
    rpa = [0 -100 0];

    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = '1020';
    cfg.feedback = 'yes';
    elec = ft_electrodeplacement(cfg, headshape);

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 2; % two mm away from the surface 
    cfg.template = 'fieldline_sensor.stl';
    [outcfg, sensor] = ft_sensorplacement(cfg, headshape);

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_headlight

The output configuration contains the rotations around the three axes that were used.

    disp(outcfg)

We can also specify that we don't want any rotations at all

    cfg = [];
    cfg.rotx = zeros(19,1);
    cfg.roty = zeros(19,1);
    cfg.rotz = zeros(19,1);
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 2; % two mm away from the surface 
    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_headlight

or that we want to rotate all sensors in a particular direction.

    cfg = [];
    cfg.rotx = zeros(19,1);
    cfg.roty = ones(19,1) * 45; % degrees
    cfg.rotz = zeros(19,1);
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 2; % two mm away from the surface 
    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_headlight

In the individual helmet design we identified that the sensors close to the ears had an orientation that was suboptimal, due to the low resolution mesh having a bump close to the ear, and due to some compression of the soft tissue by the sound-isolating headphone. We can identify the two sensors on T7 and T8, and change those accordingly:

    selT7 = find(strcmp(tmpcfg.channel, 'T7'));
    selT8 = find(strcmp(tmpcfg.channel, 'T8'));

    cfg = [];
    cfg.rotx = outcfg.rotx;
    cfg.roty = outcfg.roty;
    cfg.rotz = outcfg.rotz;
    % do not rotate these around the y-axis, which connects the ears
    cfg.rotz(selT7) = 0;
    cfg.rotz(selT8) = 0;
    % rotate plusminus 90 degrees around the x-axis, which goes to the nose
    cfg.rotx(selT7) = +90;
    cfg.rotx(selT8) = -90;
    % ... the remainder would be the same as before

{% include markup/blue %}
#### Exercise
Return to the individual MRI-based helmet design and update the orientation of the T7 and T8 sensor such that they are along the y-axis.
{% include markup/end %}

As an alternative to specifying the rotations, you can specify the orientation of each of the electrodes in the input `elec` structure. This is similar to specifying the coil orientation for MEG sensor arrays, and for electrodes also used in ft_plot_sens when you show the electrode as a disc. The following takes the line connecting the point (0,0,40), which is more or less in between T7 and T8, and each of the electrodes, and uses that line to determine the orientation of each electrode.)

    for i=1:numel(elec1020.label)
        elec.elecori(i,:) = elec.elecpos(i,:) - [0 0 40];
        elec.elecori(i,:) = elec.elecori(i,:) / norm(elec.elecori(i,:)); % unit length
    end

{% include markup/blue %}
#### Exercise
Return to the individual MRI-based helmet design and use the radial direction as seen from the point (0, 0, 0) and the point (0, 0, 40). Which orientation do you like better?
{% include markup/end %}

### Sensor rotation around its axis

Biaxial OPM sensors typically record the signal in one radial direction (i.e., perpendicular to the surface) and one tangential direction, which is also the most optimal configuration (see Schoffelen et al. 2025 [Optimal configuration of on-scalp OPMs with fixed channel counts](https://doi.org/10.1162/imag.a.22)). For the tangential direction you have to choose how to rotate the sensor around its axes. An optimal sampling of the environmental noise (useful for noise suppression) is obtained with alternating directions of neighbouring sensors, where the tangential axis of a sensor is 90 degrees rotated relative to that of its neighbours.

We can use the rotation around the z-axis to determine how sensors are rotated around their own radial axis:

    cfg = [];
    cfg.rotx = zeros(19,1);
    cfg.roty = zeros(19,1);
    cfg.rotz = ones(19,1) * 45; % degrees
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 2; % two mm away from the surface 
    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 1, 'edgecolor', 'none');
    ft_headlight

Of course this is best combined with first determining the overall orientation (rotation around x and y), then plotting, and then writing down how much you want each sensor to be rotated around its own axis.

    % this is what you would write down by hand
    correction = {
        'Cz'    0 0 0
        }

    cfg = [];
    cfg.elec = elec1020;
    cfg.channel = chansel;  % subset of 19 locations
    cfg.rotx = outcfg.rotx; % 19x1 vector
    cfg.roty = outcfg.roty; % 19x1 vector
    cfg.rotz = outcfg.rotz; % 19x1 vector

    % chansel is a cell-array with the selected locations of the 1020 system at which sensors are placed
    for i=1:size(correction,1)
      lab = correction{i,1};
      dx  = correction{i,2};
      dy  = correction{i,3};
      dz  = correction{i,4};
      cfg.rotx(strcmp(chansel, lab)) = cfg.rotx(strcmp(chansel, lab)) + dx;
      cfg.roty(strcmp(chansel, lab)) = cfg.roty(strcmp(chansel, lab)) + dy;
      cfg.rotz(strcmp(chansel, lab)) = cfg.rotz(strcmp(chansel, lab)) + dz;
    end

    % ... the remainder would be the same as before

To get a nice distribution of sensor positions, orientations relative to the scalp, and rotations around their own axis, you will probably want to iterate multiple times and plot in between.

FIXME show how to plot the labels

## Part 4 - putting the helmet design together

Throughout this tutorial we are using [Autodesk Fusion](https://www.autodesk.com/products/fusion-360/), which is the software we are most familiar with. You can sign up as a student or educator and get an educational license for free, or you can sign up for a free personal license. However, you can also use [SolidWorks](https://www.solidworks.com), [FreeCAD](https://www.freecad.org), [Blender](https://www.blender.org), or other 3D design software. The required characteristics of the software are that it should be able to read and write STL files, and that it should be able to combine different geometries by means of (Boolean) addition and subtraction. For example, we have the STL file of the basic helmet shape from an MRI and the software should be able to cut off the lower part to accommodate the face, ears and neck. Furthermore, it should be able to remove material from the helmet shell based on the cutting tool "holes" that are defined as STL files.

FIXME insert some screenshots and explanation

### Padding

The padding is an STL object that is used to make the helmet locally thicker or to give it more "body" at the location wher ethe sensor holder needs to be glued in. This is needed if you have a thin and lightweight helmet shell and if the sensor holder is placed somewhere with a lot of curvature. The padding STL object will be mainly fall inside the helmet and will largely be cut away by the hole STL object.

## Part 5 - making grad structure and a layout

To reconstruct the sources underlying the MEG recordings and for some of the denoising algorithms (specifically `ft_denoise_hfc`, `ft_denoise_amm`, and `ft_denoise_sss`) you need the specification of the [sensor definition](/faq/source/sensors_definition/). Although OPMs are commonly magnetometers, in FieldTrip we refer to this sensor definition as the `grad` structure. If you read in data from a SQUID MEG recording, you will get the `grad` structure in the raw data representation. If you read in data from an OPM MEG recording (for example a fif file), you might also get the `grad` structure in the raw data representation. In some cases the sensor positions are known to the OPM system (for example with the FieldLine smart helmet) or have been added by postprocessing the recording with custom software to add the sensor localization (for example with the QuSpin Halo). If you use a custom designed and 3D-printed OPM helmet, the OPM acquisition software will record the MEG signals just fine, but does not know where the sensors are or what their orientation is. Hence you have to construct a `grad` structure to complement the subsequent analysis.

FIXME document how to obtain the grad structure

For visualisation of the topographic distribution of the ERFs or TFRs you need a layout that maps the 3D sensor positions onto a 2D plane. For that you can use the `grad` structure, as explained in [this tutorial](/tutorial/plotting/layout/).

## Summary and conclusion

What has been covered?

What has not been covered but is relevant in the context of the tutorial?

Provide links to suggested further reading, related FAQs and example scripts.
