---
title: ft_reproducescript
---
```
 FT_REPRODUCESCRIPT is a helper function to clean up the script and intermediate
 datafiles that are the result from using the cfg.reproducescript option. You should
 call this function all the way at the end of your analysis. This function will look
 at all intermediate files in the output directory, remove input and output files
 that are the same and update the script accordingly.

 Use as
   ft_reproducescript(cfg)

 The configuration structure should contain
   cfg.reproducescript = string, directory with the script and intermediate data

 See also FT_ANALYSISPIPELINE, FT_DEFAULTS
```
