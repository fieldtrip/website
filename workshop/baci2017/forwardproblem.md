---
title: Solving the EEG forward problem using BEM and FEM
layout: default
---

## Solving the EEG forward problem using BEM and FEM

## Introduction

The aim of this tutorial is to solve the EEG forward problem using two different numerical methods, namely the Boundary Element Method (BEM) and the Finite Element Method (FEM).

## Background

{{page>:tutorial:shared:sourcelocalization_background}}

## Procedure

As already mentioned, the goal of this session is to solve the EEG forward problem, more precisely we want to compute EEG leadfields so that the inverse problem can be solved in the next session ([ inverse problem](http://www.fieldtriptoolbox.org/workshop/baci2017/inverseproblem )).
In order to compute leadfields, there are 9 main steps that have to be followed.
 1.  Load and read the anatomical data, namely a T1-MRI (**[ft_read_mri](/reference/ft_read_mri)**);
 2.  Align the MRI to the electrodes. As the electrodes are expressed in the CTF coordinate system, we translate the MRI in the CTF coordinate system (**[ft_volumerealign](/reference/ft_volumerealign)**);
 3.  Reslice the MRI image so that the voxels of the anatonical data are homogeneous (i.e. the size of the voxel is the same into each direction). This step will facilitate the segmentation step. (**[ft_volumereslice](/reference/ft_volumereslice)**)
 4.  Segment the MRI: 3 compartments for BEM (scalp, skull, brain) and 5 compartments for FEM (scalp, skull, CSF, grey matter and white matter) (**[ft_volumesegment](/reference/ft_volumesegment)**);
 5.  then we create the mesh: triangulated surface mesh for BEM and hexahedral volume mesh for FEM (**[ft_prepare_mesh](/reference/ft_prepare_mesh)**).
 6.  Create the headmodels (headmodel_bem and headmodel_fem) where geometrical and electrical information are merged together (**[ft_prepare_headmodel](/reference/ft_prepare_headmodel)**);
 7.  Align the electrodes to the MRI (**[ft_electroderealign](/reference/ft_electroderealign)**);
 8.  The sourcemodel is created, where the location of the sources is restrained to the brain compartment (from the BEM mesh) (**[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)**);
 9.  Leadfields can be computed (**[ft_prepare_leadfield](/reference/ft_prepare_leadfield)**). 

The first 3 steps are the same for BEM and FEM. Steps from 4 to 8 differ between BEM and FEM.
A more detailed description of these steps is following.

![image](/static/img/workshop/baci2017/scheme.png)
*Figure1: pipeline for forward computation, in the blue box there are the steps which differ between BEM and FEM*

##  1. Read the MRI

	mri_orig = ft_read_mri('subject01.nii');

Visualize the MRI

	cfg=[]; 
	ft_sourceplot(cfg,mri_orig);

![image](/static/img/workshop/baci2017/mri_orig.png)
*Figure2: visualization of the MRI*

##  2. Realign the MRI

In this step we will interactively align the MRI to the CTF space. We will be asked to identify the three CTF landmarks (nasion, NAS; right pre-auricular point, RPA; left pre-auricular point, LPA) in the MRI.

	cfg = [];
	cfg.method = 'interactive';
	cfg.coordsys = 'ctf';
	mri_realigned = ft_volumerealign(cfg, mri_orig);

We can visualize the realigned MRI

	cfg = []; 
	ft_sourceplot(cfg, mri_realigned);

![image](/static/img/workshop/baci2017/mri_resliced.png)
*Figure3: visualization of the realigned MRI*
##  3. Reslice the MRI

	cfg = [];
	mri_resliced = ft_volumereslice(cfg, mri_realigned);

We can visualize the resliced MRI

	cfg = []; 
	ft_sourceplot(cfg, mri_resliced);

##  A. Boundary Element Method (BEM)

##  4A. Segment the MRI

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

![image](/static/img/workshop/baci2017/mri_segmented_bem.png)
*Figure4: 3 compartment segmentation output*

##  5A. Create the mesh

	cfg=[];
	cfg.tissue={'brain','skull','scalp'};
	cfg.numvertices = [3000 2000 1000];
	mesh_bem=ft_prepare_mesh(cfg,mri_segmented_3_compartment);

Visualize the mesh and the electrode

	load elec; %load the electrodes
	figure, ft_plot_mesh(mesh_bem(1),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)
	ft_plot_mesh(mesh_bem(2),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1) 
	ft_plot_mesh(mesh_bem(3),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1) 
	hold on, ft_plot_sens(elec, 'style', '*g');

![image](/static/img/workshop/baci2017/mesh_bem_elec.png)
*Figure5: 3 compartment mesh with electrodes*

##  6A. Create the headmodel

	cfg        = [];
	cfg.method ='dipoli'; % You can also specify 'bemcp', or another method.
	headmodel_bem       = ft_prepare_headmodel(cfg, mesh_bem);

<div class="warning">
In Windows the method 'dipoli' does not work. You can either load "headmodel_bem" and continue with this tutorial, or explore other BEM method like 'bemcp'. If you use 'bemcp', the conductivity field has a different order: {'brain', 'skull', 'skin'}.
</div>
##  7A. Align the electrodes

If the electrodes are not well aligned with the mesh, we can realign them wit

	cfg          = [];
	cfg.method   = 'interactive';
	cfg.elec     = elec;
	cfg.headshape = headmodel_bem.bnd;
	elec = ft_electroderealign(cfg);

Check the alignment visually.

	
	figure;
	ft_plot_axes(mesh_bem(1))
	hold on;
	ft_plot_mesh(mesh_bem,'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)
	ft_plot_sens(elec,'style', '.k'); 

![image](/static/img/workshop/baci2017/aligned.png)
*Figure6: mesh, electrodes and axes.*

##  8A. Create the sourcemodel

	cfg = [];
	cfg.grid.resolution = 7.5;
	cfg.threshold = 0.1;
	cfg.smooth = 5;
	cfg.vol = headmodel_bem;
	cfg.inwardshift = 1; %shifts dipoles away from surfaces
	sourcemodel = ft_prepare_sourcemodel(cfg, headmodel_bem);

Visualize the sourcemodel

	figure, ft_plot_mesh(sourcemodel.pos(sourcemodel.inside,:))
	hold on, ft_plot_mesh(mesh_bem(1),'surfaceonly','yes','vertexcolor','none','facecolor',...
	             'skin','facealpha',0.5,'edgealpha',0.1)

![image](/static/img/workshop/baci2017/sourcemodel_all.png)
*Figure7: sourcemodel on the brain compartment*

Save the sourcemode

	save sourcemodel sourcemodel;

##  9A. Compute the leadfield

	cfg = [];
	cfg.grid = sourcemodel;
	cfg.vol= headmodel_bem;
	cfg.elec = elec;
	cfg.reducerank = 3;
	leadfield_bem = ft_prepare_leadfield(cfg);

##  B. Finite Element Method (FEM)

##  4B. Segment the MRI

	cfg           = [];
	cfg.output    = {'scalp','skull','csf','gray','white'};
	cfg.brainsmooth    = 1;
	cfg.scalpthreshold = 0.11;
	cfg.skullthreshold = 0.15;
	cfg.brainthreshold = 0.15;
	mri_segmented_5_compartment = ft_volumesegment(cfg, mri_resliced); 

Visualize the segmentation result

	seg_i = ft_datatype_segmentation(mri_segmented_5_compartment,'segmentationstyle','indexed');
	
	cfg              = [];
	cfg.funparameter = 'seg';
	cfg.funcolormap  = gray(5); % distinct color per tissue
	cfg.location     = 'center';
	cfg.atlas        = seg_i;    % the segmentation can also be used as atlas
	ft_sourceplot(cfg, seg_i);
	

![image](/static/img/workshop/baci2017/mri_segmented_fem.png)
*Figure8: 5 compartment segmentation output *

##  5B. Create the mesh

	cfg        = [];
	cfg.shift  = 0.3;
	cfg.method = 'hexahedral';
	cfg.resolution = 1; % this is in mm
	mesh_fem = ft_prepare_mesh(cfg,mri_segmented_5_compartment);

##  6B. Create the headmodel

	cfg = [];
	cfg.method = 'simbio';
	cfg.conductivity = [0.43 0.0024 1.79 0.14 0.33]; % same as tissuelabel in vol_simbio
	cfg.tissuelabel = {'scalp', 'skull', 'csf', 'gray','white'};
	headmodel_fem = ft_prepare_headmodel(cfg, mesh_fem);

Visualize the headmodel and the electrodes (it might take time and memory)

	% csf: 1, gm: 2, scalp: 3, skull: 4, wm: 5
	ts = 3;
	figure
	mesh2 =[];
	mesh2.hex = headmodel_fem.hex(headmodel_fem.tissue==ts,:); %mesh2.hex(1:size(mesh2.hex),:);
	mesh2.pos =  headmodel_fem.pos;
	mesh2.tissue =  headmodel_fem.tissue(headmodel_fem.tissue==ts,:);%mesh.tissue(1:size(mesh2.hex),:);
	
	mesh_ed = mesh2edge(mesh2);
	patch('Faces',mesh_ed.poly,...
	    'Vertices',mesh_ed.pos,...
	    'FaceAlpha',.5,...
	    'LineStyle','none',...
	    'FaceColor',[1 1 1],...
	    'FaceLighting','gouraud');
	
	xlabel('coronal');
	ylabel('sagital');
	zlabel('axial')
	camlight; 
	axis on;
	
	ft_plot_sens(elec, 'style', '*g');

![image](/static/img/workshop/baci2017/mesh_fem_elec.png)
*Figure9: visualization of headmodel_fem and electrodes*

## 7B. Align the electrodes

If the electrodes are not well aligned with the mesh, we can realign them wit

	cfg          = [];
	cfg.method   = 'interactive';
	cfg.elec     = elec;
	cfg.headshape = headmodel_fem;
	elec = ft_electroderealign(cfg);

##  8B. Create the sourcemodel

We will use the sourcemodel already generated in 7A. 

	load('sourcemodel.mat');

##  9B. Compute the leadfield

<div class="warning">
Please DO NOT run *ft_prepare_vol_sens* in this tutorial session! It will take too much time and memory. Load "headmodel_fem_tr". </div>

	%% compute the transfer matrix
	[headmodel_fem_tr, elec] = ft_prepare_vol_sens(headmodel_fem, elec); 

	%% compute the leadfield
	cfg = [];
	cfg.grid = sourcemodel;
	cfg.vol= headmodel_fem_tr;
	cfg.elec = elec;
	cfg.reducerank = 3;
	leadfield_fem = ft_prepare_leadfield(cfg); 

## Summary and Comments

This tutorial was about the computation of leadfields that could be feed into the inverse problem which will be explain i
 [Inverse problem](/workshop/baci2017/inverseproblem).

-----
This tutorial was last tested on 27-08-2017 by Maria Carla Piastra on Ubuntu, Matlab 2015b.
