---
layout: default
---

{{tag>faq source forward inverse warning}}
## How can I visualize the different geometrical objects that are needed for forward and inverse computations?

For forward and inverse computations several geometrical objects need to be correctly coregistered. It's good practice to verify this coregistration before proceeding with the next steps of the analysis. The simplest way of verification is obviously visual inspection. FieldTrip allows for the plotting of various geometrical objects by means of the functions in the [plotting module](/development/plotting). Earlier versions of FieldTrip contained **[ft_headmodelplot](/reference/ft_headmodelplot)**, a high-level function. This function is now deprecated and the code is not anymore supported by the FieldTrip team. The function has been moved to fieldtrip/compat. If you still want to use it, you need to move it back to your main FieldTrip path because the function depends on low-level private functions in the private directory. The following describes how you can use the lower-level plotting functions for the visualization. 

`<note warning>`
The visualization of multisphere volume conductor models for MEG is not supported by the low-level plotting functions. Should you want to use that, you need to resort to ft_headmodelplot.
`</note>`

`<note warning>`
In general, we advise to use the singleshell as a volume conductor model for MEG, rather than the multisphere model.
`</note>`\\

The following code shows how to visualize the gradiometer positions in combination with the subject's headshape and the single sphere volume conductor model. We use the example data which can be obtained from [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/Subject01.zip).\\

	
	
	% read in single sphere volume conductor model
	vol  = ft_read_vol('Subject01.hdm');
	
	% read in the gradiometer description
	hdr  = ft_read_header('Subject01.ds'); 
	grad = hdr.grad;
	
	% read in the headshape
	shape = ft_read_headshape('Subject01.shape');
	shape = rmfield(shape, 'fid'); % remove the fiducials -> these are stored in MRI-voxel coords
	
	% plot
	ft_plot_sens(grad);
	ft_plot_vol(vol, 'facecolor', 'none');
	ft_plot_headshape(shape);
	


