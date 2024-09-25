---
title: 07 May 2020 - Code update, the default SPM version is now spm12  
category: news
---

### 07 May 2020

During the recent [toolkit](/workshop/toolkit2020), which took place online, the participants worked on their own computers, causing a larger than usual variability on MATLAB versions and Operating Systems. One issue we encountered was a compatibility problem with SPM-related mex-files. Specfically, when using the default version, which up until now has been spm8, certain functions did not work. We are typically reluctant to change default behavior of functions, but now we decided to upgrade the default SPM version to spm12, for a more stable user experience overall. We expect this change to be inconsequential for most of you, but would like to note that, when needed, you can always go back to using spm8, by specifying cfg.spmversion='spm8', wherever appropriate. Note that cfg.spmversion is only a supported option for the high-level fieldtrip functions.
