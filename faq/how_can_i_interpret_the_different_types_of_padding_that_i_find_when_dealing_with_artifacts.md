---
title: How can I interpret the different types of padding in FieldTrip?
layout: default
tags: [faq, preprocessing, artifact, filter]
---

# How can I interpret the different types of padding in FieldTrip? 

Padding is an operation that extends a predetermined segment of data (usually referred to as a "trial") either with zeros or with additional data points. Consequently, for padding you should distinguish **zero padding** from **data padding**.

Note that data padding can be applied only to continuous datasets.

Besides the type of padding, there is also a difference in the specification of the time. Sometimes padding is specified as the desired total length of the segment: this is referred to as **padding to** the desired length.  The other approach requires the padding to be specified as the amount of additional data with which the initial segment should be extended, this is referred to as **padding with** a certain amount. Preprocessing and freqanalysis routines listed above make use of the **padding to** approach.

The typical routines in which padding is used are: 

*  **[ft_preprocessing](/reference/ft_preprocessing)** uses data padding **to** a certain length, see the cfg.padding option. See also the frequently asked question about [how the filter padding in ft_preprocessing works](/faq/how_does_the_filter_padding_in_preprocessing_work).

*  **[ft_freqanalysis](/reference/ft_freqanalysis)** uses zero padding **to** a certain length, see the cfg.pad option

*  the artifact detection routines use both zero and data padding **with** a certain amount.

The automatic artifacts detection functions (ft_artifact_xxx) make use of an articulated scheme of padding with different purpose

*  trial padding (fig 1): data padding **with**, to include segments of data before and after the trial.

*  filter padding (fig 1): zero padding **with**, to avoid the classification of edge effects as artifacts after filtering.

*  artifact padding (fig 2): data padding **with**, to extend the length of a detected artifact.

{% include image src="/assets/img/tutorial/artifactdetect/padding_fig1.png" %}

{% include image src="/assets/img/tutorial/artifactdetect/padding_fig2.png" %}

See also the [automatic artifact rejection tutorial](http://fieldtrip.fcdonders.nl/tutorial/automatic_artifact_rejection) for more details on the different types of padding that can be used during data preprocessing (artifact padding, trial padding, filter padding). 

And see this [FAQ](/faq/how_does_the_filter_padding_in_preprocessing_work) on filter padding in **[/reference/ft_preprocessing](/reference/ft_preprocessing)** when reading data from disk. 
