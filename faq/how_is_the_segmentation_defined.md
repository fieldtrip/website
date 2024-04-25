---
title: How is the segmentation defined?
tags: [faq, datatype, segmentation, eeg, meg, headmodel]
---

# How is the segmentation defined?

The MATLAB structure that FieldTrip uses to describe a **[segmentation](/reference/utilities/ft_datatype_segmentation)** represents different tissue-types in the anatomical MRI typically after obtained calling **[ft_volumesegment](/reference/ft_volumesegment)** or **[ft_read_atlas](/reference/fileio/ft_read_atlas)**. The segmentation is a special kind of a **[volumetric](/reference/utilities/ft_datatype_volume)** structure that contains additional fields describing for each voxel to which tissue type or brain area it belongs.

An example segmentation obtained after ft_volumesegment with the default segmentation options is shown here. The style of this representation is "probabilistic" (see below

            dim: [256 256 256]        % the size of the 3D volume in voxels
      transform: [4x4 double]         % affine transformation matrix
       coordsys: 'ctf'                % description of the coordinate system
           unit: 'mm'                 % the units in which the coordinate system is expressed
           gray: [256x256x256 double] % probabilistic map of the gray matter
          white: [256x256x256 double] % probabilistic map of the white matter
            csf: [256x256x256 double] % probabilistic map of the cerebrospinal fluid

The tissue type of each voxel can be represented in the FieldTrip structure in two different ways, which are mutually exclusive. The representation can be either _"probabilistic"_ or _"indexed"_. The remainder of this page explains the difference between the two representations.

## Probabilistic representation

### Tissue probability maps

The default output of the ft_volumesegment function (see above) is a segmentation data-type structure with probabilistic tissue maps. The **gray**, **white** and **csf** fields contain _probabilistic values_ for representing the gray, white matter and the cerebrospinal fluid. This means, for example, that at the field **white** everything that is not the white matter represented by 0, and voxels which belong to the white matter have a value between 0 and 1.

{% include image src="/assets/img/faq/how_is_the_segmentation_defined/gray.png" width="186" %}
{% include image src="/assets/img/faq/how_is_the_segmentation_defined/white.png" width="186" %}
{% include image src="/assets/img/faq/how_is_the_segmentation_defined/csf.png" width="186" %}

_Figure 1. Probabilistic maps of the gray (left), white (middle) and cerebrospinal fluid (right). The colors represent probabilities ranging from 0 to 1._

Here is to code that creates this data-structure. It makes use of one of the MRIs from the tutorials.

    % read in the anatomical data
    mri  = ft_read_mri('Subject01.mri');

    % use the ft_volumereslice function to be able to plot the MRI with the top of the head upwards
    cfg              = [];
    cfg.dim          = [256 256 256];                 % original dimension
    mri              = ft_volumereslice(cfg,mri);

    % obtain the gray, white and csf tissue probability maps (tpm)
    cfg              = [];
    tpm              = ft_volumesegment(cfg,mri);

    % plot the gray matter
    cfg              = [];
    cfg.funparameter = 'gray';
    ft_sourceplot(cfg, tpm);

The output of this code can be seen in the introduction of this faq.

{% include markup/blue %}
Here, we used the **[ft_volumereslice](/reference/ft_volumereslice)** function prior to segmentation. It is not required to use this function , but we used it here to obtain a nicer orientation of the MRI images for visualization with **[ft_sourceplot](/reference/ft_sourceplot)**.

The reason for this is explained in more detail [here](/faq/how_change_mri_orientation_size_fov).
{% include markup/end %}

### Binary representations of brain, skull and scalp

When the brain, skull and scalp tissues are requested as outputs from ft_volumesegment, the output also represents the probabilistic representation. However, in this case each fields contain a binary or boolean value, i.e. a probability of 0 (false) or 1 (true). Hence, the binary representation is a special case of the probabilistic representation.

{% include image src="/assets/img/faq/how_is_the_segmentation_defined/brain.png" width="186" %}
{% include image src="/assets/img/faq/how_is_the_segmentation_defined/skull.png" width="186" %}
{% include image src="/assets/img/faq/how_is_the_segmentation_defined/scalp.png" width="186" %}

_Figure 2. The brain (left), the skull (middle) and scalp (right). The colors represent only zeros and ones._

The brain, scalp and skull segmentations are used for creating **volume conduction models** of the head by triangulation the _outside surface_ of the three tissues. This type of segmentation of the MRI is obtained by the following cod

    % obtain the brain, skull and scalp tissues
    cfg              = [];
    cfg.output       = {'brain','skull','scalp'};
    bss              = ft_volumesegment(cfg, mri);     % the mri is the same as in the code before

    cfg              = [];
    cfg.funparameter = 'brain';
    cfg.location     = 'center';
    ft_sourceplot(cfg, bss);

This segmentation data structure looks similar to the structure above (in the introduction), but here, the fields representing the different tissue types contain binary matrices.

             dim: [256 256 256]
        transform: [4x4 double]
         coordsys: 'ctf'
             unit: 'mm'
            brain: [256x256x256 logical] % binary map representing the brain
            scalp: [256x256x256 logical] % binary map representing the scalp
            skull: [256x256x256 logical] % binary map representing the skull

Regardless of whether the probabilities are crisp (i.e. either exactly 0 or 1) or probabilistic (i.e. a floating point value ranging between 0 and 1), the representation of the volume is always in a field of the MATLAB structure with a field name that describes the tissue. A similar example would be

               dim: [256 256 256]
          transform: [4x4 double]
           coordsys: 'mni'
               unit: 'mm'
    brodmann_area_1: [256x256x256 logical] % binary map representing a Brodmann area
    brodmann_area_2: [256x256x256 logical] % binary map representing a Brodmann area
    brodmann_area_3: [256x256x256 logical] % binary map representing a Brodmann area
    brodmann_area_4: [256x256x256 logical] % binary map representing a Brodmann area
    ...

When only the scalp as output is required from the segmentation, the scalp-mask includes also the brain and skull tissues.

{% include image src="/assets/img/faq/how_is_the_segmentation_defined/scalponly.png" width="200" %}

_Figure 3. The binary representation of the outside surface of the scalp. The colors represent only zeros and ones._

This representation differentiates the boarder of the outer skin, but not the inside skin surface. The advantage of such a representation is that it is created faster.

    cfg=[];
    cfg.output='scalp';
    scalp=ft_volumesegment(cfg,mri);

    cfg              = [];
    cfg.funparameter = 'scalp';
    cfg.location     = 'center';
    ft_sourceplot(cfg, scalp);

### Indexed representation

Another way of representing tissue types is done by _indexing_. When indexing, one field structure can represent multiple non-overlapping tissues or brain areas with integer numbers. Everything that doesn't belong to any tissue types is represented by 0 and the voxels which belong to different tissues are represented by different numbers (Figure 3). The index-numbers must start with 1 and should increased one-by-one for each subsequent tissue type.

An additional field in the structure contains the labels that describe the names of the tissues for each index number. The order of the names in the label field are according to the index numbering. This representation is memory wise more efficient in the case of many tissue types and therefore often used for representing a brain atlas.

An example of an indexed segmentation data-structure (the AFNI TTatlas+tlrc segmented brain atlas

    atlas            =   ft_read_atlas('TTatlas+tlrc.BRICK');

    disp(atlas)
                 dim: [161 191 141]
           transform: [4x4 double]
               coord: 'tal'
                unit: 'mm'
              brick0: [161x191x141 uint8]  % integer values from 1 to 50, (0 means unknown)
              brick1: [161x191x141 uint8]  % integer values from 1 to 69, (0 means unknown)
         brick0label: {50x1 cell}          % names (labels) of brain areas indexed in brick0
         brick1label: {69x1 cell}          % names (labels) of brain areas indexed in brick1

In this structure, the **brick0** and **brick1** field contains two different indexed representations of brain areas. The corresponding labels of the index-numbers can be found in the **briack0label** and in the **brick1label** fields. Note that the nomenclature "brick0" and "brick1" is AFNI specific and does not mean anything in special.

An indexed representation can also be plotted to inspect the different tissues in an image (see below).

{% include image src="/assets/img/faq/how_is_the_segmentation_defined/afni_atlas.png" width="300" %}

_Figure 4. Plot of the integer values that are represented in the indexed "brick0" representation of the AFNI atlas. The figure was made with "colormap lines"._

## Conversion between probabilistic and indexed representations

The following code demonstrates how to create an indexed representation from the earlier obtained probabilistic/boolean brain, skull and scalp tissues.

    % convert to indexed representation
    bss_i                = bss;
    bss_i.seg            = double(bss.scalp);         % scalp is logical but seg will contain: 0,1,2,3
    bss_i.seg(bss.skull) = 2;                         % skull is represented by index 2
    bss_i.seg(bss.brain) = 3;                         % brain is represented by index 3
    bss_i.seglabel       = {'scalp','skull','brain'}; % label-order corresponds to index from 1 to 3

    cfg                  = [];
    cfg.funparameter     = 'seg';
    cfg.location         = 'center';
    ft_sourceplot(cfg,bss_i);

    % change the colormap
    map = [0 0 0; 1 0 0; 0 1 0; 0 0 1];

    colormap(map);

{% include image src="/assets/img/faq/how_is_the_segmentation_defined/seg_indexed.png" width="350" %}

_Figure 5. The brain (blue), skull (green) and scalp (red) after segmentation with indexing. The colors represent integers from zero to three._

It is always possible to convert a segmentation with an indexed representation to a probabilistic binary representation. The converse, i.e. a conversion from probabilistic to indexed representations, is not always easily possible.

An indexed segmentation can represent only non-overlapping tissues/brain areas, the only information that is represented is if a voxel belongs to one particular tissue/brain area. Therefore, it is possible to directly convert a binary probabilistic representation of a segmentation with non-overlapping tissue-types into an indexed representation.

When a non-binary probabilistic segmentation is used and when the binary representations of the different tissue types partially overlap, the conversion to an indexed representation would involve a disambiguation of each voxel to which tissue/brain area it belongs to and the more fine-grade information of the probability values would disappear.

{% include image src="/assets/img/faq/how_is_the_segmentation_defined/tissue_representation.png" width="500" %}

_Figure 6. Schematic figure of conversion between different representation of the segmentation. Binary probabilistic representation of non-overlapping tissue-types can be directly converted to an indexed representation (A). When an overlapping or/and non-binary probabilistic representation is converted to indexed, the representations are not equivalent (B)_
