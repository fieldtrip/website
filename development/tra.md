---
title: Resolution: see faq
layout: default
---

 <div class="alert-danger">
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
</div>

# Resolution: see faq

*  [faq/how_are_electrodes_magnetometers_or_gradiometers_described](/faq/how_are_electrodes_magnetometers_or_gradiometers_described)

# Original plan: document grad.tra

*  What is .tra?   NxM matrix with the weight of each coil into each channel.  (addressed in FAQ)

*  .tra is usually in grad.tra but may also be in elec.tra if a montage was applied. (addressed in FAQ)

*  When does grad.tra get modified? (ft_componentanalysis, ft_apply_montage)

*  It is important to compute lead field after all modifications to grad.tra are made (addressed in FAQ)

*  Effects on inverse methods: if data is reduced rank after ICA/PCA etc, how does this affect regularization strategies?  Should defaults of regularization in ft_sourceanalysis be modified?

*  Direct various pages on artifact rejection and sourceanalysis to this grad.tra page

*  How is it recommended that user gets a data.trial that is 3rd-order gradient corrected (not just data.grad.tra updated)?  Call ft_apply_montage directly, or via ft_denoise_synthetic?  

*  What is the difference between G3BR and G3AR?  (some data read in gives error that G3AR coefficients could not be found.  tip from Sarang: 'A' is for 'adaptive' which was probably only ever in beta-version with CTF when they existed) (This sounds like a personal question from Johanna, since G3AR is hardly used/present, I'd suggest not to wake sleeping dogs.) 

*  show examples of how grad.tra is for different systems, especially Neuromag

