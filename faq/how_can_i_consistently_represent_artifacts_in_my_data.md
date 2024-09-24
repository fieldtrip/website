---
title: How can I consistently represent artifacts in my data?
category: faq
tags: [preprocessing, artifact]
---

# How can I consistently represent artifacts in my data?

FieldTrip includes multiple functions for automatic artifact rejection, as explained in this [tutorial](/tutorial/automatic_artifact_rejection). These functions detect time segments in the data in which an artifact is present by the begin and end sample of that artifact. If there are N artifacts, that results in a Nx2 matrix, with the first column representing the begin samples, and the second column representing the end samples.

If you manually identify time segments with an artifact, you can represent them like

    eog.artifact    = N x 2
    muscle.artifact = M x 2
    jump.artifact   = K x 2

and pass them onto the **[ft_rejectartifact](/reference/ft_rejectartifact)** function in the cfg.artfctdef field like

    cfg.artfctdef.eog.artifact    = N x 2
    cfg.artfctdef.muscle.artifact = M x 2
    cfg.artfctdef.jump.artifact   = K x 2

followed by

    cfg = ft_rejectartifact(cfg);

## Bad channels

To specify lists of bad channels, you can use a consistent representation, e.g.

    linenoise.badchannel = {'C3', 'Fp1'};
    emg.badchannel       = {'T3', 'T4'};

and use the following code to merge the bad channels into a single list

    hdr = ft_read_header(filename);
    sel = false(size(hdr.label));

    for i=1:length(linenoise.badchannel)
    sel(strmatch(hdr.label, linenoise.badchannel{i})) = true;
    end

    for i=1:length(emg.badchannel)
    sel(strmatch(hdr.label, emg.badchannel{i}) = true;
    end

    % combine them into one list
    badchannel  = hdr.label(sel);
    goodchannel = setdiff(hdr.label, badchannel);

This list with good channels can be passed to **[ft_preprocessing](/reference/ft_preprocessing)** in the cfg.channel option.
