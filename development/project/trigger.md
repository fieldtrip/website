---
title: Consistent flank detection for triggers
---

{% include /shared/development/warning.md %}

The read_event used to have multiple re-implementations of flank detection for trigger channels, i.e. for multiple file formats (4d, bdf, fif, ctf, neuralynx). This has recently (2008/04/29) been changed by introducing a read_trigger helper function, which is used for neuromag, bti and ctf.

It is not yet used for biosemi, and it also has not yet replaced the read_ctf_trigger function. This should still be done.

Issues to be solved in the flank detection

- multiple trigger channels (OK)
- downgoing flank also interesting (OK)
- triggers sitting on top of each other (OK)
- should be combined with read_data instead of using file format specific reading functions (OK)
- bitmasking of single channel for multiple meanings (bdf-status, ctf151-back/front)
- slow rise of flank, i.e. value should be detected a few samples later
- consistent naming of triggers, but also backward compatibility
