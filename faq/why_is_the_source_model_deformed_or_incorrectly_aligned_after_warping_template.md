---
title: Why is the source model deformed or incorrectly aligned after warping template?
tags: [faq, sourcemodel, mri, normalization]
---

# Why is the source model deformed or incorrectly aligned after warping template?

A commonly used strategy to create a source model is to start with a [template source model](/template/sourcemodel/#grid-search-in-dipole-fitting) and warp or spatially deform it to the individual subject's anatomy. Warping templates makes it easy to average source estimates across subjects and do group analysis without any interpolation. This is usually done with **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** before doing the source reconstruction, see for example in [this tutorial](/tutorial/sourcemodel/#performing-group-analysis-on-3-dimensional-source-reconstructed-data).

The procedure requires estimating a transformation between the subject's anatomy and the template anatomy. This procedure can go wrong, and the source model can then end up outside the head/brain volume. That is why it is important to inspect the warped source model:

    % Plot head model and warped source model
    figure; hold on
    ft_plot_headmodel(headmodel, 'edgecolor', 'none', 'facealpha', 0.4,'facecolor', 'b');
    ft_plot_mesh(sourcespace.pos(sourcespace.inside,:));

{% include image src="/assets/img/faq/why_is_the_source_model_deformed_or_incorrectly_aligned_after_warping_template/sourcespace.png" %}

You can see that the source points are not well contained withing the head model. As a consequence, activity will be estimated outside the subject's head. Be aware that - once the source model coordinates are set back to the template coordinates - it will look as if there are no errors. The template source model will align perfectly with the template anatomy, it is just the estimated activity that will appear on the wrong place.

The error stems from the warping of the template MRI to the individual subject's MRI. To transform the template to the subject's anatomy, **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)** first does a normalization of the individual subject's MRI to the template, this gives a transformation matrix. It then inverts this transformation and applies it to the template grid. Therefore, if the normalization goes wrong, or finds a sub-optimal solution, it will create a bad inverted transformation and apply it to the template source model. We have seen this happening due to from sub-optimal anatomical MRIs, e.g., without proper contrast normalization, or with MRI scans where parts of the head are outside the field of view. An example is shown below:

{% include image src="/assets/img/faq/why_is_the_source_model_deformed_or_incorrectly_aligned_after_warping_template/bad_mri.png" %}

When you observe a inverse warped template grid that is weird, you can do a "manual" normalization with **[ft_volumenormalise](/reference/ft_volumenormalise)** to see if it is due to normalization errors.

    %% Warp MRI to template with default parameters
    cfg = [];
    cfg.spmversion = 'spm8'; % default is now spm12
    cfg.nonlinear = 'yes';
    mri_spm8 = ft_volumenormalise(cfg, mri)

    %% Plot warped image
    cfg = [];
    cfg.paramter = 'anatomy';
    ft_sourceplot(cfg, mri_spm8)

{% include image src="/assets/img/faq/why_is_the_source_model_deformed_or_incorrectly_aligned_after_warping_template/Cronenberg.png" %}

{% include markup/skyblue %}
In early 2020 we switched the default SPM version used by FieldTrip from SPM8 to SPM12.
{% include markup/end %}

In the past **[ft_volumenormalise](/reference/ft_volumenormalise)** would by default use SPM8 for normalization. SPM8 starts with an initial rough alignment of the whole MRI before stripping the skull. This rough estimation matches the intensity of the two images (for full documentation see the help for **spm_normalise**). If SPM is unable to do a good initial match, the subsequent normalization fails and so do the following steps.

The solution is to normalize MRIs with `cfg.spmversion = 'spm12'` and add `cfg.spmmethod = 'new'`.

    %% Warp MRI to template with new parameters
    cfg = [];
    cfg.spmversion = 'spm12';
    cfg.nonlinear = 'yes';
    cfg.spmmethod = 'new';
    mri_spm12 = ft_volumenormalise(cfg, mri)

    %% Plot warped image
    cfg = [];
    cfg.paramter = 'anatomy';
    ft_sourceplot(cfg, mri_spm12)

{% include image src="/assets/img/faq/why_is_the_source_model_deformed_or_incorrectly_aligned_after_warping_template/fixed_mri.png" %}

You should add these configuration options to the `cfg` structure when calling **[ft_prepare_sourcemodel](/reference/ft_prepare_sourcemodel)**. These options will be passed on to **[ft_volumenormalise](/reference/ft_volumenormalise)**. Do note that the new SPM12 method is much slower than the old method.

    % Prepare source model with new SPM method
    cfg = [];
    cfg.warpmni = 'yes';
    cfg.nonlinear = 'yes';
    cfg.unit = 'mm';
    cfg.template = template_grid;
    cfg.mri = mri;
    cfg.spmversion = 'spm12';  
    cfg.spmmethod = 'new'      % default is 'old'

    sourcespace = ft_prepare_sourcemodel(cfg);

Inspect the warped source model as before:

    % Plot head model and warped source model
    figure; hold on
    ft_plot_headmodel(headmodel, 'edgecolor', 'none', 'facealpha', 0.4,'facecolor','b');
    ft_plot_mesh(sourcespace.pos(sourcespace.inside,:));

{% include image src="/assets/img/faq/why_is_the_source_model_deformed_or_incorrectly_aligned_after_warping_template/sourcespace_fixed.png" %}

As an alternative you can consider using **[ft_volumebiascorrect](/reference/ft_volumebiascorrect)**.
