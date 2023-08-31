---
title: Template 3-D gradiometer descriptions
tags: [template, gradiometer, ctf, neuromag, 4d, bti, yokogawa, itab]
---

# Template 3-D gradiometer descriptions

SQUID-based MEG systems consist of channels that comprise of one one coil for magnetometers or multiple coils coils for axial or planar gradiometers. OPM-based MEG systems consists of small vapor-filled cells. In FieldTrip these are all described as "coils", where each coil can be described by a single point an dorientation in 3D space, or where larger coils (like for the Neuromag system) can be described using multiple integration points. all coils and/or integration points are linearly weighted and combined in a channel. There is a frequently asked question about [how the gradiometer structure is described](/faq/how_are_electrodes_magnetometers_or_gradiometers_described).

The `fieldtrip/template/gradiometer` directory contains template gradiometer descriptions for a number of MEG systems.

- ctf64
- ctf151
- ctf275
- neuromag122
- neuromag306
- bti148
- bti248
- bti248grad
- yokogawa160
- yokogawa208
- itab153

You can use the following snippet of code to get a quick overview of the template MEG gradiometer descriptions.

    dirlist  = dir('template/gradiometer/*.*');
    filename = {dirlist(~[dirlist.isdir]).name}';

    for i=1:length(filename)
      grad = ft_read_sens(filename{i});

      figure
      ft_plot_sens(grad, 'label', 'yes');
      grid on
      rotate3d
      view(135, 20);
      title(filename{i});
    end

{% include markup/warning %}
You can find the template gradiometer descriptions that are included in FieldTrip [here](https://github.com/fieldtrip/fieldtrip/tree/master/template/gradiometer).
{% include markup/end %}

SQUID-based MEG systems have the sensors placed in a rigid and fixed-size helmet. The position of the sensors relative to the head varies from subject to subject and from recording to recording. In the forward modeling the size of the head and the location of the sensors relative to the head should be taken into account.

Some of the gradiometer definitions (notably for the CTF and BTI systems) also include reference channels that are further away from the scalp surface; these channels are used to record and suppress environmental noise.

The gradiometer descriptions shared here as templates are all expressed in meter, without balancing, with the lowest resolution (single integration point per coil), and have been manually aligned with a representative subject.
