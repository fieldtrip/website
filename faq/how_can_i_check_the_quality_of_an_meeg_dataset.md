---
title: How can I check the quality of an EEG or MEG recording ?
tags: [faq, artifact]
---

# How can I check the quality of an EEG or MEG recording ?

The **[ft_qualitycheck](/reference/ft_qualitycheck)** function allows you to inspect the overall quality of a MEG dataset.

1) The data is analyzed, quantified, and stored in a .mat file in a timelock- and freq-like fashion. This allows a detailed inspection by existing FT functions.

2) The quantifications are summarized in a figure that is exported to a .png and .pdf file (see link below). The visualizations are done for one-hour segments (per page) and contains general recording information (top left), jump detections (bottom left), time courses of the head positions, raw signal, power line noise (50 or 60 hz), and low frequency noise (0 - 2 Hz) in top right. Furthermore, the average power spectrum (bottom middle) and the triggers present in the dataset, where 'values' represents the number of unique triggers detected (i.e. same value, bottom right).

Here is an example of the quality check report: [20110321_1203.pdf](/assets/pdf/faq/20110321_1203.pdf). The timecourses display the evolution of the noise characteristics for a one-hour recording, averaged over 10-second segments.

Simply call **[ft_qualitycheck](/reference/ft_qualitycheck)** with cfg.dataset pointing to the file location, for example;

    cfg         = []
    cfg.dataset = 'dataset.ds';
    ft_qualitycheck(cfg)

One can also inspect previously analyzed data without running the analysis again;

    cfg         = [];
    cfg.matfile = '/home/common/meg_quality/dataset.mat'
    cfg.analyze = 'no'
    ft_qualitycheck(cfg)

On Odin (the MEG acquisition computer at the DCCN) the recorded data is analyzed and visualized automatically with a 'cronjob' running every night. The most recent .png and .pdf files are stored in /home/common/meg_quality.
