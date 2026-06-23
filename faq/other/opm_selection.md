---
title: How do I select 32 OPM sensor positions from the 144 slots in the FieldLine Beta2 smart helmet?
tags: [opm, fieldline, template]
category: faq
---

The FieldLine Beta2 smart helmet that we have at the DCCN has 144 slots for OPM sensors. The template gradiometer definition that is included with FieldTrip lists all those slots, which each have a name like `L101_bz` or `R503_bz`. The prefix (`L` or `R`) indicates the left or right side of the helmet, the three-digit number indicates the slot, and the suffix indicates the orientation (`_bx`, `_by`, or `_bz`) of the corresponding channel. When using the FieldLine HEDscan v3 system each OPM sensor is capable of measuring the magnetic field in either one, two, or in three orthogonal directions (bx, by, and bz), so each physical slot corresponds to three separate entries in the gradiometer.

{% include markup/yellow %}
It is recommended to work with the two orientations `by` and `bz`, since the sensitivity of the `bx` channel is along the direction of the laser and is very noisy.
{% include markup/end %}

At the DCCN we currently only have 32 OPM sensors (which means 64 channels) which we can distribute over the 144 slots in the helmet. Depending on your research question you may want to position these 32 sensors over specific brain regions.

The following code demonstrates how to make a graphical selection of the helmet slots in which to place the OPM sensors

## Reading the template sensor positions

You can read the full Beta2 helmet template with all 144 slots using:

    grad = ft_read_sens('fieldtrip/template/gradiometer/fieldlinebeta2.mat');

    % it is important to work in consistent units, so let's convert everything to SI units (m, T, V, etc)
    grad = ft_convert_units(grad, 'm');

To inspect the helmet layout:

    figure
    ft_plot_sens(grad, 'fiducial', false)
    view([135 20]);

## Manual selection of sensor slots

For a specific experiment you will have to decide in which of the 144 slots to place the 32 OPM sensors. A very simple selection would for example be to select every fourth sensor location:

    cfg = [];
    cfg.channel = 1:4:144; % select every 4th sensor
    selected = ft_electrodeselection(cfg, grad);

    figure
    ft_plot_sens(selected, 'fiducial', false)

or to select all locations on the left:

    cfg = [];
    cfg.channel = 'L*'; % starting with L
    selected = ft_electrodeselection(cfg, grad);

    figure
    ft_plot_sens(selected, 'fiducial', false)

## Graphical selection of sensor slots

As demonstrated in the [OPM helmet design](/tutorial/sensor/opm_helmet_design) tutorial, using the **[ft_sensorplacement](/reference/ft_sensorplacement)** function we can distribute sensors on a 3D printed helmet. This is not what we need here, but the function also returns a 3D model of all sensor positions. This allows us to see where the sensors would or could be, and using  **[ft_electrodeselection](/reference/ft_electrodeselection)** we can subsequently make a selection.

We have to trick **[ft_sensorplacement](/reference/ft_sensorplacement)** into using our predefined OPM sensor locations from the temlpate helmet as electrode positions. On each electrode position, it will place an OPM sensor (and the 3D model).

    % make an electrode structure
    elec = keepfields(grad, {'unit', 'coordsys'});
    elec.type = 'eeg';
    elec.label = grad.label;
    elec.elecpos = grad.coilpos;  % this is the position of each "electrode" or OPM
    elec.elecori = grad.coilori;  % this is the orientation of each "electrode" or OPM

We also need a head surface on which the electrodes can be projected. We can simply take the electrode (or template OPM) positions and use that instead of a real head surface.

    headshape = elec.elecpos;

Finally we need the 3D model of the sensor geometry, which will be copied and placed on each electrode position.

    template = ft_read_headshape('fieldline_sensor.stl');
    template.unit = 'mm';
    template = ft_convert_units(template, 'm');

With these inputs, we can now generate the sensor positions, which will be the same as the original ones, but importantly also the 3D OPM sensor geometry structure.

    cfg = [];
    cfg.template = template;
    cfg.elec = elec;
    [cfg, sensor] = ft_sensorplacement(cfg, headshape);


    figure
    ft_plot_sens(grad);
    ft_plot_mesh(sensor)

Now that we have the 3D model of the 144 sensors, we can plot them as a mesh in  **[ft_electrodeselection](/reference/ft_electrodeselection)**. You can use the MATLAB rotate button to look from different angles at the helmet and when 3D rotation is off, you  can click on an electrode (which is at the base of each OPM sensor) to enable/disable each sensor.

    cfg = [];
    cfg.headshape = elec.elecpos;
    cfg.mesh = sensor;
    selected = ft_electrodeselection(cfg, grad);

Since we have 144 slots and 32 sensors, we have to disable 112 of the possible slots. Rather than starting with all sensors enabled, you can also start with a single sensor enabled. You can subsequently disable that channel, and start selecting the 32 sensor positions from a blank slate. It is not possible to start without any sensor selected, so you should always at least have one in `cfg.channel`.

    cfg = [];
    cfg.headshape = elec.elecpos;
    cfg.mesh = sensor;
    cfg.channel = 1; % only select the 1st sensor to start with
    selected = ft_electrodeselection(cfg, grad);

Recommended is to place at least 5 sensors evenly spaced around the head to keep it in place within the helmet: one on the vertex, two at the temples, and two at the front and back.

## See also

For more information on handling and analyzing OPM data see also these tutorials

{% include seealso category="tutorial" tag="opm" %}

and example scripts

{% include seealso category="example" tag="opm" %}

and frequently asked questions.

{% include seealso category="faq" tag="opm" %}
