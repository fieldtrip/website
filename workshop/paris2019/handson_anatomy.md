---
title: Creation of headmodels and sourcemodels for source reconstruction
tags: [tutorial, meg, headmodel, sourcemodel, sourceanalysis]
---

# Creation of headmodels and sourcemodels for source reconstruction

{% include markup/info %}
This tutorial was written specifically for the practicalMEEG workshop in Paris in December 2019, and is an adjusted version of the [headmodel for MEG tutorial](/tutorial/headmodel_meg).
{% include markup/end %}

## Introduction

This tutorial describes how to construct a volume conduction model of the head (headmodel) and a sourcemodel, based on an individual subject's MRI. These two geometrical objects are necessary ingredients (in combination with a specification of the MEG/EEG sensor array) for the construction of a forward model.
We will use the anatomical images that belong to the same subject whose data were analyzed in the previous tutorials ([From raw data to ERP](/workshop/paris2019/handson_raw2erp), [Time-frequency analysis using Hanning window, multitapers and wavelets](/workshop/paris2019/handson_sensoranalysis)), thus using anatomical data of subject sub-15 of the Face recognition [dataset](/workshop/meg-uk-2015/dataset).

This tutorial will **not** show how to perform the source reconstruction itself. If you are interested in source reconstruction methods, you can go to the [Localizing oscillatory sources using beamformer techniques](/tutorial/beamformer) and to the [Source reconstruction of event-related fields using minimum-norm estimate](/tutorial/minimumnormestimate) tutorials, or to the [].

{% include markup/success %}
The volume conduction model created here is MEG specific and cannot be used for EEG source reconstruction. If you are interested in EEG source reconstruction methods, you can go to the corresponding [EEG tutorial](/tutorial/headmodel_eeg).
{% include markup/end %}

## Background

The forward model is a necessary prerequisite for source reconstruction. It is a model that describes, for a given set of putative source locations (defined in the sourcemodel), the spatial distribution of the signals picked up by the sensor array. Each of the sources is modelled as an equivalent current dipole (ECD), which serve as elementary building blocks of arbitrarily complex source configurations. The headmodel is needed to account for the effect of volume currents.
There are different approaches to creating a forward model, each of which require a specific type of headmodel. Some examples of different MEG-based headmodels are given **[here](/example/make_leadfields_using_different_headmodels)**. Typically, invdidual headmodels required for accurate EEG forward modelling (for example a **[boundary element model (BEM)](/tutorial/headmodel_eeg_bem)**, or **[finite element model (FEM)](/tutorial/headmodel_eeg_fem)**) require a more sophisticated anatomical processing than sufficiently good headmodels for MEG. For the latter case, typically a single shell boundary that describes the inner surface of the skull provides good results.

## Coregistration of anatomical MRI image with MEG sensor array

The ingredients for a forward model (i.e. geometrical information about the sensor array, the headmodel, and the sourcemodel) are all defined in space, i.e. the location of their constituting elements can be described with spatial coordinates. It may sound trivial, but before anything meaningful can be done in combining these geometrical objects, we need to ensure that all spatial coordinates are expressed in the same **[coordinate system](/faq/how_are_the_different_head_and_mri_coordinate_systems_defined)**, and that the metrical units are the same. That is, the objects need to be **[coregistered](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions)** to each other. In our experience, the realm of coordinate systems is a murky one. Typically, software packages try to hide as much as possible the murky details, often by adopting rigid conventions about the coordinate systems in which the data is to be represented. This usually results in relatively robust behavior, yet, when things go wrong, they typically go **very** wrong. FieldTrip aims at being lenient with respect to the exact specification of the coordinate system, and should work fine, as long as the objects are properly coregistered. This requires some basic understanding about coordinate systems and coordinate system transforms, in order to be able to diagnose any potential problems encountered.
The coordinate system in which the MEG sensors are expressed is defined based on three anatomical landmarks that can be identified on a subject's head (i.e. the nasion, and the left and right preauricular points (lpa and rpa)). In FieldTrip, we typically coregister the anatomical image to the sensor array, which will be done with **[ft_volumerealign](/reference/ft_volumerealign)**. For the current dataset, the locations of the nasion,lpa and rpa (expressed in voxel coordinates of the corresponding MRI image) are already available, so the coregistration is straightforward. Alternatively, the researcher needs to interactively determine the location of the anatomical landmarks in the MRI image, which is possible using cfg.method = 'interactive'. Here, we will use the 'fiducial' method.
First, we extract the positions of the landmarks from the subject's MRI metadata .json file:

    subj = subject_datainfo(15);

    file_id = fopen(subj.fidfile);
    line = fgetl(file_id);
    LPA = [];
    RPA = [];
    NAS = [];
    while ~isequal(line, -1)
      if contains(line, 'LPA')
        tok = split(line, '[');
        tok = split(tok{2}, ']');
        vals = split(tok{1}, ',');
        LPA  = str2double(vals');
      end
      if contains(line, 'RPA')
        tok = split(line, '[');
        tok = split(tok{2}, ']');
        vals = split(tok{1}, ',');
        RPA  = str2double(vals');
        end
        if contains(line, 'Nasion')
        tok = split(line, '[');
        tok = split(tok{2}, ']');
        vals = split(tok{1}, ',');
        NAS  = str2double(vals');
        end
        line = fgetl(file_id);
      end
      fclose(file_id);

Next, we can inspect the location of the landmarks in the anatomical image.

      mri_orig = ft_read_mri(subj.mrifile);

      cfg = [];
      cfg.locationcoordinates = 'voxel'; % treat the location as voxel coordinates
      cfg.location = NAS;
      ft_sourceplot(cfg, mri_orig);

If the contrast of the image is a bit low, you can use the 'shift+' key to increase the contrast.

{% include image src="/assets/img/workshop/paris2019/mri_origNAS.png" width="400" %}

_Figure: The location of the NAS indicated by the crosshair in the anatomical MRI image_

#### Exercise 1

{% include markup/exercise %}
Inspect the location of the LPA and RPA.
{% include markup/end %}

Now, we can coregister the MRI image to the coordinate system as used for the MEG sensor positions:

    cfg              = [];
    cfg.method       = 'fiducial';
    cfg.fiducial.nas = NAS;
    cfg.fiducial.lpa = LPA;
    cfg.fiducial.rpa = RPA;
    cfg.coordsys     = 'neuromag';
    mri              = ft_volumerealign(cfg, mri_orig);

#### Exercise 2

{% include markup/exercise %}
Inspect the location of the NAS, LPA and RPA of the coregistered MRI. Pay special attention to the location coordinates, as compared to the location coordinates of the original MRI.
{% include markup/end %}

## Creation of the single shell head model

Now, to create a single shell model of the inner surface of the skull, we need a segmentation of the MRI image, which can be achieved with the function **[ft_volumesegment](/reference/ft_volumesegment)**. This function uses SPM for segmentation, and in its default behavior returns a probabilistic segmentation of the grey, white and csd compartments **[](/faq/how_is_the_segmentation_defined)**. Here, we only need a description of the surface of the brain, which is obtained by thresholding the probabilistic combined grey/white/csf image,

    thr = 0.5;

    % segment the coregistered mri
    cfg                = [];
    cfg.output         = 'brain';
    cfg.brainthreshold = thr;
    seg = ft_volumesegment(cfg, mri);

    % create the mesh
    cfg        = [];
    cfg.method = 'singleshell';
    headmodel  = ft_prepare_headmodel(cfg, seg);
    save(fullfile(subj.outputpath, 'anatomy', sprintf('%s_headmodel', subj.name)), 'headmodel');

You can now visualise the headmodel in combination with the anatomical image:

    cfg = [];
    cfg.intersectmesh = headmodel.bnd;
    ft_sourceplot(cfg, mri);

{% include image src="/assets/img/workshop/paris2019/mri_headmodel.png" width="400" %}

_Figure: The headmodel visualised on top of the volulmetric anatomical image_

## Creation of a cortex based source model

To creation of a state-of-the-art sourcemodel that is based on an accurate individual cortical segmentation is described in a **[dedicated tutorial](/tutorial/sourcemodel)**. Source reconstruction algorithms that assume distributed sources (for instance Minimum Norm Estimates MNEs) require these cortical models, whereas for beamformers are not absolutely necessary. The generation of cortically constrained sourcemodels, defined on a triangulated surface mesh can be rather time consuming, so we are not going to do that here. Instead, the sourcemodels have already been computed, according to a slightly modified version of the recipe described in the abovementioned tutorial. Below, the code is referenced that was used to generate the sourcemodels. It serves as an illustrative example, because it was executed on the Donders Institute's compute cluster, which uses a specific way to execute computational jobs (qsub). The overall idea would be however to tweak a set of shell scripts (**[ft_freesurferscript.sh](/reference/bin/ft_freesurferscript.sh)** and **[ft_postfreesurferscript.sh](/reference/bin/ft_postfreesurferscript.sh)**), and execute those on your own computer (requires a Linux or MatOS environment, with installed freesurfer and workbench).
In contrast to the **[referenced tutorial](/tutorial/sourcemodel)**, the input MRI image that serves as the starting point for the freesurfer pipeline is the image coregistered to the MEG coordinate system. This coordinate system is sufficently similar to the conventional coordinate system expected by freesurfer, so that the overall (post)freesurfer pipeline runs through fine. If, by contrast, the MEG coordinate system is according to the CTF system's convention, an intermediate (temporary) coregistration is required.

    % this part creates a freesurfer output base directory and fills it with
    % an anatomical image that is going to be used by freesurfer
    mkdir(fullfile(subj.outputpath, 'anatomy', 'freesurfer'));
    cfg              = [];
    cfg.filename     = fullfile(subj.outputpath, 'anatomy', 'freesurfer',       subj.name);
    cfg.filetype     = 'mgz'; % not sure whether this is supported in Windows
    cfg.parameter    = 'anatomy';
    ft_volumewrite(cfg, mri);

    % this part runs a standard automatic freesurfer pipeline, that is not
    % guaranteed to work out-of-the-box. It may require some manual tweaks along
    % along the how_are_the_different_head_and_mri_coordinate_systems_defined
    [dum, ft_path] = ft_version;
    scriptname = fullfile(ft_path,'bin','ft_freesurferscript.sh');
    subj_dir   = fullfile(subj.outputpath, 'anatomy', 'freesurfer');
    cmd_str    = sprintf('echo "%s %s %s" | qsub -l walltime=20:00:00,mem=8gb -N sub-%02d', scriptname, subj_dir, subj.name, subj.id);
    system(cmd_str);

    % this part runs a set of postprocessing steps, and requires hcp-workbench
    % to be available
    [dum, ft_path] = ft_version;
    scriptname = fullfile(ft_path,'bin','ft_postfreesurferscript.sh');
    subj_dir   = fullfile(subj.outputpath, 'anatomy', 'freesurfer');
    templ_dir  = '/home/language/jansch/projects/Pipelines/global/templates/standard_mesh_atlases';%fullfile(ft_path,'template','sourcemodel');
    cmd_str    = sprintf('echo "%s %s %s %s" | qsub -l walltime=20:00:00,mem=8gb -N sub-%02d', scriptname, subj_dir, subj.name, templ_dir, subj.id);



## Computation of the forward model
