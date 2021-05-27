---
title: Re-reference EEG and iEEG data
tags: [example, eeg, preprocessing]
---

# Re-reference EEG and iEEG data

EEG and intracranial EEG (iEEG) data, which includes sEEG and ECoG, is often recorded relative to a reference electrode that is good for the signal quality and for noise suppression (e.g. with an electrode firmly attached on the mastoid behind the ear), but that is not neccessarily the most optimal for subsequent analysis. Hence, it is quite common to apply some re-referencing in the preprocessing of EEG and iEEG data.

FieldTrip implements multiple methods for re-referencing in the **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** function. To use these, you specify `cfg.reref='yes'` and give the specific method as `cfg.refmethod`. Alternatively, if you have a more complex referencing scheme or want more control over the re-referencing, you can specify `cfg.reref='no'` and rather use `cfg.montage`.
 
## avg

With `cfg.refmethod='avg'` the average is computed over the channels specified in `cfg.refchannel` and subtracted from all channels that were selected in **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)**.

You can use this to compute an averagee reference over all electrodes like this:

    cfg = [];
    cfg.dataset = 'somefile.eeg';
    data_orig = ft_preprocessing(cfg);

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'avg';
    cfg.refchannel = 'all';
    data_avg = ft_preprocessing(cfg, data_orig);

After this preprocessing step, the median over all channels will be zero.

{% include markup/success %}
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

You can also use `cfg.refmethod='avg'` to compute an offline linked ears reference, i.e. the average of both earlobes or both mastoids.

If your original reference during data acquisition is for example FCz, then that would look like this:

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'avg';
    cfg.implicitref = 'FCz'; % see below
    cfg.refchannel = {'M1', 'M2'}; % or A1 and A2 for the ear lobes
    data_linkedears = ft_preprocessing(cfg, data_orig);

If your original data was referenced during data acquisition to the right mastoid (M2), then the potential on that mastoid is *by definition* zero. Since the potential on the reference is not interesting, there is no channel stored in the EEG file for the reference. The `cfg.implicitref` option allows to add a reference channel to the data matrix; it will be all zeros. Subsequently, it can be included in the new re-referencing scheme:

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.implicitref = 'M2'; % add the reference channel to the data
    cfg.refchannel = {'M1', 'M2'}; % compute the average over M1 and M2
    data_linkedears = ft_preprocessing(cfg, data_orig);

The implicit reference is added prior to searching for the reference channels. If M2 were used as reference and you *did not* specify it as `cfg.implicitref`, then the `cfg.refchannel` selection will look at the channels in the original data and the list `{'M1', 'M2'}` will only match channel M1, which means that the reference would be the average of M1, i.e. M1 itself, and the data is effectively not changed.

## median

Using `cfg.refmethod='median'` works largely the same as taking the average, but it computes the median instead of the mean. This is expecially useful when you have one (or a few) channels with a lot of noise: the median will be less sensitive to the outlier values than the mean.

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'median';
    cfg.refchannel = 'all';
    data_avg = ft_preprocessing(cfg, data_orig);

After this preprocessing step, the median over all channels will be zero.

We recommend the median reference when you have a lot of channels and when it is hard to identify and disable the bad channels. The median is **not recommended** when you plan to do dipole fitting or source reconstruction on the data, since the median of the data will be influenced by the noise, whereas the median of the forward computed leadfield will not be influenced by the noise. Consequently, the median reference in the forward model will never really fit that of the data. However, for source reconstruction you would want to use clean data without bad channels, so the median reference is less applicable anyway.

## rest

To be added.

## bipolar

Often the activity recorded by a channel is contaminated by the signal coming from nearby regions, that diffuses in its surroundings. This might cause the mis-classification of channels which are not correlated with the experimental task as if they were indeed task-correlated. To ensure a better detection of task-related channels, it is recommended to adopt a more localized re-referencing scheme, which could better take into account the activity relative to each channel's surroundings. For this purpose, the **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** allows the possibility to perform bipolar rereferencing and Laplacian rereferencing.

The bipolar rereferencing scheme consists of the rereferencing of each channel against its closest neighboring channel. Before calling **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** it is important to make sure that the channels are ordered on the basis of their proximity to each other. Bipolar rereferencing can be performed by simply configuring `cfg.refmethod = 'bipolar'` as in the following example:

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'bipolar';
    cfg.refchannel = 'all';
    data_avg = ft_preprocessing(cfg, data_orig);

Note that, since each of the N original channels is rereferenced against the next one in order, the last channel cannot be rereferenced and, at the end of the process, the dataset will contain N-1 channels. To emphasize the fact that the signal of each channel now derives from the subtraction between two neighbouring channels, all labels are modified. As an example, in place of the channels `C1`, `C2` and `C3`, the re-referenced dataset will present the channels `C1-C2` and `C2-C3`.

If you are analysing an iEEG dataset, you might want to rereference separately channels belonging to different electrode shafts. It is possible to do so by setting `cfg.groupchans = 'yes'` and by labelling the channels in a precise way. 

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'bipolar';
    cfg.refchannel = 'all';
    cfg.groupchans = 'yes';
    data_avg = ft_preprocessing(cfg, data_orig);

Labels should consist of an alphabetic code followed by a number, the alphabetic code being specific for the electrode (and being the same for all channels belonging to the same elctrode) and the number giving an indication about the order of the channels along the electrode. As an example, channels `'LT1'` and `'LT2'` will be rereferenced together, but separately from channels `'LP1'` and `'LP2'`. The grouping and ordering of channels is automatic, therefore, particular attention should be paid to their labelling. In case you were interested in separetely rereferencing specific groups of EEG channels, this is also possible: simply make sure that they are correctly labelled.

## laplace

The Laplacian rereferencing scheme is quite similar to the bipolar one and can be applied to both EEG and iEEG data. This method allows to reduce the number of task-correlated channels by increaseing the degree of correlation between the signal and the task. This scheme consists of the rereferencing of each channel against the mean of its two clostest neighbours. As for the bipolar rereferencing, channels should be given in input to **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)** in the order that should be used to rereference them. In this case, the first and last channels of the order will be simply rereferenced against their closest neighbor. Laplacian rereferencing can be performed by setting `cfg.refmethod = 'laplace'`.

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'laplace';
    cfg.refchannel = 'all';
    data_avg = ft_preprocessing(cfg, data_orig);

Note: differently from the bipolar method, in this case the number of channels does not vary after rereferencing and their original labels are maintained.

If you are analysing iEEG data, you are probably interested in rereferencing channels separately for each electrode shaft. This can be done exactly as it was described above for bipolar rereferencing, by configuring `cfg.groupchans = 'yes'` and by making sure that channels are correctly labelled.

    cfg = [];
    cfg.channel = 'all'; % this is the default
    cfg.reref = 'yes';
    cfg.refmethod = 'laplace';
    cfg.refchannel = 'all';
    cfg.groupchans = 'yes';
    data_avg = ft_preprocessing(cfg, data_orig);

## montage

Using the `cfg.montage` option, you can specify an arbitrarily complex "montage". All of the previous methods (except for the median) could in principle be implemented with this.

A montage (also known as a "linear derivation") specifies a linear mapping or combination from the (old) channels in the original data to the new channels in the re-referenced data. Basically it is implemented by a matrix multiplication, following some shuffling of the the rows of the data matrix. The montage is explained in more detail in the low-level **[ft_apply_montage](https://github.com/fieldtrip/fieldtrip/blob/release/forward/ft_apply_montage.m)**  function.

As an example, a bipolar montage could look like this:

    bipolar.labelold  = {'1',   '2',   '3',   '4'}
    bipolar.labelnew  = {'1-2', '2-3', '3-4'}
    bipolar.tra       = [
      +1 -1  0  0
       0 +1 -1  0
       0  0 +1 -1
    ];

Where the input data consists of 4 channels, and the output data would have three channels with the pair-wise difference between '1-2', '2-3', and '3-4'.

This can also be used to implement a single or double "banana" montage for clinical EEG, like this:

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

However, the disadvantage of doing it this way is that if you remove a channel prior to re-referencing, you have to update your montage. This is not needed when you use `cfg.refmethod='avg'`.
