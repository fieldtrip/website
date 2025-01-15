---
title: What kind of volume conduction models of the head (head models) are implemented?
parent: Source reconstruction
grand_parent: Frequently asked questions
category: faq
tags: [headmodel, source]
redirect_from:
    - /faq/what_kind_of_volume_conduction_models_are_implemented/
    - /faq/datatype_headmodel/
---

# What kind of volume conduction models of the head (head models) are implemented?

The volume conduction model of the head is an important ingredient for source analysis, since it determines how a source within the brain is visible on the EEG or MEG sensors. All forward and inverse computations that are done within FieldTrip share the same low-level code for the computation of the forward model potential or field. Since the volume conduction model depends on the geometry of the head, you have to provide anatomical data on which the geometry can be based. The most commonly used anatomical data is an anatomical MRI.

FieldTrip supports the following common volume conduction models for EEG:

- infinite homogenous medium
- infinite halfspace
- single sphere
- multiple concentric spheres with up to 4 shells
- boundary element model (dipoli, bemcp, openmeeg)
- finite element model (simbio)

and the following common volume conduction models for MEG:

- infinite homogenous medium
- single sphere
- multiple spheres that are fitted locally to the head underneath each sensor
- realistic single-shell model based on leadfield expansion
- boundary element model (openmeeg)
- finite element model (duneneuro)

Besides these volume conduction models for use on actual measured EEG and MEG data, there are a number of models implemented that are more experimental, still not 100% complete, or that are very specific for uncommon applications, e.g., for a laminar LFP probe in the cortex, or for magnetic dipoles that correspond to MEG head localizer coils.

For more information on the methods, you can also check the reference documentation of **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** and the section in the [references to implemented methods](/references_to_implemented_methods#eeg-and-meg-forward-modeling) page that is related to forward modeling.

If you wish, you can also use a forward model for which you have computed the leadfield matrices yourself outside of FieldTrip. This can then be combined with the inverse source reconstruction algorithms that are implemented in FieldTrip. Some MATLAB code that demonstrates how to do it can be found [in this example](/example/use_your_own_forward_leadfield_model_in_an_inverse_beamformer_computation).
