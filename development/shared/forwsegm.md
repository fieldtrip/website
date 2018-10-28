---
title:
layout: default
---

- Assign a transformation matrix (voxels to mm/cm) and units to the volumetric images. This step is necessary to link the units in which the head sources are defined (for example expressed in cm and head coordinates) to the voxel based coordinate system.
- Reslice the CT volume in order to obtain homogeneous voxels (cubic). The reslice step accomplishes the task of having 3 equal edges (in the cartesian or voxel coordinates) for each voxel. This allows the application of morphological operators, which give a predictable outcome only in the case of cubic voxels.
- Segment the skull compartment (smooth/threshold volumetric operators). The skull compartment defines the boundary of the volume conductor (inner skull) and the scalp boundary (outer skull). This geometrical information is used by the forward model.
- Obtain the filled volume of the inner skull (morphological  operators). The volumetric compartments can be easily tessellated (see [HERE](/#Triangulation methods)) if the volume is filled.
