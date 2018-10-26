---
title: How are electrodes, magnetometers or gradiometers described?
layout: default
tags: [faq, eeg, meg, layout]
---

## How are electrodes, magnetometers or gradiometers described?

Sensor locations are described by the elec or grad field in the data object. These definitions of the sensors can contain fewer or more channels that present in the data, i.e., you can have bipolar EOG channels that do not have a unique position on the scalp, but you can also have reference gradiometers in the MEG system that do not have a signal attached to them.

### The definition of EEG, ECoG and iEEG electrodes

As of September 23, 2011 we updated the description of how the sensors are defined in FieldTrip. The electrode definition contains the following field

    elec.label   % cell-array of length N with the label of each channel
    elec.elecpos % Mx3 matrix with the cartesian coordinates of each electrode
    elec.chanpos % Nx3 matrix with the cartesian coordinates of each channel

Note that there is typically a one-to-one match between electrodes and channels, but in principle channels and electrodes can refer to different entities. In the context of EEG, one may consider a setup containing bipolar derivations, in which each 'channel' represents the voltage difference between a pair of electrodes. Consequently, the number of channels N then is different from the number of electrodes M. An additional field is needed in the elec-structure

    elec.tra  % NxM matrix with the weight of each electrode into each channel  

to tell FieldTrip how to combine the electrodes into channels. This array can be stored as a sparse array and it also allows to set the position of the reference electrode in unipolar recordings. In case elec.tra is not provided, the forward and inverse calculations will be performed assuming an average reference over all electrodes.

<div class="alert-warning">
The EEG potential is in first instance computed on the locations in elec.elecpos, and when applicable combined using elec.tra. The elec.chanpos field is used e.g. for visualization and determining neighbours.  
</div>

### The definition of MEG sensors

The gradiometer definition generally consists of multiple coils per channel, e.g. two coils for a 1st order axial gradiometer, in which the orientation of the coils is opposite. Each coil is described separately and one large matrix (grad.tra: can be sparse) has to be given that defines how the forward computed field is combined over the coils to generate the output of each channel. The gradiometer definition consists of the following fields as of September 23, 201

    grad.coilpos   % Mx3 matrix with the position of each coil
    grad.coilori   % Mx3 matrix with the orientation of each coil
    grad.tra       % NxM matrix with the weight of each coil into each channel
    grad.label     % cell-array of length N with the channel label
    grad.chanpos   % Nx3 matrix with the position of each channel
    grad.chanori   % Nx3 matrix with the orientation of each channel.

The channel 'orientation' is needed for synthetic gradient computation for axial gradiometer or magnetometer systems. If you don't know what it means and need to construct your own grad structure, please set it to nan(N,3).

<div class="alert-warning">
MEG forward computations are performed for each grad.coilpos and grad.coilori, and subsequently combined using grad.tra. Although they are called "coils", you can better think of them as "field digitization points".

By default a first order gradiometer is described by 2 "coils", but you could use more digitization points to get a more accurate forward model.   
</div>

### The old electrode and gradiometer structure

The old electrode definition contained the following field

    elec.pnt   % Mx3 matrix with the position of each electrode
    elec.label

The old gradiometer definition contained the following field

    grad.pnt   % Mx3 matrix with the position of each coil
    grad.ori   % Mx3 matrix with the orientation of each coil
    grad.label
    grad.tra

The upgrade from this to the current representation is motivated by the fact that the relevant information that is needed from the grad/elec structure is different for different analysis/visualization step

*  for displaying purposes, usually the channels are the entities of relevance. Also, in the context of finding neighbours to a given channel (for clustering, or synthetic gradient computation, or interpolation as in scalpcurrentdensity or channelrepair), the channels are the relevant entities.

*  for forward and inverse modelling purposes, the sensing elements, i.e. the electrodes or coils are of relevance.

Originally, FieldTrip relied on the fact that the channel positions can be recovered from the electrode/coil positions by looking into the tra-matrix, because the tra-matrix specifies which electrode/coil contributes to which channel. However, FieldTrip supports increasingly complicated tra-matrices that for example include balancing coefficients (obtained through ft_denoise_synthetic, or ft_denoise_pca), projected-out spatial topographies (obtained through a sequence of ft_componentanalysis and ft_rejectcomponent), or synthetic planar gradients (obtained through ft_megplanar). With these increasingly complicated tra-matrices, recovery of the channel positions from the coil/electrode positions is not straightforward and sometimes impossible.
We decided to make the distinction between channels on the one hand, and electrodes/coils on the other hand explicit in the code.

### Some additional notes on the 'tra'-matrix

The tra-matrix is a very important piece of information that needs to be taken into account when building forward models (leadfields) for the sensor data in a given data structure. When building a forward model, we compute the magnetic/electric field distribution at the described sensors/electrodes in the data, given a known dipolar source. If the sensor data has been manipulated in any way - e.g. by creating higher order synthetic gradients by using additional information from the reference coils (as can be done with CTF MEG data with **[ft_denoise_synthetic](/reference/ft_denoise_synthetic)**, or with the custom CTF software), by using adaptive weights estimated from the data (as can be done with 4D-data, using custom software or **[ft_denoise_pca](/reference/ft_denoise_pca)**), or also when removing spatial topographies from the sensor data (using a combination of **[ft_componentanalysis](/reference/ft_componentanalysis)** and **[ft_rejectcomponent](/reference/ft_rejectcomponent)**) - the corresponding leadfields need to be manipulated in the same way, to keep the forward model consistent with the data. In FieldTrip this is achieved with the tra-matrix.

As the tra-matrix provides the recipe of how the individual electrodes/coils relate to the individual channels in the data structure, it is updated automatically upon manipulation of the sensor data in the following function

 **[ft_denoise_synthetic](/reference/ft_denoise_synthetic)**
 **[ft_denoise_pca](/reference/ft_denoise_pca)**
 **[ft_componentanalysis](/reference/ft_componentanalysis)**
 **[ft_rejectcomponent](/reference/ft_rejectcomponent)**

Algorithmically, the tra-matrix is used as a left multiplier of the unbalanced lead field (i.e. the leadfield that represents the magnetic field distribution at the location of the original magnetometer coils) in the following way: *lf_balanced = grad.tra * lf_unbalanced*. For example, to obtain a first-order axial gradiometer, each row in the tra-matrix contains two '1's (assuming the orientation of the top and bottom coils to be opposite), indicating that the modelled field estimated at the top and bottom coil of a gradiometer should be summed to obtain a model of the axial gradients. In order to obtain synthetic higher order gradients, the columns in the tra-matrix that correspond to the reference coils will have non-zero values, reflecting the 'balancing' coefficients.

In summary, if you are doing fancy things with your data, and later on want to do source reconstruction, it's not safe to just take any grad-structure to construct your leadfields with. For obvious reasons, not only do the positions of the coils need to be the same as the ones used during the measurement. Additionally, the tra-matrix needs to reflect all the manipulations you have applied to the data that you wish to source-reconstruct.
