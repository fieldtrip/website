---
title: Which methodological details should I report in an EEG/MEG manuscript?
category: faq
tags: [sharing]
redirect_from:
    - /faq/checklist/
---

# Which methodological details should I report in an EEG/MEG manuscript?

This is a checklist for authors to use it prior to submission of a manuscript, to ensure that the manuscript provides key information. It originates from the following paper, which also provides more background on how to report methodological details on MEG and EEG studies.

{% include markup/yellow %}

Keil A, Debener S, Gratton G, Junghöfer M, Kappenman ES, Luck SJ, Luu P, Miller GA, Yee CM. **Committee report: publication guidelines and recommendations for studies using electroencephalography and magnetoencephalography.** Psychophysiology. 2014 Jan;51(1):1-21. {% include badge doi="10.1111/psyp.12147" pmid="24147581" %}

{% include markup/end %}

## Checklist

For each of the following items, please consider whether you have reported it or not.

### Hypotheses

-   Specific hypotheses and predictions for the electromagnetic measures are described in the introduction

### Participants

-   Characteristics of the participants are described, including age, gender, education level, and other relevant characteristics
-   Recording characteristics and instruments YES NO The type of EEG/MEG sensor is described, including make and model
-   All sensor locations are specified, including reference electrode(s) for EEG
-   Sampling rate is indicated
-   Online filters are described, specifying the type of filter and including roll-off and cut-off parameters (in dB, or by indicating whether the cut-off represents half-power/half amplitude)
-   Amplifier characteristics are described
-   Electrode impedance or similar information is provided

### Stimulus and timing parameters YES

-   Timing of all stimuli, responses, intertrial intervals, etc., are fully specified; ensure clarity that intervals are from onset or offset
-   Characteristics of the stimuli are described such that replication is possible

### Description of data preprocessing steps

-   The order of all data preprocessing steps is included
-   Rereferencing procedures (if any) are specified, including the location of all sensors contributing to the new reference
-   Method of interpolation (if any) is described
-   Segmentation procedures are described, including epoch length and baseline removal time period
-   Artifact rejection procedures are described, including the type and proportion of artifacts rejected
-   Artifact correction procedures are described, including the procedure used to identify artifacts, the number of components removed, and whether they were performed on all subjects
-   Offline filters are described, specifying the type of filter and including roll-off and cut-off parameters (in dB, or by indicating whether the cut-off represents half-power/half amplitude)
-   The number of trials used for averaging (if any) is described, reporting the number of trials in each condition and each group of subjects. This should include both the mean number of trials in each cell and the range of trials included

### Measurement procedures

-   Measurement procedures are described, including the measurement technique (e.g., mean amplitude), the time window and baseline period, sensor sites, etc.
-   For peak amplitude measures, the following is included: whether the peak was an absolute or local peak, whether visual inspection or automatic detection was used, and the number of trials contributing to the averages used for measurement
-   An a priori rationale is given for the selection of time windows, electrode sites, etc.
-   Both descriptive and inferential statistics are included

### Statistical analyses

-   Appropriate correction for any violation of model assumptions is implemented and described (e.g., Greenhouse-Geisser, Huynh-Feldt, or similar adjustment)
-   The statistical model and procedures are described and results are reported with test statistics, in addition to p values
-   An appropriate adjustment is performed for multiple comparisons
-   If permutation or similar techniques are applied, the number of permutations is indicated together with the method used to identify a threshold for significance

### Figures

-   Data figures for all relevant comparisons are included
-   Line plots (e.g., ERP/ERF waveforms) include the following: sensor location, baseline period, axes at zero points (zero physical units and zero ms), appropriate x- and y-axis tick marks at sufficiently dense intervals, polarity, and reference information, where appropriate
-   Scalp topographies and source plots include the following: captions and labels including a key showing physical units, perspective of the figure (e.g., front view; left/right orientation), type of interpolation used, location of electrodes/sensors, and reference
-   Coherence/connectivity and time-frequency plots include the following: a key showing physical units, clearly labeled axes, a baseline period, the locations from which the data were derived, a frequency range of sufficient breadth to demonstrate frequency-specificity of effects shown

### Spectral analyses

-   The temporal length and type of data segments (single trials or averages) entering frequency analysis are defined
-   The decomposition method is described, and an algorithm or reference given
-   The frequency resolution (and the time resolution in time-frequency analyses) is specified
-   The use of any windowing function is described, and its parameters (e.g., window length and type) are given
-   The method for baseline adjustment or normalization is specified, including the temporal segments used for baseline estimation, and the resulting unit

#$# Source-estimation procedures

-   The volume conductor model and the source model are fully described, including the number of tissues, the conductivity values of each tissue, the (starting) locations of sources, and how the sensor positions are registered to the head geometry
-   The source estimation algorithm is described, including all user-defined parameters (e.g., starting conditions, regularization)

### Principle component analysis (PCA)

-   The structure of the EEG/MEG data submitted to PCA is fully described
-   The type of association matrix is specified
-   The PCA algorithm is described
-   Any rotation applied to the data is described
-   The decision rule for retaining/discarding PCA components is described

### Independent component analysis (ICA)

-   The structure of the EEG/MEG data submitted to ICA is described
-   The ICA algorithm is described
-   Preprocessing procedures, including filtering, detrending, artifact rejection, etc., are described
-   The information used for component interpretation and clustering is described
-   The number of components removed (or retained) per subject is described

### Multimodal imaging

-   Single-modality results are reported

### Current source density and Laplacian transformations

-   The algorithm used and the interpolation functions are described

### Single-trial analyses

-   All preprocessing steps are described
-   A mathematical description of the algorithm is included or a reference to a complete description is provided

## See also

See also the page with [references to review papers and teaching material](/references_to_review_papers_and_teaching_material) elsewhere on this website, and the paper from Pernet C, Garrido MI, Gramfort A, Maurits N, Michel CM, Pang E, Salmelin R, Schoffelen JM, Valdes-Sosa PA, Puce A. **Issues and recommendations from the OHBM COBIDAS MEEG committee for reproducible EEG and MEG research.** Nat Neurosci. 2020 Dec;23(12):1473-1483. {% include badge doi="10.1038/s41593-020-00709-0" pmid="32958924" %}.
