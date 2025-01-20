---
title: How can I fix a corrupt CTF res4 header file?
parent: Specific data formats
grand_parent: Reading and preprocessing data
category: faq
tags: [corrupt, ctf, raw]
redirect_from:
    - /faq/how_can_i_fix_a_corrupt_ctf_res4_header_file/
    - /faq/ctf_fixres4/
---

# How can I fix a corrupt CTF res4 header file?

If the .res4 file of your dataset is corrupt, you can recreate it by copying an intact .res4 file of another comparable dataset and give it the proper name. Subsequently, you can use the changeHeadPos utility to change the head localization parameters to match those of your subject. This requires that the .hc file is intact. If the .hc file is also corrupt, you first will have to recreate that file using the hz.ds and hz2.ds headlocalizer measurements.
