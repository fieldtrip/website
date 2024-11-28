---
title: What is the conductivity of the brain, CSF, skull and skin tissue?
category: faq
tags: [headmodel, source]
redirect_from:
    - /faq/what_is_the_conductivity_of_the_brain_csf_skull_and_skin_tissue/
---

# What is the conductivity of the brain, CSF, skull and skin tissue?

There are multiple literature references from which you can get estimates for the conductivity, e.g.

- McCann H, Pisano G, Beltrachini L. _Variation in Reported Human Head Tissue Electrical Conductivity Values._ Brain Topogr. 2019
- Gabriel S, Lau RW, Gabriel C. _The dielectric properties of biological tissues: II. Measurements in the frequency range 10 Hz to 20 GHz._ Phys Med Biol, vol. 41, pp. 2251-69, Nov 1996.
- Manola L, Roelofsen BH, Holsheimer J, Marani E, Geelen J. _Modelling motor cortex stimulation for chronic pain control: electrical potential field, activating functions and responses of simple nerve fibre models._ Med Biol Eng Comput, vol. 43, pp. 335-43, May 2005.

In a spherical or realistic  three-shell EEG volume conduction model, conductivity ratio's of 1, 1/80, 1 are commonly specified for scalp, skull and brain. The proper conductivities are then 0.3300, 0.0042 and 0.3300 S/m respectively. For a four-shell EEG volume conduction model the conductivities of scalp, skull, CSF and brain are commonly specified as 0.3300, 0.0042, 1.7900 and 0.3300 S/m.

Note however that there is no agreement on the correct conductivity values of the skull. For example in

- Hoekema R, Wieneke GH, Leijten FS, van Veelen CW, van Rijen PC, Huiskamp GJ, Ansems J, van Huffelen AC. "Measurement of the conductivity of skull, temporarily removed during epilepsy surgery." Brain Topogr. 2003;16(1):29-38

skull conductivities of 0.0320 to 0.0800 are reported, which are 8-20 times larger than the value mentioned above.

The scalp topography obtained from EEG forward models shows an inverse relation between the thickness of the skull and the conductivity, i.e. _increasing_ the thickness of the skull has a similar effect on the scalp topography as _decreasing_ the skull conductivity. In both cases the scalp topography becomes more blurred.

## Is the tissue conductivity frequency dependent?

It is commonly assumed that - at the frequencies that we consider in EEG/MEG - the impedances of the tissues relevant for EEG/MEG source modeling are purely resistive, i.e. there are no capacitive or inductive effects. This means that the conductivity is frequency independent and the attenuation of the source activity by the skull therefore does not depend on the temporal or frequency characteristics of the sources.

## See also

  * Documentation on [Source Analysis Head Models](http://wiki.besa.de/index.php?title=Source_Analysis_Head_Models) on the BESA wiki
  * [Online tool](http://niremf.ifac.cnr.it/tissprop/htmlclie/htmlclie.php) for the calculation of the Dielectric Properties of Body Tissues
