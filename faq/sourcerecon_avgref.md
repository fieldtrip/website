---
title: Why should I use an average reference for EEG source reconstruction?
category: faq
tags: [eeg, reference, source]  
redirect_from:  
    - /faq/why_should_i_use_an_average_reference_for_eeg_source_reconstruction/
---

# Why should I use an average reference for EEG source reconstruction?

With EEG we measure potential differences. This means we always need N+1 electrodes to obtain N independent representations of the potential differences. This is the case with a common reference (e.g., M1 behind the left ear), with offline re-referenced linked mastoids (i.e. using the average of M1 and M2 as the reference), and also with a common average reference over all electrodes.

If you have recorded relative to a reference electrode that is not in the data file (which happens in most cases), you can add that implicit reference channel using the `cfg.implicitref` option in **[ft_preprocessing](/reference/ft_preprocessing)**. This adds a channel for the reference electrode containing all zeros. Subsequently (in the same call to ft_preprocessing) you can specify that you want to re-reference with the `cfg.reref` and `cfg.refchannel` options.

The prime reason for using the average reference in EEG source estimation is that in the forward model of how the sources project to the channels there is a (small) model error at each channel, including at the reference channel. If you use a single common reference, the forward model error of that reference channel contributes to the model estimate of the potential difference at all other channels. The model error in the reference therefore is present in the forward solution for all other channels. Consequently, the model error at the reference is weighted heavily in the inverse source estimate.

Taking a common average reference in the EEG data, also corresponds to taking a common average reference in the forward model. The consequence of subtracting the average potential (from each channel) is that the model error is *averaged over all channels*. Since there is no reason to assume that the model error is specifically positive or negative, the model error tends to average out and the forward solution at each channel will have a much smaller forward model error.

## Biosemi and other EEG systems with DRL and CMS

The Biosemi system uses a common mode sense (CMS) and a driven right leg (DRL) electrode, which injects a small amount of current to improve the CMMR and minimize the effect of external noise sources. When recording data to disk and when reading it into FieldTrip, it is expressed as potential difference relative to the CMS. With this type of amplifier systems you should **always** reference after reading the data from disk, i.e. change the reference from CMS to another electrode, and you should **not** add the CMS electrode as implicit reference channel to the data.

For channel-level analysis you may want to use linked mastoids, or linked T7 and T8. For source analysis you would (as with other systems) best reference to the average of all electrodes (minus CMS).

See also [this](http://www.biosemi.com/faq/cms&drl.htm) explanation on the Biosemi website.
