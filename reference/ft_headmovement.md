---
title: ft_headmovement
---
```
 FT_HEADMOVEMENT creates a raw data structure, or cell-array of datastructures
 containing the HLC-coil data, which have a grad structure that has the
 head position information incorporated.

 Use as
   data = ft_headmovement(cfg)

 where the configuration should contain
   cfg.dataset      = string with the filename
   cfg.method       = 'updatesens' (default), 'cluster', 'avgoverrpt',
                        'pertrial_cluster', 'pertrial'

 optional arguments are
   cfg.trl          = empty (default), or Nx3 matrix with the trial 
                        definition, can be empty.see FT_DEFINETRIAL. If
                        defined empty, the whole recording is used
   cfg.numclusters  = number of segments with constant headposition in
                        which to split the data (default = 10). This
                        argument is used in some of the methods only (see
                        below), and is used in a kmeans clustering scheme.

 If cfg.method = 'updatesens', the grad in the single output structure has
 a specification of the coils expanded as per the centroids of the position
 clusters. The balancing matrix is s a weighted concatenation of the
 original tra-matrix. This method requires cfg.numclusters to be specified

 If cfg.method = 'avgoverrpt', the grad in the single output structure has
 a specification of the coils according to the average head position
 across the specified samples.

 If cfg.method = 'cluster', the cell-array of output structures represent
 the epochs in which the head was considered to be positioned close to the
 corresponding kmeans-cluster's centroid. The corresponding grad-structure
 is specified according to this cluster's centroid. This method requires
 cfg.numclusters to be specified.

 If cfg.method = 'pertrial', the cell-array of output structures contains
 single trials, each trial with a trial-specific grad structure. Note that
 this is extremely memory inefficient with large numbers of trials, and
 probably an overkill.

 If cfg.method = 'pertrial_clusters', the cell-array of output structures
 contains sets of trials where the trial-specific head position was
 considered to be positioned close to the corresponding kmeans-cluster's
 centroid. The corresponding grad-structure is specified accordin to the
 cluster's centroid. This method requires cfg.numclusters to be specified.

 The updatesens method and related methods are described by Stolk et al., Online and
 offline tools for head movement compensation in MEG. NeuroImage, 2012.

 See also FT_REGRESSCONFOUND FT_REALTIME_HEADLOCALIZER
```
