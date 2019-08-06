---
title: Source space is deformed or wrongly aligned after warping template
tags: [faq, sourcespace, MRI, normalisation, preprocessing]
---
# Source space is deformed or wrongly aligned after warping template

It is common to create a source space that is a warped version of a [template source space](http://www.fieldtriptoolbox.org/template/sourcemodel/#grid-search-in-dipole-fitting) to the individual subject's anatomy. Warping templates makes it possible to average across subjects and do group analysis on the anatomical level. This step is usually done when creating the source space with **ft_prepare_sourcemodel** before doing the source reconstruction (see http://www.fieldtriptoolbox.org/tutorial/sourcemodel/#performing-group-analysis-on-3-dimensional-source-reconstructed-data).

The procedure requires estimating a transformation between the subject's anatomy and the template anatomy. This procedure can go wrong, and the source space ends up outside the head/brain volume.

Inspect the warped source space:

```Octave
% Plot head model and warped source space
figure; hold on
ft_plot_headmodel(headmodel, 'edgecolor', 'none', 'facealpha', 0.4,'facecolor','b');
ft_plot_mesh(sourcespace.pos(sourcespace.inside,:));
```

{% include image src="/assets/img/faq/source_space_is_deformed_or_wrongly_aligned_after_warping_template/sourcespace.png" %}

The source points are not well contained withing the head model. 
As a consequence, there will appear to activity outside the subject's head.

Be aware that once the source space coordinates are set back to the template coordinates, it looks as if there are no errors as it will align perfectly with the template anatomy.

The error stems from the warping of the template MRI to subject MRI. To transform the template to the subject's anatomy, ft_prepare_sourcespace first does normalization of the individual subject's MRI to the template to get the transformation. It then inverts the transformation and applies it to the template grid. Therefore, if the normalization goes wrong, or finds a sub-optimal solution, it will create a bad inverted transformation and apply it to the template source space. Errors might come from sub-optimal MRI, e.g., without proper contrast normalization or images where parts of the head are cut off. For example, as is the case below:

{% include image src="/assets/img/faq/source_space_is_deformed_or_wrongly_aligned_after_warping_template/bad_mri.png" %}

You can do a "manual" normalization with **ft_volumenormalise** to see if the error in the source space warping might be due to normalization errors. 

```Octave
%% Warp MRI to template with default parameters
cfg = [];
cfg.spmversion  = 'spm8';
cfg.nonlinear   = 'yes';
mri_spm8 = ft_volumenormalise(cfg, mri)

%% Plot warped image
cfg = [];
cfg.paramter = 'anatomy';
ft_sourceplot(cfg, mri_spm8)
```

{% include image src="/assets/img/faq/source_space_is_deformed_or_wrongly_aligned_after_warping_template/Cronenberg.png" %}

As a default ft_volumenormalize will use SPM8 for volume normalization. SPM8 initially align based on an initial rough alignment of all of the MRI based on before stripping the skull. The rough estimation is based on simply matching the intensity of the two images (for full documentation see help for **spm_normalise**). If SPM is unable to do a good initial match, then the normalization goes wrong and so do the following steps.

The solution to the problem is to switch the method FieldTrip use to normalize MRIs. Change _cfg.spmversion_ to _SPM12_ and add _cfg.spmmethod_ = _new_.

```Octave
%% Warp MRI to template with new parameters
cfg = [];
cfg.spmversion  = 'spm12';
cfg.nonlinear   = 'yes';
cfg.spmmethod   = 'new';
mri_spm12 = ft_volumenormalise(cfg, mri)

%% Plot warped image
cfg = [];
cfg.paramter = 'anatomy';
ft_sourceplot(cfg, mri_spm12)
```

{% include image src="/assets/img/faq/source_space_is_deformed_or_wrongly_aligned_after_warping_template/fixed_mri.png" %}

Add config options to the _cfg_ structure when calling **ft_prepare_sourcemodel**. The config options will be passed on to **ft_volumenormalise**. Note that the new SPM method is much slower than the old method.

```Octave
% Prepare source model with new SPM method
cfg = [];
cfg.warpmni         = 'yes';
cfg.nonlinear       = 'yes';
cfg.unit            = 'mm';
cfg.template        = template_grid;
cfg.mri             = mri;
cfg.spmversion      = 'spm12';   % default is 'spm8'
cfg.spmmethod       = 'new'      % default is 'old'

sourcespace = ft_prepare_sourcemodel(cfg);
```

Inspect the warped source space as before:

```Octave
% Plot head model and warped source space
figure; hold on
ft_plot_headmodel(headmodel, 'edgecolor', 'none', 'facealpha', 0.4,'facecolor','b');
ft_plot_mesh(sourcespace.pos(sourcespace.inside,:));
```

{% include image src="/assets/img/faq/source_space_is_deformed_or_wrongly_aligned_after_warping_template/sourcespace_fixed.png" %}
