---
title: Designing an OPM helmet
category: tutorial
tags: [opm]
---

{% include /shared/development/warning.md %}

## Introduction

Measuring MEG with OPMs allows for flexible sensor placement. This is a significant departure from the rigidity of traditional SQUID-based systems, which confine participants within a fixed sensor array. With OPMs, researchers can now tailor the magnetometer configuration to an individual's unique head shape and size, a benefit that is particularly impactful when studying children or patient populations. The flexible placement allows sensors to be positioned close to the scalp and to brain regions expected to be activated.

The flexible OPM sensor placement opens the door for a range of novel experimental paradigms, as subjects are no longer tethered to a single, bulky dewar; they can potentially move, interact, and perform tasks in a much more naturalistic environment, thereby capturing brain activity that is more representative of real-world cognition. It should be noted, however, that OPMs in a helmet or cap that moves along with the participant will pick up considerable artifacts due to the OPMs moving and/or rotating through the residual magnetic field in the MSR. Extra shielding of the MSR with 3 instead of 2 layers of mu metal, and/or the use of nulling coils can reduce, but not completely eliminate these movement-related artifacts. Although denoising algorithms like HFC and AMM can help to clean the data from the artifacts caused by the movements, it should also always be considered whether the measurement is not better done with a head-fixed setup.

This tutorial aims to design OPM arrays with relatively uniform whole-head coverage. It does not include forward simulations of how a hypothetical dipole in the brain is visible on the OPM sensor array, and also does not cover how to place (a limited set of) OPMs to specifically target activity in a particular brain area. Furthermore, this tutorial will not discuss how OPM recordings are processed.

## Background

OPMs differ in size, depending on the manufacturer, but in general can be conceived as a rectangular box with a cable attached. For the FieldLine system, for example, the individual sensors are 15x13x35 mm. The OPMs are placed in holders which can in principle be mounted on a flexible cap just like EEG electrodes, but this comes with the potential disadvantage that the sensor orientations are not fixed and might vary depending on the head orientation and movements. With a fixed/rigid helmet as demonstrated in this tutorial, the position _and_ orientation of all sensors is well-defined.

The tutorial demonstrates the placement of FieldLine sensors, but is equally applicable to the sensors from QuSpin, Mag4health, or other companies. The OPM sensors and the holders are modeled (outside of MATLAB) as STL files; these sensors and holders are then distributed over the shell that forms the helmet. Furthermore, additional geometrical objects can be modeled as STL files and can be used as "tools" in the fabrication process to make holes in the helmet, or to add a small rim to facilitate gluing the sensor holder to the shell.

## Procedure

In this tutorial we will separate the design into multiple steps.

In part 1 we use different approaches to make the overall helmet shape.

- from a regular geometrical shape, like a sphere
- from an individual anatomical MRI
- from an individual 3D scan
- from a large sample of MRIs to make a population-optimized helmet

In part 2 we demonstrate different procedures to distribute the OPM sensors over the helmet:

- based on the 10-20 placement scheme for EEG
- based on an equidistant distribution
- using templates, for example existing EEG electrode distributions
- by interactively clicking to specify the sensor positions

In part 3 we look at how the sensor orientation and rotation can be optimized. This is not relevant for mono-axial sensors, but is especially important for bi-axial OPMs, like the FieldLine v3 and Mag4Health sensors.

In part 4 we will show how the STL files that have been generated are combined into a complete helmet that can be 3D printed. This is not done in MATLAB, but in 3D design software like Fusion. From experience we know that it is best to print the sensor holders separately and to glue them into place, so the helmet-shaped shell will have a hole with a rim around it for each sensor holder.

Finally, in part 5 we will generate the gradiometer definition that can be used by FieldTrip during OPM data analysis for forward and inverse source modelling, and the layout for topographic plotting.

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

In the next step, we use **[ft_sensorplacement](/reference/ft_sensorplacement)**, which reads the STL models for the sensor, the sensor holder, for some padding to create an elevated rim, and for an STL model of a hole where the sensor holder needs to be glued. The **[ft_sensorplacement](/reference/ft_sensorplacement)** function will translate the STL objects to each of the selected electrode locations on the head shape, rotate the STL object such that it is perpendicular to the surface, and then move it outward a little bit.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.outwardshift = 10/2; % the helmet is 10 mm thick, the bottom of the sensor holder will be halfway in

    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    [tmpcfg, holder] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_hole.stl';
    [tmpcfg, hole] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_padding.stl';
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

You should check that the LPA and RPA landmarks are on the flat pieces that represent the temples, as it is easy to get it wrong and have them 90 degrees rotated relative to the model. Furthermore, you can see in the image that the landmarks are now slightly _below_ the axes. That is in general not what we want, since the axes of the coordinate system should pass through the fiducials. We could use **[ft_transform_geometry](/reference/ft_transform_geometry)** to move the head (and helmet) 10 mm up, and then give the fiducials a z-coordinate of 0 instead of -10. However, since it does not really affect the following steps, we will leave it like this and continue.

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
    cfg.outwardshift = 10/2; % the helmet is 10 mm thick, the bottom of the sensor holder will be halfway in

    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    [tmpcfg, holder] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_hole.stl';
    [tmpcfg, hole] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_padding.stl';
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

The template STL file for the individual OPM sensor not only consists of a 15x13x35 mm rectangular block, but also has a small off-center protrusion that represents where the cable is attached. The bi-axial FieldLine v3 sensors have the laser pointing in the x-direction and can record the field along the y- and z-axis, which are the intermediate (15 mm) and long axes (35 mm). It is obvious that you will place the sensor with the cable pointing outward, but the sensor in principle fits in two ways, rotated 180 degrees around its own z-axis.

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
        filename = sprintf('flattenedspherical-padding-%s.stl', chansel{i});
        ft_write_headshape(filename, padding(i), 'fileformat', 'stl');
    end

In part 4 of this tutorial we will explain how to combine the different STL files into the final helmet design.

### Individualized based on MRI

We start by reading the individual anatomical MRI, either from a NIfTI file or from DICOM files. With **[ft_determine_coordsys](/reference/ft_determine_coordsys)** we can see that - although the axes are indicated as "unknown" - the x-axis goes through the nasion and the y-axis goes through the pre-auricular points, consistent with the [CTF coordinate system](/faq/coordsys).

    mri = ft_read_mri('individual.nii');

    ft_determine_coordsys(mri, 'interactive', 'no')
    rotate3d

{% include image src="/assets/img/tutorial/opm_helmet_design/individual1.png" width="600" %}

In the next step we have to determine the location of the anatomical landmarks. We will use the nasion and left and right pre-auricular points to align the MRI with the desired coordinate system (which is not strictly needed here, as it already appears to be aligned), but we also need the anatomical landmarks including the inion for the sensor placement.

By clicking in the image we can see the voxel indices, which we write down and store in the script.

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

    % convert from voxel indices to head coordinates
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

The axes of the coordinate system are not aligned with the voxels in the MRI volume. Furthermore, we don't know for sure that the voxels are isotropic, i.e., uniform in size. For the subsequent image processing we want the voxels to be exactly 1x1x1 mm, hence we reslice the MRI.

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

We plot it again and repeat, until we are happy with what we see.

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

We need a helmet around the head that gives a little bit of space, so we will "inflate" the scalp segmentation by one voxel (which is 1 mm) to make an air gap. Furthermore, we "inflate" the air gap again with 5 voxels to make a 5 mm thick shell all around the head.

Since we don't need the helmet shell to go all the way down, we mark the lowest 50 slices of the MRI as "not-scalp". Then we use the MATLAB **[imdilate](https://nl.mathworks.com/help/images/ref/imdilate.html)** function to dilate or inflate the binary image.

    mri_segmented.scalp(:,:,1:50) = 0;
    mri_segmented.airgap = imdilate(mri_segmented.scalp,  strel('sphere', 1));
    mri_segmented.helmet = imdilate(mri_segmented.airgap, strel('sphere', 5));

The `mri_segmented` structure now contains three binary volumes that largely overlap. For visualisation purposes we can change those into a single one with an indexed representation, i.e. where the tissues are not separate binary fields in the structure, but a single field with numeric values as 1, 2, 3. See **[ft_datatype_segmentation](/reference/ft_datatype_segmentation)** for details.

    mri_indexed = ft_checkdata(mri_segmented, 'segmentationstyle', 'indexed');

    cfg = [];
    cfg.funparameter = 'tissue';
    cfg.location = [0 0 0];
    cfg.locationcoordinates = 'head';
    cfg.atlas = mri_indexed;
    ft_sourceplot(cfg, mri_indexed)

{% include image src="/assets/img/tutorial/opm_helmet_design/individual8.png" width="600" %}

{% include markup/blue %}
#### Exercise
Get a better understanding of the indexed representation of the segmentation by using another colormap and by explicitly specifying the "functional" colors that are plotted. Add the following to the configuration for **[ft_sourceplot](/reference/ft_sourceplot)**. See also **[ft_colormap](/reference/plotting/ft_colormap)**.

    cfg.funcolormap = ft_colormap('flag', 4); % or prism, or Set1
    cfg.funcolorlim = [0 4];)

{% include markup/end %}

From the binary images of the segmented air gap and helmet, we construct surface meshes that describe the inside of the helmet (i.e. the outside of the air gap) and the outside of the helmet.

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

The next step is to determine the desired position of the sensors. As before, we will here use the 10-20 electrode placement scheme.

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
    cfg.outwardshift = 5/2 + 1; % the helmet is 5 mm thick, plus the 1 mm airgap

    cfg.template = 'fieldline_sensor.stl';
    [tmpcfg, sensor] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_holder.stl';
    [tmpcfg, holder] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_hole.stl';
    [tmpcfg, hole] = ft_sensorplacement(cfg, headshape);

    cfg.template = 'fieldline_padding.stl';
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

{% include markup/yellow %}
If you look closely at the 3D figure, you can see that the sensors located at T7 and T8 are tilted to the front. This is due to them being placed on the flank of the bump caused by the (low resolution) ear. Furthermore, the sound-isolating headphones used during the MRI scan caused some indentation on the cheeks. For now we leave it like this, but in part 3 you will learn how to optimize the sensor orientations.
{% include markup/end %}

If we are (for now) happy with the sensor distribution, we can export all geometrical objects to STL files for postprocessing, which is explained in part 4.

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

In this tutorial we are not going to use a large database with MRIs but only a small set of MRIs for practical and privacy reasons. This set of MRIs was constructed by taking an individual subject's MRI that was scaled, rotated and translated, to create some variability in the head size and in the position relative to the MRI scanner field-of-view.

As before, the data is available from our [download server](https://download.fieldtriptoolbox.org/tutorial/opm_helmet_design). You need to download the 10 `.nii` files from the population directory.

We have prepared 10 different anatomical MRIs:

    >> ls population/*.nii
    population/subject001.nii
    population/subject002.nii
    ...
    population/subject010.nii

Since they all need to be aligned to each other, we have also prepared corresponding MATLAB files with the anatomical landmarks:

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
        mri{i} = ft_read_mri(mrifile);
        mri{i}.coordsys = 'ctf';
        
        fidfile = sprintf('population/fiducial%03d.mat', i);
        fiducial{i} = load(fidfile);
    end

There are two cell-arrays, one with the MRIs and the other with the anatomical landmarks.

The individual subjects' MRIs have all been aligned to the CTF coordinate system with the x-axis going through the nose. We can confirm this with **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)**.

    ft_determine_coordsys(mri{1}, 'interactive', 'no')

Note that the fiducial locations are not identical, since some heads are smaller than others.

    >> fiducial{1}
    struct with fields:
        nas: [82.8648 -2.8422e-14 0]
        ini: [-94.3201 1.0090 29.7481]
        lpa: [2.9110 68.1849 -1.4211e-14]
        rpa: [-2.9110 -68.1849 -7.1054e-15]

    >> fiducial{2}
    struct with fields:
        nas: [80.3743 2.8422e-14 1.4211e-14]
        ini: [-91.2260 1.1314 32.6141]
        lpa: [2.2625 75.9092 2.1316e-14]
        rpa: [-2.2625 -75.9092 7.1054e-15]

You can see that the nasion is in both cases along the x-axis, since its y- and z-value are zero (up to some numerical precision error). But for subject 1 the head is slightly larger than for subject 2.

We can check the position of the nasion, or any of the other anatomical landmarks.

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = fiducial{3}.nas;
    cfg.locationcoordinates = 'head';
    ft_sourceplot(cfg, mri{1});

{% include image src="/assets/img/tutorial/opm_helmet_design/population1.png" width="600" %}

We reslice all of the MRIs so that the voxels are isotropic and aligned with the head coordinate system. Furthermore, as before, we segment the MRIs to get the head or scalp surface.

    mri_resliced = {};
    mri_segmented = {};

    for i=1:nsubj
        fprintf('------------------------------- %d -------------------------------\n', i);
        cfg = [];
        cfg.xrange = [ -97.5000 157.5000] - 30;
        cfg.yrange = [-127.5000 127.5000];
        cfg.zrange = [ -87.5000 167.5000] - 5;
        mri_resliced{i} = ft_volumereslice(cfg, mri{i});

        cfg = [];
        cfg.output = 'scalp';
        mri_segmented{i} = ft_volumesegment(cfg, mri_resliced{i});
    end

We can check the segmentation, again by specifically looking at the cross-section of one of the anatomical landmarks.

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = fiducial{1}.nas;
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_segmented{1});

{% include image src="/assets/img/tutorial/opm_helmet_design/population2.png" width="600" %}

Now that we know which voxels correspond to the head, we can combine the binary segmentations which have the value of 0 for air and 1 for the head or scalp. To do that, we simply copy the one from subject 1, and for each of the subsequent subjects we add the segmentation. The consequence is that for a voxel that is part of the scalp segmentation in all 10 subjects, the summed value will be 10, whereas if a voxel is part of the scalp segmentation in half of the subjects, the summed value is 5. After summing them, we divide by the total number of subjects to get for each voxel the fraction of subjects that the voxel is part of the scalp segmentation.

    mri_averaged = rmfield(mri_segmented{1}, 'cfg');
    for i=2:nsubj
        mri_averaged.scalp = mri_averaged.scalp + mri_segmented{i}.scalp;
    end
    mri_averaged.scalp = mri_averaged.scalp/nsubj;

The `scalp` field in the averaged segmentation now contains fractional values between 0 (air in all subjects) and 1 (head/scalp in all subjects).

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_averaged);

{% include image src="/assets/img/tutorial/opm_helmet_design/population3.png" width="600" %}

{% include markup/yellow %}
For the actual MEG recording in the lab the subjects will stick their head all the way in the helmet, hence the top of their head (vertex) will be flush with the top of the inside of the helmet. We could therefore improve the population helmet design by determining the vertex position in every individual MRI and vertically shifting the MRIs to align the vertex of all individuals prior to computing the averaged scalp segmentation. However, that falls outside the scope of this tutorial.
{% include markup/end %}

To determine the volume that would accommodate 90% of the participants, we have to determine which voxels are less than 10% probable to be part of the scalp. I.e., the outermost voxels with low scalp probabilities are removed, whereas if the scalp probability is 10% or higher, we retain the voxels.

    mri_90percentile       = mri_averaged;
    mri_90percentile.scalp = mri_averaged.scalp>=0.1;

This again results in a binary or boolean volume with a head outline that should fit 90% of our participants.

    cfg = [];
    cfg.method = 'ortho';
    cfg.location = [0 0 0];
    cfg.funparameter = 'scalp';
    ft_sourceplot(cfg, mri_90percentile);

{% include image src="/assets/img/tutorial/opm_helmet_design/population4.png" width="600" %}

We can use a similar trick to make the outline of the scalp perfectly symmetric. We flip the segmented scalp along the 2nd dimension (the y-axis), and combine it with the original using a logical "or" operation.

    % make it perfectly symmetric
    mri_90percentile.scalp =  mri_90percentile.scalp | flip(mri_90percentile.scalp, 2);

From here on the code is largely the same as for processing the individual anatomical MRI, so we make the inside and outside of the helmet using imdilate.

    % we now do the same as for the individual MRI
    mri_segmented = mri_90percentile;

    % we still need to make the headshape mesh, so don't modify the scalp segmentation directly
    tmp = mri_segmented.scalp;
    tmp(:,:,1:50) = 0;

    mri_segmented.airgap = imdilate(tmp,                  strel('sphere', 1));
    mri_segmented.helmet = imdilate(mri_segmented.airgap, strel('sphere', 5));

And as before we make the meshes for the headshape, the inside, and the outside of the helmet.

    cfg = [];
    cfg.method = 'projectmesh';
    cfg.numvertices = 4000;

    cfg.tissue = 'scalp';
    headshape = ft_prepare_mesh(cfg, mri_segmented);

    cfg.tissue = 'airgap'; % this makes a surface from the outside of the "airgap" part
    tmp = removefields(mri_segmented, {'scalp', 'helmet'}); % FIXME this is a hack that should be resolved
    inside = ft_prepare_mesh(cfg, tmp);

    cfg.tissue = 'helmet';
    tmp = removefields(mri_segmented, {'scalp', 'airgap'}); % FIXME this is a hack that should be resolved
    outside = ft_prepare_mesh(cfg, tmp);

Now that we have the headshape and the inside and outside of the helmet, again accommodating for a 1 mm gap on the insider of the helmet, we have to distribute the sensors over the headshape and helmet. Since all participants have different head sizes, their anatomical landmarks are also at different locations.

    figure
    ft_plot_axes([], 'unit', 'mm', 'coordsys', 'als');
    for i=1:nsubj
        ft_plot_mesh(fiducial{i}.nas, 'vertexcolor', 'k');
        ft_plot_mesh(fiducial{i}.lpa, 'vertexcolor', 'k');
        ft_plot_mesh(fiducial{i}.rpa, 'vertexcolor', 'k');
        ft_plot_mesh(fiducial{i}.ini, 'vertexcolor', 'k');
    end

{% include image src="/assets/img/tutorial/opm_helmet_design/population5.png" width="600" %}

As for the segmentations, we can compute the average location of all anatomical landmarks.

    nas_avg = fiducial{1}.nas;
    ini_avg = fiducial{1}.ini;
    lpa_avg = fiducial{1}.lpa;
    rpa_avg = fiducial{1}.rpa;

    for i=2:nsubj
        nas_avg = nas_avg + fiducial{i}.nas;
        ini_avg = ini_avg + fiducial{i}.ini;
        lpa_avg = lpa_avg + fiducial{i}.lpa;
        rpa_avg = rpa_avg + fiducial{i}.rpa;
    end

    nas_avg = nas_avg/nsubj;
    ini_avg = ini_avg/nsubj;
    lpa_avg = lpa_avg/nsubj;
    rpa_avg = rpa_avg/nsubj;

    % average the position of left and right ear
    tmp1 = (lpa_avg + [1 -1 1] .* rpa_avg)/2;
    tmp2 = (rpa_avg + [1 -1 1] .* lpa_avg)/2;
    % now we can safely overwrite them
    lpa_avg = tmp1;
    rpa_avg = tmp2;

    % the nose and inion should be exactly on the y=0 plane
    nas_avg(2) = 0;
    ini_avg(2) = 0;

We can plot the averaged anatomical landmark positions together with the population headshape.

    headshape.fid.pos = [
        nas_avg
        ini_avg
        lpa_avg
        rpa_avg
        ];

    headshape.fid.label = {
        'nas'
        'ini'
        'lpa'
        'rpa'
        };

    figure
    ft_plot_headshape(headshape, 'axes', 'on', 'facecolor', 'skin', 'facealpha', 0.5, 'fidmarker', '.', 'fidcolor', 'k', 'fidlabel', true, 'fidsize', 24)
    ft_headlight

{% include image src="/assets/img/tutorial/opm_helmet_design/population6.png" width="600" %}

If you look carefully, you will see that the landmarks are not on the scalp surface, but slightly inside.

{% include markup/blue %}
#### Exercise

Explain why the landmarks are not on the surface.
{% include markup/end %}

Although the **[ft_electrodeplacement](/reference/ft_electrodeplacement)** function will project the landmarks on the surface, the projected nasion landmark will not be on the nasion but rather on the nearest surface point, which happens to be to the side of the nose. This subsequently causes the 10-20 placement scheme to fail. We can shift all anatomical landmarks outward a little bit to ensure that the projections onto the surface are correct.

    cfg = [];
    cfg.fiducial.nas = nas_avg + [+10 0 0];
    cfg.fiducial.ini = ini_avg + [-10 0 0];
    cfg.fiducial.lpa = lpa_avg + [0 +10 0];
    cfg.fiducial.rpa = rpa_avg + [0 -10 0];
    cfg.method = '1020';
    elec = ft_electrodeplacement(cfg, headshape);

{% include image src="/assets/img/tutorial/opm_helmet_design/population7.png" width="600" %}

From this point on the code is the same before, so we use **[ft_sensorplacement](/reference/ft_sensorplacement)** to rotate and translate the STL models to the desired sensor positions, we can visualize the result, and export it to STL files for postprocessing.

## Part 2 - sensor distributions

### 10-20 distribution

In all examples above we used the **[ft_electrodeplacement](/reference/ft_electrodeplacement)** function to determine the positions of the extended 10-20 system on the scalp, took a subset of those positions, and rotated and translated the sensors, sensor holders, etcetera to those positions. This is a very powerful and flexible way, since there are more than 300 locations in the [5% electrode placement scheme](https://doi.org/10.1016/s1388-2457(00)00527-7).

The selection was made using the **[ft_channelselection](/reference/utilities/ft_channelselection)** helper function, which knows some default channel groups like 'eeg1020'. Furthermore, we excluded FPz and Oz, since we already have their close neighbours on both sides.

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

We could also have specified it as follows

    chansel = {'Fp1', 'Fp2', 'F7', 'F3', 'Fz', 'F4', 'F8', 'T7', 'C3', 'Cz', 'C4', 'T8', 'P7', 'P3', 'Pz', 'P4', 'P8', 'O1', 'O2'};

and similarly you can make your own list, for example by hand-picking locations from a 2D representation of all positions.

    cfg = [];
    cfg.layout = 'eeg1005';
    cfg.channel = {'all'}; % modify this to your selection
    cfg.skipcomnt = 'yes';
    cfg.skipscale = 'yes';
    cfg.feedback = 'yes';
    layout = ft_prepare_layout(cfg);

{% include image src="/assets/img/tutorial/opm_helmet_design/distribution1.png" width="600" %}

With the `cfg.feedback` option this creates a figure, but you could also use **[ft_plot_layout](/reference/plotting/ft_plot_layout)** to have more control over the figure. Note that in this simple 2D layout, the anatomical location of the electrodes is not correct with respect to the schematic nose and ears, as T9 and T10 should be in front of the ears, more or less on the same location as LPA and RPA.

### Equidistant

We can also use **[ft_electrodeplacement](/reference/ft_electrodeplacement)** to make an approximate equidistant arrangement of an arbitrary number of OPM sensor locations. We can demonstrate this on the spherical headshape, but it works just as well on a realistic individual or population-based headshape.

    headshape = ft_read_headshape('spherical-head.stl');
    headshape.coordsys = 'ctf';

The mesh describing the sphere has over 28k triangles. To speed up the plotting, we can reduce the number of triangles while still retaining the overall spherical shape.

    [headshape.tri, headshape.pos] = reducepatch(headshape.tri, headshape.pos, 800);

As before, we specify the position of the anatomical landmarks to distribute the electrode positions.

    nas = [+100 0 0];
    ini = [-100 0 0];
    lpa = [0 +100 0];
    rpa = [0 -100 0];

    cfg = [];
    cfg.fiducial.nas = nas;
    cfg.fiducial.ini = ini;
    cfg.fiducial.lpa = lpa;
    cfg.fiducial.rpa = rpa;
    cfg.method = 'equidistant';
    cfg.numelec = 64;
    cfg.maxiter = 500;
    cfg.feedback = 'yes';
    elec = ft_electrodeplacement(cfg, headshape);

{% include image src="/assets/img/tutorial/opm_helmet_design/distribution2.png" width="600" %}

This results in an iteratively updating figure that shows the electrode positions over the left hemisphere. The positions are repeatedly updated to make the distance between them as equal as possible. There are a number of positions that remain fixed, which correspond to Fpz, Oz, T7 and T8. During optimization the electrodes are not allowed to go below the sideline over the ear, or across the midline. After optimization, the positions are copied to the right hemisphere and labels are assigned.

We can plot the positions together with their labels using **[ft_plot_sens](/reference/ft_plot_sens)**. The position labeled with "1" corresponds to the "Fpz" position in the 10-20 system.

    {% include image src="/assets/img/tutorial/opm_helmet_design/distribution3.png" width="600" %}

The total number of positions must be specified by you. The number of positions along the midline (running over the vertex) and over the sideline (above the ear) can also be specified.

After determining the equidistant positions, you would proceed just as before with the **[ft_sensorplacement](/reference/ft_sensorplacement)** function to place the OPM sensors, sensor holders, etcetera.

### From a template

The two sections above demonstrate how we can construct sensor positions on basis of distributing electrode positions. We could similarly start with [template electrode](/template/electrode) locations from FieldTrip, or from other software like EEGLAB. The **[ft_electroderealign](/reference/ft_electroderealign)** function can be used to translate, rotate and scale the electrodes such that they fit on your head surface.

Again, after determining the positions from the template, you would proceed just as before with the **[ft_sensorplacement](/reference/ft_sensorplacement)** function to place the OPM sensors, sensor holders, etcetera.

### Interactive manual specification

If you have a headshape, you can also use the "headshape" method in **[ft_electrodeplacement](/reference/ft_electrodeplacement)** This will show the headshape and allows you to click to manually specify where the positions are to be placed. This approach is described in more detail in the [tutorial on electrode placement](/tutorial/source/electrode).

## Part 3 - sensor orientation and rotation

Besides determining _where_ to place the sensors on the head or helmet, we also need to decide how the sensors should be oriented. By default **[ft_sensorplacement](/reference/ft_sensorplacement)** will orient the sensors (and sensor holders, etc.) perpendicular to the headshape surface. This defines two of the three rotations, but still leaves the rotation around the (radial) axis to be determined.

Let's first have a look at the sensor holder and how it is defined in 3D space.

    sensor = ft_read_headshape('fieldline_sensor.stl');
    holder = ft_read_headshape('fieldline_holder.stl');

    figure
    ft_plot_mesh(sensor, 'facecolor', 'r', 'edgecolor', 'none')
    ft_plot_mesh(holder, 'facecolor', 'lightgray', 'edgecolor', 'none')
    ft_plot_axes([], 'unit', 'mm')
    ft_headlight

    axis on; grid on
    xlabel('x')
    ylabel('y')
    zlabel('z')

{% include image src="/assets/img/tutorial/opm_helmet_design/orientation1.png" width="600" %}

The sensor is 15x13x35 mm, where the 15 mm corresponds to the x, the 13 mm to the y, and the 35 mm to the z direction. The STL model for the sensor is "decorated" with a small piece of the cable sticking out and a small dent corresponding to a screw hole. The cable is on the -x side, the screw hole is on the +x side. The bottom of the sensor holder is flush with the z=0 plane. The sensor itself is 1 mm shifted upwards, in the positive z-direction.

The **[ft_sensorplacement](/reference/ft_sensorplacement)** function operates by shifting the object that is specified in `cfg.template` (so for example the sensor, or the sensor holder) with `cfg.outwardshift` in the positive z-direction. Subsequently the object is rotated so that it is perpendicular to the surface, and finally it is translated to its final position.

The orientation and rotation are determined by a rotation around the z-axis, followed by a rotation around the y- and finally the x-axis. Since rotations are not [commutative](https://en.wikipedia.org/wiki/Commutative_property), the order in which they are applied matters. These rotations can be specified as `cfg.rotz`, `cfg.roty` and `cfg.rotx`, respectively. Besides the geometrical objects that can be plotted, **[ft_sensorplacement](/reference/ft_sensorplacement)** also returns the `cfg` structure as it was used in the placement, so if you did not explicitly specify the rotations in the input `cfg`, the output `cfg` will have the rotations, which allows you to change them and re-run the placement.

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
    cfg.feedback = 'no';
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

{% include image src="/assets/img/tutorial/opm_helmet_design/orientation2.png" width="600" %}

The output configuration contains the rotations around the three axes that were used.

    >> disp(outcfg)
        ...
        rotx: [19x1 double]
        roty: [19x1 double]
        rotz: [19x1 double]
        ...

We could explicitly specify that we don't want any rotations at all with

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

{% include image src="/assets/img/tutorial/opm_helmet_design/orientation3.png" width="600" %}

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

{% include image src="/assets/img/tutorial/opm_helmet_design/orientation4.png" width="600" %}

In the individual helmet design we identified that the sensors close to the ears had orientations that were suboptimal, due to the low-resolution headshape mesh having a bump due to the ears, and due to some compression of the soft tissue by the sound-isolating headphone. We can identify the two sensors on T7 and T8, and change those accordingly:

    selT7 = find(strcmp(tmpcfg.channel, 'T7'));
    selT8 = find(strcmp(tmpcfg.channel, 'T8'));

    cfg = [];
    cfg.rotx = outcfg.rotx; % copy this from the previous call 
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

As an alternative to specifying the rotations around the z-, y- and x-axis, you can specify the orientation of each of the electrodes in the input `elec` structure. This is similar to specifying the coil orientation for MEG sensor arrays, and for electrodes also used in **[ft_plot_sens](/reference/ft_plot_sens)** when you show the electrode as a disc. The following takes the line connecting the point (0,0,40), which is more or less in between T7 and T8, and each of the electrodes, and uses that line to determine the orientation of each electrode.)

    for i=1:numel(elec1020.label)
        elec.elecori(i,:) = elec.elecpos(i,:) - [0 0 40];
        elec.elecori(i,:) = elec.elecori(i,:) / norm(elec.elecori(i,:)); % unit length
    end

{% include markup/blue %}
#### Exercise
Return to the individual MRI-based helmet design and use the radial direction as seen from the point (0, 0, 0) and the point (0, 0, 40). Which orientation do you like better?
{% include markup/end %}

### Sensor rotation around its own axis

Bi-axial OPM sensors typically record the signal in one radial direction (i.e., perpendicular to the surface) and one tangential direction, which is also the most optimal configuration (see Schoffelen et al. (2025) [Optimal configuration of on-scalp OPMs with fixed channel counts](https://doi.org/10.1162/imag.a.22)). For the tangential direction you have to choose how to rotate the sensor around its own axis. An optimal sampling of the environmental noise (useful for noise suppression) is obtained with alternating directions of neighbouring sensors, where the tangential axis of a sensor is 90 degrees rotated relative to that of its neighbours.

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

{% include image src="/assets/img/tutorial/opm_helmet_design/orientation5.png" width="600" %}

Of course this is best combined with first determining the overall orientation (rotation around x and y), then plotting, and then writing down how much you want each sensor to be rotated around its own axis.

    % this is what you would write down by hand
    correction = {
        'Cz'    0 0   0
        'T7'    0 0 -30
        'T8'    0 0 +30
        % ...
        };

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

To get a nice distribution of sensor positions, orientations relative to the scalp, and rotations around their own axis, you will probably want to iterate multiple times and plot them in between.

### Plotting sensors together with their label

You can use the following piece of code to identify which of the sensors needs to be rotated. It plots the OPM sensors together with the electrode positions on which they are based, with (very large) the label that corresponds to each of the positions.

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_mesh(sensor, 'facecolor', 'r', 'facealpha', 0.5, 'edgecolor', 'none');
    ft_headlight

    chanindx = match_str(elec.label, chansel);
    ft_plot_sens(elec, 'chanindx', chanindx, 'label', 'label', 'fontsize', 30)

## Part 4 - putting the helmet design together

Throughout this tutorial we are using [Autodesk Fusion](https://www.autodesk.com/products/fusion-360/), which is the software we are most familiar with. You can sign up as a student or educator and get an educational license for free, or you can sign up for a free personal license. However, you can also use [SolidWorks](https://www.solidworks.com), [FreeCAD](https://www.freecad.org), [Blender](https://www.blender.org), or other 3D design software. The required characteristics of the software are that it should be able to read and write STL files, and that it should be able to combine different geometries by means of (Boolean) addition and subtraction. For example, we have the STL file of the basic helmet shape from an MRI and the software should be able to cut off the lower part to accommodate the face, ears and neck. Furthermore, it should be able to add some material from the padding STL file and remove material based on the hole STL file.

{% include markup/green %}
The padding is an STL file that is used to make the helmet locally thicker or to give it more "body" at the location where the sensor holder needs to be glued in. This is needed if you have a thin and lightweight helmet shell and if the sensor holder is placed somewhere with a lot of curvature. The padding will be mainly fall inside the helmet and will largely be cut away by the hole STL file.
{% include markup/end %}

In Fusion you start with importing the STL files for the inside and outside of the helmet, the hole, the sensor holder and the sensor itself. Optionally you should also import the STL file for the padding. In the spherical and flattened sphere examples above we started with a helmet that was designed in Fusion, so importing the inside and outside helmet surface only applies to the individual MRI and population-based headshape derived helmets. 

You can use the STL files that you created yourself, or the ones that we have shared on the [download server](https://download.fieldtriptoolbox.org/tutorial/opm_helmet_design/). It can help to get a quick overview of all the STL files by using 3D visualisation software like [MeshLab](https://www.meshlab.net).

{% include markup/yellow %}
Since you don't have the original Fusion design for the spherical helmet or for the flattened sphere, you should read the `spherical-helmet.stl` or the `flattenedspherical-helmet.stl` files.
{% include markup/end %}

After importing all STL objects, you have to convert each of them from a "mesh" into a "solid".

### Making the helmet

For the individual MRI and population-based headshape derived helmets, you then have to use the "combine" tool to make a binary intersection between the solid outside and the solid inside objects; this will result in a hollow outline of the helmet.

You can use "inspect -> section analysis" to visualize a cut-through of the head and/or helmet.

Under the "construct" option, you then make a "plane at angle" around the axis that connects the left and right ear, and subsequently relative to this make an "offset plane". This results in an angled offset plane. Using the "split body" tool you cut off the lower part of the hollow helmet outline.

Once you have the helmet, you are at the same level as where we started with the spherical and flattened sphere examples.

### Cutting holes for the sensor holders

Using the "combine" tool you can combine objects as if you are adding them or subtracting them from each other. So we select the helmet shape and use the "combine" tool to **add** the padding to the helmet, and subsequently use the "combine" tool to **subtract** the solid representing the hole from the helmet.

{% include image src="/assets/img/tutorial/opm_helmet_design/fusion.gif" %}

Adding the padding has no effect for the spherical example here, as the helmet is 10 mm thick. If you imagine the helmet being much thinner (and hence lighter) and also strongly curved, the flat cutout of the sensor holder could result a hole with not enough surface where the helmet touches the sensor holder. In that case the padding object adds a bit of "meat", ensuring that the hole is well defined and that the sensor holder can be glued properly into the helmet.

The sensor holder and the sensor itself are actually not needed, since we don't combine them with the helmet in the same 3D model. We only use them here for visual inspection.

The result is a 3D model for the helmet with the holes that fit the sensor holders.

{% include image src="/assets/img/tutorial/opm_helmet_design/fusion_spherical.png" %}

### Adding decoration

Very likely you will want to make small modifications to the helmet and/or add some additional features, like

- fillets along the rim to remove the sharp edges
- slots for a chin-strap
- clips for cable management
- suspension eye bolts or lugs

Also, you may want to cut out extra space around the ears, or to add protruding markers or fiducials for coregistration using a 3D scanner or Polhemus. See also the tutorial on [coregistration of OPM data](/tutorial/source/coregistration_opm).

### Printing the helmet and the holders

The helmet can be printed using an [FDM printer](https://en.wikipedia.org/wiki/Fused_filament_fabrication). If you have a large enough 3D printer it can be printed in one piece, or if it is too large your 3D printing software has options to cut it into pieces that you can print seperately and glue together.

The holders are printed seperately and are later glued into the corresponding holes in the helmet. This allows printing the sensor holders nicely aligned at a 90 degree angle on the build plate, resulting in a more accurate geometry and them being stronger. Furthermore, by printing them seperately you will also need less support material.

You can print the sensor holders with [FDM](https://en.wikipedia.org/wiki/Fused_filament_fabrication), or you may want to use an [SLA printer](https://en.wikipedia.org/wiki/Stereolithography). SLA printers have a smaller build volume, but are more precise and result in stronger and smoother surfaces than FDM printers, so the sensors will nicely slide into the holders.

## Part 5 - making the grad structure and layout

To reconstruct the sources underlying the MEG recordings and for some of the denoising algorithms (see below), you need the specification of the [sensor definition](/faq/source/sensors_definition/#the-definition-of-meg-sensors). Although OPMs are commonly magnetometers, in FieldTrip we refer to this sensor definition as the `grad` structure. If you read in data from a SQUID MEG recording, you will get the `grad` structure in the raw data representation.

{% include markup/green %}
Some MEG denoising algorithms like **[ft_denoise_hfc](/reference/ft_denoise_hfc)**, **[ft_denoise_amm](/reference/ft_denoise_amm)**, and **[ft_denoise_sss](/reference/ft_denoise_sss)** make a spatial model of the field distribution and need the `grad` sensor definition, whereas others like **[ft_denoise_ssp](/reference/ft_denoise_ssp)**, **[ft_denoise_ssp](/reference/ft_denoise_ssp)**, and ICA do not need a sensor definition.
{% include markup/end %}

If you read in data from an OPM MEG recording (for example a fif file), you might also get the `grad` structure in the raw data representation. In some cases the sensor positions are known to the OPM system (for example when the measurement was done with the FieldLine smart helmet) or have been added by postprocessing the recording with custom software to add the sensor localization (for example with the QuSpin Halo).

If you use a custom 3D-printed helmet, the OPM acquisition software will record the MEG signals just fine, but will not know where the sensors are or what their orientation is. Hence you have to construct a `grad` structure to complement the subsequent analysis.

### Grad for source modelling

To demonstrate this, we will again start with the spherical configuration

    headshape = ft_read_headshape('spherical-head.stl');
    headshape.coordsys = 'ctf';

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
    cfg.feedback = 'no';
    elec = ft_electrodeplacement(cfg, headshape);

    chansel = ft_channelselection({'eeg1020', '-Fpz', '-Oz'}, elec.label);

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.template = 'fieldline_sensor.stl';
    cfg.outwardshift = 2; % two mm away from the surface
    [outcfg, sensor] = ft_sensorplacement(cfg, headshape);

Note that here we have shifted the sensor 2 mm away from the headshape.

We now repeat the placement, but rather than reading the 15x13x35 mm sensor geometry from the STL file, we specify a single OPM sensor with three channels corresponding to the x, y, and z-direction.

    opm_single = [];
    opm_single.label = {
        'x'
        'y'
        'z'
    };
    opm_single.coilpos = [
        0 0 0
        0 0 0
        0 0 0
    ];
    opm_single.coilori = [
        1 0 0
        0 1 0
        0 0 1
    ];
    opm_single.tra = eye(3);

We specify the single OPM sensor as the template, which cause it to be copied for each of the channels and rotated and translated as before.

    cfg = [];
    cfg.elec = elec;
    cfg.channel = chansel;
    cfg.template = opm_single;
    cfg.outwardshift = 2 + 1 + 5; % IMPORTANT see below
    [outcfg, opm_all] = ft_sensorplacement(cfg, headshape);

In the previous example in the tutorial we moved the STL model for the sensor 2 mm away from the headshape. The STL design of the **sensor holder** has its bottom flush with the z=0 plane, and the STL design of the **sensor** itself has the sensor 1 mm shifted upwards along the +z direction, since there is a 1 mm rim to keep the sensor in place in the holder. Finally, the sensitive spot in the sensor where the field is actually detected is not at the bottom of the sensor enclosure, but has a 5 mm offset from the bottom. Consequently, the `cfg.outwardshift` needs to be specified as 2+1+5.

Whereas we start with only 19 sensors in this tutorial, since each sensor in this example is assumed to have three sensitive axes, each sensor contributes **three** channels to the grad structure. Each channel has a coilpos, coilori and label, as described in this [frequently asked question](/faq/source/sensors_definition/#the-definition-of-meg-sensors). Note that FieldTrip uses the phrase "coils" just as for SQUID sensors, even though the OPM does not have coils.

The output `opm_all` is a structure array with 19 OPM _sensors_, where each sensor represents three _channels_. We combine all of them into a single `grad` structure.

    grad = [];
    grad.label = {};
    grad.coilpos = zeros(0,3);
    grad.coilori = zeros(0,3);
    for i=1:length(chansel)
        lab{1} = [outcfg.channel{i} '_' all_opm(i).label{1}]; % _x
        lab{2} = [outcfg.channel{i} '_' all_opm(i).label{2}]; % _y
        lab{3} = [outcfg.channel{i} '_' all_opm(i).label{3}]; % _z
        grad.label = cat(1, grad.label, lab(:));
        grad.coilpos = cat(1, grad.coilpos, all_opm(i).coilpos);
        grad.coilori = cat(1, grad.coilori, all_opm(i).coilori);
    end
    grad.tra = eye(length(grad.label));

We can plot the resulting OPM sensor positions for all channels with ft_plot_sens.

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);
    ft_plot_sens(grad);
    ft_headlight

{% include image src="/assets/img/tutorial/opm_helmet_design/grad.png" width="600" %}

or only with the z-oriented channels, including their labels.

    ft_plot_sens(grad, 'chanindx', endsWith(grad.label, 'z'), 'label', 'label')

### Layout for plotting

For 2D visualisation of the topographic distribution of the ERFs or TFRs you need a layout that maps the 3D sensor positions onto a 2D plane. For that you can use the `grad` structure, as explained in the [layout tutorial](/tutorial/plotting/layout/). 

Here is a short piece of code to make a simple layout.

    cfg = [];
    cfg.grad = grad; % this contains x, y, and z channels
    cfg.channel = grad.label(endsWith(grad.label, 'z'));
    cfg.rotate = 90;
    cfg.feedback = 'yes';
    layout = ft_prepare_layout(cfg);

{% include image src="/assets/img/tutorial/opm_helmet_design/layout1.png" width="600" %}

More elaborate options are explained in the [layout tutorial](/tutorial/plotting/layout), and you may want to put some effort in making a really nice layout with a helmet shaped mask and outline, as you can see for some of the [template layouts](/template/layout).

The layout above only includes the radially oriented channels, i.e., the channels in the z-direction, as the field distribution on these is the easiest to interpret. It is in principle possible to make layouts for all sensor orientations:

    cfg = [];
    cfg.grad = grad; % this contains x, y, and z channels
    cfg.rotate = 90;
    cfg.feedback = 'no';

    cfg.channel = grad.label(endsWith(grad.label, 'x'));
    layout_x = ft_prepare_layout(cfg);

    cfg.channel = grad.label(endsWith(grad.label, 'y'));
    layout_y = ft_prepare_layout(cfg);

    cfg.channel = grad.label(endsWith(grad.label, 'z'));
    layout_z = ft_prepare_layout(cfg);

    cfg = [];
    layout_xyz = ft_appendlayout(cfg, layout_x, layout_y, layout_z);

    figure
    ft_plot_layout(layout_xyz)

If you use this layout with **[ft_multiplotER](/reference/ft_multiplotER)** or **[ft_multiplotTFR](/reference/ft_multiplotTFR)**, you will automatically see the three "heads" with the different sensor orientations side-by-side. 

{% include image src="/assets/img/tutorial/opm_helmet_design/layout2.png" width="600" %}

{% include markup/yellow %}
The channels in the x and y-direction are sensitive for magnetic fields in the x and y-direction of the sensor itself, which is not necessarily in the x or y-direction of the head coordinates or of the figure on screen. The layout above that combines the channels in the x, y, and z-orientations might therefore be useful for multiplotting (e.g. plotting an ERF at every sensor location), but should **not** be used for topoplotting.
{% include markup/end %}

## Summary and conclusion

This tutorial explains how to design 3D‑printable OPM helmets. We started by creating helmet shells from spherical geometric templates, from individual MRIs, or for population averages. We then looked at different ways of distributing OPM sensors using extended 10–20, equidistant, or interactive placement. In part 3 we looked at optimizing sensor orientations and rotations (important for bi‑ and tri-axial sensors) and in part 4 we assembled the actual helmet to be 3D printed by combining the shell, the holes and the sensor holders. Finally in the last part we constructed the grad structure for source modelling, and the layout for topographic plotting.

Throughout this tutorial we have mostly been working with a relatively simple geometry and with a small number of sensors to keep the procedure simple and fast. However, by combining part 1, 2, and 3 in a smart way, you can design arbitrarily complex OPM helmets for many sensors.

Not covered in this tutorial is how to do the actual 3D printing; for that we recommend that you team up with someone who has experience with that, or that you involve your technical support group or a 3D printing company. Important in the 3D design is that tolerances are considered (i.e. how tight is the fit of the components), that additional features of the helmet are added, like holes for the ears, or slits to attach a chin strap, and that sharp edges are avoided where possible by using fillets.

Also not covered in this tutorial is how to do the coregistration of the OPM sensors with the anatomical MRI or how to preprocess and analyze the OPM data in sensor and source space; for that we have separate tutorials.

### See also these tutorials

{% include seealso category="tutorial" tag1="opm" %}

### See also these "getting started" pages with vendor specific details

{% include seealso category="getting_started" tag1="opm" %}
