---
title: Getting started with fMRI timeseries data
tags: [dataformat, fmri]
---

# Getting started with fMRI timeseries data

Although FieldTrip is not designed for processing functional MRI data, you can nevertheless read data from NIFTI files and use the various timeseries, spectral and statistical analysis methods on that data.

## As channel-level raw data

The FieldTrip [raw data structure](/reference/utilities/ft_datatype_raw) requires that each voxel timeseries is represented as a channel with a label.

```
fmridata = ft_read_mri('sub-01_ses-mri_task-facerecognition_run-01_bold.nii', 'outputfield', 'functional');

ntime = fmridata.dim(4);
nchan = prod(fmridata.dim(1:3));

tr = fmridata.hdr.niftihdr.pixdim(4);

tim = ((1:ntime)-1) * tr;                        % the time vector starts at t=0 seconds
dat = reshape(fmridata.functional, nchan, ntime) % reshape it into a chan*time matrix

% represent the data as one continuous trial
data = [];
data.time = {tim};
data.trial = {dat}
data.fsample = 1/tr;
data.label = cell(nchan,1);
for i=1:nchan
  data.label{i} = sprintf('voxel%08d', i);
end
```

With so many channels, you will notice that some FieldTrip functions will be slow. This is mainly due to the bookkeeping that those functions do, as each call to a function will involve selecting the channels of interest and hence comparing two long lists of strings.

## As source-level data

You can also represent the 4D timeseries data as a source representation, similar how virtual-channel timeseries are represented, for example from an LCMV beamformer estimate.

```
filename3d = 'sub-01_ses-mri_acq-mprage_T1w.nii';                    % 3D anatomical
filename4d = 'sub-01_ses-mri_task-facerecognition_run-01_bold.nii';  % 4D functional

%%

volume3d = ft_read_mri(filename3d);
volume4d = ft_read_mri(filename4d, 'outputfield', 'functional');

volume4d.avg = mean(volume4d.functional, 4);
volume4d.std = std(volume4d.functional, [], 4);

tr = volume4d.hdr.niftihdr.pixdim(4);

volume3d = ft_checkdata(volume3d, 'datatype', 'volume', 'insidestyle', 'logical');
volume4d = ft_checkdata(volume4d, 'datatype', 'volume', 'insidestyle', 'logical');

%%

figure
ft_plot_ortho(volume3d.anatomy, 'transform', volume3d.transform, 'style', 'intersect');
ft_plot_ortho(volume4d.std, 'transform', volume4d.transform, 'style', 'intersect', 'colormap', 'jet');

%%

source3d = ft_checkdata(volume3d, 'datatype', 'source');
source4d = ft_checkdata(volume4d, 'datatype', 'source'); % note the warning: could not determine dimord of "functional"

% add the time axis that describes the 4th dimension of the functional data
source4d.time = (0:volume4d.dim(4)-1) * tr;

% reshape the functional data so that it is pos*time
source4d = ft_checkdata(source4d, 'datatype', 'source');

%%

cfg = [];
cfg.anaparameter = [];
cfg.funparameter = 'std';
cfg.funcolormap = 'jet';
ft_sourceplot(cfg, source4d);
```

## Parcellate and average over a region of interest

In many cases you have a region of interest (ROI) over which you want to average, for example based on an anatomical atlas or a prior GLM analysis resulting in a specific ROI.

```
% The next sequence of steps will
% - define ROIs on basis of the original 3D anatomical data
% - interpolate the ROIs from the 3D onto the 4D representation
% - average the non-interpolated functional data over some parcels

% make a structure with subject-specific ROIs starting from the original 3D anatomical representation
parcellation3d = rmfield(source3d, 'anatomy');

% here we make three ROIs, each is a slab that spans 1/3rd of the whole volume
% this first representation is "probabilistic"
parcellation3d.roi1 = false(parcellation3d.dim); parcellation3d.roi1(1:end,1:end,1:64) = true;
parcellation3d.roi2 = false(parcellation3d.dim); parcellation3d.roi2(1:end,1:end,65:128) = true;
parcellation3d.roi3 = false(parcellation3d.dim); parcellation3d.roi3(1:end,1:end,129:192) = true;

% this converts it to an "indexed" representation
parcellation3d = ft_checkdata(parcellation3d, 'type', 'parcellation', 'parcellationstyle', 'indexed')

cfg = [];
cfg.anaparameter = [];
cfg.funparameter = 'tissue';
cfg.funcolormap = 'jet';
ft_sourceplot(cfg, parcellation3d);

% interpolate the 3D tissue parcellation onto the voxel positions of the lower resolution 4D representation
cfg = [];
cfg.parameter = 'all';
cfg.interpmethod = 'nearest';
parcellation4d = ft_sourceinterpolate(cfg, parcellation3d, source4d)

cfg = [];
cfg.anaparameter = [];
cfg.funparameter = 'tissue';
cfg.funcolormap = 'jet';
ft_sourceplot(cfg, parcellation4d);

cfg = [];
cfg.parcellation = 'tissue';
rawdata3d = ft_sourceparcellate(cfg, source3d, parcellation3d);
rawdata4d = ft_sourceparcellate(cfg, source4d, parcellation4d);

```

The data is now represented again as a raw data structure as returned by **[ft_preprocessing](/reference/ft_preprocessing)**, but only with a few channels.

You could also do the interpolation the other way around, but interpolating the relatively low-resolution 4D data on the high-resolution 3D requires a lot of memory.

## Parcellate using an atlas

It is also possible to use an atlas for the parcellation, see [here](/template/atlas) for a description of the template atlases that are included. Note that you can also construct and use your own atlas, the only requirement is that it represented as a [parcellated](/reference/utilities/ft_datatype_parcellation) or [segmented](/reference/utilities/ft_datatype_segmentation) data structure with an indexed representation, i.e. each voxel or vertex belongs to a single tissue type.

```

[ftver, ftpath] = ft_version;
atlas = ft_read_atlas(fullfile(ftpath, 'template', 'atlas', 'aal', 'ROI_MNI_V4.nii'));

%%

% You could now
% - interpolate the 4D functional data onto the 3D anatomical
% - spatially transform both the 3D and the 4D to the MNI template
% - interpolate the atlas onto the 3D and 4D representation
% - average the interpolated and transformed functional data over some parcels

%%

% You could also
% - spatially transform the atlas to the 3D anatomical
% - interpolate the atlas onto the 3D and 4D representation
% - average the non-interpolated functional data over some parcels
```
