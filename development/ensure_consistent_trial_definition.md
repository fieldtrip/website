---
layout: default
---

`<note warning>`
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

# Ensure consistent trial definition

There are certain functions that rely on the trl somwhere hidden in the config. After resampledata the trl is invalid. Simulated data also does not have a trl. No idea what appenddata does, but is probably also related...

All functions that take preprocessed/raw data as input should deal with this trl=problem in a consistent fashion. 

if th etrl is inconsistent with the data, it should be recreated. 

Tod

*  determine all functions that (optionally) take raw data as input

*  figure out how existing functions do it

*  implement consistent trl-recreation in all functions

Update (june 29, 2010

*  instead of relying on data.cfg.previous....trl, the trial information (when consistent with data representation, so only on the level of raw data, and in original sampling rate) should be directly on the main level of the structure.

*  this means that raw data should get a field trialdef containing the first 2 columns of the original trl-matrix (done: fixtrialdef and preprocessing).

*  the 3rd column of the trl matrix is the offset column and is represented in each trial's individual time axis.

*  user-defined columns > 3 should go to the field trialinfo. this field can percolate deeper into the pipeline. yet, once data is not raw datatype anymore (or resampled) the trialdef field should be removed, because consistency with the data is lost.

*  the trialdef and trialinfo fields will be updated by subselecting rows (done: selfromraw)

*  trialdef should be changed by ft_redefinetrial (done)

*  trialdef should be removed by ft_resampledata (done) and any other function working on the raw datatype and outputting any other datatype

*  trialdef and trialinfo should be concatenated in ft_appenddata (done)

