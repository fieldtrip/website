---
title: How can I interpret the different types of padding in FieldTrip?
category: faq
tags: [preprocessing, artifact, filter]
---

# How can I interpret the different types of padding in FieldTrip?

Padding is an operation that extends a predetermined segment of data (usually referred to as a "trial") either with zeros or with additional data. You should distinguish **data padding**, which can be helpful to improve filter characteristics, but is also used to extend the length of a window for a certain type of analysis (such as detecting behavioral artifacts), versus **zero padding**, which only plays a role in preventing filter artifacts. Padding with actual data can only be applied to continuous datasets while reading data from disk.

Besides the difference between data and zero padding, there are also differences how it is specified. Sometimes padding is specified as the desired total length of the segment: this is referred to as **padding to** the desired length. This is used in preprocessing and spectral analysis:

- **[ft_preprocessing](/reference/ft_preprocessing)** uses data padding **to** a certain length, see the cfg.padding option.
- **[ft_freqanalysis](/reference/ft_freqanalysis)** uses zero padding **to** a certain length, see the cfg.pad option.

The other approach specifies the padding as the amount of additional data with which the initial segment is extended, this is referred to as **padding with** a certain amount. This is used in the automatic artifacts detection functions, such as **[ft_artifact_zvalue](/reference/ft_artifact_zvalue)**.

There are different purposes for padding in the artifact detection functions:

- trial padding (fig 1): data padding **with**, to extend the data segment in which artifacts are detected, for example to exclude trials where the subject blinked or moved in the inter-stimulus interval.
- filter padding (fig 1): zero padding **with**, to extend the data segment to prevent edge artifacts due to filtering.
- artifact padding (fig 2): data padding **with**, to extend the length of a detected artifact, for example if you also want to exclude data from being analyzed in a time window following some artifact.

{% include image src="/assets/img/faq/how_can_i_interpret_the_different_types_of_padding_that_i_find_when_dealing_with_artifacts/padding_fig1.png" %}

{% include image src="/assets/img/faq/how_can_i_interpret_the_different_types_of_padding_that_i_find_when_dealing_with_artifacts/padding_fig2.png" %}

See also the [automatic artifact rejection tutorial](/tutorial/automatic_artifact_rejection) for more details on the filter padding, trial padding and artifact padding.

And see this [FAQ](/faq/how_does_the_filter_padding_in_preprocessing_work) on filter padding when reading data from disk and preprocessing that data.
