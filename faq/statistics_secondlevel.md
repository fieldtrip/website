---
title: What is the idea behind statistical inference at the second-level?
category: faq
tags: [statistics, cluster]
redirect_from:
    - /faq/what_is_the_idea_behind_statistical_inference_at_the_second-level/
    - /faq/statistics_secondlevel/
---

# What is the idea behind statistical inference at the second-level?

A common approach for statistical inference is to split the statistics into two levels. At level 1 you compute a within-subject statistic which **describes** the effect size (i.e. no inference). At level 2 you do the **inference**, testing whether the effect is consistent over subjects.

Conventionally you would do the inference over the single subject between-condition difference in the averages. Here you replace the difference between the averages by another difference measure. Using the t-score as the measure of difference suppresses differences in the non-consistent parts of the data (e.g., channels that don't show an effect and time points in the baseline) and stresses the difference in consistent large-effect channels. The second level statistical inference thereby becomes more sensitive. Furthermore, the multiple comparison problem at the second level becomes easier to solve using randomization testing, because the randomization distribution will be less broadened by the uninteresting noisy parts of the data.

Some notes:

1.  also in conventional statistics you do it in two steps: the first being the computation of the difference in a measure of central tendency (the mean), the second being the inference based on the between-subject consistency of these difference scores. The first step in conventional statistics (the computation of the mean) is often not recognized as such.
2.  if you have different numbers of trials between subjects, it is better to carry z-scores to the second level. You can convert t- to z-scores.
3.  instead of taking conventional t-scores to start with, you can use a [Winsorized estimate of the mean](https://en.wikipedia.org/wiki/Winsorized_mean) and standard deviation to compute the t-scores at the first level. That makes them more robust for outliers (common in EEG).
4.  quite often beta values estimated with a GLM are used as the statistic to be carried on to the second level. This allows you to explain part of the uninteresting variance in the data with confound-regressors.
