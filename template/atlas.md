---
title: Template anatomical atlases and parcellation schemes
tags: [template, atlas]
---

# Template anatomical atlases and parcellation schemes

We define an atlas as a volumetric or surface based description of the geometry of the brain, where each anatomical coordinate is labeled according to some scheme, e.g., as [Brodmann area](https://en.wikipedia.org/wiki/Brodmann_area). A review of brain templates and atlases is presented in [Brain templates and atlases (2012)](http://www.ncbi.nlm.nih.gov/pubmed/22248580) in NeuroImage.

In general an atlas can be read with **[ft_read_atlas](/reference/fileio/ft_read_atlas)**. It is represented as a volumetric segmentation as in **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)**, or as a surface-based parcellation as in **[ft_datatype_parcellation](/reference/utilities/ft_datatype_parcellation)**. The volume based representation can be used with **[ft_volumelookup](/reference/ft_volumelookup)** or with the cfg.atlas option in **[ft_sourceplot](/reference/ft_sourceplot)**.

You can find volumetric and surface-based atlases in the `fieldtrip/template/xxx` directory, with XXX referring to the specific template (e.g., "aal" or "afni").

{% include markup/warning %}
You can have a look at the template anatomical atlases and parcellation schemes [here on GitHub](https://github.com/fieldtrip/fieldtrip/tree/master/template/atlas). Furthermore, this page describes some atlases that are released along with FreeSurfer and FSL.
{% include markup/end %}

## The AAL atlas

The AAL atlas included with FieldTrip was downloaded from [here](http://www.gin.cnrs.fr/en/tools/aal-aal2/). The same atlas is also included in the SPM "WFU-PickAtlas" toolbox with a slight difference in the format of the text file.

N. Tzourio-Mazoyer, B. Landeau, D. Papathanassiou, F. Crivello, O. Etard, N. Delcroix, B. Mazoyer, and M. Joliot. _Automated Anatomical Labeling of Activations in SPM Using a Macroscopic Anatomical Parcellation of the MNI MRI Single-Subject Brain._ NeuroImage 2002. 15:273-289.

    >> atlas = ft_read_atlas(fullfile(ftpath, 'template/atlas/aal/ROI_MNI_V4.nii'))

    aal =
              dim: [91 109 91]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
           tissue: [91x109x91 double]
      tissuelabel: {1x116 cell}

    >> imagesc(aal.tissue(:,:,45))

{% include image src="/assets/img/template/atlas/aal.png" width="400" %}

## The Brainnetome Atlas

The Brainnetome Atlas is designed to study activation and connectivity. Each hemisphere is subdivided into 123 subregions and the parcellation is based on both structural and functional connectivity features. More information can be found [here](http://atlas.brainnetome.org/).

The atlas is described in Fan, L., Li, H., Zhuo, J., Zhang, Y., Wang, J., Chen, L., Yang, Z., Chu, C., Xie, S., Laird, A.R., Fox, P.T., Eickhoff, S.B., Yu, C. & Jiang, T. (2016) [The Human Brainnetome Atlas: A New Brain Atlas Based on Connectional Architecture](https://doi.org/10.1093/cercor/bhw157). Cerebral Cortex, 26(8):3508-26.

In FieldTrip, the atlas is included as a nifti file, complemented with a text file with the tissue labels. You can read it like this:

    >> brainnetome = ft_read_atlas(fullfile(ftpath, 'template/atlas/brainnetome/BNA_MPM_thr25_1.25mm.nii'))

    brainnetome =
              dim: [145 173 145]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
           tissue: [145x173x145 double]
         coordsys: 'mni'
      tissuelabel: {1x246 cell}

    >> imagesc(brainnetome.atlas(:,:,68))

{% include image src="/assets/img/template/atlas/brainnetome_atlas2.png" width="400" %}

## The Eickhoff/Zilles/Amunts cytoarchitectonic atlas

This atlas is the same one as the on implemented in SPM's anatomy toolbox. The version that is in FieldTrip was downloaded from [here](http://www.fz-juelich.de/inm/inm-1/DE/Forschung/_docs/SPMAnatomyToolbox/SPMAnatomyToolbox_node.html).

The atlas and the toolbox are described in S.B. Eickhoff, K.E. Stephan, H. Mohlberg, C. Grefkes, G.R. Fink, K. Amunts, K. Zilles (2005) [A new SPM toolbox for combining probabilistic cytoarchitectonic maps and functional imaging data](https://doi.org/10.1016/j.neuroimage.2004.12.034). NeuroImage, 1;25(4):1325-35.

    >> spm_anatomy = ft_read_atlas(fullfile(ftpath, 'template/atlas/spm_anatomy/AllAreas_v17_MPM.mat'))

    spm_anatomy =
              dim: [151 188 154]
              hdr: [1x1 struct]
        transform: [4x4 double]
             unit: 'mm'
           tissue: [151x188x154 double]
      tissuelabel: {67x1 cell}
         coordsys: 'spm'

Besides the 'v17' version, the 'v18' is also supported.

## FreeSurfer FsAverage

We often use [FreeSurfer](https://surfer.nmr.mgh.harvard.edu/fswiki/FreeSurferWiki) to extract cortical sheets which we use as the basis for a [source model](/tutorial/sourcemodel) or for the projection of [ECoG electrodes](/tutorial/human_ecog). FreeSurfer also comes with atlasses (or cortical parcellations), which can be used to label the vertices of the individual's cortical sheet.

The FreeSurfer atlasses are quite large and therefore not copied into FieldTrip, but you may have them on your local computer. There are multiple [parcellations available](https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation):

- Desikan-Killiany Atlas (?h.aparc.annot)
- Destrieux Atlas (?h.aparc.a2009s.annot)
- DKT Atlas (?h.aparc.DKTatlas40.annot)

You can read the FsAverage parcellations per hemisphere like this:

    >> cd /opt/freesurfer/7.3.2/subjects/fsaverage  % or wherever your FreeSurfer is installed
    >> fsaverage_lh_aparc = ft_read_atlas({'label/lh.aparc.annot', 'surf/lh.pial'})
    >> fsaverage_rh_aparc = ft_read_atlas({'label/rh.aparc.annot', 'surf/rh.pial'})
    
    fsaverage_lh_aparc =
           pos: [163842x3 double]
           tri: [327680x3 double]
         aparc: [163842x1 double]
    aparclabel: {36x1 cell}
          rgba: [36x4 double]
          unit: 'mm'

    % plot the mesh with color-coded parcels
    >> ft_plot_mesh(fsaverage_lh_aparc, 'vertexcolor', fsaverage_lh_aparc.aparc)
    >> view([-1 0 0 ])
    >> camlight
    >> material dull

{% include image src="/assets/img/template/atlas/fsaverage.png" width="400" %}

Following the segmentation and meshing of your individual participant with [recon-all](https://surfer.nmr.mgh.harvard.edu/fswiki/recon-all), you can find a similar `surf` and `label` directory for your participant. Reading the individual parcellation with the anatomical labels is therefore similar to reading them from the fsaverage template.

## FSL atlasses

The [FMRIB Software Library](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki) (FSL) release comes with a number of [atlasses](https://fsl.fmrib.ox.ac.uk/fsl/fslwiki/Atlases) that you can also read directly into FieldTrip.

    >> cd /opt/fsl/6.0.6/data/atlases  % or wherever your FSL is installed
    >> talairach = ft_read_atlas('Talairach.xml')
    >> juelich = ft_read_atlas('Juelich.xml')
    >> harvard_oxford = ft_read_atlas('HarvardOxford-Cortical.xml')

## The Yeo Atlases

The Yeo Atlases are designed to study intrinsic functional connectivity. Each hemisphere is subdivided into either 7 or 17 functionally coupled regions across the cerebral cortex. More information can be found [here](https://surfer.nmr.mgh.harvard.edu/fswiki/CorticalParcellation_Yeo2011). The atlases included with FieldTrip were created by transforming Yeo2011_7Networks_MNI152_FreeSurferConformed1mm.nii.gz and Yeo2011_17Networks_MNI152_FreeSurferConformed1mm.nii.gz into standardized space (single_subj_T1_1mm) using volume-based anatomical registration approaches.

The atlases are described in Yeo BT, Krienen FM, Sepulcre J, Sabuncu MR, Lashkari D, Hollinshead M, Roffman JL, Smoller JW, Zollei L., Polimeni JR, Fischl B, Liu H, Buckner RL. (2011) [The organization of the human cerebral cortex estimated by intrinsic functional connectivity](https://doi.org/10.1152/jn.00338.2011). J Neurophysiol, 106(3):1125-65.

In FieldTrip, the two atlases are included as nifti files. You can read them like this:

    >> yeo7 = ft_read_atlas(fullfile(ftpath, 'template/atlas/yeo/Yeo2011_7Networks_MNI152_FreeSurferConformed1mm_LiberalMask_colin27.nii'))

    yeo7 =
            dim: [256 256 256]
            hdr: [1x1 struct]
      transform: [4x4 double]
           unit: 'mm'
         tissue: [256x256x256 double]
    tissuelabel: {7x1 cell}
       coordsys: 'mni'

    >> yeo17 = ft_read_atlas(fullfile(ftpath, 'template/atlas/yeo/Yeo2011_17Networks_MNI152_FreeSurferConformed1mm_LiberalMask_colin27.nii'))

    yeo17 =
            dim: [256 256 256]
            hdr: [1x1 struct]
      transform: [4x4 double]
           unit: 'mm'
         tissue: [256x256x256 double]
    tissuelabel: {17x1 cell}
       coordsys: 'mni'

## The AFNI TTatlas+tlrc Dataset

This is a binary representation of the Talairach Tournoux atlas [ref 1]. It was digitized for the Talairach Daemon [ref 2] and converted into AFNI format. It is described in some detail on the [AFNI website](https://sscc.nimh.nih.gov/afni/doc/misc/afni_ttatlas/index_html). Note that the website seems to be unstable and relatively often unresponsive. Next to the template that is shipped with FieldTrip, it is also possible to load in other atlases that are defined in AFNI format. For instance, the atlases that can be obtained from [here](https://afni.nimh.nih.gov/pub/dist/atlases/).

{% include markup/danger %}
Note that this atlas is defined in [Talairach-Tournoux coordinates](/faq/coordsys/#details-of-the-talairach-tournoux-coordinate-system) (tal) and not in MNI/SPM coordinates.
{% include markup/end %}

The atlas and the toolbox are described in

- Talairach J, Tournoux P (1988). [Co-planar stereotaxic atlas of the human brain](http://www.amazon.com/Co-Planar-Stereotaxic-Atlas-Human-Brain/dp/0865772932). Thieme, New York.
- Lancaster JL, Rainey LH, Summerlin JL, Freitas CS, Fox PT, Evans AC, Toga AW, Mazziotta JC. (1997) [Automated labeling of the human brain: a preliminary report on the development and evaluation of a forward-transform method](https://doi.org/10.1002/(sici)1097-0193(1997)5:4%3C238::aid-hbm6%3E3.0.co;2-4). Hum Brain Mapp. 5(4):238-42.

You can use the following snippet of code to get a quick idea of this atlases.

   >> [ftver, ftpath] = ft_version;
   >> afni = ft_read_atlas(fullfile(ftpath, '/template/atlas/afni/TTatlas+tlrc.HEAD'))

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

You can read it like this:

    >> melb_subcortical = ft_read_atlas(fullfile(ftpath, 'template/atlas/melb_subcortical/melb_sub.mat'))

The atlas is described in Tian, Y., Margulies, D.S., Breakspear, M. et al. (2020) [Topographic organization of the human subcortex unveiled with functional connectivity gradients](https://doi.org/10.1038/s41593-020-00711-6). Nat Neurosci 23, 1421–1432.

## The VTPM Atlas

The VTPM atlas was downloaded from [here](http://www.princeton.edu/~napl/vtpm.htm).The atlas was constructed from a population of 53 subjects and contains probabilistic maps for 25 visual areas. The version of the atlas included with FieldTrip was created by the authors of the original paper, by transforming data into standardized space using surface-based anatomical registration approaches, and subsequently assigning a voxel-wise label based on a maximum probability criterion. For convenience, the version of the atlas that is distributed with FieldTrip has the original left and right hemispheres merged in a single file. One known issue is the absence of the right IPS5 parcel.

The atlas is described in Wang L, Mruczek REB, Arcaro MJ, Kastner S. (2015) [Probabilistic Maps of Visual Topography in Human Cortex](https://doi.org/10.1093/cercor/bhu277). Cerebral Cortex, 25(10):3911-31.

    >> atlas = ft_read_atlas(fullfile(ftpath, 'template/atlas/vtpm/vtpm.mat'))

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

## The BrainWeb Dataset

Using the normal anatomical model downloaded from the [BrainWeb](http://www.bic.mni.mcgill.ca/brainweb/) website we constructed a discrete and fuzzy segmentation of the human head in 9 tissue types.

The segmentation is defined at a 1 mm isotropic voxel grid in Talairach space, with dimensions 181x217x181 (XxYxZ) and start coordinates -90,-126,-72 (x,y,z).

The discrete model is represented in a MATLAB .mat file as

    >> discrete = ft_read_atlas(fullfile(ftpath, 'template/atlas/brainweb/brainweb_discrete.mat'))

    discrete =
              dim: [181 217 181]
        transform: [4x4 double]
             unit: 'mm'
           tissue: [181x217x181 double]
      tissuelabel: {'csf'  'grey_matter'  'white_matter'  'fat'  'muscle_and_skin'  'skin'  'skull'  'glial_matter'  'connective'}

The fuzzy model is represented in a MATLAB .mat file as

    >> atlas = ft_read_atlas(fullfile(ftpath, 'template/atlas/brainweb/brainweb_fuzzy.mat'))

    fuzzy =
                  dim: [181 217 181]
            transform: [4x4 double]
                 unit: 'mm'
             coordsys: 'mni'
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

Both discrete and fuzzy model are consistent with the data representation described in **[ft_datatype_segmentation](/reference/utilities/ft_datatype_segmentation)**.

The atlas is described in:
- DL Collins, AP Zijdenbos, V Kollokian, JG Sled, NJ Kabani, CJ Holmes, AC Evans (1998) [Design and Construction of a Realistic Digital Brain Phantom](https://doi.org/10.1109/42.712135). IEEE Trans Med Imaging, Jun;17(3):463-8.
- CA Cocosco, V Kollokian, RK-S Kwan, AC Evans (1997) "BrainWeb: Online Interface to a 3D MRI Simulated Brain Database" NeuroImage, vol.5, no.4, part 2/4, S425, 1997 - Proceedings of 3rd International Conference on Functional Mapping of the Human Brain, Copenhagen.
- RK-S Kwan, AC Evans, GB Pike (1999) "MRI simulation-based evaluation of image-processing and classification methods" IEEE Transactions on Medical Imaging, 18(11):1085-97.
- RK-S Kwan, AC Evans, GB Pike (1996) "An Extensible MRI Simulator for Post-Processing Evaluation" Visualization in Biomedical Computing (VBC'96). Lecture Notes in Computer Science, vol. 1131. Springer-Verlag, 135-140.

## See also

The **[ft_read_atlas](/reference/fileio/ft_read_atlas)** function can read geometrical information and anatomical labels from a variety of file formats, and can therefore also be used for other atlasses. You can find more atlases here:
- <https://www.loni.usc.edu/research/atlases>
- <http://www.bmap.ucla.edu/portfolio/atlases>
- <https://www.ebrains.eu/tools/human-brain-atlas>
- <https://balsa.wustl.edu>
