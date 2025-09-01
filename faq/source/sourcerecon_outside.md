---
title: Is it good or bad to have dipole locations outside of the brain for which the source reconstruction is computed?
category: faq
tags: [source]
redirect_from:
    - /faq/is_it_good_or_bad_to_have_dipole_locations_outside_of_the_brain_for_which_the_source_reconstruction_is_computed/
    - /faq/sourcerecon_outside/
---

This depends on the type of source reconstruction you are performing, and on the head model (also called volume conduction model) with which you create your source model (also called grid). Depending on this it is beneficial in some cases, but harmful in others. To determine whether it is harmful, one could ask the following question

1.  is my source reconstruction of locations inside the brain affected by the source reconstruction of other locations? (e.g., with minimum norm estimate (MNE) based methods, but not with beamformers)
2.  can my head model create meaningful lead fields for dipole locations that fall outside of the brain? (e.g., with 'singleshell/singlesphere/localsphere' models, but not with boundary element models (BEM))

If the answer the first question is 'Yes', then it can be harmful. If the answer to the second question is 'No', the results are not meaningful at these locations. If the answer the first question is 'No', and the answer to the second question is 'Yes', then it can be beneficial. Below some examples.

## Single shell head model used for a beamformer-type source reconstruction

In this case, the head and source models are created with the intent of using a beamformer-type source reconstruction. As indicated by the red dots in the figure below, there are many dipoles for which the source reconstruction will be performed (i.e. they are labeled as 'inside'), but which do not fall inside the head. The source estimate at these location is interesting, because they can be used to identify e.g., muscle activity. Muscle activity in muscles at the back of the head would show increasing power towards the back of the brain, and will continue to increase in power passed the skull boundary. If power at these out-of-brain locations is not reconstructed, then it (muscle activity) could mistakingly be interpreted as activity in primary visual areas.

{% include image src="/assets/img/faq/sourcerecon_outside/singleshelldipolelocations.png" width="400" %}

_Dipole locations of a source model plotted with on top of a singleshell head model. Dipole locations marked as 'inside' are red, dipole locations marked as 'outside' are blue._

## Single sphere head model

In this example, a single sphere is used as a head model. The brain however, is not spherical. If we want to prevent brain areas to be missed in source reconstruction, a sphere is needed with a radius that is at least equal to the longest distance between any two points in the brain. Such a situation is depicted in the figure below. Here, the sphere is large enough to encompass the entire brain, and will therefore have many dipole locations which are not inside the brain (e.g., near temporal cortex).

{% include image src="/assets/img/faq/sourcerecon_outside/singlespheredipolelocations.png" %}

_Dipole locations of a source model plotted with on top of a 'singlesphere' head model. Inside the sphere, the 'singleshell' head model in the above figure is plotted as well, to indicate the shape of the brain inside the sphere. Dipole locations marked as 'inside' are red, dipole locations marked as 'outside' are blue._

## Local spheres head model

In this case, it ain't working! Robert, I forgot why specifically. Is this because of the lead fields not being meaningful for locations where there isn't a 'local sphere'? Or am I confusing this with BEM? Could you add something here?
