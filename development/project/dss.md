---
title: Use denoising source separation (DSS) to remove ECG artifacts
---

{% include /shared/development/warning.md %}

## Use denoising source separation (DSS) to remove ECG artifacts

### Description

This script demonstrates how you can use denoising source separation (DSS) for cleaning the ECG/BCG artifacts from your MEEG data. It consists of four steps:

1.  detection of QRS-complexes using the ECG channel, which has been recorded along with the data
2.  use the identified peaks as prior information to inform the DSS algorithm to unmix the MEEG channel data
2.  selection of a number of components to remove from MEEG data
3.  removal of the identified components

DSS is a blind source separation technique that is akin to ICA, with the added functionality of that it can use prior information to unmix the signals into sources that have certain characteristics. While in ICA the defining characteristic of the sources is statistical independence, in DSS one can for instance steer the unmixing towards the identification of sources that are timelocked to certain events. This is the exact feature that we are going to exploit in this example, because it shows how to remove the ECG artifact, using information about the timing of the QRS-complexes. What is therefore needed, is a sufficiently clean ECG-like signal to begin with, to allow for the identification of those peaks. This will be done, using the ft_artifact_zvalue function. Next, the output of ft_artifact_zvalue will be used to call ft_componentanalysis with 'dss' as method. 

### Example dataset

You can run the code below on your own data. Alternatively, try with the example MEG dataset [ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/ArtifactRemoval.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/ArtifactRemoval.zip). All figures in this example script are based on these data. 

To load this dataset into MATLAB and preprocess with FieldTrip, use:

    cfg         = [];
    cfg.dataset = 'ArtifactRemoval.ds'; % ensure that you are in the correct folder for this to run
    cfg.trialdef.eventtype = 'trial';
    cfg     = ft_definetrial(cfg);
    cfg.trl = cfg.trl(1:end-1,:); % remove the last one, because it clips.

    cfg.channel = 'MEG';
    cfg.demean  = 'yes';
    meg         = ft_preprocessing(cfg);

### ECG peak detection

We will use ft_artifact_zvalue for this step. To this end, we read in the ECG channel (in the dataset used this is channel 'EEG058'), and apply some filtering etc. to facilitate the identification of peaks in the signal.

    cfg = removefields(cfg, {'channel', 'demean'});
    cfg.artfctdef.zvalue.channel         = 'EEG058';
    cfg.artfctdef.zvalue.cutoff          = 2;
    cfg.artfctdef.zvalue.interactive     = 'yes';
    cfg.artfctdef.zvalue.bpfilter        = 'yes';
    cfg.artfctdef.zvalue.bpfreq          = [5 30];
    cfg.artfctdef.zvalue.hilbert         = 'yes';
    cfg.artfctdef.zvalue.artfctpeak      = 'yes';
    cfg.artfctdef.zvalue.artfctpeakrange = [-.25 .5]; % save out 250ms prior and 500ms post ECG peak
    cfg = ft_artifact_zvalue(cfg);

The DSS code wants a 'params' structure which contains peak time points, as well as the range around the peak that you think is relevant. Note that the subfield 'dssartifact' is different from 'artifact' in 2 ways: 1) beginning/end points based on cfg.artfctdef.zvalue.artfctpeakrange rather than where the channel exceeded the threshold, and 2) the sample counts between trial end to the start of next trial have been subtracted.

    params.tr  = cfg.artfctdef.zvalue.peaks_indx;
    params.pre = 0.25*meg.fsample;
    params.pst = 0.50*meg.fsample;
    params.demean = true;
    
### DSS component rejection

    cfg                   = [];
    cfg.method            = 'dss';
    cfg.dss.denf.function = 'denoise_avg2';
    cfg.dss.denf.params   = params;
    cfg.dss.wdim          = 75;
    cfg.numcomponent      = 4;
    cfg.channel           = 'MEG';
    cfg.cellmode          = 'yes';
    comp                  = ft_componentanalysis(cfg, meg);

The output compdss contains the components to reject. You can use ft_databrowser to plot all components at once and decide which components to reject. Unlike ICA, where the order of the components is rather random, usually the first (and second) components are the ones to be rejected. This is because, given the default settings, DSS iteratively searches for the the 'sources' that contain the required features, in this case: 'are heartbeat like'. Thus, the first component looks most like a heartbeat signal, followed by the second one, etc.

    cfg = [];
    cfg.layout = 'CTF275_helmet.mat'; % specify the layout file that should be used for plotting
    ft_databrowser(cfg, comp);

Once you are happy with the number of components to reject, then actually remove them from the data.

    cfg           = [];
    cfg.component = [1 2];
    meg_clean     = ft_rejectcomponent(cfg, comp, meg);
