---
title: OPM helmet design
---

{% include /shared/development/warning.md %}

## Introduction

Measuring MEG with OPMs allow for flexible sensor placement. This is a significant departure from the rigidity of traditional SQUID-based systems, which confine participants within a fixed sensor array. With OPMs, researchers can now tailor the magnetometer configuration to an individual's unique head shape and size, a benefit that is particularly impactful when studying children or patient populations. The flexible placement allows positioning the sensors close to the scalp and to brain regions expected to be activated.

The flexible OPM sensor placement opens the door for a range of novel experimental paradigms, as subjects are no longer tethered to a single, bulky dewar; they can potentially move, interact, and perform tasks in a much more naturalistic environment, thereby capturing brain activity that is more representative of real-world cognition. It should be noted, however, that OPMs in a helmet or cap that moves along with the participant will pick up considerable artifacts due to the OPMs moving and/or rotating through the residual magnetic field in the MSR. Extra shielding of the MSR with 3 instead of 2 layers of mu metal, and/or the use of nulling coils can reduce, but completely eliminate these movement-related artifacts. Although denoising algorithms like HFC and AMM can help to clean the data from the artifacts caused by the movements, it should also always be considered whether the measurement is not better done with a head-fixed setup.

In this tutorial we will cover the process of designing custom OPM helmets for individual participants and for specific populations. We will start either with anatomical MRIs of a single or multiple individuals, or with a geometric model as the basis for the helmet. It demonstrates how a given number of OPM sensors can be distributed over that helmet, and how the design files can be combined to make a model that can be 3D printed.

This tutorial aims for designing OPM arrays with relatively uniform whole whole-head coverage. It does not include forward simulations of how a hypothetical dipole in the brain is visible on the OPM sensor array, and also does not cover how to place (a limited set of) OPMs to specifically target activity in a particular brain area. Furthermore, this tutorial will not discuss how OPM recordings are processed.

## Background

OPMs differ in size, depending on the manufacturer, but in general can be conceived as a rectangular box with a cable attached. For the FieldLine system, for example, the individual sensors are 13x15x35 mm. The OPMs are placed in holders which can in principle be mounted on a flexible cap just like EEG electrodes, but this comes with the potential disadvantage that the sensor orientations are not fixed and might vary depending on the head orientation and movements. With a fixed/rigid helmet as demonstrated in this tutorial, the position _and_ orientation of all sensors is well-defined.

The tutorial demonstrates the placement of FieldLine sensors, but is equally applicable to the sensors from QuSpin, Mag4health, or other companies. The OPM sensors and the holders are modeled (outside of MATLAB) as STL files; these sensors and holders are then distributed over the shell that forms the helmet. Furtermore, additional geometrical objects can be modeled as STL files and can be used as "tools" in the fabrication process to make holes in the helmet, or to add a small rim to facilitate glueing the sensor holder to the shell.

## Procedure

We distinguish the OPM helmet into the shell, i.e. the basic outline that fits around the head, and the details such as the sensor holders. The sensor holders are printed seperately and glued into place onto the shell. To ensure that the sensor holders are on the right position and hold well, we will make well-defined holes in the shell to accomodate the sensor holders.

For making the helmet shapes, we will use a number of different approaches:

1. from a regular geometrical shape
2. from an individual anatomical MRI
3. from an individual 3D scan
4. from a large sample of MRIs to make a population-optimized helmet

Furthermore, we demonstrate different procedures to distribute the OPM sensors, based on the 10-20 electorde placement, based on an equidistant distribution of the sensors, and based on manual interactive clicking of the sensor positions.

{% include markup/yellow %}
In the following we will be using [Autodesk Fusion](https://www.autodesk.com/products/fusion-360/). You can sign up as a student or educator and get an educational license for free, or you can sign up for a free personal license. Alternatively, you could also [SolidWorks](https://www.solidworks.com), [FreeCAD](https://www.freecad.org), [Blender](https://www.blender.org), or other 3D design software.
{% include markup/end %}

## Using different helmet shapes

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

We proceed  with determining the sensor positions. For that we can either read one of the [template electrode](/template/electrode) specifications, or we can use **[ft_electrodeplacement](/reference/ft_electrodeplacement)**. With that fucntion we can interactively determine electrode positions by clicking on the surface, just like in [this tutorial](/tutorial/source/electrode/). Alternatively, we can specify anatomical landmarks on the head and use an automatic placement of the electrodes according to the 10-20 system or using an equidistant placement. 

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

Subsequently we call **[ft_electrodeplacement](/reference/ft_electrodeplacement)** to automatically determine the positions of the electrodes.

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

    chansel = ft_channelselection('eeg1020', elec.label);

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

This returns a cell-array for each of the objects, which we can plot in MATLAB:

    figure
    ft_plot_headshape(headshape, 'facecolor', 'skin', 'facealpha', 1, 'axes', 1);

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

This results in 21 channels times 3 files, so 63 STL files on disk. In principle you only need the cuttingtool files, since the sensors don't need to be printed (these are basically only dummies for visualisation purposes), and multiple sensor holders can be 3D printed from the original sensor STL file without translatiopns and rotations.

In the 3rd secction of this tutorial we will explain how to combine the shell and the cuttingtool for the final helmet design.

### Flattened spherical helmet

This is again a helmet that starts with a design in Fusion (or your 3D design software of choice). It consists of a sphere, that to the bottom is extended with a cylinder and subsequently flattened on the left and right hemisphere. As before, there is a STL model for the headshape and an STL model for the shell that forms the helmet.  

{% include image src="/assets/img/tutorial/opm_helmet_design/figure2.png" width="600" %}

    headshape = ft_read_headshape('flattenedspherical-head.stl')
    helmet = ft_read_headshape('flattenedspherical-helmet.stl')

In the previous spherical helmet design , we had a hemisphere and hence the lowest sensors on the plane spanned by FPz-T7-T8-Oz needed to be _above_ the mid-plane of the sphere. Now the head and helmet extend further down, so we can also place the fidicuals a bit lower.

    nas = [+100 0 -10];
    ini = [-100 0 -10];
    lpa = [0 +80 -10];
    rpa = [0 -80 -10];

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

You should check that the LPA and RPA landmark points are indeed on the flat pieces that represent the temples. Furthermore, you can see in the image that the fiducials are now slightly _below_ the axes. That is in general not what we want, since the axes of the coordinate system pass through the fiducials. We could use **[ft_transform_geometry](/reference/ft_transform_geometry)** to move the head (and helmet) 10 mm up, and then give the fiducials a z-coordinate of 0 instead of -10. However, since it does not significantly affect the following steps, we will leave it like this and continue.

    % specify the coordinate system as ALS or anterior-left-superior
    % it is not CTF, since the axes don't go through the nasion and ears
    headshape.coordsys = 'als';
    helmet.coordsys = 'als';

Again we can distribute the electrodes over the head surface.

    cfg = [];
    cfg.fiducial.nas   = nas;
    cfg.fiducial.ini   = ini;
    cfg.fiducial.lpa   = lpa;
    cfg.fiducial.rpa   = rpa;
    cfg.method = '1020';
    cfg.feedback = 'yes';
    elec = ft_electrodeplacement(cfg, headshape);

We make the same selection of 21 electrodes and use those to place the OPM sensors.

    chansel = ft_channelselection('eeg1020', elec.label);

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

Use the same for-loop as before to plot all the sensors. Compare not only the position of the sensors to those in the previoous helmet, but also the rotation around their own axes. What is the consequence of rotating the OPM Nsensors around the axes (hint: think of the x-, y-, and z-direction sensitivity that the sensors may or may not have).
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

### Individualized based on 3D scan

### Adapted to percentile of population

## Different sensor distributions

### 10-20 distribution

### Equidistant

### From a template

### Interactive manual specification

## Putting the 3D model together

## Summary and conclusion

What has been covered?

What has not been covered but is relevant in the context of the tutorial?

Provide links to suggested further reading, related FAQs and example scripts.
