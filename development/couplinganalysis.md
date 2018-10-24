---
layout: default
---

`<note warning>`

The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

The code development project mentioned on this page has been finished by now. Chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

Status: the connectivityanalysis and connectivitysimulation function have been implemented.

The goal is to create a multi-purpose function which takes raw/timelock/freq/source/mvar data as an input and computes coupling measures such as

 1.   coherence
 2.   coherency
 3.   correlation
 4.   any of the previous partial or multiple or canonical
 5.   cross-correlation
 6.   granger causality
 7.   partial directed coherence
 8.   directed transfer function
 9.   amplitude correlation
 10.   cross-frequency interactions

Furthermore create a simulator for

 1.  dipolesimulation
 2.  freqsimulation
 3.  connectivitysimulation

