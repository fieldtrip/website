---
title: Template anatomical atlases and parcellation schemes
layout: default
tags: [template]
toc: true
---

# Template anatomical atlases and parcellation schemes

An atlas is a volumetric or surface based description of the geometry of the brain, where each anatomical coordinate is labeled according to some scheme, e.g. as [Brodmann area](http://en.wikipedia.org/wiki/Brodmann_area). A recent review of brain templates and atlases is presented in [Brain templates and atlases (2012)](http://www.ncbi.nlm.nih.gov/pubmed/22248580) in NeuroImage.

In general an atlas can be read with **[ft_read_atlas](/reference/ft_read_atlas)**. It is represented as a volumetric segmentation as in **[ft_datatype_segmentation](/reference/ft_datatype_segmentation)**, or as a surface-based parcellation as in **[ft_datatype_parcellation](/reference/ft_datatype_parcellation)**. The volume based representation can be used with **[ft_volumelookup](/reference/ft_volumelookup)** or with the cfg.atlas option in **[ft_sourceplot](/reference/ft_sourceplot)**.

In the FieldTrip release, you can find the volumetric or surface based atlases in the fieldtrip/template/xxx directory, with XXX being the specific template (e.g. "aal" or "afni").
## The AFNI TTatlas+tlrc Dataset

This is a binary representation of the Talairach Tournoux atlas [ref 1]. It was digitized for the Talairach Daemon [ref 2] and converted into AFNI format. It is described in some detail on the [AFNI website](http://afni.nimh.nih.gov/afni/doc/misc/afni_ttatlas/). Note that the website seems to be unstable and relatively often unresponsive.

 1.  Talairach J, Tournoux P (1988). Co-planar stereotaxic atlas of the human brain. Thieme, New York. [Amazon](http://www.amazon.com/Co-Planar-Stereotaxic-Atlas-Human-Brain/dp/0865772932)
 2.  Lancaster JL, Rainey LH, Summerlin JL, Freitas CS, Fox PT, Evans AC, Toga AW, Mazziotta JC. *Automated labeling of the human brain: a preliminary report on the development and evaluation of a forward-transform method.* Hum Brain Mapp. 1997;5(4):238-42. [Pubmed](http://www.ncbi.nlm.nih.gov/pubmed/20408222)

 You can use the following snippet of code to get a quick idea of this atlases.


	>> afni = ft_read_atlas('fieldtrip/template/atlas/afni/TTatlas+tlrc.HEAD')

	afni =
	            dim: [161 191 141]
	            hdr: [1x1 struct]
	      transform: [4x4 double]
	           unit: 'mm'
	          coord: 'tal'
	         brick0: [161x191x141 uint8]
	    brick0label: {50x1 cell}
	         brick1: [161x191x141 uint8]
	    brick1label: {69x1 cell}

	>> imagesc(afni.brick0(:,:,70))

{% include image src="/assets/img/template/afni.png" width="400" %}

## The AAL atlas

The AAL atlas included with FieldTrip was downloaded from [here](http://www.gin.cnrs.fr/en/tools/aal-aal2/). The same atlas is also included in the SPM "WFU-PickAtlas" toolbox  with a slight difference in the format of the text file.

N. Tzourio-Mazoyer, B. Landeau, D. Papathanassiou, F. Crivello, O. Etard, N. Delcroix, B. Mazoyer, and M. Joliot. *Automated Anatomical Labeling of Activations in SPM Using a Macroscopic Anatomical Parcellation of the MNI MRI Single-Subject Brain.* NeuroImage 2002. 15:273-289.


	>> aal = ft_read_atlas('fieldtrip/template/atlas/aal/ROI_MNI_V4.nii')

	aal =
	            dim: [91 109 91]
	            hdr: [1x1 struct]
	      transform: [4x4 double]
	           unit: 'mm'
	         tissue: [91x109x91 double]
	    tissuelabel: {1x116 cell}    

	>> imagesc(aal.tissue(:,:,45))

{% include image src="/assets/img/template/aal.png" width="400" %}

## The BrainWeb Dataset

Using the normal anatomical model downloaded from the [BrainWeb](http://www.bic.mni.mcgill.ca/brainweb/) website we constructed a discrete and fuzzy segmentation of the human head in 9 tissue types.

The segmentation is defined at a 1 mm isotropic voxel grid in Talairach space, with dimensions 181x217x181 (XxYxZ) and start coordinates -90,-126,-72 (x,y,z).

The discrete model is represented in a MATLAB .mat file as

	>> load brainweb_discrete
	>> disp(segmentation)
	segmentation =
	            dim: [181 217 181]
	      transform: [4x4 double]
	           unit: 'mm'
	         tissue: [181x217x181 double]
	    tissuelabel: {'csf'  'grey_matter'  'white_matter'  'fat'  'muscle_and_skin'  'skin'  'skull'  'glial_matter'  'connective'}

The fuzzy model is represented in a MATLAB .mat file as

	>> load brainweb_fuzzy
	>> disp(segmentation)

	segmentation =
	                dim: [181 217 181]
	          transform: [4x4 double]
	               unit: 'mm'
	                csf: [181x217x181 double]
	        grey_matter: [181x217x181 double]
	       white_matter: [181x217x181 double]
	                fat: [181x217x181 double]
	    muscle_and_skin: [181x217x181 double]
	               skin: [181x217x181 double]
	              skull: [181x217x181 double]
	       glial_matter: [181x217x181 double]
	         connective: [181x217x181 double]
	         background: [181x217x181 double]

Both discrete and fuzzy model are consistent with the data representation descibed in **[ft_datatype_segmentation](/reference/ft_datatype_segmentation)**.

## The Eickhoff/Zilles/Amunts cytoarchitectonic atlas

This atlas is the same one as the on implemented in SPM's anatomy toolbox. The version that is in FieldTrip was downloaded from [here](http://www.fz-juelich.de/inm/inm-1/DE/Forschung/_docs/SPMAnatomyToolbox/SPMAnatomyToolbox_node.html).

The atlas and the toolbox are described in the publication belo

S.B. Eickhoff, K.E. Stephan, H. Mohlberg, C. Grefkes, G.R. Fink, K. Amunts, K. Zilles, *A new SPM toolbox for combining probabilistic cytoarchitectonic maps and functional imaging data*, NeuroImage, Volume 25, Issue 4, 1 May 2005, Pages 1325-1335.


	>> atlas = ft_read_atlas('fieldtrip/template/atlas/spm_anatomy/AllAreas_v17_MPM')

	atlas =
	            dim: [151 188 154]
	            hdr: [1x1 struct]
	      transform: [4x4 double]
	           unit: 'mm'
	         tissue: [151x188x154 double]
	    tissuelabel: {67x1 cell}
	       coordsys: 'spm'    


Besides the 'v17' version, the 'v18' is also supported.

## The VTPM Atlas

The VTPM atlas was downloaded from [here](http://www.princeton.edu/~napl/vtpm.htm).The atlas was constructed from a population of 53 subjects and contains probabilistic maps for 22 visual areas. The version of the atlas included with FieldTrip was created by transforming data into standardized space using surface-based anatomical registration approaches.

The atlas is described in the publication belo

Wang L, Mruczek REB, Arcaro MJ, Kastner S. (2015) Probabilistic Maps of Visual Topography in Human
Cortex. Cerebral Cortex. 25: 3911-3931


	>> load ('fieldtrip/template/atlas/vtpm.mat')

	vtpm =

	            dim: [182 218 182]
	            hdr: [1x1 struct]
	      transform: [4x4 double]
	           unit: 'mm'
	    tissuelabel: {1x50 cell}
	         tissue: [182x218x182 double]
	       coordsys: 'mni'    

	figure;
	subplot(2,2,1);imagesc(vtpm.tissue(:,:,70))
	subplot(2,2,2);imagesc(vtpm.tissue(:,:,80))
	subplot(2,2,3);imagesc(vtpm.tissue(:,:,90))
	subplot(2,2,4);imagesc(vtpm.tissue(:,:,100))

{% include image src="/assets/img/template/vtpm.png" width="400" %}

## The Brainnetome Atlas

The Brainnetome Atlas is designed to study activation and connectivity. Each hemisphere is subdivided into 123 subregions and the parcellation is based on both structural and functional connectivity features. More information can be found [here](http://atlas.brainnetome.org/).

The atlas is described in the publication belo

Fan, L., Li, H., Zhuo, J., Zhang, Y., Wang, J., Chen, L., Yang, Z., Chu, C., Xie, S., Laird, A.R., Fox, P.T., Eickhoff, S.B., Yu, C. & Jiang, T. The Human Brainnetome Atlas: A New Brain Atlas Based on Connectional Architecture. Cerebral Cortex, 26 (8): 3508-3526,(2016)

In FieldTrip, the atlas is included as a nifti file, complemented with a text file with the tissue labels. You can read it like thi


	brainnetome = ft_read_atlas('template/atlas/brainnetome/BNA_MPM_thr25_1.25mm.nii')

	brainnetome =

	            dim: [145 173 145]
	            hdr: [1x1 struct]
	      transform: [4x4 double]
	           unit: 'mm'
	         tissue: [145x173x145 double]
	       coordsys: 'mni'
	    tissuelabel: {1x246 cell}

	imagesc(brainnetome.tissue(:,:,68))

{% include image src="/assets/img/template/brainnetome_atlas2.png" width="400" %}

## References

*  http://www.bic.mni.mcgill.ca/brainweb/
*  C.A. Cocosco, V. Kollokian, R.K.-S. Kwan, A.C. Evans : "BrainWeb: Online Interface to a 3D MRI Simulated Brain Database" NeuroImage, vol.5, no.4, part 2/4, S425, 1997 -- Proceedings of 3-rd International Conference on Functional Mapping of the Human Brain, Copenhagen, May 1997.
*  R.K.-S. Kwan, A.C. Evans, G.B. Pike : "MRI simulation-based evaluation of image-processing and classification methods" IEEE Transactions on Medical Imaging. 18(11):1085-97, Nov 1999.
*  R.K.-S. Kwan, A.C. Evans, G.B. Pike : "An Extensible MRI Simulator for Post-Processing Evaluation" Visualization in Biomedical Computing (VBC'96). Lecture Notes in Computer Science, vol. 1131. Springer-Verlag, 1996. 135-140.
*  D.L. Collins, A.P. Zijdenbos, V. Kollokian, J.G. Sled, N.J. Kabani, C.J. Holmes, A.C. Evans : "Design and Construction of a Realistic Digital Brain Phantom" IEEE Transactions on Medical Imaging, vol.17, No.3, p.463--468, June 1998.
*  S.B. Eickhoff, K.E. Stephan, H. Mohlberg, C. Grefkes, G.R. Fink, K. Amunts, K. Zilles, A new SPM toolbox for combining probabilistic cytoarchitectonic maps and functional imaging data, NeuroImage 25(4), 2005, 1325-1335.
*  Wang L, Mruczek REB, Arcaro MJ, Kastner S. (2015) Probabilistic Maps of Visual Topography in  Human Cortex. Cerebral Cortex. 25: 3911-3931
