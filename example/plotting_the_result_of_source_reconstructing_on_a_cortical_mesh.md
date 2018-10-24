---
layout: default
tags: [example, plot, source]
---

## Plotting the result of source reconstructing on a cortical mesh

The following function can be used to plot the results of source reconstruction on a cortical surface sheet. It assumes a cortical sheet *surf*, described by vertices (pnt) and triangles (tri). The vertices can be used as positions in **[ft_sourceanalysis](/reference/ft_sourceanalysis)** by specifying cfg.grid.pos = surf.pnt.

	
	function [handles] = myownsurfplot(cfg,surf,source)
	
	% function [handles] = myownsurfplot(cfg,surf,source)
	%
	% allows to plot source results obtained from a cortical mesh
	%
	% cfg - opacity: specifies the opacities of the vertices e.g. [0,1]
	% cfg - colormapping: defines the colorrange of the vertices e.g. [0,1]
	% cfg - edgealpha: defines the transparency of the edges for identifying gyri & sulci, e.g. 0.2
	% cfg - mask matrix specifying opacity, format: [n,1] for n vertices
	
	if nargin < 3
	    cfg = struct();
	end;
	
	    
	cortex_light = [0.781 0.762 0.664];
	cortex_dark  = [0.781 0.762 0.664]/2;
	
	  
	sourcevals = source.avg.pow(:);
	backgcolor = repmat(cortex_light, size(surf.pnt,1), 1);
	
	if ~isfield(cfg,'opacity')
	    opacmin = min((source.avg.pow(:)));
	    opacmax = max((source.avg.pow(:)));
	else
	    opacmin = cfg.opacity(1);
	    opacmax = cfg.opacity(2);
	end;
	if ~isfield(cfg,'colormapping')
	    fcolmin = min((source.avg.pow(:)));
	    fcolmax = max((source.avg.pow(:)));
	else
	    fcolmin = cfg.opacity(1);
	    fcolmax = cfg.opacity(2);
	end;
	if ~isfield(cfg,'edgealpha'), edgealpha = 1; end;
	if ~isfield(cfg,'mask'), 
	    maskval = source.avg.pow(:);
	else
	    maskval = cfg.mask;
	end;
	
	
	figure;
	
	h1 = patch('Vertices', surf.pnt, 'Faces', surf.tri, 'FaceVertexCData', backgcolor , 'FaceColor', 'interp');
	%set(h1, 'EdgeColor', 'none');
	set(h1, 'EdgeColor', [0,0,0],'EdgeAlpha',edgealpha);
	axis   off;
	axis vis3d;
	axis equal;
	
	h2 = patch('Vertices', surf.pnt, 'Faces', surf.tri, 'FaceVertexCData', sourcevals , 'FaceColor', 'interp');
	%set(h2, 'EdgeColor',  'none');
	set(h2, 'EdgeColor', [0,0,0],'EdgeAlpha',edgealpha);
	set(h2, 'FaceVertexAlphaData', maskval);
	set(h2, 'FaceAlpha',          'interp');
	set(h2, 'AlphaDataMapping',   'scaled');
	alim(gca, [opacmin opacmax]);
	caxis(gca,[fcolmin fcolmax]);
	lighting gouraud
	
	colorbar;
	
	handles.h1 = h1;
	handles.h2 = h2;
	

