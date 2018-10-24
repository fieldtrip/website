---
layout: default
tags: [example, eeg, fem, leadfield, headmodel]
---

# Example script for leadfield based on FEM headmodel

	%% read mri
	if ispc
	    datadir = 'H:';
	else
	    datadir = '/home';
	end
	
	mri = ft_read_mri(strcat(datadir,'/common/matlab/fieldtrip/data/Subject01.mri'));
	
	%% segmentation
	
	cfg          = [];
	cfg.output   = {'gray', 'white', 'csf','skull','scalp'};
	segmentedmri = ft_volumesegment(cfg,mri);
	    
	%% mesh
	
	cfg        = [];
	cfg.shift  = 0.3;
	cfg.method = 'hexahedral';
	mesh       = ft_prepare_mesh(cfg,segmentedmri);
	
	%% volume conductor
	
	cfg              = [];
	cfg.method       = 'simbio';
	cfg.conductivity = [0.33 0.14 1.79 0.01 0.43];    
	vol              = ft_prepare_headmodel(cfg,mesh);
	
	%% electrode alignment
	
	elec = ft_read_sens(strcat(datadir,'/common/matlab/fieldtrip/template/electrode/standard_1020.elc'));
	mri = ft_read_mri(strcat(datadir,'/common/matlab/fieldtrip/data/Subject01.mri'));
	
	
	nas = mri.hdr.fiducial.head.nas;
	lpa = mri.hdr.fiducial.head.lpa;
	rpa = mri.hdr.fiducial.head.rpa;
	
	 
	fiducials.chanpos = [nas; lpa; rpa];
	fiducials.label   = {'Nz','LPA','RPA'};
	fiducials.unit    = 'mm';
	  
	cfg          = [];
	cfg.method   = 'fiducial';
	cfg.template = fiducials;
	cfg.elec     = elec;
	cfg.fiducial = {'Nz', 'LPA', 'RPA'};
	elec_align   = ft_electroderealign(cfg);
	
	% add 12 mm to x-axis 
	
	n=size(elec_align.chanpos,1);
	for i=1:n
	   elec_align.chanpos(i,1)=elec_align.chanpos(i,1)+12; 
	   elec_align.elecpos(i,1)=elec_align.elecpos(i,1)+12; 
	end
	
	% figure;
	% ft_plot_sens(elec_align,'style','sr','label','label');
	% hold on;
	% ft_plot_mesh(mesh,'edgeonly','yes','vertexcolor','none','facecolor',[0.5 0.5 0.5],'facealpha',1,'edgealpha',0.1)
	     
	%% make grid (sourcemodel): 
	% At the moment the sourcemodel is defined prior
	% to the leadfield because ft_prepare_sourcemodel does not automatically create 
	% a sourcemodel based on a hexahedral vol.
	
	cfg                 = [];
	cfg.mri             = mri;
	cfg.sourceunits     = vol.unit;
	grid                = ft_prepare_sourcemodel(cfg);
	
	
	cfg      = [];
	cfg.vol  = vol;  
	cfg.elec = elec_align;
	cfg.grid = grid;
	lf       = ft_prepare_leadfield(cfg);
	
	% plot the leadfield for a few representative locations: points around
	% z-axis with increasing z values
	
	
	plotpos = [];
	positions=[];
	n=size(lf.pos,1);
	p=1;
	for i = 1:n
	    if lf.pos(i,1)==-0.1 && lf.pos(i,2)==-0.2
	        plotpos(p)=i;
	        positions(p,:)=lf.pos(i,:);
	        p=p+1;
	    end
	end
	
	positions;
	
	%n=length(plotpos);
	
	figure;
	for i=1:20
	            
	    subplot(4,5,i);
	    ft_plot_topo3d(lf.cfg.elec.chanpos,lf.leadfield{plotpos(i)}(:,3));
	    %view([0 0]);
	       
	    
	end
	

