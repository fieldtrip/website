---
title: How can I determine the anatomical label of a source or electrode?
tags: [faq, source]
---

# How can I determine the anatomical label of a source?

FieldTrip supports the use of an anatomical atlas to look up the anatomical label of a source that you have localized. Vice versa you can also first look up the location of an anatomical region and subsequently use that in source analysis, e.g. as region of interest for beamforming or as starting point for dipole fitting.

The function **[ft_read_atlas](/reference/ft_read_atlas)** reads in a specified atlas with coordinates and anatomical labels. It either uses the [AFNI brik file](http://afni.nimh.nih.gov/afni/doc/misc/afni_ttatlas/), or it uses one of the [WFU atlases](http://fmri.wfubmc.edu). The following example code shows a simple demonstration:

    atlas = ft_read_atlas('ROI_MNI_V4.nii');

    cfg              = [];
    cfg.method       = 'ortho';
    cfg.funparameter = 'brick0';
    cfg.funcolormap  = 'jet';
    ft_sourceplot(cfg, atlas)

Atlases can be used in several FieldTrip functions. For instance in the **[ft_sourceplot](/reference/ft_sourceplot)** function if you specify cfg.atlas and cfg.atlascoordinates you can click on a voxel in the interactive mode (cfg.method = ‘ortho’) and the label of that voxel according to the specified atlas is given.

The most important function for using an atlas is **[ft_volumelookup](/reference/ft_volumelookup)**. It can be used in two approaches.

1.  Given the anatomical or functional label, it looks up the locations and creates a mask (as a binary volume) based on the label, or creates a sphere or box around a point of interest.
2.  Given a binary volume that indicates a region of interest, it looks up the corresponding anatomical or functional labels from a given atlas.

# How can I determine the anatomical or functional label of an (intracranial) electrode?

In the context of intracranial EEG recordings, FieldTrip supports looking up the anatomical or functional labels corresponding to electrodes in a number of atlases, including the AFNI Talairach Tournoux atlas, the AAL atlas, the BrainWeb data set, the JuBrain cytoarchitectonic atlas, the VTPM atlas, and the Brainnetome atlas, in addition to the subject-tailored Desikan-Killiany and Destrieux atlases produced by FreeSurfer. Given that no two electrodes end up in the exact same location across subjects due to inter-individual variability in electrode coverage and brain anatomy, atlases are particularly useful for the systematic combination of neural activity from different subjects in a so-called region of interest (ROI) analysis. With exception of the above FreeSurfer-based atlases, the atlases are in MNI coordinate space and require the electrodes to be spatially normalized (Steps 26 through 27 of the [human iEEG tutorial](/tutorial/human_ecog)). First, import an atlas of interest, e.g., the AAL atlas, into the MATLAB workspace.

    atlas = ft_read_atlas([ftpath filesep 'template/atlas/aal/ROI_MNI_V4.nii']);

Look up the corresponding anatomical label of an electrode of interest, e.g., electrode LHH1, targeting the left hemisphere’s hippocampus. [Supplementary File 3](https://static-content.springer.com/esm/art%3A10.1038%2Fs41596-018-0009-6/MediaObjects/41596_2018_9_MOESM5_ESM.pdf) represents a tool that automatically overlays all channels in an electrode structure with all of the above atlases and stores the resulting anatomical labels in an excel table (e.g., SubjectUCI29_electable.xlsx in the zip file).

    cfg            = [];
    cfg.roi        = elec_mni_frv.chanpos(match_str(elec_mni_frv.label,'LHH1'),:);
    cfg.atlas      = atlas;
    cfg.inputcoord = 'mni';
    cfg.output     = 'label';
    labels = ft_volumelookup(cfg, atlas);

    [~, indx] = max(labels.count);
    labels.name(indx)
    ans =

    'ParaHippocampal_L'
