---
title: What are the units of the data and of the derived results?
tags: [units]
category: faq
redirect_from:
    - /faq/units/
---

It depends. FieldTrip tries to adhere to the units of the original manufacturer file formats, which are not always consistent. Furthermore, not all file formats clearly specify the units, so sometimes the units are not even known.

For geometrical objects that do not specify the units, FieldTrip estimates the units, assuming that the object approximates a human head. e.g., if the span of the geometrical object is about 200, FieldTrip assumes the units to be in "mm". If the span of the object is 0.2, FieldTrip assumes the units to be in "m".

Geometrical objects have the units expressed in the "unit" field of the data structure. Where needed, the units of geometrical objects are converted on the fly to match other geometrical objects (e.g., electrode positions measured with a Polhemus are matched to an anatomical MRI).

Raw data structures with EEG or MEG data may include the "hdr" field, which is the header of the original data file. The header can contain the "chanunit" subfield. The channel unit can be something like "V" or "uV" for EEG channels, and "T" or "fT" for MEG magnetometers.

Your EEG or MEG data structures may also contain sensor descriptions, which may have the chanunit field (especially relevant for Neuromag/Elekta/MEGIN data) and the unit field. Planar gradiometers in the Neuromag/Elekta/MEGIN system have "T/m" or "T/cm" as units (field per distance), although axial gradiometer data in the CTF system is expressed as "T" (field difference between bottom and top coil, not divided by the distance).

{% include markup/yellow %}
If you want to ensure that all computations are done correctly, you should ensure that all physical quantities are expressed according to the [International System of Units](https://en.wikipedia.org/wiki/International_System_of_Units) (SI). That means: meter, volt, tesla, ohm, amperes, kilogram, etc.

These SI units are not necessarily the most convenient to work with, but you can always change the units back at the time of editing your figures to get more convenient values.
{% include markup/end %}
