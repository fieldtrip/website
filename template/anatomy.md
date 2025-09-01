---
title: Anatomical templates for visualizing source reconstructed activity
tags: [template]
---

When visualizing source reconstructed activity, one can interpolate the activity maps onto a subject-specific anatomical image, using [ft_sourceinterpolate](/reference/ft_sourceinterpolate). Subsequently, the interpolated activity can be spatially normalized (using volumetric normalization) using [ft_volumenormalise](/reference/ft_volumenormalise). The activity can also be rendered onto the cortical surface. FieldTrip includes a set of template surfaces that have been derived from the "colin27" brain (in MNI152 space) with FreeSurfer. These surfaces have been derived from the SPM Canonical Brain.

{% include markup/yellow %}
You can find the anatomical templates included in FieldTrip [here](https://github.com/fieldtrip/fieldtrip/tree/master/template/anatomy).
{% include markup/end %}

## High resolution triangulations of the neocortical sheet

The FreeSurfer cortical sheets can be downloaded from the [SurfRend toolbox website](http://spmsurfrend.sourceforge.net/). The mat-files that are in FieldTrip have been obtained using [ft_read_headshape](/reference/fileio/ft_read_headshape). The following sheets are included:

- surface defined at the gray/white matter boundary: surface_white_both/left/right.
- surface defined at the pial surface: surface_pial_both/left/right.
- inflated surface: surface_inflated_both/left/right.
- inflated surface generated with Caret (added May 26, 2014 using the command caret_command -surface-generate-inflated), preserving the main sulcal structure: surface_inflate_both/left/right_caret.

{% include markup/red %}
FieldTrip versions 9031-9400 (Dec 13, 2013 - April 12, 2014) contain the surfaces in an incorrect coordinate system. The consequence of this is that the on-the-fly interpolation and rendering of source reconstructed data onto the cortical sheets (using ft_sourceplot) was incorrect. This has been fixed in revision 9401. The figures below show an overlay of the current (r.9401) cortical sheet surface_white_both with the single_subj_T1_1mm.nii. The incorrect coordinate system was due to not taking into account that the original surfaces were expressed in the FreeSurfer coordinate system. The correction that had to be taken into account was the xfm matrix in spm_CanonicalBrain from the spm-surfrend toolbox.
{% include markup/end %}

{% include image src="/assets/img/template/anatomy/surface_white_both.png" width="600" %}

## Volumetric anatomical image at 1mm isotropic resolution

The volumetric image `fieldtrip/template/anatomy/single_subj_T1_1mm.nii` is the "colin27" brain at 1 mm resolution downloaded from <http://www.bic.mni.mcgill.ca/ServicesAtlases/Colin27>.

## Volumetric anatomical image at 2mm isotropic resolution

The volumetric image `fieldtrip/template/anatomy/single_subj_T1.nii` is a downsampled version of single_subj_T1_1mm.nii, obtained with [ft_volumedownsample](/reference/ft_volumedownsample), using cfg.downsample=2. The anatomical volume was written back to disk, using [ft_volumewrite](/reference/ft_volumewrite).
