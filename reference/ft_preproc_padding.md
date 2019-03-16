---
title: ft_preproc_padding
---
```
 FT_PREPROC_PADDING performs padding on the data, i.e. adds or removes samples
 to or from the data matrix.

 Use as
   [dat] = ft_preproc_padding(dat, padtype, padlength)
 or as
   [dat] = ft_preproc_padding(dat, padtype, prepadlength, postpadlength)
 where
   dat           data matrix (Nchan x Ntime)
   padtype       'zero', 'mean', 'localmean', 'edge', 'mirror', 'nan' or 'remove'
   padlength     scalar, number of samples that will be padded
   prepadlength  scalar, number of samples that will be padded before the data
   postpadlength scalar, number of samples that will be padded after the data

 If padlength is used instead of prepadlength and postpadlength, padding
 will be symmetrical (i.e. padlength = prepadlength = postpadlength)

 See also FT_PREPROCESSING
```
