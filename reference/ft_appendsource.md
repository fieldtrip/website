---
title: ft_appendsource
---
```
 FT_APPENDSOURCE concatenates multiple volumetric source reconstruction data
 structures that have been processed separately.

 Use as
   combined = ft_appendsource(cfg, source1, source2, ...)

 If the source reconstructions were computed for different ROIs or different slabs
 of a regular 3D grid (as indicated by the source positions), the data will be
 concatenated along the spatial dimension.

 If the source reconstructions were computed on the same source positions, but for
 different frequencies and/or latencies, e.g. for time-frequency spectrally
 decomposed data, the data will be concatenared along the frequency and/or time
 dimension.

 See also FT_SOURCEANALYSIS, FT_DATATYPE_SOURCE, FT_APPENDDATA, FT_APPENDTIMELOCK,
 FT_APPENDFREQ
```
