---
title: Why should I use the cfg.correcttail option when using statistics_montecarlo?
category: faq
tags: [statistics, cluster]
redirect_from:
    - /faq/why_should_i_use_the_cfg.correcttail_option_when_using_statistics_montecarlo/
    - /faq/clusterstats_correcttail/
---

# Why should I use the cfg.correcttail option when using statistics_montecarlo?

When running statistics using **[ft_freqstatistics](/reference/ft_freqstatistics)**, **[ft_timelockstatistics](/reference/ft_timelockstatistics)**, or **[ft_sourcestatistics](/reference/ft_sourcestatistics)** with `cfg.method = 'montecarlo'` you are presented with the option `cfg.correcttail`, which is relevant when you are doing a two-sided test:

    % cfg.correcttail = correct p-values or alpha-values when doing a two-sided test, 'alpha','prob' or 'no' (default = 'no')

{% include markup/yellow %}
When doing a two-sided test with alpha = 0.05 and *not correcting*, you are effectively testing with alpha = 0.1.
{% include markup/end %}

## Correct alpha

In case of a two-tailed test, the type-I error rate (alpha) refers to both tails
of the distribution, whereas the `stat.prob` value computed with the montecarlo
method corresponds to one tail, i.e. the probability, under the assumption of no
effect or no difference (the null hypothesis), of obtaining a result equal to or
more extreme than what was actually observed. The decision rule whether the
null-hypothesis should be rejected given the observed probability therefore
should consider alpha divided by two, to correspond with the probability in one
of the tails (the most extreme tail).

In case of a two-sided test, with alpha = 0.05, the configuration would contain:

    cfg.alpha       = 0.05;
    cfg.tail        = 0; % two-sided test
    cfg.correcttail = 'alpha';

This is conceptually equivalent to performing a Bonferroni correction for the
two tails, i.e., divide alpha by two. Each tail will be tested with alpha = 0.025.

## Correct probabilities

An alternative solution to distribute the alpha level over both tails is
achieved by multiplying the probability with a factor of two, prior to
thresholding it with cfg.alpha. The advantage of this solution is that
it results in a p-value that corresponds with a parametric probability.

Use the following configuration:

    cfg.alpha       = 0.05;
    cfg.tail        = 0; % two-sided test
    cfg.correcttail = 'prob';

Effectively, this means multiplying the p-values (in `stat.prob`, `stat.posclusters.prob` and `stat.negclusters.prob`) with a factor of two.
