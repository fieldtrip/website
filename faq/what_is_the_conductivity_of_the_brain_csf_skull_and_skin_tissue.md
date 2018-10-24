---
layout: default
tags: [faq, headmodel, source]
---

## What is the conductivity of the brain, CSF, skull and skin tissue?

There are multiple literature references from which you can get estimates for the conductivity, e.g. 

*  Gabriel S, Lau RW, Gabriel C. "The dielectric properties of biological tissues: II. Measurements in the frequency range 10 Hz to 20 GHz." Phys Med Biol, vol. 41, pp. 2251-69, Nov 1996.  

*  Manola L, Roelofsen BH, Holsheimer J, Marani E, Geelen J. "Modelling motor cortex stimulation for chronic pain control: electrical potential field, activating functions and responses of simple nerve fibre models." Med Biol Eng Comput, vol. 43, pp. 335-43, May 2005. 

In a three-shell EEG volume conduction model (either spherical or realistic) the conductivity ratio's of 1, 1/80, 1 are commonly specified for scalp, skull and brain. The proper conductivities are then 0.3300, 0.0042 and 0.3300 S/m respectively. For a four-shell EEG volume conduction model the conductivities of scalp, skull, CSF and brain are commonly specified as 0.3300, 0.0042, 1.0000 and 0.3300 S/m. 

Note that there is no agreement in the correct conductivity values of the skull. For example in 

*  Hoekema R, Wieneke GH, Leijten FS, van Veelen CW, van Rijen PC, Huiskamp GJ, Ansems J, van Huffelen AC. "Measurement of the conductivity of skull, temporarily removed during epilepsy surgery." Brain Topogr. 2003;16(1):29-38

skull conductivities of 0.0320 to 0.0800 are reported, which are 8-20 times larger than the value mentioned above.

The scalp topography obtained from EEG forward models shows an inverse relation between the thickness of the skull and the conductivity, i.e. *increasing* the thickness of the skull has a similar effect on the scalp topography as *decreasing* the skull conductivity. In both cases the scalp topography becomes more blurred. 

 
## Is the tissue conductivity frequency dependent?

It is commonly assumed that the impedances of the tissues relevant for EEG/MEG source modeling are purely resistive, i.e. there are no capacitive or inductive effects at the frequencies that we consider in EEG/MEG. This means that the impedance is frequency independent. The attenuation of the source activity at the skull therefore does not depend on the temporal or frequency characteristics of the source.

