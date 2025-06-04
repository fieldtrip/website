---
title: Rereference EEG and iEEG data
category: example
tags: [eeg, preprocessing, laplace, bipolar, montage]
redirect_from:
    - /example/rereference/
---

# Rereference EEG and iEEG data

EEG and intracranial EEG (iEEG) data, which includes sEEG and ECoG, is often recorded relative to a reference electrode that is good for the signal quality and for noise suppression (e.g., with an electrode firmly attached on the mastoid behind the ear), but that is not necessarily the most optimal for subsequent analysis or interpretation of the data. Hence, it is common to apply some rereferencing in the preprocessing of EEG and iEEG data.

FieldTrip implements multiple methods for rereferencing in the **[ft_preprocessing](/reference/ft_preprocessing)** function. To use these, you specify `cfg.reref='yes'` and give the specific method as `cfg.refmethod`. Alternatively, if you have a more complex referencing scheme or want more control over the rereferencing, you can specify `cfg.reref='no'` and rather use `cfg.montage` in combination with **[ft_prepare_montage](/reference/ft_prepare_montage)**.

The process and consequences of applying a certain rereferencing scheme which is also known as a "montage" to clinical 1020 EEG recordings is very nicely explained on the [Learning EEG](https://www.learningeeg.com/montages-and-technical-components) website.

## avg

With `cfg.refmethod='avg'` the average is computed over the channels specified in `cfg.refchannel` and subtracted from all channels that were selected in **[ft_preprocessing](/reference/ft_preprocessing)**.

You can use this to compute an average reference over all electrodes like this:

    cfg = [];
    cfg.dataset = 'somefile.eeg';
    data_orig = ft_preprocessing(cfg);

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'avg';
    cfg.refchannel = 'all';
    data_avg = ft_preprocessing(cfg, data_orig);

After this preprocessing step, the average or mean over all channels will be zero.

{% include markup/green %}
Note that you can also do the reading and rereferencing in one step like this:

    cfg = [];
    cfg.dataset = 'somefile.eeg';
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'avg';
    cfg.refchannel = 'all';
    data_avg = ft_preprocessing(cfg);

In the examples here we are doing it in two steps to reuse the data that is read into memory and to make it easier to compare the before and after data.
{% include markup/end %}

You can also use `cfg.refmethod='avg'` to compute an offline linked-ears reference, i.e. the average of both earlobes or both mastoids.

If your original reference during data acquisition is for example FCz and both mastoids are also recorded, then that would look like this:

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'avg';
    cfg.implicitref = 'FCz'; % see below
    cfg.refchannel = {'M1', 'M2'}; % or A1 and A2 for the ear lobes
    data_linkedears = ft_preprocessing(cfg, data_orig);

If your original data was referenced during data acquisition to the right mastoid (M2), then the potential on that mastoid is *by definition* zero. Since the potential on the reference is not interesting, there is no channel stored in the EEG file for the reference. The `cfg.implicitref` option allows to add a reference channel to the data matrix; it will be all zeros. Subsequently, it can be included in the new rereferencing scheme:

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.implicitref = 'M2'; % add the M2 reference channel to the data with zeros
    cfg.refchannel = {'M1', 'M2'}; % compute the average over M1 and M2
    data_linkedears = ft_preprocessing(cfg, data_orig);

The implicit reference is added prior to searching for the reference channels. If M2 were used as reference and you *did not* specify it as `cfg.implicitref`, then the `cfg.refchannel` selection will look at the channels in the original data and the list `{'M1', 'M2'}` will only match channel M1, which means that the reference would be the average of M1, i.e. M1 itself, and the data is effectively not changed.

## median

Using `cfg.refmethod='median'` works largely the same as taking the average, but it computes the median instead of the mean. This is especially useful when you have one (or a few) channels with a lot of noise: the median will be less sensitive to the outlier values than the mean.

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'median';
    cfg.refchannel = 'all';
    data_median = ft_preprocessing(cfg, data_orig);

After this preprocessing step, the median over all channels will be zero.

We recommend the median reference when you have a lot of channels and when it is hard to identify and disable the bad channels. The median is **not recommended** when you plan to do dipole fitting or source reconstruction on the data, since the median of the data will be influenced by the noise, whereas the median of the forward computed leadfield will not be influenced by the noise. Consequently, the median reference in the forward model will never really fit that of the data. However, for source reconstruction you would want to use clean data without bad channels, so the median reference is less applicable anyway.

## rest

The REST or Reference Electrode Standardization Technique for scalp EEG recordings approximates a reference at a point at infinity. See [A method to standardize a reference of scalp EEG recordings to a point at infinity](https://doi.org/10.1088/0967-3334/22/4/305) by Dezhong Yao (2001) for details.

This method requires a forward model for the sources that are assumed to have generated the EEG data, this can be computed using **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**.

The following example uses a spherical arrangement of the electrodes, in combination with a three layer spherical headmodel. The sources consist of a layer of 642 evenly distributed dipoles that are shifted inward from the inner skull surface.

    elec = ft_read_sens('template/electrode/easycap-M1.txt');

    headmodel = [];
    headmodel.type = 'singlesphere';
    headmodel.cond = [0.3300 1 0.0042 0.3300];  % conductivities of each sphere
    headmodel.r = [71 72 79 85];                % radius of each sphere
    headmodel.o = [0 0 0];
    headmodel.unit = 'mm';

    cfg = [];
    cfg.headmodel = headmodel;
    cfg.elec = elec;
    cfg.method = 'basedonvol';
    cfg.inwardshift = 20; % in mm, relative to the scalp surface which is at 85 mm radius
    sourcemodel = ft_prepare_sourcemodel(cfg);

    figure
    ft_plot_headmodel(headmodel);
    alpha 0.3
    ft_plot_mesh(sourcemodel);
    ft_plot_sens(elec, 'label', 'label', 'elecshape', 'disc');
    view([80, 120, 20])

    cfg = [];
    cfg.headmodel = headmodel;
    cfg.elec = elec;
    cfg.sourcemodel = sourcemodel;
    leadfield = ft_prepare_leadfield(cfg);

    data_org = [];
    data_org.label = elec.label;
    data_org.time{1} = (1:1000)/1000;
    data_org.trial{1} = rand(length(data_org.label), length(data_org.time{1}));

    cfg = [];
    cfg.implicitref = [];
    cfg.reref = 'yes';
    cfg.refmethod = 'rest';
    cfg.refchannel = 'all';
    cfg.leadfield = leadfield;
    data_rest = ft_preprocessing(cfg, data_org);

## bipolar

{% include markup/yellow %}
The implementation for `cfg.refmethod = 'bipolar'` is primarily designed for sEEG where each contact along each chaft starts with the same letter(s). If you have EEG data with a 1020 electrode placement, you probably want to use one of the explicit bipolar schemes, such as the double banana (see below).
{% include markup/end %}

Often the activity recorded by a channel is contaminated by the signal coming from nearby regions, that diffuses in its surroundings. This might cause the mis-classification of channels which are not correlated with the experimental task as if they were indeed task-correlated. To ensure a better detection of task-related channels, it is recommended to adopt a more localized rereferencing scheme, which could better take into account the activity relative to each channel's surroundings. For this purpose, **[ft_preprocessing](/reference/ft_preprocessing)** allows the possibility to perform bipolar or Laplacian rereferencing.

The bipolar rereferencing scheme consists of the rereferencing of each channel against its closest neighboring channel. Before calling **[ft_preprocessing](/reference/ft_preprocessing)** it is important to make sure that the channels are ordered on the basis of their proximity to each other. Bipolar rereferencing is performed by specifying `cfg.refmethod = 'bipolar'` as in the following example.

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'bipolar';
    cfg.refchannel = 'all';
    data_bipolar = ft_preprocessing(cfg, data_orig);

Note that, since each of the N original channels is rereferenced against the next one in order, the last channel cannot be rereferenced and, at the end of the process, the dataset will contain N-1 channels. To emphasize the fact that the signal of each channel now derives from the subtraction between two neighbouring channels, all labels are modified. As an example, in place of the channels `C1`, `C2` and `C3`, the rereferenced dataset will present the channels `C1-C2` and `C2-C3`.

If you are analyzing an sEEG dataset, you might want to rereference separately channels belonging to different electrode shafts. It is possible to do so by setting `cfg.groupchans = 'yes'` and by ensuring your channels are labeled correctly. Channels of each shaft should start with one or multiple letters (e.g., 'LT', 'LP', ...) and the subsequent electrodes should be numbered (e.g., 'LT1', 'LT2', ...).

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'bipolar';
    cfg.refchannel = 'all';
    cfg.groupchans = 'yes';
    data_bipolar = ft_preprocessing(cfg, data_orig);

## laplace

The Laplacian rereferencing scheme is relatively similar to the bipolar scheme. It allows to reduce the number of task-correlated channels by increasing the degree of correlation between the signal and the task. This scheme consists of the rereferencing of each channel against the mean of its two clostest neighbours. As for the bipolar rereferencing, channels should be given in input to **[ft_preprocessing](/reference/ft_preprocessing)** in the order that should be used them. In this case, the first and last channels of the order will be simply rereferenced against their closest neighbor. Laplacian rereferencing is be performed by specifying  `cfg.refmethod = 'laplace'` as in the following example.

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'laplace';
    cfg.refchannel = 'all';
    data_laplace = ft_preprocessing(cfg, data_orig);

Note that, differently from the bipolar method, the number of channels is the same as the input data and the original labels are maintained.

If you are analyzing iEEG data, you are probably interested in rereferencing channels separately for each electrode shaft. This can be done exactly as it was described above for bipolar rereferencing, by configuring `cfg.groupchans = 'yes'` and by making sure that channels are correctly labeled. Channels of each shaft should start with one or multiple letters (e.g., 'LT', 'LP', ...) and the subsequent electrodes should be numbered (e.g., 'LT1', 'LT2', ...).

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'laplace';
    cfg.refchannel = 'all';
    cfg.groupchans = 'yes';
    data_laplace = ft_preprocessing(cfg, data_orig);

## longitudinal or doublebanana

The longitudinal montage for the 1020 EEG system, also known as the double banana montage, consists of multiple chains of bipolar channels that run from the front to the back of the head. See [Learning EEG](https://www.learningeeg.com/montages-and-technical-components) for details.

    cfg = [];
    cfg.channel = 'eeg1020'; % channels not in the 10-20 system will be ignored anyway
    cfg.reref = 'yes';
    cfg.refmethod = 'longitudinal'; % or 'doublebanana'
    data_longitudinal = ft_preprocessing(cfg, data_orig);

## circumferential

In the circumferential montage for the 1020 EEG system the electrodes are chained in a circle around the head. See [Learning EEG](https://www.learningeeg.com/montages-and-technical-components) for details.

    cfg = [];
    cfg.channel = 'eeg1020'; % channels not in the 10-20 system will be ignored anyway
    cfg.reref = 'yes';
    cfg.refmethod = 'circumferential';
    data_circumferential = ft_preprocessing(cfg, data_orig);

## transverse

In the transverse montage for the 1020 EEG system the electrodes are chained from the left to the right. See [Learning EEG](https://www.learningeeg.com/montages-and-technical-components) for details.

    cfg = [];
    cfg.channel = 'eeg1020'; % channels not in the 10-20 system will be ignored anyway
    cfg.reref = 'yes';
    cfg.refmethod = 'transverse';
    data_transverse = ft_preprocessing(cfg, data_orig);

## montage

Using the `cfg.montage` option, you can specify an arbitrarily complex "montage". All of the previous methods (except for the median) could in principle be implemented with this, and some of them actually use a montage "under the hood" that is constructed on the fly with **[ft_prepare_montage](/reference/ft_prepare_montage)**.

A montage, also known as a "linear derivation" or as a "re-referencing scheme" specifies a linear mapping from the (old) channels in the original data to the new channels in the rereferenced data. Basically it is implemented by a matrix multiplication, following some shuffling of the the rows of the data matrix. The montage is explained in more detail in the **[ft_prepare_montage](/reference/ft_prepare_montage)**  and **[ft_apply_montage](/reference/forward/ft_apply_montage)** functions.

As an example, a bipolar montage could look like this:

    bipolar.labelold  = {'1',   '2',   '3',   '4'}
    bipolar.labelnew  = {'1-2', '2-3', '3-4'}
    bipolar.tra       = [
      +1 -1  0  0
       0 +1 -1  0
       0  0 +1 -1
    ];

Where the input data consists of 4 channels, and the output data would have three channels with the pair-wise difference between '1-2', '2-3', and '3-4'.

This can also be used to implement your own single or double "banana" montage for clinical EEG, like this:

{% include image src="/assets/img/example/rereference/banana_montage.png" width="400" %}

    banana_montage.labelold = {
     'Fp1'
     'F7'
     'T3'
     'T5'
     'O1'
     'F3'
     'C3'
     'P3'
     'Fp2'
     'F8'
     'T4'
     'T6'
     'O2'
     'F4'
     'C4'
     'P4'
     };

    banana_montage.labelnew = {
      'F7-Fp1'
      'T3-F7'
      'T5-T3'
      'O1-T5'
      'F3-Fp1'
      'C3-F3'
      'P3-C3'
      'O1-P3'
      'F8-Fp2'
      'T4-F8'
      'T6-T4'
      'O2-T6'
      'F4-Fp2'
      'C4-F4'
      'P4-C4'
      'O2-P4'
    };

    banana_montage.tra = [
     -1  +1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
      0  -1  +1   0   0   0   0   0   0   0   0   0   0   0   0   0
      0   0  -1  +1   0   0   0   0   0   0   0   0   0   0   0   0
      0   0   0  -1  +1   0   0   0   0   0   0   0   0   0   0   0
     -1   0   0   0   0  +1   0   0   0   0   0   0   0   0   0   0
      0   0   0   0   0  -1  +1   0   0   0   0   0   0   0   0   0
      0   0   0   0   0   0  -1  +1   0   0   0   0   0   0   0   0
      0   0   0   0  +1   0   0  -1   0   0   0   0   0   0   0   0

      0   0   0   0   0   0   0   0  -1  +1   0   0   0   0   0   0
      0   0   0   0   0   0   0   0   0  -1  +1   0   0   0   0   0
      0   0   0   0   0   0   0   0   0   0  -1  +1   0   0   0   0
      0   0   0   0   0   0   0   0   0   0   0  -1  +1   0   0   0
      0   0   0   0   0   0   0   0  -1   0   0   0   0  +1   0   0
      0   0   0   0   0   0   0   0   0   0   0   0   0  -1  +1   0
      0   0   0   0   0   0   0   0   0   0   0   0   0   0  -1  +1
      0   0   0   0   0   0   0   0   0   0   0   0  +1   0   0  -1
     ];

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'no'; % use the cfg.montage option instead
    cfg.montage = banana_montage;
    data_banana = ft_preprocessing(cfg, data_orig);

You can also use the `cfg.montage` to construct an average reference like this:

    montage_avg.labelold = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'};
    montage_avg.labelnew = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '10'};
    montage_avg.tra = eye(10) - 1/10;

However, the disadvantage of doing it this way is that if you remove a channel prior to rereferencing, you have to update your montage. This is not needed when you use `cfg.refmethod='avg'`.
