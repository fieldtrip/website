---
title: NIRS development
---

{% include /shared/development/warning.md %}

# NIRS development

See <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=2753>

Analysis of NIRS data is not particularly different from analyzing any other signal. A few nuts and bolts need to be twisted differently, and some more transformations are possible (changes in optical densities to concentration changes, i.e. changes in oxygenated and deoxygenated blood). The specific NIRS part should become a toolbox similar to the spike toolbox (see fieldtrip/contrib/spike). As Jörn Horschig started working at Artinis and got several requests of using FieldTrip to analyze multimodal EEG/NIRS data, he will take the lead in implementing this.

Points of action:

- define a standardized way to represent data and their peculiarities
- extend getting started section on NIRS. Information on different devices need to come from the manufacturers
- if analysis steps specific to NIRS should be implemented, these need to be written by experienced NIRS researchers
- a tutorial for analyzing NIRS and/or combined NIRS/EEG needs to be written

Mark van Wanrooij (DCN/biophysics) and his group might substantially contribute to this project.

## Header

The FieldTrip header contains meta information about the recording. More information be found in the respective reading file [ft_read_header](/reference/fileio/ft_read_header). For MEG data, the header also contains a .grad field, which contains information about the gradiometers. The respective counterpart for EEG data is .elec, but is commonly not stored together with the recorded data and thus not represented in the header.

NIRS data has another kind of sensor called "optode". An optode can either emit light, laser light or LED light, called a "transmitter", or receive light, e.g., by avalanching photodiodes, called "receiver". A channel is defined by the amount of transmitted light from the "transmitter" that is received by the "receiver" (hence the nomenclature). I propose the header of NIRS data to contain a .opto field, that includes optode specific information. These types need to be incorporated in ft_senstype and ft_chantype.

In a similar vein as for MEG data, the .opto field should contain a .tra matrix, that contains information on how the channels are defined in terms of transmitters and receivers. Note that, in contrast to electrophysiological measurements, this is a 1-1-1 mapping, i.e. exactly one transmitter and exactly one receiver make up one channel (technically this is commonly achieved by multiplexing).

Optode specifications, where M is the number of channels, N is the number of optodes and K is the number of wavelengths:

    opto.label         = Mx1 cell-array with channel labels
    opto.chanpos       = contains information about the position of the channels (usually halfway the transmitter and receiver)
    opto.optopos       = contains information about the position of individual optodes
    opto.optotype      = contains information about the type of optode (receiver or transmitter)
    opto.optolabel     = Nx1 cell-array with optode labels
    opto.transmits     = NxK matrix, boolean, where N is the number of optodes and K the number of wavelengths. Specifies which optode is transmitting at what wavelength (or nothing at all, indicating that it is a receiver)
    opto.wavelength    = 1xK vector of all wavelengths that were used
    opto.laserstrength = 1xK vector of the strength of the emitted light of the lasers
    opto.tra           = MxN matrix, boolean, contains information about how N receivers and transmitters form M channels

## Datatype

There are different datatypes in FieldTrip. The basic starting point is a raw data, see **[ft_datatype_raw](/reference/utilities/ft_datatype_raw)** for more information. There will be no changes requires for NIRS data structures. Labels will be represented as 'RxY - TxZ [type]', where Y and Z are integer numbers indexing the receiver number and type can be the type of chromophore or the wavelength at which the measurement was taken.

## Chantype

New channels for **[ft_chantype](/reference/fileio/ft_chantype)** should be 'nirs', 'receiver' and 'transmitter'.

## Filetype

**[ft_filetype](/reference/fileio/ft_filetype)** need to be able to identify NIRS data files correctly. Die to copyright issues, these files should be best put into fieldtrip\external\manufacturer. The following table shows manufacturers and systems and the respective extension of the data files. Note that I do not know all these different types, and below is just an example table:

| Manufacturer                                                                                               | System(s)                            | File format | Proprietary file format |
| ---------------------------------------------------------------------------------------------------------- | ------------------------------------ | ----------- | ----------------------- |
| [Artinis Medical Systems](http://www.artinis.com)                                                          | Oxymon, Octamon, Portamon, Portalite | .oxy3/.oxy4 | yes                     |
| [Hitachi Medical Systems](http://www.hitachi-medical-systems.nl/products-and-services/optical-topography/) | ETG-4000                             | .csv        | no                      |

## Transformations

NIRS data requires transformations from (changes in) optical densities to (changes in) concentrations (oxygenated hemoglobin and changes in deoxygenated hemoglobin). These changes can be expressed in log-ratios or ln-ratios. Different labs have different preferences. In either case, we need a respective lookup table for the absorption coefficient (or extinction coefficient, which is proportional. The absorption coefficient is measured in natural logarithm, whereas the extinction coefficient uses the base 10 logarithm) for different wavelengths. ft_chanunit needs to be adjusted to incorporate the respective units (molar for concentrations, Watt for transmitter). The transformation is dependent on the wavelengths of the transmitter, the change in optical density (fraction of received light), the distance between transmitter and receiver and the differential path length factor (DPF), which is mostly estimated by the age of the participant and a lookup table.

Robert and me settled on creating a forward- and an inverse-function for this purpose.

    function [transform] = ft_convertODs(cfg, opto)

with

    cfg.channel = cell-array of strings or 1xN vector, defines on which channels the transformation matrix should be computed
    cfg.target = string, can be 'HbO' (oxygenated hemoglobin) or 'HbR' (deoxygenated hemoglobin')
    cfg.age = scalar, age of the participant

or

    cfg.dpf = scalar, differential path length factor

additional fields can contain the lookup table for the absorption coefficient or dpf.

The resulting transform matrix can be multiplied with the data to obtain the concentrations. A respective ft_convertToODs function can be made to undo the conversion.

{% include markup/skyblue %}
I think we actually _do_ need a high-level function dealing directly with the data. Otherwise the channel labels will not be updated respectively. The ft_convertODs function can, however, serve as the low-level implementation.

Update: We might overcome this problem by having the function return a montage, which contains the new channel labels and the mixing coefficient of the channels
{% include markup/end %}

## Preprocessing

Preprocessing of NIRS data mostly consists of filtering and artifact rejection or correction. Filtering is most often performed by simple bandpass filtering, which are already implemented in FieldTrip. Some labs prefer to apply a gaussian moving average filter. Artifact correction is most often done using bandpass-filtering (filtering out physiological artifacts such as heartbeat and respiration) or using "wavelet-based detrending", i.e. a more fancy form of band-pass filtering. This could also be performed using standard FieldTrip functions, but more information on this would be required.

The most crucial step in preprocessing is to transform the optical densities to concentrations, which has to be an ft_nirs_XXX function.

## Layouts

Layouts should be created on-the-fly by ft_prepare_layout. Neuromag layouts can be taken as an example, where within the same data, different sensortypes are present at the same/nearby locations. The function should create an outline where optode positions are indicated (i.e. by a circle), and space for the different numbers of measures (concentrations) is computed and reserved, e.g., for multiplotting. The space depends on the cfg, i.e. desired channels/concentrations to be plotted (reminder: concentrations will be read out by the data labels).

## Code structure

Overall structure:
In case a high-level FieldTrip function calls a NIRS function, ft_hastoolbox will check whether the respective subfolder is already added and adds it, and a splash screen is shown, indicating a change in copyright (probably not GPL, definitely not for medical use, etc.).

## Other MATLAB NIRS toolboxes

The original [NIRS-SPM](http://bispl.weebly.com/nirs-spm.html) was developed by Korea Advanced Institute of Science & Technology. The general NIRS-SPM approach is to solve a GLM based on different approaches of nongaussian random field theory. One of the developers, Sungho Tak, is now working at UCL in Will Penny's group. He reworked NIRS-SPM, which can now be found as on [NIRTC as SPM for fNIRS toolbox](http://www.nitrc.org/projects/spm_fnirs). SPM-fNIRS includes DCM as well.

[Homer2](http://www.nmr.mgh.harvard.edu/PMI/resources/homer2/home.htm), developed by the Martinos Centre in Harvard, and primarily maintained by Ted Huppert from University in Pittsburgh. Is the most commonly used toolbox for NIRS analysis. Includes some forward modeling in the AtlasViewer.

The [NIRS toolbox](https://bitbucket.org/huppertt/nirs-toolbox/) for analysis of functional Near-Infrared Spectroscopy developed by the Huppert lab at the University of Pittsburgh is one of the best toolboxes available at the moment.

Other available toolboxes such as [EasyTopo](https://sites.google.com/site/fenghuatian/software/easytopo) (for visualization) or the [NIRS Analysis package (NAP)](https://sites.google.com/site/tomerfekete2/) are not widely used.
