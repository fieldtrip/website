---
title: Plot the topographies of HPI coils and different MEG phantoms 
tags: [meg, phantom, opm]
category: example
redirect_from:
    - /example/phantom_topographies/
---

In this example we compute the spatial topographies of a variety of MEG phantoms: first for three magnetic dipole coils that are placed as head position indicators (HPIs) on the location of the nasion and left and right preauricular points (LPA and RPA). Subsequently, we compute and plot the topographies for different types of MEG phantoms.

All computations below are done for 144 radial OPM channels placed in a FieldLine beta 2 helmet, but they could equally well be done for any other arragmenent of the MEG sensors, either for SQUID or for OPM sensors. You can also provide your own sensor definition, see this [FAQ](/faq/source/sensors_definition/#the-definition-of-meg-sensors) and the documentation in the **[ft_datatype_sens](/reference/ft_datatype_sens)** function.

When changing the MEG sensor array to another template or to your own, please consider that the sensor arrays can be expressed relative to different [head coordinaye systems](/faq/source/coordsys). The FieldLine beta 2 helmet used below follows the Neuromag convention and has the x-axis towards the right, the y-asix to the front, and the z-axis in the superior direction.

    % The following templates are located in fieldtrip/template/gradiometer

    % load bti148.mat
    % load bti248.mat
    % load bti248grad.mat
    % load ctf64.mat
    % load ctf151.mat
    % load ctf275.mat
    % load neuromag122.mat
    % load neuromag306.mat
    % load yokogawa160.mat
    % load yokogawa208.mat
    % load fieldlinealpha1.mat

    load fieldlinebeta2.mat

Since all phantoms that we will consider here for now are coils that emulate a magnetic dipole phantoms, we construct an infinite volume conductor.

    headmodel = ft_headmodel_infinite();
    headmodel.unit = 'm';

## Construct the phantom coils

{% include markup/green %}
The snippets of code for the different HPI or phantom coil arrangements below are all handled in the same way. We first construct a `phantom` structure with the positions and orientations of the phantom coils. Those are formatted similar to the FieldTrip `grad` structure, so that we can use the **[ft_plot_sens](/reference/plotting/ft_plot_sens)** function for visualization.

After constructing one of the `phantom` structures, we plot the phantom coils together with the OPM helmet and then we compute and visualise the spatial topographies of all the phantom coils.

To move or rotate either the OPM helmet or the phantom coil array, you can use **[ft_transform_geometry](/reference/ft_transform_geometry)** or other functions for realignment.
{% include markup/end %}

### HPI coils on the anatomical landmarks

    % this approximates where I would expect the nose and ears
    nas = [0  8 0]/100;
    lpa = [-8 0 0]/100;
    rpa = [+8 0 0]/100;

    phantom.coilpos = [
        nas
        lpa
        rpa
    ];
    phantom.coilori = [
         0 1 0
        -1 0 0
        +1 0 0
    ];
    phantom.label = {
        'nas'
        'lpa'
        'rpa'
    };

{% include image src="/assets/img/example/phantom_topographies/hpi.png" width=400 %}

This is the image of the topographies for the HPI coils, computed and plotted with the shared [code further down](#compute-and-plot-the-phantom-coil-topographies).

{% include image src="/assets/img/example/phantom_topographies/hpi_topo.png" width=600 %}

### QuSpin HALO

QuSpin has designed their HALO to calibrate the OPM sensor positions and orientations. It consists of a circular printed circuit board (PCB) with 16 electromagnetic coil positions arranged in three distinct concentric layouts. Each of the 16 coils has a diameter of approximately 22 mm. The flat circular board is mounted on a base that holds it roughly 5 cm directly above the participant's helmet or sensor array. It is described in the publication ["Determining sensor geometry and gain in a wearable MEG system"](https://doi.org/10.1162/imag_a_00535) by Hill et al. (2025).

    % Outer Circle: 12 dipolar coils are evenly spaced every 30 degrees around a circle with a radius of 12.7 cm.
    % Inner Circle: 3 dipolar coils are spaced at 120-degree intervals around a smaller circle with a radius of 6.3 cm.
    % Center: 1 final dipole coil is positioned directly at the center of the circular board.

    phantom.coilpos = zeros(16,3);
    phantom.coilori = zeros(16,3);
    phantom.coilori(:,3) = 1; % they are all pointing in the z-direction
    % phantom.label = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'};
    phantom.label = {'12', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '13', '16', '15', '14'};
    
    for i=1:12
        [x, y] = pol2cart(pi/2 - (i-1)*2*pi/12, 0.127);
        phantom.coilpos(i,1) = x;
        phantom.coilpos(i,2) = y;
        phantom.coilpos(i,3) = 0.05 + max(fieldlinebeta2.coilpos(:,3)); % 5 cm above the top of the helmet
    end

    for i=1:3
        [x, y] = pol2cart(pi/2 - (i-1)*2*pi/3, 0.063);
        phantom.coilpos(12+i,1) = x;
        phantom.coilpos(12+i,2) = y;
        phantom.coilpos(12+i,3) = 0.05 + max(fieldlinebeta2.coilpos(:,3)); % 5 cm above the top of the helmet
    end

    phantom.coilpos(16,1) = 0;
    phantom.coilpos(16,2) = 0;
    phantom.coilpos(16,3) = 0.05 + max(fieldlinebeta2.coilpos(:,3)); % 5 cm above the top of the helmet

{% include image src="/assets/img/example/phantom_topographies/halo.png" width=400 %}

This is the image of the HALO coil topographies, computed and plotted with the shared [code further down](#compute-and-plot-the-phantom-coil-topographies).

{% include image src="/assets/img/example/phantom_topographies/halo_topo.png" width=600 %}

### Cerca "Squalo"

Cerca has a PCB board with a 5x5 arrangement of magnetic dipole coils that I have seen in the MEG lab in Amsterdam. I don't know the exact dimensions, so this is just an approximation.

    % the following constructs a 20x20 cm grid placed posterior of the participant
    % you can change this according to where you want the grid to be located 
    xgrid = linspace(-0.1, 0.1, 5);  
    ygrid = -0.2;
    zgrid = linspace(-0.1, 0.1, 5);
    [X, Y, Z] = ndgrid(xgrid, ygrid, zgrid);

    phantom = [];
    phantom.coilpos = [X(:) Y(:) Z(:)];
    phantom.coilori = zeros(size(phantom.coilpos));
    phantom.coilori(:,2) = 1;
    phantom.label = arrayfun(@num2str, 1:size(phantom.coilpos,1), 'UniformOutput', false)';

{% include image src="/assets/img/example/phantom_topographies/squalo.png" width=400 %}

This is the image of the Squalo coil topographies, computed and plotted with the shared [code further down](#compute-and-plot-the-phantom-coil-topographies).

{% include image src="/assets/img/example/phantom_topographies/squalo_topo.png" width=600 %}

### Spherical HPI array

At the DCCN we constructed an array with 24 HPI coils on a 120 mm diameter sphere that we use in combination with a 24-channel phantom current driver. More details will be posted soon on the [open hardware](/faq/other/open_hardware) page.

    phantomcoil.unit = 'mm';
    phantomcoil.coilpos = [
              0         0   60.0000
         0.0000   36.4237   47.6793
        34.6410   11.2555   47.6793
        21.4093  -29.4674   47.6793
       -21.4093  -29.4674   47.6793
       -34.6410   11.2555   47.6793
        31.5439   43.4164   26.8328
        51.0390  -16.5836   26.8328
         0.0000  -53.6656   26.8328
       -51.0390  -16.5836   26.8328
       -31.5439   43.4164   26.8328
         0.0000   58.9348   11.2555
        56.0503   18.2119   11.2555
        34.6410  -47.6793   11.2555
       -34.6410  -47.6793   11.2555
       -56.0503   18.2119   11.2555
        34.6410   47.6793  -11.2555
        56.0503  -18.2119  -11.2555
         0.0000  -58.9348  -11.2555
       -56.0503  -18.2119  -11.2555
       -34.6410   47.6793  -11.2555
         0.0000   53.6656  -26.8328
        34.6410  -11.2555  -47.6793
       -34.6410  -11.2555  -47.6793
    ];
    phantomcoil.coilori = [
              0         0    1.0000
         0.0000    0.6071    0.7947
         0.5774    0.1876    0.7947
         0.3568   -0.4911    0.7947
        -0.3568   -0.4911    0.7947
        -0.5774    0.1876    0.7947
         0.5257    0.7236    0.4472
         0.8507   -0.2764    0.4472
        -0.0000   -0.8944    0.4472
        -0.8507   -0.2764    0.4472
        -0.5257    0.7236    0.4472
         0.0000    0.9822    0.1876
         0.9342    0.3035    0.1876
         0.5774   -0.7947    0.1876
        -0.5774   -0.7947    0.1876
        -0.9342    0.3035    0.1876
         0.5774    0.7947   -0.1876
         0.9342   -0.3035   -0.1876
        -0.0000   -0.9822   -0.1876
        -0.9342   -0.3035   -0.1876
        -0.5774    0.7947   -0.1876
         0.0000    0.8944   -0.4472
         0.5774   -0.1876   -0.7947
        -0.5774   -0.1876   -0.7947
    ];
    phantomcoil.label = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24' };

{% include image src="/assets/img/example/phantom_topographies/spherical.png" width=400 %}

This is the image of the topographies of the 24 coils in this spherical arrangement, computed and plotted with the shared [code further down](#compute-and-plot-the-phantom-coil-topographies).

{% include image src="/assets/img/example/phantom_topographies/spherical_topo.png" width=600 %}

### Adachi sphere

Adachi and colleagues describe a spherical phantom in their 2023 paper ["A Spherical Coil Array for the Calibration of Whole-Head Magnetoencephalograph Systems"](https://doi.org/10.1109/TIM.2023.3265750) that consists of large coils wrapped around a sphere. At the DCCN we constructed one based on a 3D-printed sphere with 120 mm diameter. This phantom can be described with the following geometry, where the center of each coil is teh same as the center of the sphere.

    phantom = [];
    phantom.unit = 'm';
    phantom.coilpos = zeros(16,3);
    phantom.coilori = [
              0         0    1.0000
         0.8944         0    0.4472
         0.2764   -0.8507    0.4472
        -0.7236   -0.5257    0.4472
        -0.7236    0.5257    0.4472
         0.2764    0.8507    0.4472
         0.4911   -0.3568    0.7947
        -0.1876   -0.5774    0.7947
        -0.6071         0    0.7947
        -0.1876    0.5774    0.7947
         0.4911    0.3568    0.7947
         0.7947   -0.5774    0.1876
         0.3035   -0.9342   -0.1876
        -0.3035   -0.9342    0.1876
        -0.7947   -0.5774   -0.1876
        -0.9822         0    0.1876
        ];
    phantom.label = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16'}';

Each of the 16 coils has a diameter of 120 mm. To plot these correctly with **[ft_plot_sens](/reference/plotting/ft_plot_sens)**, you have to specify a a coilsize of 120 mm.

{% include image src="/assets/img/example/phantom_topographies/adachi.png" width=400 %}

All other phantoms considered here have very small HPI-like coils that we model as a magnetic dipole. For most EEG and MEG volume conduction models the **[ft_compute_leadfield](/reference/forward/ft_compute_leadfield)** will assume that the source is an equivalent current dipole (ECD). When we specify the volume conductor type as as "infinite" and pass a MEG sensor array rather than an EEG electrode array, it will compute the leadfield for a magnetic dipole.

To compute the leadfield matrix (i.e. the topography for a coil in the x, y, and z-direction) for a coil of a specific size, we have to specify the size in the headmodel. So to compute the topography for coils wrapped around the 120 mm diameter sphere, you have to specify the following headmodel:

    headmodel = [];
    headmodel.type = 'circularcoil';
    headmodel.diameter = 0.12;
    headmodel.unit = 'm';

This is the image of the topographies of the 24 coils in this spherical arrangement, more or less computed and plotted with the shared [code further down](#compute-and-plot-the-phantom-coil-topographies) with the headmodel as specified above.

{% include image src="/assets/img/example/phantom_topographies/adachi_topo.png" width=600 %}

### Neuromag dry phantom

The Neuromag/Elekta/MEGIN system comes with a dry current-dipole phantom that is detailed on [this page](https://neuroimage.usc.edu/brainstorm/Tutorials/PhantomElekta) from the BrainStorm documentation.

Since this does not use magnetic dipoles, but emulates equivalent current dipoles, we cannot work with the infinite homogenous medium but have to specify a spehere with a given radius and origin:

    headmodel = [];
    headmodel.type = 'singlesphere';
    headmodel.unit = 'm';
    headmodel.r = 0.12;
    headmodel.o = [0 0 0];

The coordinates below are in millimetres, relative to the phantom sphere centre, with +X toward the nasion, +Y toward the left ear, and +Z upward.

    phantom = [];
    phantom.coilpos = [
       0    -59.7  22.9  % negative Y, so this should be close to the right ear
       0    -48.6  23.5
       0    -35.8  25.5
       0    -24.8  23.1
       0    -37.2  52
       0    -27.5  46.4
       0    -15.8  41
       0    -7.9   33
     -59.7   0     22.9
     -48.6   0     23.5
     -35.8   0     25.5
     -24.8   0     23.1
     -37.2   0     52
     -27.5   0     46.4
     -15.8   0     41
      -7.9   0     33
       0    46.1   44.4
       0    41.9   34
       0    38.3   21.6
       0    31.5   12.7
       0    13.9   62.4
       0    16.2   51.5
       0    20     39.1
       0    19.3   27.9
      46.1   0     44.4
      41.9   0     34
      38.3   0     21.6
      31.5   0     12.7
      13.9   0     62.4
      16.2   0     51.5
      20     0     39.1
      19.3   0     27.9
    ];

    phantom.coilori = [
         0.00  0.36  0.93
         0.00  0.44  0.90
         0.00  0.58  0.81
         0.00  0.68  0.73
         0.00  0.81  0.58
         0.00  0.86  0.51
         0.00  0.93  0.36
         0.00  0.97  0.23
         0.36  0.00  0.93
         0.44  0.00  0.90
         0.58  0.00  0.81
         0.68  0.00  0.73
         0.81  0.00  0.58
         0.86  0.00  0.51
         0.93  0.00  0.36
         0.97  0.00  0.23
         0.00 -0.69  0.72
         0.00 -0.63  0.78
         0.00 -0.49  0.87
         0.00 -0.37  0.93
         0.00 -0.98  0.22
         0.00 -0.95  0.30
         0.00 -0.89  0.46
         0.00 -0.82  0.57
        -0.69  0.00  0.72
        -0.63  0.00  0.78
        -0.49  0.00  0.87
        -0.37  0.00  0.93
        -0.98  0.00  0.22
        -0.95  0.00  0.30
        -0.89  0.00  0.46
        -0.82  0.00  0.57
    ];

    phantom.label = { '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32'}';

    % convert to meter
    phantom.coilpos = phantom.coilpos/1000;

    % the FieldLine helmet is defined in a coordinate system with +X to the right and +Y to the nose
    % rotate the phantom so that the first dipole (with negative Y) is close to the right ear
    phantom = ft_transform_geometry([0 0 90], phantom, 'rotate');

Plotting these is also slightly different than plotting the HPI coils. We can use the following code:

    figure
    ft_plot_sens(fieldlinebeta2, 'axes', false, 'fiducial', false)
    % ft_plot_sens(phantom, 'label', 'label')
    ft_plot_dipole(phantom.coilpos, phantom.coilori', 'unit', 'm')

{% include image src="/assets/img/example/phantom_topographies/neuromag.png" width=600 %}

Computing and plotting the topographies of all ECD sources resuylts in the following figure.

{% include image src="/assets/img/example/phantom_topographies/neuromag_topo.png" width=600 %}

## Shared code

### Visualize the phantom coils together with the OPM sensors

The following code can be used with most of the `phantom` structures that we created above. The coil size that is plotted is not geometrically correct, but set to 10 mm to make it easier to see the coil and orientation.

For the Adachi sphere the coil size should be specified as 120 mm. For the Neuromag dry phantom we should not plot the ECDs as coils, but only as dipoles.

    figure
    ft_plot_sens(fieldlinebeta2, 'axes', false, 'fiducial', false)
    ft_plot_sens(phantom, 'coil', true, 'orientation', false, 'coilsize', 0.01)
    % ft_plot_sens(phantom, 'label', 'label')
    ft_plot_dipole(phantom.coilpos, phantom.coilori', 'unit', 'm')

### Compute and plot the phantom coil topographies

The following code (with some minor changes) can be used with all `phantom` structures that we created above.

    % compute actual magnetic field values in SI units
    diameter = 0.006;
    turns    = 3;
    area     = pi*(diameter/2)^2;
    current  = 5 / 200000; % 5V peak-to-peak over a 200 kOhm resistor
    mom      = turns * area * current;

    nchans = length(fieldlinebeta2.label);
    ncoils = length(phantom.label);

    dat = zeros(nchans, ncoils);
    for i=1:ncoils
        dat(:,i) = ft_compute_leadfield(phantom.coilpos(i,:), fieldlinebeta2, headmodel) * mom * phantom.coilori(i,:)';
    end

    m = max(abs(dat(:)));
    fprintf('max field is %f pT\n', m * 1e12)

    figure
    clear ax
    n = ceil(sqrt(length(phantom.label)));

    for i=1:ncoils
        ax(i) = subplot(n,n,i);
        ft_plot_topo3d(fieldlinebeta2.coilpos, dat(:,i), 'refine', 1);
        ft_colormap('-RdBu')
        ft_plot_sens(fieldlinebeta2, 'fiducial', false)
        ft_plot_sens(phantom, 'chanindx', i, 'coil', true, 'orientation', true, 'coilsize', diameter);
        ft_plot_dipole(phantom.coilpos(i,:), phantom.coilori(i,:)', 'unit', 'm')
        clim([-m m])
    end

    linkprop(ax, {'CameraPosition', 'CameraUpVector'});
    rotate3d on

You should rotate the helmet topographies to get a correct 3D representation of the OPMs, the phantom coils, and their topographies. For the configurations with more phantoms coils this is difficult to capture in a screen shot, so please compute and plot them yourself.
