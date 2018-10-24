---
layout: default
---

### Sphere fitting and scaling of the template (Colin 27) MRI to the MEG polhemus headshape

	
	
	%% Sphere fitting and scaling of the template (Colin 27) MRI to the polhemus headshape
	
	clc;clear;close all;
	restoredefaultpath
	addpath('/nashome1/wexu/matlab/fieldtrip')
	ft_defaults
	
	load standard_mri %Colin 27 template in fieldtrip
	
	% read MEG sensor location
	MEG_sens = ft_read_sens('/nashome1/wexu/MNE_data/CN/MEG/CN19/CN19_raw_tsss_mc.fif');
	MEG_sens = ft_convert_units(MEG_sens,'mm');
	% read polhemus headshape
	headshape = ft_read_headshape('/nashome1/wexu/MNE_data/CN/MEG/CN19/CN19_raw_tsss_mc.fif');
	headshape    = ft_convert_units(headshape,'mm');
	
	save headshape headshape
	save MEG_sens MEG_sens
	
	% realign to neuromag coordinate system
	lpa=    [  7 104  26]; 
	nas=    [ 92 210  32];
	rpa=    [176 104  26];
	zpoint= [ 92 106 139];
	
	cfg                = [];
	cfg.method         = 'fiducial';
	cfg.fiducial.nas    = nas;
	cfg.fiducial.lpa    = lpa;
	cfg.fiducial.rpa    = rpa;
	cfg.fiducial.zpoint = zpoint;
	cfg.coordsys       = 'neuromag';
	mri_realigned_fiducial      = ft_volumerealign(cfg,mri);
	
	cfg           = [];
	cfg.output    = {'brain','skull','scalp'};
	segmentedmri  = ft_volumesegment(cfg, mri);
	
	T_neuromag=mri_realigned_fiducial.transform;
	segmentedmri.transform=T_neuromag;
	segmentedmri.coordsys='neuromag';
	
	cfg             = [];
	cfg.tissue      = {'brain'};
	cfg.numvertices = 3600;
	brain           = ft_prepare_mesh(cfg, segmentedmri);
	
	cfg             = [];
	cfg.tissue      = {'scalp'};
	cfg.numvertices = [3600];
	bnd             = ft_prepare_mesh(cfg, segmentedmri);
	
	% remove the lower part of the head
	cfg=[];
	cfg.translate=[0 0 -140];
	cfg.scale=[300 300 300];
	cfg.selection='outside';
	bnd_deface=ft_defacemesh(cfg,bnd);
	
	% remove digitized head points on the nose
	cfg=[];
	cfg.translate=[0 90 -50];
	cfg.scale=[400 400 100];
	cfg.selection='outside';
	headshape_denosed=ft_defacemesh(cfg,headshape);
	
	
	figure
	ft_plot_headshape(headshape);
	hold on
	ft_plot_mesh(bnd_deface, 'edgecolor', 'none', 'facecolor', 'skin', 'facealpha',0.9)
	ft_plot_mesh(brain, 'edgecolor', 'none', 'facecolor', [1 0 1]/1.2, 'facealpha',  0.5)
	ft_plot_axes(headshape_denosed)
	camlight left
	camlight right
	material dull
	alpha 0.8
	lighting phong
	
	%fit a sphere to MRI template
	cfg=[];
	cfg.method='singlesphere';
	scalp_sphere=ft_prepare_headmodel(cfg,bnd_deface);
	
	%fit a sphere to polhemus headshape
	cfg=[];
	cfg.method='singlesphere';
	headshape_sphere=ft_prepare_headmodel(cfg,headshape_denosed);
	
	%scale the template MRI
	scale=headshape_sphere.r/scalp_sphere.r;
	
	T2=[1 0 0 scalp_sphere.o(1);
	    0 1 0 scalp_sphere.o(2);
	    0 0 1 scalp_sphere.o(3);
	    0 0 0 1                ];
	
	T1=[1 0 0 -scalp_sphere.o(1);
	    0 1 0 -scalp_sphere.o(2);
	    0 0 1 -scalp_sphere.o(3);
	    0 0 0 1                 ];
	
	S= [scale 0 0 0;
	    0 scale 0 0;
	    0 0 scale 0;
	    0 0 0 1 ];
	
	TRANSFORM=T1*S*T2;
	
	segmentedmri.transform=TRANSFORM*T_neuromag;
	
	
	cfg             = [];
	cfg.tissue      = {'scalp'};
	cfg.numvertices = 3600;
	scalp_scaled    = ft_prepare_mesh(cfg, segmentedmri);
	
	
	cfg             = [];
	cfg.tissue      = {'brain'};
	cfg.numvertices = 3600;
	brain_scaled    = ft_prepare_mesh(cfg, segmentedmri);
	
	figure
	%ft_plot_sens(MEG_sens, 'style', '*b');
	ft_plot_headshape(headshape_denosed);
	hold on
	ft_plot_mesh(scalp_scaled, 'edgecolor', 'none', 'facecolor', [1 1 1]/1.2, 'facealpha',  0.5)
	ft_plot_mesh(brain_scaled, 'edgecolor', 'none', 'facecolor', [1 0 1]/1.2, 'facealpha',  0.5)
	ft_plot_axes(headshape_denosed)
	camlight left
	camlight right
	material dull
	alpha 0.8
	lighting phong
	

