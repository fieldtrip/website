---
title: Template anatomical atlases and parcellation schemes
tags: [template, atlas]
---

# Template anatomical atlases and parcellation schemes

An atlas is a volumetric or surface based description of the geometry of the brain, where each anatomical coordinate is labeled according to some scheme, e.g., as [Brodmann area](https://en.wikipedia.org/wiki/Brodmann_area). A review of brain templates and atlases is presented in [Brain templates and atlases (2012)](http://www.ncbi.nlm.nih.gov/pubmed/22248580) in NeuroImage.

In general an atlas can be read with **[ft_read_atlas](/reference/fileio/ft_read_atlas)**. It is represented as a volumetric segmentation as in **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)**, or as a surface-based parcellation as in **[ft_datatype_parcellation](/reference/utilities/ft_datatype_parcellation)**. The volume based representation can be used with **[ft_volumelookup](/reference/ft_volumelookup)** or with the cfg.atlas option in **[ft_sourceplot](/reference/ft_sourceplot)**.

In the FieldTrip release, you can find the volumetric or surface based atlases in the fieldtrip/template/xxx directory, with XXX referring to a specific template (e.g., "aal" or "afni").

{% include markup/warning %}
You can find the template anatomical atlases and parcellation schemes included in FieldTrip [here](https://github.com/fieldtrip/fieldtrip/tree/master/template/atlas).
{% include markup/end %}

## The AFNI TTatlas+tlrc Dataset

This is a binary representation of the Talairach Tournoux atlas [ref 1]. It was digitized for the Talairach Daemon [ref 2] and converted into AFNI format. It is described in some detail on the [AFNI website](https://sscc.nimh.nih.gov/afni/doc/misc/afni_ttatlas/index_html). Note that the website seems to be unstable and relatively often unresponsive. Next to the template that is shipped with FieldTrip, it is also possible to load in other atlases that are defined in AFNI format. For instance, the atlases that can be obtained from [here](https://afni.nimh.nih.gov/pub/dist/atlases/).

1.  Talairach J, Tournoux P (1988). Co-planar stereotaxic atlas of the human brain. Thieme, New York. [Amazon](http://www.amazon.com/Co-Planar-Stereotaxic-Atlas-Human-Brain/dp/0865772932)
2.  Lancaster JL, Rainey LH, Summerlin JL, Freitas CS, Fox PT, Evans AC, Toga AW, Mazziotta JC. _Automated labeling of the human brain: a preliminary report on the development and evaluation of a forward-transform method._ Hum Brain Mapp. 1997;5(4):238-42. [Pubmed](http://www.ncbi.nlm.nih.gov/pubmed/20408222)

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

{% include image src="/assets/img/template/atlas/afni.png" width="400" %}

## The AAL atlas

The AAL atlas included with FieldTrip was downloaded from [here](http://www.gin.cnrs.fr/en/tools/aal-aal2/). The same atlas is also included in the SPM "WFU-PickAtlas" toolbox with a slight difference in the format of the text file.

N. Tzourio-Mazoyer, B. Landeau, D. Papathanassiou, F. Crivello, O. Etard, N. Delcroix, B. Mazoyer, and M. Joliot. _Automated Anatomical Labeling of Activations in SPM Using a Macroscopic Anatomical Parcellation of the MNI MRI Single-Subject Brain._ NeuroImage 2002. 15:273-289.

    >> aal = ft_read_atlas('fieldtrip/template/atlas/aal/ROI_MNI_V4.nii')

    aal =
              dim: [91 109 91]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
           tissue: [91x109x91 double]
      tissuelabel: {1x116 cell}

    >> imagesc(aal.tissue(:,:,45))

{% include image src="/assets/img/template/atlas/aal.png" width="400" %}

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

Both discrete and fuzzy model are consistent with the data representation descibed in **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)**.

## The Eickhoff/Zilles/Amunts cytoarchitectonic atlas

This atlas is the same one as the on implemented in SPM's anatomy toolbox. The version that is in FieldTrip was downloaded from [here](http://www.fz-juelich.de/inm/inm-1/DE/Forschung/_docs/SPMAnatomyToolbox/SPMAnatomyToolbox_node.html).

The atlas and the toolbox are described in the publication belo

S.B. Eickhoff, K.E. Stephan, H. Mohlberg, C. Grefkes, G.R. Fink, K. Amunts, K. Zilles, _A new SPM toolbox for combining probabilistic cytoarchitectonic maps and functional imaging data_, NeuroImage, Volume 25, Issue 4, 1 May 2005, Pages 1325-1335.

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

The VTPM atlas was downloaded from [here](http://www.princeton.edu/~napl/vtpm.htm).The atlas was constructed from a population of 53 subjects and contains probabilistic maps for 25 visual areas. The version of the atlas included with FieldTrip was created by the authors of the original paper, by transforming data into standardized space using surface-based anatomical registration approaches, and subsequently assigning a voxel-wise label based on a maximum probability criterion. For convenience, the version of the atlas that is distributed with FieldTrip has the original left and right hemispheres merged in a single file. One known issue is the absence of the right IPS5 parcel.

The atlas is described in the publication below

Wang L, Mruczek REB, Arcaro MJ, Kastner S. (2015) Probabilistic Maps of Visual Topography in Human
Cortex. Cerebral Cortex. 25: 3911-3931

    >> load ('fieldtrip/template/atlas/vtpm.mat')
    >> disp(vtpm)
    
    vtpm =
              dim: [182 218 182]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
      tissuelabel: {50x1 cell}
           tissue: [182x218x182 double]
         coordsys: 'mni'

    >> figure;
    >> subplot(2,2,1);imagesc(vtpm.tissue(:,:,70))
    >> subplot(2,2,2);imagesc(vtpm.tissue(:,:,80))
    >> subplot(2,2,3);imagesc(vtpm.tissue(:,:,90))
    >> subplot(2,2,4);imagesc(vtpm.tissue(:,:,100))

{% include image src="/assets/img/template/atlas/vtpm.png" width="400" %}

## The Brainnetome Atlas

The Brainnetome Atlas is designed to study activation and connectivity. Each hemisphere is subdivided into 123 subregions and the parcellation is based on both structural and functional connectivity features. More information can be found [here](http://atlas.brainnetome.org/).

The atlas is described in the publication below

Fan, L., Li, H., Zhuo, J., Zhang, Y., Wang, J., Chen, L., Yang, Z., Chu, C., Xie, S., Laird, A.R., Fox, P.T., Eickhoff, S.B., Yu, C. & Jiang, T. The Human Brainnetome Atlas: A New Brain Atlas Based on Connectional Architecture. Cerebral Cortex, 26 (8): 3508-3526,(2016)

In FieldTrip, the atlas is included as a nifti file, complemented with a text file with the tissue labels. You can read it like this:

    >> brainnetome = ft_read_atlas('template/atlas/brainnetome/BNA_MPM_thr25_1.25mm.nii')
    
    brainnetome =
              dim: [145 173 145]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
           tissue: [145x173x145 double]
         coordsys: 'mni'
      tissuelabel: {1x246 cell}

    >> imagesc(brainnetome.tissue(:,:,68))

{% include image src="/assets/img/template/atlas/brainnetome_atlas2.png" width="400" %}


## The Yeo Atlases

The Yeo Atlases are designed to study intrinsic functional connectivity. Each hemisphere is subdivided into either 7 or 17 functionally coupled regions across the cerebral cortex. More information can be found [here](https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation_Yeo2011). The atlases included with FieldTrip were created by transforming Yeo2011_7Networks_MNI152_FreeSurferConformed1mm.nii.gz and Yeo2011_17Networks_MNI152_FreeSurferConformed1mm.nii.gz into standardized space (single_subj_T1_1mm) using volume-based anatomical registration approaches.

The atlases are described in the publication below

Yeo BT, Krienen FM, Sepulcre J, Sabuncu MR, Lashkari D, Hollinshead M, Roffman JL, Smoller JW, Zollei L., Polimeni JR, Fischl B, Liu H, Buckner RL. The organization of the human cerebral cortex estimated by intrinsic functional connectivity. J Neurophysiol 106(3):1125-65, 2011.

In FieldTrip, the two atlases are included as nifti files. You can read them like this:

    >> yeo7 = ft_read_atlas('/template/atlas/yeo/Yeo2011_7Networks_MNI152_FreeSurferConformed1mm_LiberalMask_colin27.nii')
        
    yeo7 =
            dim: [256 256 256]
            hdr: [1x1 struct]
      transform: [4x4 double]
           unit: 'mm'
         tissue: [256x256x256 double]
    tissuelabel: {7x1 cell}
       coordsys: 'mni'

    >> yeo17 = ft_read_atlas('/template/atlas/yeo/Yeo2011_17Networks_MNI152_FreeSurferConformed1mm_LiberalMask_colin27.nii')
    
    yeo17 =
            dim: [256 256 256]
            hdr: [1x1 struct]
      transform: [4x4 double]
           unit: 'mm'
         tissue: [256x256x256 double]
    tissuelabel: {17x1 cell}
       coordsys: 'mni'

## Melbourne Subcortical Atlas (Tian et al., 2020)

The Melbourne Subcortical Atlas is a volumetric parcellation of the human subcortex. The atlas was created using functional and structural MRI data from 1000 healthy adult subjects, using functional connectivity gradient mapping. The atlas will be useful for those interested in subcortical structures, and can be easily combined with other cortical atlases. Please note that there is emerging evidence that hippocampal activity can be detected using MEG (see: https://doi.org/10.1002/hbm.24445 and https://doi.org/10.1038/s41467-019-08665-5).

The "scale I" atlas has been implemented in FieldTrip and includes the following regions (all bilateral):
- Amygdala (AMY)
- Hippocampus (HIP)
- Globus Pallidus (GP)
- Nucleus Accumbens (NAc)
- Caudate (CAU)
- Putamen (PUT)
- Anterior Thalamus (aTHA)
- Posterior Thalamus (pTHA)

The atlas can be read into FieldTrip using the following code:

    >> atlas = ft_read_atlas('/template/atlas/melb_subcortical/melb_sub.mat')


## References

- http://www.bic.mni.mcgill.ca/brainweb/
- C.A. Cocosco, V. Kollokian, R.K.-S. Kwan, A.C. Evans : "BrainWeb: Online Interface to a 3D MRI Simulated Brain Database" NeuroImage, vol.5, no.4, part 2/4, S425, 1997 -- Proceedings of 3-rd International Conference on Functional Mapping of the Human Brain, Copenhagen, May 1997.
- R.K.-S. Kwan, A.C. Evans, G.B. Pike : "MRI simulation-based evaluation of image-processing and classification methods" IEEE Transactions on Medical Imaging. 18(11):1085-97, Nov 1999.
- R.K.-S. Kwan, A.C. Evans, G.B. Pike : "An Extensible MRI Simulator for Post-Processing Evaluation" Visualization in Biomedical Computing (VBC'96). Lecture Notes in Computer Science, vol. 1131. Springer-Verlag, 1996. 135-140.
- D.L. Collins, A.P. Zijdenbos, V. Kollokian, J.G. Sled, N.J. Kabani, C.J. Holmes, A.C. Evans : "Design and Construction of a Realistic Digital Brain Phantom" IEEE Transactions on Medical Imaging, vol.17, No.3, p.463--468, June 1998.
- S.B. Eickhoff, K.E. Stephan, H. Mohlberg, C. Grefkes, G.R. Fink, K. Amunts, K. Zilles, A new SPM toolbox for combining probabilistic cytoarchitectonic maps and functional imaging data, NeuroImage 25(4), 2005, 1325-1335.
- Tian, Y., Margulies, D.S., Breakspear, M. et al. Topographic organization of the human subcortex unveiled with functional connectivity gradients. Nat Neurosci 23, 1421–1432 (2020). https://doi.org/10.1038/s41593-020-00711-6
- Wang L, Mruczek REB, Arcaro MJ, Kastner S. (2015) Probabilistic Maps of Visual Topography in Human Cortex. Cerebral Cortex. 25: 3911-3931

## See also

You can find more atlases on <https://www.loni.usc.edu/research/atlases> and on <http://www.bmap.ucla.edu/portfolio/atlases>. 
