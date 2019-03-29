---
title: nmt_peaksearch
---
```
 [vox_idx, t_idx] = nmt_peaksearch(cfg)
 cfg.time = single time point, or time range, or 'current'; if unspecified, search over time at specified voxel
 cfg.vox = find peak time at specified voxel, or 'current'; if unspecified, search over voxels at specified time
 cfg.peaktype = 'mag' (max magnitude, default) or 'max' or 'min'
 cfg.searchradius = minimum and maximum distance to search for peak
```
