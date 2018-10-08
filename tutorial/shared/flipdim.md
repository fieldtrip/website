---
layout: default
---

### Checking your segmented volumes

Flipping dimensions after segmenting the volumes (gray, white, and CSF) can easily introduce offsets. Make sure they are correctly aligned with the anatomical scan. See the following procedure. 

The example segmented data is available at [ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/beamformer/segmentedmri.mat](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial/beamformer/segmentedmri.mat).   


	load segmentedmri
	
	mri = ft_read_mri('Subject01.mri');
	segmentedmri.transform = mri.transform;
	segmentedmri.anatomy   = mri.anatomy;
	
	figure
	cfg = [];
	ft_sourceplot(cfg,segmentedmri); %only mri
	figure
	cfg.funparameter = 'gray';
	ft_sourceplot(cfg,segmentedmri); %segmented gray matter on top
	figure
	cfg.funparameter = 'white';
	ft_sourceplot(cfg,segmentedmri); %segmented white matter on top
	figure
	cfg.funparameter = 'csf';
	ft_sourceplot(cfg,segmentedmri); %segmented csf matter on top


{{:example:mnispace:segmentcheck_right.jpg|}}


When the segmented volumes are not correctly aligned with the anatomical volume, they could look like this. 

{{:example:mnispace:segmentcheck_wrong.jpg|}}

In this particular example, the volumes are flipped one too many times around the x-axis. In order to solve this, one could flip the image around the x-axis again before preparing the headmodel. For exampl


	segmentedmri.gray  = flipdim(segmentedmri.gray,1);
	segmentedmri.white = flipdim(segmentedmri.white,1);
	segmentedmri.csf   = flipdim(segmentedmri.csf,1);


