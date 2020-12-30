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

To be added.

## laplace

To be added.

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
