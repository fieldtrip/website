---
title:
layout: default
---

<div class="warning">
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
</div>

Goal: convert ft_connectivityanalysis into a module, to facilitate collaboration with Tim Mullen's EEGLAB connectivity module.
Action plan (from the FT side):

*  facilitate interaction with EEGLAB developers by providing more detailed information with respect to the datatypes (wiki)

*  reorganise the code a bit such that univariate2bivariate moves to checkdata.

*  move the connectivity computation subfunctions into subdirectory/module connectivity (done)

*  standardise the api to the connectivity subfunctions (done)

*  work with key/value pairs (done)
