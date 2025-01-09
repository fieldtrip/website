---
title: Can I restrict the source reconstruction to the grey matter?
parent: Source reconstruction
category: faq
tags: [source, mri, headmodel]
redirect_from:
    - /faq/can_i_restrict_the_source_reconstruction_to_the_grey_matter/
---

# Can I restrict the source reconstruction to the grey matter?

Yes, there are two strategies you can use. You can either make a regular 3D grid spanning the whole brain in which only grid locations in grey matter are considered in the source estimation. The alternative is to construct a triangulated surface description of the cortical sheet.

## Constraining the 3D grid to gray matter

You can create a regularly spaced 3D grid with only dipoles in the grey matter. That is done in the **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)**, **[ft_prepare_leadfield](/reference/ft_prepare_leadfield)** or **[ft_sourceanalysis](/reference/ft_sourceanalysis)** functions.

It requires that you have a segmentation of your anatomical MRI, which specifies the different tissue types. Such a segmentation can be made from the anatomical MRI using **[ft_volumesegment](/reference/ft_volumesegment)** (which internally uses the SPM toolbox). The anatomical MRI and its segmentation have to be aligned to the coordinate system in which you want to perform the source reconstruction. That often means that the MRI should be expressed in MEG head coordinates.

If you want to use the canonical MRI that is included in SPM, you can also use the accompanying segmentation into the different tissue types. You can download the [anatomical](http://www.bic.mni.mcgill.ca/brainweb/selection_normal.html) 1mm MRI and the [segmentations](http://www.bic.mni.mcgill.ca/brainweb/anatomic_normal.html) from the MNI brainweb site. You should use the "crisp" segmentation for creating the grey matter volume. If you have SPM2 on your MATLAB path, the MINC file format will automatically be detected and supported by FieldTrip.

## Making a surface model of the cortical sheet

FieldTrip does not have its own methods for this, but relies on external software such as BrainVoyager or FreeSurfer. The [minumum-norm estimate tutorial](/tutorial/minimumnormestimate) has more details on this. You could also use the MATLAB [isosurface](http://www.mathworks.com/help/matlab/ref/isosurface.html) function on a segmented brain, although the resulting surface topology will not be as nice.
