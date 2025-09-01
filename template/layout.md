---
title: Template 2-D layouts for plotting
tags: [template, eeg, meg, opm, layout]
---

EEG electrode and MEG gradiometer positions in the layouts are represented as points in 2-D Cartesian space, i.e. with an X and Y position for each electrode. Furthermore, each electrode has a label. In the [layout tutorial](/tutorial/plotting/layout) you can find more details on how to create and use them. The file format for layout files specified as ASCII `.lay` files is explained [here](/faq/plotting/layout_fileformat).

## EEG layouts

### Standard 10-20, 10-10 and 10-5 caps

The following template layouts are for an electrode cap based on a standard 10-20 (20%), 10-10 (10%) and 10-5 (5%) montage.

{% include image src="/assets/img/template/layout/eeg1020.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/eeg1010.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/eeg1005.lay.png" width="200" %}

{% include image src="/assets/img/template/layout/elec1020.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/elec1010.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/elec1005.lay.png" width="200" %}

### BrainProducts

The following template layouts are for electrode caps from [Brain Products](http://www.brainproducts.com). FieldTrip provides .mat files (since r6121 - june 2012) that are based on the bitmap images shown below. Note that some of these layouts were created specifically for the DCCN, DCC and MPI, and may differ from other actiCAP layouts. For a standard actiCap layout, see `acticap-64ch-standard2.mat`.

##### dccn_customized_acticap64.mat

This is a custom 64-channel arrangement for the Donders Centre for Cognitive Neuroimaging (DCCN). It is based on a equidistant M10 cap and has electrode numbers rather than electrode names. The 32 channels from the 1st amplifier are located central, the 32 channels from the 2nd amplifier are along the rim, which means that electrodes preparation goes in outward moving circles.

{% include image src="/assets/img/template/layout/original/dccn_customized_acticap64.png" width="200" %}
{% include image src="/assets/img/template/layout/dccn_customized_acticap64.mat.png" width="200" %}

##### dcc_customized_acticap64.mat

This is a custom 64-channel arrangement for the Donders Centre for Cognition (DCC). It is based on a 10-10 electrode layout, and uses two 32-channel EEG amplifiers. The green electrode holders correspond to the 32 channels from the 1st amplifier, and the yellow electrode holders correspond to the 32 channels from the 2nd amplifier. The reference and ground are included in the layout with the original name for the electrode location (TP9 and AFz).

{% include image src="/assets/img/template/layout/original/dcc_customized_acticap64.png" width="200" %}
{% include image src="/assets/img/template/layout/dcc_customized_acticap64.mat.png" width="200" %}

##### mpi_customized_acticap64.mat

This is a custom 64-channel arrangement for the Max Planck Institute for Psycholinguistics (MPI). It is based on a equidistant M10 cap and has electrode numbers rather than electrode names. Note that the electrode positions are the same as for the DCCN customized version above, but that the channel order is different. The MPI version has the 32 channels from the 1st amplifier on the right and the 32 channels from the 2nd amplifier on the left, making it easier for two researchers to prepare the EEG cap on the subject simultaneously.

{% include image src="/assets/img/template/layout/original/mpi_customized_acticap64.png" width="200" %}
{% include image src="/assets/img/template/layout/mpi_customized_acticap64.mat.png" width="200" %}

##### acticap-64ch-standard2.mat

This is the standard 64-channel actiCAP arrangement from [Brain Products](http://www.brainproducts.com/files/public/downloads/actiCAP-64-channel-Standard-2_1201.pdf). It is based on the same coordinates as the EasyCap electrode caps. This particular layout was created from the EasyCap M1 layout and then removing eight electrodes (FPz, Iz, F9, F10, P9, P10, O9, O10) which are not present in this cap. Furthermore, two electrodes (AFz, FCz) were renamed to their purpose of being Ground (Gnd) and Reference (Ref) electrode.

{% include image src="/assets/img/template/layout/original/acticap-64-channel-standard-2.jpg" width="200" %}
{% include image src="/assets/img/template/layout/acticap-64ch-standard2.mat.png" width="200" %}

##### BrainProducts R-Net

The following layout is for the 64-channel wet-sponge [R-Net](https://www.brainproducts.com/solutions/r-net/) from BrainProducts.

{% include image src="/assets/img/template/layout/original/rnet64.png" width="200" %}
{% include image src="/assets/img/template/layout/rnet64.mat.png" width="200" %}

### BioSemi

The following template layouts are for [BioSemi](http://www.biosemi.com) caps for active electrodes.

{% include image src="/assets/img/template/layout/biosemi16.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi32.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi64.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi128.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi160.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi256.lay.png" width="200" %}

### EasyCap

The following series of template layouts is for the electrode caps from [EasyCap](http://www.easycap.de). They are sorted based on their electrode montages. FieldTrip provides .mat files (since r5201 - feb 2012) that are based on the bitmap images obtained from the easycap website and shown below. The layout structure stored in those .mat files contains fields that describe the position (.pos), the width (.width), and the height (.height), and the naming (.label) of the electrodes. Furthermore, it contains fields that describe the topographic interpolation boundaries (.mask) and the outlines of the 'head' (.outline).

#### EasyCap 10% arrangements

##### easycapM1 - 74-channel arrangement (used in EC80)

{% include image src="/assets/img/template/layout/original/easycapm1.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm1.mat.png" width="200" %}

##### easycapM3 - Extended 10/20-System with 30 Channels

{% include image src="/assets/img/template/layout/original/easycapm3.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm3.mat.png" width="200" %}

##### easycapM11 - 61-channel arrangement ("10%-System") (used in BrainCap64)

{% include image src="/assets/img/template/layout/original/easycapm11.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm11.mat.png" width="200" %}

##### easycapM15 - 128-channel arrangement

{% include image src="/assets/img/template/layout/original/easycapm15.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm15.mat.png" width="200" %}

##### easycapM22 - Small Equidistant 29-channel arrangement (used in Braincap32)

{% include image src="/assets/img/template/layout/original/easycapm22.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm22.mat.png" width="200" %}

##### easycapM23 - Large Equidistant 32-channel arrangement

{% include image src="/assets/img/template/layout/original/easycapm23.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm23.mat.png" width="200" %}

##### easycapM24 - Large Equidistant 34-channel arrangement (used in EC40)

{% include image src="/assets/img/template/layout/original/easycapm24.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm24.mat.png" width="200" %}

##### easycapM25 - International 10/20-System (used in EC20)

{% include image src="/assets/img/template/layout/original/easycapm25.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm25.mat.png" width="200" %}

#### EasyCap triangulated equidistant arrangements

##### easycapM7 - Spherical 32-channel arrangement

{% include image src="/assets/img/template/layout/original/easycapm7.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm7.mat.png" width="200" %}

##### easycapM10 - Equidistant 61-channel arrangement

{% include image src="/assets/img/template/layout/original/easycapm10.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm10.mat.png" width="200" %}

##### easycapM14 - Spherical 124-channel arrangement

{% include image src="/assets/img/template/layout/original/easycapm14.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm14.mat.png" width="200" %}

##### easycapM16 - Equidistant 88-channel arrangement

{% include image src="/assets/img/template/layout/original/easycapm16.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm16.mat.png" width="200" %}

#### EasyCap miscellaneous arrangements

The following template layouts are provided

- easycapM17.mat
- easycapM20.mat

##### easycapM17 - 29-channel arrangement for Language Research

{% include image src="/assets/img/template/layout/original/easycapm17.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm17.mat.png" width="200" %}

##### easycapM20 - BESA 32-channel arrangement for Epilepsy Diagnostics

{% include image src="/assets/img/template/layout/original/easycapm20.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm20.mat.png" width="200" %}

### EGI geodesic sensor nets

The following template layouts were created from the `.sfp` files that define the 3D electrode positions for EGI geodesic sensor nets. The code to generate these layouts is in `fieldtrip/test/test_layout_egi.m`.

{% include image src="/assets/img/template/layout/gsn-hydrocel-32.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/gsn-hydrocel-64.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/gsn-hydrocel-65.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/gsn-hydrocel-128.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/gsn-hydrocel-129.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/gsn-hydrocel-256.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/gsn-hydrocel-257.mat.png" width="200" %}

### NeuroScan Quick-Cap

The following template layouts are for electrode caps from [NeuroScan](http://www.neuroscan.com). The origin and construction is described on <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=679>. The quikcap_nsl_128 layout has been kindly provided by Andre Cravo.

{% include image src="/assets/img/template/layout/quickcap64.mat.png" width="200" %} (since june 2012 - r6055)
{% include image src="/assets/img/template/layout/quikcap_nsl_128.mat.png" width="200" %} (since nov 2012 - r6915)

### TMSi infinity gel headcap

The following template layouts are for the [32- and 64-channel electrode caps](https://knowledge.tmsi.com/electrode-lay-out-infinity-gel-cap) from [TMSi](https://www.tmsi.com/).

##### tmsi32 - TMSi 32-channel infinity gel headcap

{% include image src="/assets/img/template/layout/tmsi32.lay.png" width="200" %} 

##### tmsi64 - TMSi 64-channel infinity gel headcap

{% include image src="/assets/img/template/layout/tmsi64.lay.png" width="200" %}

## MEG layouts

### BTi/4D system

The following template layouts are for the sensor arrays of the BTi/4D MEG system.

{% include image src="/assets/img/template/layout/4d148.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/4d248.lay.png" width="200" %}

#### With a more realistic display along the rim

{% include image src="/assets/img/template/layout/4d248_helmet.mat.png" width="200" %}

### CTF system

The following template layouts are for a sensor array of the CTF MEG system.

{% include image src="/assets/img/template/layout/ctf151.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/ctf275.lay.png" width="200" %}

#### With a more realistic display along the rim

{% include image src="/assets/img/template/layout/ctf151_helmet.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/ctf275_helmet.mat.png" width="200" %}

### FieldLine OPM system

##### Alpha-1 smart helmet

{% include image src="/assets/img/template/layout/fieldlinealpha1_helmet.mat.png" width="200" %}

##### Beta-2 smart helmet

{% include image src="/assets/img/template/layout/fieldlinebeta2bx_helmet.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/fieldlinebeta2by_helmet.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/fieldlinebeta2bz_helmet.mat.png" width="200" %}
{% include image src="/assets/img/template/layout/fieldlinebeta2all_helmet.mat.png" width="200" %}

### Neuromag/Elekta/Megin system

#### 306-channel system

##### with all channels

{% include image src="/assets/img/template/layout/neuromag306all.lay.png" width="200" %}

##### with only the magnetometers

{% include image src="/assets/img/template/layout/neuromag306mag.lay.png" width="200" %}

##### with only the planar gradiometers

{% include image src="/assets/img/template/layout/neuromag306planar.lay.png" width="200" %}

##### with the combined planar gradiometers

{% include image src="/assets/img/template/layout/neuromag306cmb.lay.png" width="200" %}

##### with a more realistic display along the rim, all channels

{% include image src="/assets/img/template/layout/neuromag306all_helmet.mat.png" width="200" %}

##### with a more realistic display along the rim, planar gradiometers only

{% include image src="/assets/img/template/layout/neuromag306planar_helmet.mat.png" width="200" %}

##### with a more realistic display along the rim, planar gradiometers combined

{% include image src="/assets/img/template/layout/neuromag306cmb_helmet.mat.png" width="200" %}

##### with a more realistic display along the rim, magnetometers only

{% include image src="/assets/img/template/layout/neuromag306mag_helmet.mat.png" width="200" %}

#### 122-channel system

##### with the planar gradiometers

{% include image src="/assets/img/template/layout/neuromag122planar.lay.png" width="200" %}

##### with the combined planar gradiometers

{% include image src="/assets/img/template/layout/neuromag122cmb.lay.png" width="200" %}

### Yokogawa system

The following template layouts are for a sensor array of the Yokogawa MEG system. The labels in these layouts, except for the "old" variant, are prefixed to indicate the gradiometer type (`PG` - planar gradiometer, `AG` - axial gradiometer).

{% include image src="/assets/img/template/layout/yokogawa440.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/yokogawa440_old.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/yokogawa440all.lay.png" width="200" %}

##### with only the axial gradiometers

{% include image src="/assets/img/template/layout/yokogawa440ag.lay.png" width="200" %}

##### with only the planar gradiometers

{% include image src="/assets/img/template/layout/yokogawa440pg.lay.png" width="200" %}

## iEEG layouts (ECoG and sEEG)

Intracranial electrodes are in general placed according to a patient-specific implantation scheme, hence we don't have general template layouts. The layout tutorial contains a specific section that shows various ways to make a layout for various [sEEG and ECoG](/tutorial/layout/#making-a-layout-for-ieeg-electrodes) arrangements.

Furthermore, this section from the **[ft_prepare_layout](/reference/ft_prepare_layout)** help is of relevance.

    % Alternatively you can specify the following options for systematic layouts which
    % will be generated for all channels present in the data. Note that these layouts are
    % only suitable for multiplotting, not for topoplotting.
    %   cfg.layout = 'ordered'    will give you a NxN ordered layout
    %   cfg.layout = 'vertical'   will give you a Nx1 ordered layout
    %   cfg.layout = 'horizontal' will give you a 1xN ordered layout
    %   cfg.layout = 'butterfly'  will give you a layout with all channels on top of each other
    %   cfg.layout = 'circular'   will distribute the channels on a circle
    %   cfg.width  = scalar (default is automatic)
    %   cfg.height = scalar (default is automatic)
    %
    % For an sEEG shaft the option cfg.layout='vertical' or 'horizontal' is useful to
    % represent the channels in a linear sequence . In this case you can also specify the
    % direction of the shaft as going from left-to-right, top-to-bottom, etc.
    %   cfg.direction = string, can be any of 'LR', 'RL' (for horizontal), 'TB', 'BT' (for vertical)
    %
    % For an ECoG grid the option cfg.layout='ordered' is useful to represent the
    % channels in a grid array. In this case you can also specify the number of rows
    % and/or columns and hwo the channels increment over the grid (e.g., first
    % left-to-right, then top-to-bottom). You can check the channel order of your grid
    % using FT_PLOT_LAYOUT.
    %   cfg.rows      = number of rows (default is automatic)
    %   cfg.columns   = number of columns (default is automatic)
    %   cfg.direction = string, can be any of 'LRTB', 'RLTB', 'LRBT', 'RLBT', 'TBLR', 'TBRL', 'BTLR', 'BTRL' (default = 'LRTB')

## NIRS layouts

Since NIRS caps are in general custom-made with the transmitter and receiver optodes over specific ROIs, we don't have template NIRS layouts. The option `cfg.layout = 'ordered'` that is explained in the **[ft_prepare_layout](/reference/ft_prepare_layout)** help can be useful for a quick visualisation of all channels. The [layout tutorial](/tutorial/plotting/layout) explains in general how to create your own channel layout for plotting, and we have a [layout example](/example/plotting/nirs_layout) specific to NIRS.

## Plotting all layouts

You can use the following code to get a quick overview of the template layouts.

    [ftver, ftpath] = ft_version;
    dirlist = dir(fullfile(ftpath, 'template', 'layout', '*.*')); % here you can make a selection
    filename = {dirlist(~[dirlist.isdir]).name}';

    for i=1:length(filename)
      cfg = [];
      cfg.layout = filename{i};
      cfg.skipcomnt = 'yes';
      cfg.skipscale = 'yes';
      layout = ft_prepare_layout(cfg);

      figure
      ft_plot_layout(layout);
      title(filename{i}, 'Interpreter', 'none');

      [p, f, x] = fileparts(filename{i});
      print([lower(f) x '.png'], '-dpng');
      
      close all
    end

After creating all bitmaps you can use [ImageMagick](https://www.imagemagick.org/script/command-line-options.php#trim) on the Linux or macOS command-line to trim the whitespace.

```bash
for file in *.png ; do convert $file -trim $file ; done
```

{% include markup/yellow %}
You can find all template 2-D layouts for plotting [here on GitHub](https://github.com/fieldtrip/fieldtrip/tree/master/template/layout/).
{% include markup/end %}

These layouts are meant for plotting on a 2D screen or on paper using **[ft_topoplotER](/reference/ft_topoplotER)**, **[ft_topoplotTFR](/reference/ft_topoplotTFR)**, or any of the other high-level plotting functions explained in [this tutorial](/tutorial/plotting). Furthermore, you can use them with the low-level **[ft_plot_topo](/reference/plotting/ft_plot_topo)** function.

If you are looking for 3D positions of the EEG electrodes or MEG sensors to be used for forward modeling and inverse source reconstruction, or for more fancy 3D visualisation of the measured EEG potential over the scalp or MEG field distribution around the head using **[ft_plot_topo3d](/reference/plotting/ft_plot_topo3d)**, you should look in the [electrode template](/template/electrode) and [gradiometer template](/template/gradiometer) documentation.
