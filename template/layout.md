---
title: Template 2-D layouts for plotting
tags: [template, layout]
---

# Template 2-D layouts for plotting

EEG electrode and MEG gradiometer positions in the layouts are represented as points in 2-D Cartesian space, i.e. with an X and Y position for each electrode. Furthermore, each electrode has a label. In the [layout tutorial](/tutorial/layout) you can find more details on how to create and use them. The file format for layout files specified as ASCII `.lay` files is explained [here](/faq/what_is_the_format_of_the_layout_file_which_is_used_for_plotting).

You can use the following snippet of code to get a quick overview of the template layout sets.

    dirlist  = dir('template/layout/*.*');
    filename = {dirlist(~[dirlist.isdir]).name}';

    for i=1:length(filename)
      cfg = [];
      cfg.layout = filename{i};
      layout = ft_prepare_layout(cfg);

      figure
      ft_plot_layout(layout);
      title(filename{i}, 'Interpreter', 'none');

      [p, f, x] = fileparts(filename{i});
      print([lower(f) '.png'], '-dpng');
    end

{% include markup/warning %}
You can find the template 2-D layouts for plotting that are included in FieldTrip [here on GitHub](https://github.com/fieldtrip/fieldtrip/tree/master/template/layout/).
{% include markup/end %}

These layouts are meant for plotting on a 2D screen or on paper. If you are looking for 3D positions of the EEG electrodes or MEG sensors to be used for forward modeling and inverse source reconstruction, or for more fancy 3D visualisation of the measured EEG potential over the scalp or MEG field distribution around the head using **[ft_plot_topo3d](/reference/plotting/ft_plot_topo3d)**, you should look in the [electrode template](/template/electrode) and [gradiometer template](/template/gradiometer) documentation.

## EASYCAP

The following series of template layouts is for the electrode caps from [EASYCAP](http://www.easycap.de). They are sorted based on their electrode montages. FieldTrip provides .mat files (since r5201 - feb 2012) that are based on the bitmap images obtained from the easycap website and shown below. The layout structure stored in those .mat files contains fields that describe the position (.pos), the width (.width), and the height (.height), and the naming (.label) of the electrodes. Furthermore, it contains fields that describe the topographic interpolation boundaries (.mask) and the outlines of the 'head' (.outline).

### 10%-Arrangements

The following template layout sets are provided

- easycapM25.mat
- easycapM3.mat
- easycapM22.mat
- easycapM23.mat
- easycapM24.mat
- easycapM11.mat
- easycapM1.mat
- easycapM15.mat

#### easycapM25 - International 10/20-System (used in EC20)

{% include image src="/assets/img/template/layout/easycapm25.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm25.mat.png" width="200" %}

#### easycapM3 - Extended 10/20-System with 30 Channels

{% include image src="/assets/img/template/layout/easycapm3.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm3.mat.png" width="200" %}

#### easycapM22 - Small Equidistant 29-Channel-Arrangement (used in Braincap32)

{% include image src="/assets/img/template/layout/easycapm22.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm22.mat.png" width="200" %}

#### easycapM23 - Large Equidistant 32-Channel-Arrangement

{% include image src="/assets/img/template/layout/easycapm23.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm23.mat.png" width="200" %}

#### easycapM24 - Large Equidistant 34-Channel-Arrangement (used in EC40)

{% include image src="/assets/img/template/layout/easycapm24.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm24.mat.png" width="200" %}

#### easycapM11 - 61-Channel-Arrangement ("10%-System") (used in BrainCap64)

{% include image src="/assets/img/template/layout/easycapm11.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm11.mat.png" width="200" %}

#### easycapM1 - 74-Channel-Arrangement (used in EC80)

{% include image src="/assets/img/template/layout/easycapm1.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm1.mat.png" width="200" %}

#### easycapM15 - 128-Channel-Arrangement

{% include image src="/assets/img/template/layout/easycapm15.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm15.mat.png" width="200" %}

### Triangulated Equidistant Arrangements

The following template layout sets are provided

- easycapM7.mat
- easycapM10.mat
- easycapM16.mat
- easycapM14.mat

#### easycapM7 - Spherical 32-Channel-Arrangement

{% include image src="/assets/img/template/layout/easycapm7.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm7.mat.png" width="200" %}

#### easycapM10 - Equidistant 61-Channel-Arrangement

{% include image src="/assets/img/template/layout/easycapm10.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm10.mat.png" width="200" %}

#### easycapM16 - Equidistant 88-Channel-Arrangement

{% include image src="/assets/img/template/layout/easycapm16.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm16.mat.png" width="200" %}

#### easycapM14 - Spherical 124-Channel-Arrangement

{% include image src="/assets/img/template/layout/easycapm14.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm14.mat.png" width="200" %}

### Miscellaneous Arrangements

The following template layout sets are provided

- easycapM20.mat
- easycapM17.mat
- easycapM19.mat

#### easycapM20 - BESA 32-Channel-Arrangement for Epilepsy Diagnostics

{% include image src="/assets/img/template/layout/easycapm20.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm20.mat.png" width="200" %}

#### easycapM17 - 29-Channel-Arrangement for Language Research

{% include image src="/assets/img/template/layout/easycapm17.png" width="200" %}
{% include image src="/assets/img/template/layout/easycapm17.mat.png" width="200" %}

## BrainProducts actiCAP

The following template layouts are for electrode caps from [Brain Products actiCAP](http://www.brainproducts.com). FieldTrip provides .mat files (since r6121 - june 2012) that are based on the bitmap images shown below. Note that these layouts were created for the DCCN and the MPI specifically and may differ from other actiCAP layouts. For a standard actiCap layout, see: acticap-64ch-standard2.mat.

#### dccn_customized_acticap64.mat

This is a custom 64-Channel-Arrangement for the Donders Centre for Cognitive Neuroimaging (DCCN). The 32 channels from the 1st amplifier are located central, the 32 channels from the 2nd amplifier are along the rim.

{% include image src="/assets/img/template/layout/dccn_customized_acticap64.png" width="200" %}
{% include image src="/assets/img/template/layout/dccn_customized_acticap64.mat.png" width="200" %}

#### mpi_customized_acticap64.mat

This is a custom 64-Channel-Arrangement for the MPI. Note that the electrode positions are the same as for the DCCN customized version, but that the channel order is different. The MPI version has the 32 channels from the 1st amplifier on the right and the 32 channels from the 2nd amplifier on the left.

{% include image src="/assets/img/template/layout/mpi_customized_acticap64.png" width="200" %}
{% include image src="/assets/img/template/layout/mpi_customized_acticap64.mat.png" width="200" %}

#### acticap-64ch-standard2.mat

This is the standard 64-channel-Arrangement from [Brain Products](http://www.brainproducts.com/files/public/downloads/actiCAP-64-channel-Standard-2_1201.pdf). It is based on the same coordinates as the easycap electrode caps. This particular layout was created using the [easycapM1 layout](/assets/img/template/layout/easycapm1.png) and then removing eight electrodes (FPz, Iz, F9, F10, P9, P10, O9, O10) which are not present in the cap. Furthermore, two electrodes (AFz, FCz) were renamed to their purpose of being Ground (Gnd) and Reference (Ref) electrode.

{% include image src="/assets/img/template/layout/acticap-64-channel-standard-2.jpg" width="200" %}
{% include image src="/assets/img/template/layout/acticap-64-channel-standard-2.mat.jpg" width="200" %}

## NeuroScan Quick-Cap

The following template layout sets are for electrode caps from [NeuroScan](http://www.neuroscan.com). The origin and construction is described on <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=679>. The quikcap_nsl_128 layout has been kindly provided by Andre Cravo.

{% include image src="/assets/img/template/layout/quickcap64.mat.png" width="200" %} (since june 2012 - r6055)
{% include image src="/assets/img/template/layout/quikcap_nsl_128.mat.png" width="200" %} (since nov 2012 - r6915)

## BioSemi cap

The following template layouts are for an electrode cap from [BioSemi](http://www.biosemi.com).

{% include image src="/assets/img/template/layout/biosemi16.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi32.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi64.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi128.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi160.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/biosemi256.lay.png" width="200" %}

## Standard 10-XX cap

The following template layouts are for an electrode cap based on a standard 10-XX montage.

{% include image src="/assets/img/template/layout/EEG1005.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/EEG1010.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/EEG1020.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/elec1005.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/elec1010.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/elec1020.lay.png" width="200" %}

## EGI-system sensor nets

The following template layouts were created from the files that define the 3D electrode positions for EGI sensor nets(*.sfp files). The code to generate these layouts is in fieldtrip/test/test_layout_egi.m

{% include image src="/assets/img/template/layout/GSN-HydroCel-32.png" width="400" %}
{% include image src="/assets/img/template/layout/GSN-HydroCel-64_1.png" width="400" %}
{% include image src="/assets/img/template/layout/GSN-HydroCel-65.png" width="400" %}
{% include image src="/assets/img/template/layout/GSN-HydroCel-128.png" width="400" %}
{% include image src="/assets/img/template/layout/GSN-HydroCel-129.png" width="400" %}
{% include image src="/assets/img/template/layout/GSN-HydroCel-256.png" width="400" %}
{% include image src="/assets/img/template/layout/GSN-HydroCel-257.png" width="400" %}

## BTi/4D system

The following template layouts are for the sensor arrays of the BTi/4D MEG system.

{% include image src="/assets/img/template/layout/4D148.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/4D248.lay.png" width="200" %}

### With a more realistic display of temporal sensors

{% include image src="/assets/img/template/layout/4D248_helmet.png" width="200" %}

## CTF system

The following template layouts are for a sensor array of the CTF MEG system.

{% include image src="/assets/img/template/layout/CTF151.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/CTF275.lay.png" width="200" %}

### With a more realistic display of temporal sensors

{% include image src="/assets/img/template/layout/CTF151_helmet.png" width="200" %}
{% include image src="/assets/img/template/layout/CTF275_helmet.png" width="200" %}

## Neuromag/Elekta/Megin system

### 306-channel system

#### with all channels

{% include image src="/assets/img/template/layout/neuromag306all.lay.png" width="200" %}

#### with only the magnetometers

{% include image src="/assets/img/template/layout/neuromag306mag.lay.png" width="200" %}

#### with only the planar gradiometers

{% include image src="/assets/img/template/layout/neuromag306planar.lay.png" width="200" %}

#### with the combined planar gradiometers

{% include image src="/assets/img/template/layout/neuromag306cmb.lay.png" width="200" %}

#### with a more realistic display of temporal sensors, all channels

{% include image src="/assets/img/template/layout/neuromag306all_helmet.png" width="200" %}

#### with a more realistic display of temporal sensors, planar gradiometers only

{% include image src="/assets/img/template/layout/neuromag306planar_helmet.png" width="200" %}

#### with a more realistic display of temporal sensors, planar gradiometers combined

{% include image src="/assets/img/template/layout/neuromag306cmb_helmet.png" width="200" %}

#### with a more realistic display of temporal sensors, magnetometers only

{% include image src="/assets/img/template/layout/neuromag306mag_helmet.png" width="200" %}

### 122-channel system

#### with the planar gradiometers

{% include image src="/assets/img/template/layout/neuromag122planar.lay.png" width="200" %}

#### with the combined planar gradiometers

{% include image src="/assets/img/template/layout/neuromag122cmb.lay.png" width="200" %}

## Yokogawa system

The following template layouts are for a sensor array of the Yokogawa MEG system. The labels in these layouts, except for the old variant, are prefixed to indicate the gradiometer type (`PG` - planar gradiometer, `AG` - axial gradiometer).

{% include image src="/assets/img/template/layout/yokogawa440.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/yokogawa440_old.lay.png" width="200" %}
{% include image src="/assets/img/template/layout/yokogawa440all.lay.png" width="200" %}

#### with only the axial gradiometers

{% include image src="/assets/img/template/layout/yokogawa440ag.lay.png" width="200" %}

#### with only the planar gradiometers

{% include image src="/assets/img/template/layout/yokogawa440pg.lay.png" width="200" %}
