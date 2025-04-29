---
title: Why should I start with rereferencing for Biosemi EEG data?
category: faq
tags: [biosemi, preprocessing]
authors: [Robert Oostenveld]
redirect_from:
    - /faq/biosemi_reference
---

# Why should I start with rereferencing for Biosemi EEG data?

{% include markup/yellow %}
Biosemi explains it themselves in their frequently asked question about [the function of the CMS and DRL electrodes](https://www.biosemi.com/faq/cms&drl.htm).
{% include markup/end %}

The Biosemi system uses a reference scheme with a driven-right-leg (DRL) and common-mode-sense (CMS), where a very small current is actively "driven" through the DRL electrode into the participant/patient to minimize the voltage difference between all measuring electrodes and the CMS. See for example [here](https://electronics.stackexchange.com/questions/595051/how-does-a-driven-right-leg-work) for a schematic explanation and the figure below from the Biosemi website. This active DRL scheme reduces the common-mode signal.

{% include image src="/assets/img/faq/biosemi_reference/zero_ref1_big.gif" width="400" %}

## Why is the common mode relevant

We want to measure the differential signal, i.e., the voltage difference between two electrodes. The common-mode signal itself isn’t interesting, but it makes measuring the difference more difficult. Let's use an analogy to explain this: imagine trying to measure the height of a LEGO brick sitting on top of the Mount Everest. So you measure the top of the brick and the ground level right next to it, to determine the height as the difference betweeen the two. If you do this from a large distance, you have to account for the _entire mountain_ in your measurement. That’s difficult and requires a system with an extremely large dynamic range (on a 10 km scale, it still needs 1 mm accuracy). It’s much easier to use a measurement system like a short ruler that doesn’t detect the common mode (the mountain underneath).

## Why do I still need to re-reference?

The active electronic common-mode suppression via DRL isn’t perfect. Some common-mode signal remains, especially at higher frequencies (like 50/60 Hz). All channels in your recording will still have some common mode. Therefore, after digitizing the EEG with the amplifier, you can still improve the signal and further suppress the common mode noise by choosing a reference (which also contains the 50 Hz noise) and digitally subtract it from all other channels to suppress the common mode. This allows to improve the common-mode rejection ratio (CMRR) from 40dB to 80dB.

The digital subtraction of a reference electrode is not implemented in the acqusition software; you have to do it offline using the software that you use to analyze the EEG data in the BDF file. For the offline reference, you could use a mastoid, but also an FCz or any other electrode, or linked ears. However — unlike with EEG systems using a conventional reference — you should _not_ add the CMS electrode as the implicit reference channel, because that’s where the common-mode noise resides. Normally, the implicit reference is zero by definition, but in this case, the CMS still contains some noise.

## References

See [this paper](http://dx.doi.org/10.1109/10.99079) from 1991 authored by the founders of Biosemi.
