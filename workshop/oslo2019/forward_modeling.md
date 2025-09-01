---
title: Forward modeling for EEG source reconstruction
tags: [oslo2019, eeg-audodd, headmodel]
---

## Introduction

This tutorial goes through the necessary steps for creating a robust forward model for EEG source reconstruction.

It is part of the [Oslo 2019 workshop tutorials](/workshop/oslo2019), where tutorials can be found on [preprocessing and ERPs](/workshop/oslo2019/introduction), [time-frequency representations](/workshop/oslo2019/timefrequency), [statistics](/workshop/oslo2019/statistics) and [source reconstruction](/workshop/oslo2019/beamforming).

The data for the tutorial is available [here](https://download.fieldtriptoolbox.org/workshop/oslo2019/)

## Background

To do source reconstruction, a so-called forward model is needed. The forward model constrains the solution space for the inverse models (source reconstructions) that we may wish to apply to our data sets. If we had no constraints at all, there would be an infinite number of solutions (inverse models) that would satisfy the problem that we are trying to solve, which is: which are the _latent/unobserved_ variables (sources) that give rise to the _observed_ variables (the time courses observed on electrodes, i.e. the EEG data). By constraining the solution in sensible ways and applying sensible algorithms we can find a unique solution for the inverse model. In this tutorial, we will focus on constraining the solution, i.e. providing a sensible _forward model_. The application of sensible algorithms is the source reconstruction presented by Britta Westner yesterday.

Optimally, we have individual Magnetic Resonance Images (MRIs) available for each subject. If this is not so, it is also possible to use a template brain for source reconstruction. See [here](/template/sourcemodel). In this tutorial we will assume that you have individual structural MRIs at your disposal.

There are four components of a forward model

1. A _head model_: we need to know how the electric currents generated at the source spread throughout the volume conductor (the head, containing the borders between brain and skull and between skull and skin)
2. A _sensor description_: we need to know where the sensors are that pick up the activity coming from the sources
3. A _source model_: we need to know where the sources are - preferably they should be in the brain
4. A _lead field_ : we need to know how the sources and sensors "connect" to one another. That is, for each source (activated at unit strength (1 Am)) we calculate the electric potential vector at each sensor (electrode). It may be seen that the _lead field_ (component 4) is really the "sum" of the information from components 1-3.

{% include markup/skyblue %}
Note that the _forward model_ is completely independent of the actual EEG data.
All it models is how a source _given_ that it was active with a given current (1 Am), _would_ be seen at the sensor level.
{% include markup/end %}

## The challenge of coordinate systems

One challenge that we will face is that the _source model_ and the _head model_ are going to be based on the MRI data where positions are going to be expressed in the scanner's coordinate system, whereas the _sensor description_ is based on a another coordinate system. In our case, they were digitized using a so-called [Polhemus system](https://polhemus.com/scanning-digitizing/digitizing-products/), where the coordinate system is centered on an _x-axis_ which runs between the _pre-auricular_ points on the ears of the subject. The _y-axis_ runs through the center point of the _x-axis_ and towards the _nasion_ of the subject. Finally, the _z-axis_ is perpendicular to the _x-_ and _y-axes_. The three points, the _pre-auricular_ points and the nasion are together called the _fiducials_.

We **need** to bring these two coordinate systems together before we can create a sensible forward model. The first step, however, is to read in the MRI data.

### Before we begin

We will clear all variables that we have in the workspace, restore the default path, add fieldtrip and run _ft_defaults_

    clear variables
    restoredefaultpath

    addpath /home/lau/matlab/fieldtrip/ %% set your own path
    ft_defaults

### Read in and visualize the MRI data

The anatomical MRI data available here comes directly from the scanner in the DICOM format (read more about the DICOM format [here](https://en.wikipedia.org/wiki/DICOM). You can download [dicom.zip](https://download.fieldtriptoolbox.org/workshop/oslo2019/dicom.zip). Please unzip the files in a folder called _dicom_, which should be put in the folder where you have the other scripts used for the Oslo 2019 tutorials.

DICOM datasets consist of a large number of files, one per slice. As filename you have to specify a single file, the reading function will automatically determine which other slices are part of the same anatomical volume and put them in the correct order.

We read in the data using **[ft_read_mri](/reference/fileio/ft_read_mri)**

    mri_file = './dicom/00000001.dcm';
    mri = ft_read_mri(mri_file);

And plot it using **[ft_sourceplot](/reference/ft_sourceplot)** with an empty _cfg_. This is the same function that can be used to overlay MRIs with functional data.

    cfg = [];

    ft_sourceplot(cfg, mri);

    print -dpng original_mri.png

{% include image src="/assets/img/workshop/oslo2019/original_mri.png" width="650" %}
_Figure 1: Plot of the original MRI_

### Co-register the anatomical MRI to the EEG

The next step is to bring the two coordinate systems (DICOM and Polhemus) together. Choosing _interactive_ for _cfg.method_ allows us to click on the _fiducial_ points on the MR image. We choose _neuromag_ as our coordinate system here, which has its origo at (0, 0, 40) in the coordinate system digitized by the Polhemus.

    cfg          = [];
    cfg.method   = 'interactive';
    cfg.coordsys = 'neuromag';

    mri_aligned_fiducials = ft_volumerealign(cfg, mri);

In this case, we also have extra head shape points digitized with the Polhemus system. We are going to better the co-registration using these as well. If the initial looks okay (e.g., nose points are around the MRI-nose), then just press quit, and the Iterative Closest Point algorithm do its work (_cfg.headshape.icp_)

    load headshape.mat

    cfg                     = [];
    cfg.method              = 'headshape';
    cfg.headshape.headshape = headshape;
    cfg.headshape.icp       = 'yes'; % use iterative closest point procedure
    cfg.coordsys            = 'neuromag';

    mri_aligned_headshape = ft_volumerealign(cfg, mri_aligned_fiducials);

We follow this up by a check running **[ft_volumerealign](/reference/ft_volumerealign)** again

    ft_volumerealign(cfg, mri_aligned_headshape);

{% include image src="/assets/img/workshop/oslo2019/headshape_registration.png" width="650" %}
_Figure 2: Plot of the co-registration after applying Iterative Closest Points on the Polhemus head shape points_

{% include markup/skyblue %}
A version of _mri_aligned_headshape_ is already included in downloaded data. Using this, you will achieve the same solutions as us, but do try to do the co-registration yourself as well. Note also that _neuromag_ coordinates are seen under the voxel indices when you run **[ft_sourceplot](/reference/ft_sourceplot)** on _mri_aligned_headshape_.
{% include markup/end %}

    load mri_aligned_headshape

### Re-slice the MRI

We reslice the MRI on to a 1x1x1 mm cubic grid which is aligned with the coordinate axes. This is convenient for plotting,

    cfg            = [];
    cfg.resolution = 1;

    mri_resliced = ft_volumereslice(cfg, mri_aligned_headshape);

and when we plot it now, the axes are more conveniently located - note that everything could have been done with the "flipped" images as well.

    cfg = [];

    ft_sourceplot(cfg, mri_resliced);

    print -dpng mri_aligned_resliced.png

{% include image src="/assets/img/workshop/oslo2019/mri_aligned_resliced.png" width="650" %}
_Figure 3: Plot of the resliced MRI, where axes are located in a more convenient manner_

{% include markup/skyblue %}
Make sure that the coordinate system is correct, i.e. _up_ is _z-positive_, _anterior_ is _y-positive_ and _right_ is _x-positive_
{% include markup/end %}

### Segment the brain

The next step is to segment our coregistered and resliced MR image into the three kinds of tissues that we need to care about in our forward model for EEG data, namely the _brain_ tissue, the _skull_ tissue and the _scalp_ tissue. We use **[ft_volumesegment](/reference/ft_volumesegment)** for this. (This function relies on implementations from [SPM](https://www.fil.ion.ucl.ac.uk/spm))

    cfg        = [];
    cfg.output = {'brain' 'skull' 'scalp'};

    mri_segmented = ft_volumesegment(cfg, mri_resliced);

### Creating meshes

From this segmentation, we will now create a mesh for each of the three tissues.

    cfg             = [];
    cfg.method      = 'projectmesh';
    cfg.tissue      = 'brain';
    cfg.numvertices = 3000;

    mesh_brain = ft_prepare_mesh(cfg, mri_segmented);
    mesh_brain = ft_convert_units(mesh_brain, 'm'); % Use SI Units

    cfg             = [];
    cfg.method      = 'projectmesh';
    cfg.tissue      = 'skull';
    cfg.numvertices = 2000;

    mesh_skull = ft_prepare_mesh(cfg, mri_segmented);
    mesh_skull = ft_convert_units(mesh_skull, 'm'); % Use SI Units

    cfg             = [];
    cfg.method      = 'projectmesh';
    cfg.tissue      = 'scalp';
    cfg.numvertices = 1000;

    mesh_scalp = ft_prepare_mesh(cfg, mri_segmented);
    mesh_scalp = ft_convert_units(mesh_scalp, 'm'); % Use SI Units

    mesh_eeg = [mesh_brain mesh_skull mesh_scalp];

and we will plot them

    figure

    ft_plot_mesh(mesh_brain, 'edgecolor', 'none', 'facecolor', 'r')
    ft_plot_mesh(mesh_skull, 'edgecolor', 'none', 'facecolor', 'g')
    ft_plot_mesh(mesh_scalp, 'edgecolor', 'none', 'facecolor', 'b')
    alpha 0.3
    view(132, 14)

    print -dpng meshes.png

{% include image src="/assets/img/workshop/oslo2019/meshes.png" width="650" %}
_Figure 4: Plot of the three meshes (\_brain, skull \_and_ scalp*)*

## Head models (component 1)

We will now use these non-intersecting meshes to specify the head models, which will later be used to indicate how currents spread throughout the volume conductor. We create two models, one with the _bemcp_ method and one with the _dipoli_ method. For the article on the _dipoli_ method, see [Oostendorp & van Oosterom, 1989](https://doi.org/10.1109/10.19859) and for an article on the _bemcp_ method, see for example [Mosher et al., 1999](https://doi.org/10.1109/10.748978). Do note that the _dipoli_ method will not work on a Windows computer. The _headmodel_dipoli_ can be downloaded [here](https://download.fieldtriptoolbox.org/workshop/oslo2019/) instead. The best choice is to use [OpenMEEG](https://openmeeg.github.io/), (_cfg.method = 'openmeeg'_). This requires some manual installation and setting up, so it is not covered here.

    cfg              = [];
    cfg.method       = 'bemcp';
    cfg.conductivity = [1 1/80 1] * (1/3); % S/m

    headmodel_bem = ft_prepare_headmodel(cfg, mesh_eeg);
    headmodel_bem = ft_convert_units(headmodel_bem, 'm'); % Use SI Units

    cfg              = [];
    cfg.method       = 'dipoli'; % will not work with Windows
    cfg.conductivity = [1 1/80 1] * (1/3); % S/m

    headmodel_dipoli = ft_prepare_headmodel(cfg, mesh_eeg);
    headmodel_dipoli = ft_convert_units(headmodel_dipoli, 'm'); % Use SI Units

Now let's set the headmodel that we are going to use for now, starting with _headmodel_bem_

    headmodel = headmodel_bem;

and let's plot it

    figure
    ft_plot_headmodel(headmodel, 'facealpha', 0.5)
    view(90, 0)

{% include image src="/assets/img/workshop/oslo2019/headmodel.png" width="650" %}
_Figure 5: Plot of the head model with the three meshes (\_brain, skull \_and_ scalp*). Use the zooming tools to see the differences between the different tissues.*

## Getting electrodes in the right position (component 2)

Now, we will load the electrodes description _elec.mat_ that we have gotten from our Polhemus data and convert units to SI.

    load elec.mat
    elec = ft_convert_units(elec, 'm'); % Use SI units

and then plot them

    figure
    hold on
    ft_plot_sens(elec, 'elecsize', 40);
    ft_plot_headmodel(headmodel, 'facealpha', 0.5);
    view(90, 0)

{% include image src="/assets/img/workshop/oslo2019/elec_headmodel_wrong.png" width="650" %}
_Figure 6: Some electrodes are inside the head_

### Realigning electrodes

We will now realign the electrodes by projecting them to the surface

    % scalp indices differ for the two types of head models
    if strcmp(headmodel.type, 'bemcp')
        scalp_index = 3;
    elseif strcmp(headmodel.type, 'dipoli')
        scalp_index = 1;
    end

    cfg = [];
    cfg.method = 'project'; % onto scalp surface
    cfg.headshape = headmodel.bnd(scalp_index); % scalp surface

    elec_realigned = ft_electroderealign(cfg, elec);

and plot again

    figure
    hold on
    ft_plot_sens(elec_realigned, 'elecsize', 40);
    ft_plot_headmodel(headmodel, 'facealpha', 0.5);
    view(90, 0)

    print -dpng elec_headmodel_correct.png

{% include image src="/assets/img/workshop/oslo2019/elec_headmodel_correct.png" width="650" %}
_Figure 7: Electrodes are in meaningful places_

## Creating a source model (a volumetric grid (fit for beamformer and dipole analysis)) (Component 3)

The next step is to create a source model that indicates where our sources are. For beamformer and dipole analyses, so-called volumetric grids will do just fine. (For Minimum Norm Estimates, a source model, where sources are constrained to the cortical surface is needed, see for example this [tutorial](/tutorial/source/minimumnormestimate))

    cfg             = [];
    cfg.headmodel   = headmodel; % used to estimate extent of grid
    cfg.resolution  = 0.01; % a source per 0.01 m -> 1 cm
    cfg.inwardshift = 0.005; % moving sources 5 mm inwards from the skull, ...
                             % since BEM models may be unstable here

    sourcemodel = ft_prepare_sourcemodel(cfg);

and plot it

    figure
    hold on
    ft_plot_mesh(sourcemodel, 'vertexsize', 20);
    ft_plot_headmodel(headmodel, 'facealpha', 0.5)
    view(90, 0)

    print -dpng sourcemodel.png

{% include image src="/assets/img/workshop/oslo2019/sourcemodel.png" width="650" %}
_Figure 8: Head model overlain with source model (black dots)_

and highlight the sources inside the brain (in red)

    inside = sourcemodel;
    outside = sourcemodel;

    inside.pos = sourcemodel.pos(sourcemodel.inside, :);
    outside.pos = sourcemodel.pos(~sourcemodel.inside, :);

    figure
    hold on
    ft_plot_mesh(inside, 'vertexsize', 20, 'vertexcolor', 'red');
    ft_plot_mesh(outside, 'vertexsize', 20)
    ft_plot_headmodel(headmodel, 'facealpha', 0.1)
    view(125, 10)

    print -dpng sourcemodel_inside_outside.png

{% include image src="/assets/img/workshop/oslo2019/sourcemodel_inside_outside.png" width="650" %}
_Figure 9: Head model overlain with sources outside (black dots) and sources inside the brain (red dots)_

## Estimating the lead field (Component 4)

    cfg = [];
    cfg.sourcemodel = sourcemodel;    %% where are the sources?
    cfg.headmodel   = headmodel;      %% how do currents spread?
    cfg.elec        = elec_realigned; %% where are the sensors?

    % how do sources and sensors connect?
    sourcemodel_and_leadfield = ft_prepare_leadfield(cfg);

Let's have a look at the output of _sourcemodel_and_leadfield_

    sourcemodel_and_leadfield =

                    dim: [14 18 14]
                    pos: [3528x3 double]
                   unit: 'm'
                 inside: [3528x1 logical]
                    cfg: [1x1 struct]
              leadfield: {1x3528 cell}
                  label: {128x1 cell}
        leadfielddimord: '{pos}_chan_ori'

- _dim_ contains the dimensions of the grid in which the 3528 (14x18x14) sources are placed
- _pos_ contains the _xyz_ coordinates for the sources in the source model
- _unit_ contains the unit of _pos_
- _inside_ contains a logical vector indicating whether the source is a source or not
- _cfg_ contains information about the call of _ft_prepare_leadfield_
- _leadfield_ a cell array, where each cell (3528) contains a matrix of 128 rows (n channels) and 3 columns (\_xyz-coordinates). (The ones that are outside the brain are empty though). For each channel-orientation pair, you get the electric potential measured given that the relevant source has an activation of 1 Am
- _label_ contains the electrode names
- _leadfielddimord_ indicates the dimension. Each cell is a position, which contains a matrix ordered by channels x orientations (_xyz_)

### Plotting the lead field

It is always recommended to plot the lead fields alongside the electrodes and head model to see if things look okay.
The code for this takes a bit more work as can be seen by the length of the code below. Note that we use a realistic source current of 100 nAm (_sensory_dipole_current_)

    figure('units', 'normalized', 'outerposition', [0 0 0.5 0.5])
    source_index = 1200; %% a superficial sources
    sensory_dipole_current = 100e-9; % Am (realistic)

    n_sensors = length(elec_realigned.label);

    inside_sources = find(sourcemodel_and_leadfield.inside);
    inside_index = inside_sources(source_index);
    lead = sourcemodel_and_leadfield.leadfield{inside_index};
    xs = zeros(1, n_sensors);
    ys = zeros(1, n_sensors);
    zs = zeros(1, n_sensors);
    voltages = zeros(1, n_sensors);
    titles = {'Lead field (x)' 'Lead field (y)' 'Lead field (z)'};

    % get the xyz and norm

    for sensor_index = 1:n_sensors
        this_x = lead(sensor_index, 1);
        this_y = lead(sensor_index, 2);
        this_z = lead(sensor_index, 3);
        this_norm = norm(lead(sensor_index, :));
        xs(sensor_index) = this_x * sensory_dipole_current;
        ys(sensor_index) = this_y * sensory_dipole_current;
        zs(sensor_index) = this_z * sensory_dipole_current;
        voltages(sensor_index) = this_norm * sensory_dipole_current;
    end

    % plot xyz
    axes = {xs ys zs};

    for axis_index = 1:3
        this_axis = axes{axis_index};
        subplot(1, 3, axis_index)
        hold on
        ft_plot_topo3d(elec_realigned.chanpos, this_axis, 'facealpha', 0.8)
        if strcmp(headmodel.type, 'dipoli')
            caxis([-10e-6, 10e-6])
        end
        c = colorbar('location', 'southoutside');
        c.Label.String = 'Lead field (V)';
        axis tight
        ft_plot_mesh(mesh_brain, 'facealpha', 0.10);
        ft_plot_sens(elec_realigned, 'elecsize', 20);
        title(titles{axis_index})
        plot3(sourcemodel_and_leadfield.pos(inside_index, 1), ...
          sourcemodel_and_leadfield.pos(inside_index, 2), ...
          sourcemodel_and_leadfield.pos(inside_index, 3), 'bo', ...
          'markersize', 20, 'markerfacecolor', 'r')
    end

    % plot norm

    figure('units', 'normalized', 'outerposition', [0 0 0.5 0.85])
    hold on
    ft_plot_topo3d(elec_realigned.chanpos, voltages, 'facealpha', 0.8)
    if strcmp(headmodel.type, 'dipoli')
        caxis([0, 10e-6])
    end
    c = colorbar('location', 'eastoutside');
    c.Label.String = 'Lead field (V)';
    axis tight
    ft_plot_mesh(mesh_brain, 'facealpha', 0.10);
    ft_plot_sens(elec_realigned, 'elecsize', 20);
    title('Leadfield magnitude')
    plot3(sourcemodel_and_leadfield.pos(inside_index, 1), ...
      sourcemodel_and_leadfield.pos(inside_index, 2), ...
      sourcemodel_and_leadfield.pos(inside_index, 3), 'bo', ...
      'markersize', 20, 'markerfacecolor', 'r')

    view(-90, 0)

{% include image src="/assets/img/workshop/oslo2019/leadfield_components_topo_wrong.png" width="650" %}
_Figure 10: Lead fields in the_ XYZ-_directions for_ headmodel_bem _for a superficial source. **Note that there is something wrong**._

{% include image src="/assets/img/workshop/oslo2019/leadfield_magnitude_topo_wrong.png" width="650" %}
_Figure 11: Magnitude of the lead fields for_ headmodel_bem _for a superficial source. **Note that there is something wrong**._

{% include markup/yellow %}
Here it is quickly seen that something is **awry...** (the topographies are not smooth, and the lead fields are of too great a magnitude (millivolts))
{% include markup/end %}

Let's change to the _dipoli_ head model (load it if you cannot create it)

    headmodel = headmodel_dipoli;

and run the code creating _elec_realigned_, _sourcemodel_ and _sourcemodel_and_leadfield_ again with _headmodel_ as _headmodel_dipoli_

{% include markup/skyblue %}
Now the plots look **correct** - (the electric potentials are in the order of microvolts and the topographies look smooth)
{% include markup/end %}

{% include image src="/assets/img/workshop/oslo2019/leadfield_components_topo.png" width="650" %}
_Figure 12: Lead fields in the_ XYZ-_directions for_ headmodel_dipoli _for a superficial source_

{% include image src="/assets/img/workshop/oslo2019/leadfield_magnitude_topo.png" width="650" %}
_Figure 13: Magnitude of the lead fields for_ headmodel_dipoli _for a superficial source_

{% include markup/skyblue %}
When plotting the lead field topographies, try to change _source_index_ and _sensory_dipole_current_ to change the topography and get a feeling for how it works. Also change the source index (will work for a number between 1 and 1659)
{% include markup/end %}

{% include markup/skyblue %}
Do always check the lead field of both a superficial source, as this is where errors are most prone, and a central source. If you see errors for the superficial sources, you can use _cfg.inwardshift_ from **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** as this removes sources from the outermost parts of the brain
{% include markup/end %}

We can also plot the vectors - note that they are more or less normal to the scalp surface. Also note that we are using an unrealistic source current here, 1 mAm. This is just to make sure that they are visible. Do play around with it to see its effect.

    % source_index 300 is central, 1200 is superficial

    figure
    hold on
    ft_plot_sens(elec_realigned, 'elecsize', 40);
    ft_plot_headmodel(headmodel, 'facealpha', 0.5);
    view(90, 0)

    source_index = 1200;
    sensory_dipole_current = 1e-3; % Am (unrealistic)
    n_sensors = length(elec_realigned.label);

    inside_sources = find(sourcemodel_and_leadfield.inside);
    inside_index = inside_sources(source_index);
    lead = sourcemodel_and_leadfield.leadfield{inside_index};

    for sensor_index = 1:n_sensors
        this_pos = elec_realigned.chanpos(sensor_index, :);
        this_lead = lead(sensor_index, :);
        this_voltage = this_lead * sensory_dipole_current;
        quiver3(this_pos(1), this_pos(2), this_pos(3), ...
                this_voltage(1), this_voltage(2), this_voltage(3), 'r', ...
                'linewidth', 3, 'markersize', 100);
    end

    plot3(sourcemodel_and_leadfield.pos(inside_index, 1), ...
          sourcemodel_and_leadfield.pos(inside_index, 2), ...
          sourcemodel_and_leadfield.pos(inside_index, 3), 'o', ...
          'markersize', 60, 'markerfacecolor', 'r')

{% include image src="/assets/img/workshop/oslo2019/leadfield_vector.png" width="650" %}
_Figure 14: Orientations of the lead fields for_ headmodel_dipoli _for a superficial source_

## Bonus: troubleshooting the meshes

The _bemcp_ algorithm might have failed due to the meshes overlapping (_brain_, _skull_ and _scalp_). One way to test this is to increase the number of vertices when creating the meshes at the expense of an increase in processing time. I tested it with a fine head model where all the meshes had 10,000 vertices. This also didn't succeed. In other cases, you might succeed, so it might be worth trying. One reason that it might fail is that the segmented surfaces are "too" thin at places. The following code will exemplify this. First, we create a "binary" mri, where _brain_, _skull_ and _scalp_ are expressed binarily. Then a _combined_ field is created.

    mri_segmented_binary = mri_segmented; % make a copy

    binary_brain = mri_segmented.brain;
    binary_skull = mri_segmented.skull | mri_segmented.brain;
    binary_scalp = mri_segmented.scalp | mri_segmented.skull | mri_segmented.brain;

    mri_segmented_binary.combined = binary_scalp + binary_skull + binary_brain;

We subsequently plot this _combined_ field at a location where the skin is very thin. Please have a look around and ascertain for yourself that these thin places exist

    cfg              = [];
    cfg.funparameter = 'combined';
    cfg.location     = [-74 -4 30];

    ft_sourceplot(cfg, mri_segmented_binary);

{% include image src="/assets/img/workshop/oslo2019/surfaces.png" width="650" %}
_Figure 15: The_ brain _(white),_ skull _(yellow) and_ scalp _surfaces (red). Notice how thin the scalp is at places, which will make the potentials (in the model) escape from the skull to the air around it directly_

## Which BEM algorithm to use?

If possible, you should use the [OpenMEEG algorithm](https://openmeeg.github.io/) implemented in FieldTrip (in **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** use _cfg.method = 'openmeeg'_. This may require some [careful installation](/faq/source/openmeeg) before it works, and it only works on Linux and Mac systems.

If you cannot make this work, then _dipoli_, which also only works on Linux and Mac systems (at the moment) is your next choice, and finally _bemcp_ which works on all platforms.
