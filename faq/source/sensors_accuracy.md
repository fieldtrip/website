---
title: Is it important to have accurate measurements of electrode locations for EEG source reconstruction?
category: faq
tags: [source, eeg]
redirect_from:
    - /faq/is_it_important_to_have_accurate_measurements_of_electrode_locations_for_eeg_source_reconstruction/
    - /faq/sensors_accuracy/
---

# Is it important to have accurate measurements of electrode locations for EEG source reconstruction?

Yes, it is if you want your source reconstruction to be as accurate as possible. Important is to realize that there are different types of errors: You can have random errors in each electrode location. Assuming that you use a non-linear dipole fit method for source localization, you will get an increase in your residual variance. The fitted source location does not have to be wrong. You can also have a systematic misalignment of all your electrodes with respect to the volume conduction model of the head. That will result in a systematic mislocalization of your sources. So the latter error should be a bigger concern to you than the first error.

## See also

- Wang Y, Gotman J. _The influence of electrode location errors on EEG dipole source localization with a realistic head model._ Clin Neurophysiol. 2001 Sep;112(9):1777-80.
- Khosla D, Don M, Kwong B. _Spatial mislocalization of EEG electrodes -- effects on accuracy of dipole estimation._ Clin Neurophysiol. 1999 Feb;110(2):261-71.
