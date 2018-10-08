---
layout: default
---

{{tag>faq headmodel source}}

## What kind of volume conduction models of the head (head models) are implemented?

The volume conduction model of the head is an important ingredient for source analysis, since it determines how a source within the brain is visible on the EEG or MEG sensors. All forward and inverse computations that are done within Fieldtrip share the same low-level code for the computation of the forward model potential or field. Since the volume conduction model depends on the geometry of the head, you have to provide anatomical data on which the geometry can be based. The most commonly used anatomical data is an anatomical MRI.

FieldTrip supports the following common volume conduction models for EE

*  single sphere

*  multiple concentric spheres with up to 4 shells

*  boundary element model (dipoli, bemcp)

*  finite element model (simbio)

and the following common volume conduction models for ME

*  single sphere

*  multiple spheres that are fitted locally to the head underneath each sensor

*  realistic single-shell model based on leadfield expansion (Nolte method)

Besides these volume conduction models which are for general use on EEG and MEG data, there are a number of models implemented that are more experimental, still not 100% complete, or that are very specific for uncommon applications, e.g. for a laminar probe in the cortex, or magnetic dipoles (MEG localizer coils).

For more information on the methods, you can also check the reference documentation of **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** and the [References to implemented methods](/references_to_implemented_methods#eeg_and_meg_forward_modeling) related to forward modeling.

If you wish, you can also use a forward model for which you have computed the leadfield matrices outside of fieldtrip in combination with the inverse source reconstruction algorithms that are implemented within FieldTrip. Some matlab code that demonstrates how to do it can be found [in this example](/example/use_your_own_forward_leadfield_model_in_an_inverse_beamformer_computation).

