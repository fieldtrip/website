---
title: How can I use the ivar, uvar, wvar and cvar options to precisely control the permutations?
parent: Statistical analysis
grand_parent: Frequently asked questions
category: faq
tags: [statistics]
redirect_from:
    - /faq/how_can_i_use_the_ivar_uvar_wvar_and_cvar_options_to_precisely_control_the_permutations/
    - /faq/clusterstats_iuwcvar/
---

# How can I use the ivar, uvar, wvar and cvar options to precisely control the permutations?

In **[ft_timelockstatistics](/reference/ft_timelockstatistics)**, **[ft_freqstatistics](/reference/ft_freqstatistics)**, and **[ft_sourcestatistics](/reference/ft_sourcestatistics)** you can specify cfg.method='montecarlo' to use the permutation framework to get an estimate of the probability of the null-hypothesis that the data can be exchanged over the conditions. If that probability is low, you usually reject the null-hypothesis (H0) in favor of the alternative hypothesis (H1).

However, not all permutations of the data are relevant for making a decision between the H0 and H1 in which you are interested. It might for example be that you have observed data for two conditions in 10 subjects. In that case, you probably are interested in whether the data is different for the conditions within a subject. So, you don't want to randomly shuffle the data over all subjects, but instead would like to know whether or not shuffling _within_ the subjects destroys the difference between the conditions. In conventional statistics, you might use a [paired two-samples t-test](https://en.wikipedia.org/wiki/Student's_t-test).

The Monte Carlo method (cfg.method='montecarlo') allows you to specify in detail the allowed permutations for the columns of your experimental design matrix. You can use the following options.

    cfg.ivar             = number or list with indices, independent variable(s)
    cfg.uvar             = number or list with indices, unit variable(s)
    cfg.wvar             = number or list with indices, within-cell variable(s)
    cfg.cvar             = number or list with indices, control variable(s)

The "Independent variable" codes the condition numbers. This is the crucial variable in any permutation test, with which you want to investigate whether there is a difference between the conditions. The null hypothesis involves that the data are assumed to be independent from the condition number, and therefore (under this null hypothesis) any reshuffling of the condition numbers does NOT affect the outcome in a systematic way.

The "Unit of observation variable" corresponds to the subject number (in a
within-subject manipulation) or the trial number (in a within-trial
manipulation). It is best understood by considering that it corresponds
to the "pairing" of the data in a paired T-test or repeated measures
ANOVA. The uvar affects the "resampling" (a bit of a confusing name) outcome in the way that only
permutations of condition numbers within one unit of observation are returned.

The "Within-cell variable" corresponds to the grouping of the data in
cells, where the multiple observations in a group should not be broken
apart. This for example applies to multiple tapers in a spectral estimate
of a single trial of data (the "rpttap" dimension), where different
tapers should not be redistributed over different conditions. Another example is a blocked
fMRI design, with a different condition in each block and multiple
repetitions of the same condition within a block. Assuming that there is
a slow HRF that convolutes the trials within a block, you can shuffle the
blocks but not the individual trials in a block.

The "Control variable" allows you to specify blocks within which the permutation should
be done, while controlling that repetitions are not permuted _between_ different control blocks. Specifying a control variable is an excellent way to control for a potentially confounding variable that associated with your independent variable.

If you want to understand in detail what the consequences are of specifying these options, I suggest you to do "cd fieldtrip/private" and "edit resampledesign". That is the low-level function used for the permutations and other resamplings.
