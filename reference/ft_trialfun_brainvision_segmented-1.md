---
title: ft_trialfun_brainvision_segmented
---
```
 FT_TRIALFUN_BRAINVISION_SEGMENTED creates trials for a Brain Vision Analyzer
 dataset that was segmented in the BVA software.

 Use as 
   cfg          = [];
   cfg.dataset  = '<datasetname>.vhdr';
   cfg.trialfun = 'ft_trialfun_brainvision_segmented';
   cfg  = ft_definetrial(cfg);
   data = ft_preprocessing(cfg);

 Optionally, you can specify:
   cfg.stimformat = 'S %d'
 
 The stimformat instruct this function to parse stimulus triggers according to
 the specific format. The default is 'S %d'. The cfg.stimformat always
 needs to contain exactly one %d code. The trigger values parsed in this way
 will be stored in columns 4 and upwards of the output 'trl' matrix, and
 after FT_PREPROCESSING will end up in data.trialinfo.

 A BrainVision dataset consists of three files: an .eeg, .vhdr, and a .vmrk 
 file. The option cfg.dataset should refer to the .vhdr file.

 See also FT_DEFINETRIAL, FT_PREPROCESSING
```
