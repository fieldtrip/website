---
title: How can I fix a corrupt CTF res4 header file?
category: faq
tags: [corrupt, ctf, raw]
---

# How can I fix a corrupt CTF res4 header file?

If the .res4 file of your dataset is corrupt, you can recreate it by copying an intact .res4 file of another comparable dataset and give it the proper name. Subsequently, you can use the changeHeadPos utility to change the head localization parameters to match those of your subject. This requires that the .hc file is intact. If the .hc file is also corrupt, you first will have to recreate that file using the hz.ds and hz2.ds headlocalizer measurements.
