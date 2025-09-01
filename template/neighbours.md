---
title: Templates for defining neighbouring channels
tags: [template, neighbours]
---

# Templates for defining neighbouring channels

A definition of neighbouring channels is needed when computing cluster in channel-space (see [ft_timelockstatistics](/reference/ft_timelockstatistics) and [ft_freqstatistics](/reference/ft_freqstatistics)) or when repairing missing channels (because a missing channel will be reconstructed by some weighted average of its neighbours, see [ft_channelrepair](/reference/ft_channelrepair)). FieldTrip comes with a variety of templates for defining neighbouring channels. The rationale for these templates was that sensor positions across measurements do not vary drastically, so that it is safe to assume that neighbouring sensors are always equal. The templates are manually modified versions of automatically generated templates, with the idea to make them symmetric if the sensor positions are symmetric as well. The following provides an explanation how we derived the templates for different systems.

{% include markup/yellow %}
You can find the templates for defining neighbouring channels included in FieldTrip [here](https://github.com/fieldtrip/fieldtrip/tree/master/template/neighbours).
{% include markup/end %}

## Electrode neighbour templates

EEG neighbour templates are based on [automatic, symmetric triangulation](/faq/stats/neighbours_prepare) of the [2D layout templates](/template/layout). After the automatic definition, we used [3D electrode positions](/template/electrode) and [ft_neighbourplot](/reference/ft_neighbourplot) with cfg.enableedit='yes' to manually add and/or remove edges between sensors.

Currently, the following neighbour templates are shipping with FieldTrip (note that neighbour templates are always suffixed with \_neighb

### BioSemi

- BioSemi 16-electrode cap (biosemi16_neighb.mat)
- BioSemi 32-electrode cap (biosemi32_neighb.mat)
- BioSemi 64-electrode cap (biosemi64_neighb.mat)

### Easycap

- Easycap M1 (easycapM1_neighb.mat)
- Easycap M11 (easycapM11_neighb.mat)
- Easycap M14 (easycapM14_neighb.mat)
- Easycap M15 (easycapM15_neighb.mat)

{% include markup/skyblue %}
Other 'Easycaps' constitute a subset of one of these systems or feature freely placable electrodes. You are required to manually edit them for your purposes. Please see [the layout section](/template/layout) and [the Easycap webpage](http://www.easycap.de) for more information.
{% include markup/end %}

### The standard 10% system

- Standard 10-05 system (elec1005_neighb.mat)
- Standard 10-10 system (elec1010_neighb.mat)
- Standard 10-20 system (elec1020_neighb.mat)

### Special arrangement of the MPI for Psycholinguistic

- Averaged 29-channel cap (language29-avg_neighb.mat)
- 59-channel cap (mpi_59_neighb.mat)

### ECOG

- ECOG 256channels, average referenced (ecog256_neighb.mat)
- ECOG 256channels, bipolar referenced (ecog256bipolar_neighb.mat)

## MEG neighbour templates

MEG neighbour templates are based on [automatic, symmetric triangulation](/faq/stats/neighbours_prepare) of the [2D layout templates](/template/layout). After the automatic definition, we used gradiometer information from one test measurement per system and [ft_neighbourplot](/reference/ft_neighbourplot) with cfg.enableedit='yes' to manually add and/or remove edges between sensors.

### BTI systems

- BTI 148-channel system (bti148_neighb.mat)
- BTI 248-channel system (bti248_neighb.mat)
- BTI 248 gradiometer system (bti248grad_neighb.mat)

### CTF systems

- CTF 64 axial gradiometer(ctf64_neighb.mat)
- CTF 151 axial gradiometer(ctf151_neighb.mat)
- CTF 275 axial gradiometer(ctf275_neighb.mat)

### ITAB systems

- ITAB 28-channel system (itab28_neighb.mat)
- Old ITAB 28-channel system (itab28_old_neighb.mat)
- ITAB 153-channel system (itab153_neighb.mat)

### Neuromag systems

- Neuromag306, planar gradiometer and magnetometer (neuromag306_neighb.mat)
- Neuromag306, only planar gradiometer (neuromag306planar_neighb.mat)
- Neuromag306, only magnetometer (neuromag306mag_neighb.mat)

{% include markup/skyblue %}
Please see our FAQ for [why there are multiple neighbour templates for the neuromag306 system](/faq/stats/neighbours_neuromag)
{% include markup/end %}

### Yokogawa systems

- Yokogawa 160-channel system (yokogawa160_neighb.mat)
- Yokogawa 440-channel system (yokogawa440_neighb.mat)
- Old Yokogawa 440-channel system (yokogawa440_old_neighb.mat)
