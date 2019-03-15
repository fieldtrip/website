---
title: Template head models for forward volume conduction modeling
tags: [template]
---

## Template head models for forward volume conduction modeling

Volume conduction models of the head are a necessary ingredient for source reconstruction. Sources are typically modelled as equivalent current dipoles (ECDs), i.e. point sources with a location and orientation. These sources produce an electrical current that flows through all surrounding tissue. The geometrical and conductive aspects of the tissue influence how the source becomes visible in the EEG or MEG.

{% include markup/warning %}
You can find the template head models included in FieldTrip [here](https://github.com/fieldtrip/fieldtrip/tree/master/template/headmodel).
{% include markup/end %}

### standard_bem

This file contains a standard Boundary Element Method volume conduction model of the head that can be used for EEG forward and inverse computations. The geometry is based on the "colin27" template that is described further down. The BEM model is expressed in MNI coordinates in mm.

The BEM model is based on the segmentation from [BrainWeb: Anatomical Model of Normal Brain](http://brainweb.bic.mni.mcgill.ca/brainweb/anatomic_normal.html). Its construction is detailled in [Oostenveld R, Stegeman DF, Praamstra P, van Oosterom A. Brain symmetry and topographic analysis of lateralized event-related potentials. Clin Neurophysiol. 2003 Jul;114(7):1194-202.](http://www.ncbi.nlm.nih.gov/pubmed/12842715) Please cite this reference if you use this template volume conduction model in your analyses.

Accompanying electrode positions according to the 10-20, the 10-10 and the 10-5 standards (with different naming schemes) can be found in the template/electrode directory.

A very similar BEM volume conduction model (based on the same template data) is described and validated by Fuchs et al. in [Clin Neurophysiol. 2002 May;113(5):702-12.](http://www.ncbi.nlm.nih.gov/pubmed/11976050)

### standard_mri

The "colin27" anatomical MRI and its relation to the TT and MNI template atlas is described in detail on http://imaging.mrc-cbu.cam.ac.uk/imaging/MniTalairach


  One of the MNI lab members, Colin Holmes, was scanned 27 times, and
  the scans were coregistered and averaged to create a very high
  detail MRI dataset of one brain. This average was also matched to
  the MNI305, to create the image known as "colin27". colin27 is used
  in the MNI brainweb simulator. SPM96 used colin27 as its standard
  template. [...] SPM96 and later contains a 2mm resolution copy of
  the same image, in the canonical directory of the SPM distribution.
  In SPM96 this is called T1 in later distributions it is called
  single_subj_T1.

The original construction of the averaged MRI is detailed in
[[http://www.ncbi.nlm.nih.gov/pubmed/9530404|
Holmes CJ, Hoge R, Collins L, Woods R, Toga AW, Evans AC.
Enhancement of MR images using registration for signal averaging.
J Comput Assist Tomogr. 1998 Mar-Apr;22(2):324-33.]]

##### revision information

Up to r7413 (Jan 2013) the file content corresponded to the original anatomical
MRI. From r7414 onwards the anatomical MRI  was updated with private/volumeedit to remove the aliasing effect that resulted in the volume to contain segmentation-corrupting data very close to the top of the head.

As of August 23, 2018, the hdr-field has been removed from the data structures in standard_mri, and standard_seg. This was done because there was confusing information in these hdrs, which was inconsistent with the volumetric image (transformation matrices and fiducial locations).
###  skin

This directory contains a triangulated high-resolution geometrical description of the skin surface. This skin surface is not used in the BEM model itself for computational reasons, but can be used for visualization. It is expressed in MNI coordinates in mm.  

You can visualize it with


  >> skin = ft_read_headshape('standard_skin_14038.vol')

  skin =
       pnt: [14038x3 double]
       fid: [1x1 struct]
       tri: [28072x3 double]
      unit: 'mm'

  >> ft_plot_mesh(skin, 'edgecolor', 'none', 'facecolor', 'skin')
  >> camlight

{% include image src="/assets/img/template/headmodel/headmodel_skin.png" width="300" %}
