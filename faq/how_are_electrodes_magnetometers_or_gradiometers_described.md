---
title: How are electrodes, magnetometers or gradiometers described?
tags: [faq, electrode, eeg, meg, fiducial, layout]
---

# How are electrodes, magnetometers or gradiometers described?

Sensor locations are described by the `elec` or `grad` field in the data structure. These sensor definitions can contain fewer or more sensors than channels actually present in the data, i.e., you can have bipolar EOG channels that do not have a unique position on the scalp, but you might also have reference gradiometers positions for which you did not read or preprocess the data.

## The definition of EEG and IEEG (ECoG and sEEG) electrodes

As of September 23, 2011 we updated the description of how the sensors are defined in FieldTrip. The electrode definition contains the following field

    elec.label   = cell-array of length N with the label of each channel
    elec.elecpos = Mx3 matrix with the cartesian coordinates of each electrode
    elec.chanpos = Nx3 matrix with the cartesian coordinates of each channel

We typically think of a one-to-one correspondence between electrodes and channels, but in principle EEG channels and EEG electrodes are conceptually different since the channel represents the potential difference between an electrode of interest and a reference. For EEG you could e.g., consider a bipolar montage, in which each channel represents the voltage difference between an adjacent pair of electrodes. In case of an implicit (i.e. not specified) unipolar reference or a common-average reference, we set the channel position identical to the electrode position. So in general the number of channels N can be different from the number of EEG electrodes M.

To explicitly represent the reference, an additional field is needed in the `elec` structure:

    elec.tra  % NxM matrix with the weight of each electrode into each channel

This tells FieldTrip (and specifically the EEG forward modeling code) how to combine the electrodes into channels. This makes the reference explicit and allows to set the position of the reference electrode in unipolar recordings. In case `elec.tra` is not provided, the forward and inverse calculations will be performed assuming an average reference over all electrodes.

{% include markup/yellow %}
The EEG potential is in first instance computed on the locations specified in `elec.elecpos`, and when applicable combined using `elec.tra`. The `elec.chanpos` field is not used in the forward computations, but only for data visualization and for determining neighbours.
{% include markup/end %}

## The definition of MEG sensors

The gradiometer definition generally consists of multiple coils per channel, e.g., two coils for a 1st order axial gradiometer, in which the orientations of the bottom and top coil are opposite. Each coil is described separately and a `grad.tra` matrix is used to define how the forward computed magnetic field is combined over the coils to generate the MEG gradient of each channel. The gradiometer definition consists of the following fields as of September 23, 201

    grad.coilpos   = Mx3 matrix with the position of each coil
    grad.coilori   = Mx3 matrix with the orientation of each coil
    grad.tra       = NxM matrix with the weight of each coil into each channel
    grad.label     = cell-array of length N with the channel label
    grad.chanpos   = Nx3 matrix with the position of each channel
    grad.chanori   = Nx3 matrix with the orientation of each channel

The channel orientation is used for synthetic gradient computation for axial gradiometer or magnetometer systems. If you don't know what it means and if you need to construct your own grad structure, you can set it to `nan(N,3)`.

{% include markup/yellow %}
MEG forward computations are performed for each `grad.coilpos` and `grad.coilori`, and subsequently combined using `grad.tra`. Although they are called "coils", you can better think of them as integration points.

By default a first order gradiometer is described by 2 "coils", but you could use more integration points to get a more accurate forward model (see `cfg.coilaccuracy` in **[ft_preprocessing](/reference/ft_preprocessing)**).
{% include markup/end %}

## The definition of NIRS optodes and channels

Channels in a NIRS acquisition system comprise a pair of transmitting and receiving optodes. Furthermore, each optode is used with multiple wavelengths of the infrared light.

The optode definition contains the following fields

    opto.label         = Mx1 cell-array with channel labels
    opto.chanpos       = contains information about the position of the channels (usually halfway the transmitter and receiver)
    opto.optopos       = contains information about the position of individual optodes
    opto.optotype      = contains information about the type of optode (receiver or transmitter)
    opto.optolabel     = Nx1 cell-array with optode labels
    opto.transmits     = NxK matrix, boolean, where N is the number of optodes and K the number of wavelengths. Specifies which optode is transmitting at what wavelength (or nothing at all, indicating that it is a receiver)
    opto.wavelength    = 1xK vector of all wavelengths that were used
    opto.laserstrength = 1xK vector of the strength of the emitted light of the lasers
    opto.tra           = MxN matrix, boolean, contains information about how N receivers and transmitters form M channels

## The old electrode and gradiometer structure

The old electrode definition contained the following fields:

    elec.pnt   % Mx3 matrix with the position of each electrode
    elec.label

The old gradiometer definition contained the following fields:

    grad.pnt   % Mx3 matrix with the position of each coil
    grad.ori   % Mx3 matrix with the orientation of each coil
    grad.label
    grad.tra

The upgrade from the old to the current representation is required since the relevant information that is needed from the grad/elec structure is different for different analysis/visualization steps:

- for data displaying purposes, usually the channels are the entities of relevance. Also, in the context of finding neighbours using ft_prepare_neighbours for ft_megplanar, or for interpolation in ft_scalpcurrentdensity or ft_channelrepair, the channels are the relevant entities.

- for forward and inverse modeling purposes, the sensing elements, i.e. the electrodes or coils are of relevance.

Originally, FieldTrip relied on recovering sensor positions from the electrode/coil positions by looking into the `tra` matrix, because the `tra` matrix specifies which electrode/coil contributes to which channel. However, since we are now supporting increasingly complex `tra` matrices which can include balancing coefficients (obtained through **[ft_denoise_synthetic](/reference/ft_denoise_synthetic)**, or **[ft_denoise_pca](/reference/ft_denoise_pca)**), projected-out spatial topographies (obtained through a sequence of **[ft_componentanalysis](/reference/ft_componentanalysis)** and **[ft_rejectcomponent](/reference/ft_rejectcomponent)**), or synthetic planar gradients (obtained through **[ft_megplanar](/reference/ft_megplanar)**). With these increasingly complex `tra` matrices, reconstructing the channel positions from the coil/electrode positions is not straightforward and sometimes impossible, therefore we now make the explicit distinction between channels and electrodes/coils.

## Some additional notes on the `tra` matrix

The `tra` matrix is an important piece of information to be taken into account when computing forward models (leadfields) for the sensor data in a given data structure. When computing a forward model, we compute the magnetic/electric field distribution at the described sensors/electrodes in the data, given a known dipolar source. If the sensor data has been manipulated in any way - e.g., by creating higher order synthetic gradients using additional  reference coils (as can be done with CTF MEG data with **[ft_denoise_synthetic](/reference/ft_denoise_synthetic)**, or with the custom CTF software), by using adaptive weights estimated from the data (as can be done with 4D-data, using custom software or **[ft_denoise_pca](/reference/ft_denoise_pca)**), or also when removing spatial topographies from the sensor data (using a combination of **[ft_componentanalysis](/reference/ft_componentanalysis)** and **[ft_rejectcomponent](/reference/ft_rejectcomponent)**) - the corresponding leadfields need to be manipulated in the same way, to ensure that the forward model is consistent with the data.

As the `tra` matrix provides information how the individual electrodes/coils relate to the individual channels in the data structure, it is updated automatically upon manipulation of the data in the following functions:

- [ft_combineplanar](/reference/ft_combineplanar)
- [ft_componentanalysis](/reference/ft_componentanalysis)
- [ft_denoise_pca](/reference/ft_denoise_pca)
- [ft_denoise_synthetic](/reference/ft_denoise_synthetic)
- [ft_denoise_tsr](/reference/ft_denoise_tsr)
- [ft_preprocessing](/reference/ft_preprocessing)
- [ft_rejectcomponent](/reference/ft_rejectcomponent)

The `tra` matrix is used as a left multiplier of the unbalanced lead field (i.e. for MEG the leadfield that represents the magnetic field distribution at the location of the individual magnetometer coils) in the following way: `lf_balanced = grad.tra * lf_unbalanced`. For example, to obtain a first-order axial gradiometer, each row in the `tra` matrix contains two '1's (assuming the orientation of the top and bottom coils to be opposite), indicating that the modeled field estimated at the top and bottom coil of a gradiometer should be summed to obtain a model of the axial gradients. To obtain synthetic higher order gradients, the columns in the `tra` matrix that correspond to the reference coils will have non-zero values, reflecting the 'balancing' coefficients.

In summary, if you are doing fancy things with your data and later on want to do source reconstruction, it is not safe to just take any `grad` structure to compute your leadfields. For obvious reasons, not only do the positions of the coils need to be the same as the ones used during the measurement, but the `tra` matrix also needs to reflect all the manipulations you have applied to the data.
