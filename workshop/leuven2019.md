---
title: ChildBrain pre-conference workshop in Leuven, Belgium
---

# ChildBrain pre-conference workshop in Leuven, Belgium

-   By whom: Raul Granados, Simon Homölle
-   When: 5 February 2019
-   Where: Pre-conference training courses at the ChildBrain conference in Leuven <http://www.baci-conference.com>
-   Local organization: Raul Granados.

## How should you prepare for the workshop?

For the hands on session, we kindly require you to bring a functional laptop with MATLAB and FieldTrip installed. This session will be divided in a theoretical introduction, followed by the practical session, for which we ask you to read the points below:
-   We expect that you know the basics of MATLAB and that you already have experience with MEG/EEG preprocessing and analysis.
-   As the focus is on source reconstruction, topics that will NOT be covered in great detail are segmenting, artifact handling, averaging, frequency and time-frequency analysis, statistics.
-   If you are not familiar with MATLAB or are not certain about your MATLAB skills, please go through the “MATLAB for psychologists” tutorial on http://www.antoniahamilton.com/matlab.html to understand the FieldTrip toolbox design please read the FieldTrip reference paper.
-   We will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this introduction tutorial.

In the hands-on session we will start with preprocessing structral MRI data, but will not spend too much time on understanding how MATLAB works and how FieldTrip organizes the data. Therefore if you have never done any FieldTrip analysis in MATLAB before, you should read this [introduction tutorial](/tutorial/introduction).
_We will start at 9:00 sharp and will finish around 12:00._

#### Tuesday

| 09:00-09:15 | Welcome       |
| 09:15-10:15 | Lecture       |
| 10:15-10:30 | Coffee break  |
| 10:45-12:00 | Hands on      |

To get going, you need to start MATLAB. Then, you need to issue the following command

    restoredefaultpath
    cd path_to_fieldtrip
    addpath(pwd)
    ft_defaults

{% include markup/danger %}
Please do NOT use the graphical path management tool from MATLAB. In this hands-on session we'll manage the path from the command line, but in general you are much better off using the startup.m file than the path GUI.

Please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed.
{% include markup/end %}

The restoredefaultpath command clears your path, keeping only the
official MATLAB toolboxes. The addpath(pwd) statement adds the
present working directory, i.e. the directory containing the fieldtrip
main functions. The ft_defaults command ensures that all required
subdirectories are added to the path.

If you get the error "can't find the command ft_defaults" you should check the present working directory.

After installing FieldTrip to your path, you need to change into the hands-on specific directory, containing the data that is necessary to run the specific hands-on session. These folders are located in C:\\FieldTrip_workshop\\.



#Creating a head model

## Introduction

The aim of this tutorial is to create a head model of an adolescent with the numerical method of the Boundary Element Method (BEM), and if as an additional task with the Finite Element Method (FEM). The
[John E. Richards Lab]((https://jerlab.sc.edu)) provided us with an example MRI which is based of the averaged of several MRIs from 14 year old subjects.

## Background

{% include /shared/tutorial/sourcelocalization_background.md %}

## Procedure

As already mentioned, the goal of this session is to solve the EEG forward problem, more precisely we want to compute EEG leadfields so that the inverse problem can be solved.
In order to compute leadfields, there are 9 main steps that have to be followed.
 1.  Load and read the anatomical data (**[ft_read_mri](/reference/ft_read_mri)**);
 2.  Align the MRI to the electrodes. As the electrodes are expressed in the CTF coordinate system, we translate the MRI in the CTF coordinate system (**[ft_volumerealign](/reference/ft_volumerealign)**);
 3.  Reslice the MRI image so that the voxels of the anatomical data are homogeneous (i.e. the size of the voxel is the same into each direction). This step will facilitate the segmentation step. (**[ft_volumereslice](/reference/ft_volumereslice)**)
 4.  Segment the MRI: 3 compartments (scalp, skull, brain) (**[ft_volumesegment](/reference/ft_volumesegment)**);
 5.  then we create the mesh: triangulated surface mesh for BEM and hexahedral volume mesh for FEM (**[ft_prepare_mesh](/reference/ft_prepare_mesh)**).
 6.  Create the head models (headmodel_bem) where geometrical and electrical information are merged together (**[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**);
 7.  Align the electrodes to the head surface (**[ft_electroderealign](/reference/ft_electroderealign)**);
 8.  The source model is created, where the location of the sources is restrained to the brain compartment (from the BEM mesh) (**[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)**);
 9.  Leadfields can be computed (**[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**).

{% include image src="/assets/img/workshop/baci2017/forwardproblem/scheme.png" %}
*Figure 1: Pipeline for forward computation, in the blue box there are the steps which differ between BEM and FEM*

##  1. Read the MRI

First of all we have to load the data

	mri_orig = ft_read_mri('ANTS14-0Years3T_head_bias_corrected.nii.gz');

Visualize the MRI

	cfg=[];
	ft_sourceplot(cfg,mri_orig);

{% include image src="/assets/img/workshop/leuven2019/mri_orig.png" %}
*Figure 2: Visualization of the MRI*

##  2. Realign the MRI

In this step we will interactively align the MRI to the CTF space. We will be asked to identify the three CTF landmarks (nasion, NAS; right pre-auricular point, RPA; left pre-auricular point, LPA) in the MRI.

	cfg = [];
	cfg.method = 'interactive';
	cfg.coordsys = 'ctf';
	mri_realigned = ft_volumerealign(cfg, mri_orig);

We can visualize the realigned MRI

	cfg = [];
	ft_sourceplot(cfg, mri_realigned);

  {% include image src="/assets/img/workshop/leuven2019/mri_resliced.png" %}
  *Figure 3: Visualization of the realigned MRI*

##  3. Reslice the MRI

	cfg = [];
	mri_resliced = ft_volumereslice(cfg, mri_realigned);

We can visualize the resliced MRI

	cfg = [];
	ft_sourceplot(cfg, mri_resliced);


{% include image src="/assets/img/workshop/leuven2019/mri_resliced.png" %}
*Figure 3: Visualization of the realigned MRI*

##  4. Segment the MRI

	cfg           = [];
	cfg.output    = {'brain','skull', 'scalp'};
	mri_segmented_3_compartment = ft_volumesegment(cfg, mri_resliced);

Visualize the segmentation

	seg_i = ft_datatype_segmentation(mri_segmented_3_compartment,'segmentationstyle','indexed');

	cfg              = [];
	cfg.funparameter = 'seg';
	cfg.funcolormap  = gray(4); % distinct color per tissue
	cfg.location     = 'center';
	cfg.atlas        = seg_i;   
	ft_sourceplot(cfg, seg_i);

{% include image src="/assets/img/workshop/leuven2019/mri_segmented_bem.png" %}
*Figure 4: 3 compartment segmentation output*

##  5. Create the mesh

	cfg=[];
	cfg.tissue={'brain','skull','scalp'};
	cfg.numvertices = [3000 2000 1000];
	mesh_bem=ft_prepare_mesh(cfg,mri_segmented_3_compartment);

Visualize the mesh

	figure, ft_plot_mesh(mesh_bem(1),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)
	ft_plot_mesh(mesh_bem(2),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)
	ft_plot_mesh(mesh_bem(3),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)

{% include image src="/assets/img/workshop/leuven2019/mesh_bem.png" %}
*Figure 5: 3 compartment mesh with electrodes*

##  6. Create the head model

	cfg        = [];
	cfg.method ='dipoli'; % You can also specify 'bemcp', or another method.
	headmodel_bem       = ft_prepare_headmodel(cfg, mesh_bem);

{% include markup/danger %}
In Windows the method 'dipoli' does not work. You can explore other BEM method like 'bemcp'. If you use 'bemcp', the conductivity field has a different order: {'brain', 'skull', 'skin'}.
{% include markup/end %}

##  7. Align the electrodes

First we have to load a suitable electrode set. For this tutorial we will load a template dataset and transform it in such a way that it will fit the head surface.

  elec = ft_read_sens('standard_1020.elc');

And now we will fit it to the head surface.

	cfg          = [];
	cfg.method   = 'interactive';
	cfg.elec     = elec;
	cfg.headshape = headmodel_bem.bnd(3);
	elec = ft_electroderealign(cfg);

Check the alignment visually.

	figure;
	ft_plot_axes(mesh_bem(1))
	hold on;
	ft_plot_mesh(mesh_bem,'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)
	ft_plot_sens(elec,'style', '.k');

{% include image src="/assets/img/workshop/leuven2019/aligned.png" %}
*Figure 6: Mesh, electrodes and axes.*

##  8. Create the source model

	cfg = [];
	cfg.grid.resolution = 7.5;
	cfg.threshold = 0.1;
	cfg.smooth = 5;
	cfg.vol = headmodel_bem;
	cfg.inwardshift = 1; %shifts dipoles away from surfaces
	sourcemodel = ft_prepare_sourcemodel(cfg, headmodel_bem);

Visualize the source model

	figure, ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:))
	hold on, ft_plot_mesh(mesh_bem(1),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)

{% include image src="/assets/img/workshop/leuven2019/sourcemodel_all.png" %}
*Figure 7: Sourcemodel on the brain compartment*

Save the source model

save sourcemodel sourcemodel;

##  9. Compute the leadfield

	cfg = [];
	cfg.grid = sourcemodel;
	cfg.vol= headmodel_bem;
	cfg.elec = elec;
	leadfield_bem = ft_prepare_leadfield(cfg);

## 10. Further tasks



#### Exercise 1

{% include markup/info %}
Thus far we only created a BEM volume conduction model. To create a FEM volume conduction model use the same steps as beforehand.
{% include markup/end %}
Change Step 5 into

  cfg=[];
  cfg.tissue={'brain','skull','scalp'};
  cfg.method='hexahedral';
  mesh_fem=ft_prepare_mesh(cfg,mri_segmented_3_compartment);

and Step 6 into

  cfg        = [];
  cfg.method ='simbio'; % Unfortunately this is not available on Windows.
  headmodel_bem       = ft_prepare_headmodel(cfg, mesh_bem);

#### Exercise 2

{% include markup/info %}
You can also find the segmentation 'AVG14-0Years3T_segmented_BEM3.mat' to create a head model. This a segmentation is processed version of a segmentation provided by alongside the MRI in the Neurodevelopmental MRI Database from the [John E. Richards Lab]((https://jerlab.sc.edu)). The segmentation was already preprocessed with the Steps 1-4.
{% include markup/end %}

## Summary and Comments

This tutorial was about the computation of leadfields that could be feed into the inverse problem.

## Further reading
Another interesting data base to consider for volume conduction modeling for infants is the [Pediatric Head Modeling Project]((https://www.pedeheadmod.net/)).

For acquisition of electrode positions we can also suggest:
{% include seealso tag1="electrode" %}

For head model creation we also suggest following tutorials:
{% include seealso tag1="headmodel" %}


-----
This tutorial was last tested on 04-01-2019 by Simon Homölle on Windows 10, Matlab 2018a.
