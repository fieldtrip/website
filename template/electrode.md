---
title: Template 3-D electrode sets
tags: [template, electrode]
---

# Template 3-D electrode sets

Electrodes are represented as points in 3-D Cartesian space, i.e. with an X, Y and Z position for each electrode. Furthermore, each electrode has a label. There is a frequently asked question about [how the electrode structure is described](/faq/how_are_electrodes_magnetometers_or_gradiometers_described).

You can use the following snippet of code to get a quick overview of the template electrode sets.

    dirlist  = dir('template/electrode/*.*');
    filename = {dirlist(~[dirlist.isdir]).name}';

    for i=1:length(filename)
      elec = ft_read_sens(filename{i});

      figure
      ft_plot_sens(elec, 'label', 'yes');
      grid on
      rotate3d
      view(135, 20);
      title(filename{i}, 'Interpreter', 'none');

      [p, f, x] = fileparts(filename{i});
      print([lower(f) '.png'], '-dpng');
    end

{% include markup/warning %}
You can find the template 3-D electrode sets included in FieldTrip [here](https://github.com/fieldtrip/fieldtrip/tree/master/template/electrode).
{% include markup/end %}

## The 10-20, 10-10 and 10-5 system for electrode placement

The following template electrode sets describe the 10-20 EEG electrodes and were constructed by Robert Oostenveld as part of the study described in _Robert Oostenveld and Peter Praamstra. **The five percent electrode system for high-resolution EEG and ERP measurements.** Clin Neurophysiol. 2001 Apr;112(4):713-9._ More details on the electrode positioning and the different naming schemes can be found in the paper (link to [pubmed](http://www.ncbi.nlm.nih.gov/pubmed/11275545), [sciencedirect](http://www.sciencedirect.com/science/article/pii/S1388245700005277)) and on Robert's [personal blog](http://robertoostenveld.nl/?p=5).

The electrodes are stored in an ASA `.elc` file which can be read with **[ft_read_sens](/reference/fileio/ft_read_sens)**. The electrode positions are represented in mm in the MNI coordinate system and correspond to the template BEM volume conduction model detailed in [this publication](http://www.ncbi.nlm.nih.gov/pubmed/12842715) and that is available in the `fieldtrip/template/headmodel` directory as `standard_bem.mat`. See also [this page](/template/headmodel/#standard_bemmat).

- standard_1005.elc
- standard_1020.elc
- standard_alphabetic.elc
- standard_postfixed.elc
- standard_prefixed.elc
- standard_primed.elc

## The EGI geodesic sensor net

The following template electrode sets are for the [EGI](http://www.egi.com) geodesic sensor net and were downloaded from the EGI [FTP server](ftp://www.egi.com/).

- GSN-HydroCel-32.sfp
- GSN-HydroCel-64.sfp
- GSN-HydroCel-65.sfp
- GSN-HydroCel-128.sfp
- GSN-HydroCel-129.sfp
- GSN-HydroCel-256.sfp
- GSN-HydroCel-257.sfp

Note that the even versions (32, 64, 128, 256) do not include the position of the reference electrode which is on the vertex (aka Cz), whereas the odd versions (65, 129, 257) do include the position of the reference electrode.

## Easycap electrode arrangements

The following template electrode sets are for the [Easycap](http://www.easycap.de/easycap/e/products/products.htm) electrode arrangements and were downloaded from the Easycap [download page](http://www.easycap.de/easycap/e/downloads/electrode_sites_coordinates.htm).

- easycap-M1.sfp (Full 10%-System)
- easycap-M10.sfp (Equidistant 61-Channel-Arrangement)
