---
title: Details on the resting-state EEG dataset recorded with different sedation levels
tags: [eeg-chennu]
---

# Details on the resting-state EEG dataset recorded with different sedation levels

Full details on the dataset are included in the [publication](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1004669) by Chennu et al. Below follows an excerpt with the most important aspects of the data.

Approximately 7 minutes of 128-channel high-density EEG data were collected at each level of sedation. EEG was sampled at 250Hz and referenced to the vertex, using the EGI NetAmps 300 amplifier. Participants had their eyes closed.

Raw data was preprocessed using EEGLAB and data from 91 channels over the scalp surface were retained for further analysis. Channels on the neck, cheeks and forehead were excluded. The data was filtered between 0.5–45 Hz, and segmented into 10-second long epochs. Each epoch thus generated was baseline-corrected relative to the mean voltage over the entire epoch.

Data containing excessive eye movement or muscular artifacts were rejected by a quasi-automated procedure: abnormally noisy channels and epochs were identified by calculating their normalized variance and then manually rejected or retained by visual inspection. Finally, previously rejected channels were interpolated using spherical spline interpolation, and data were re-referenced to the average of all channels.

{% include markup/danger %}
The baseline correction following segmentation means that there are (possibly small) jumps in each channel at the segment boundaries. When reading and segmenting this data, you should ensure that your segments are aligned with the 10-second segments used in the original preprocessing.
{% include markup/end %}

The original dataset is available under the [CC BY 2.0 UK](https://creativecommons.org/licenses/by/2.0/uk/) license from the [University of Cambridge Data Repository](https://www.repository.cam.ac.uk/handle/1810/252736).
