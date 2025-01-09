---
title: Should I use t or F values for cluster-based permutation tests?
parent: Statistical analysis
category: faq
tags: [statistics]
authors: [Christoph Huber-Huber]
redirect_from:
    - /faq/should_I_use_t_or_F_values_for_cluster-based_permutation_tests/
---

# Should I use t or F values for cluster-based permutation tests?

Both t and F distributions are interchangeable for a two-sample setting. In this setting, the F value is simply the t value to the power of two: ```F = t^2```.
Cluster-based permutation tests have originally been used with a t-test statistic (Maris & Oostenveld, 2007, in J. of Neurosci. Methods) but their implementation in FieldTrip allows to use any other statistic function in addition to the common [ft_statfun_depsamplesT](/reference/statfun/ft_statfun_depsamplesT) and [ft_statfun_indepsamplesT](/reference/statfun/ft_statfun_indepsamplesT), such as [ft_statfun_depsamplesFunivariate](/reference/statfun/ft_statfun_depsamplesFunivariate) and [ft_statfun_indepsamplesF](/reference/statfun/ft_statfun_indepsamplesF). Using F values instead of t values for cluster-based permutation tests looks like a good opportunity to test for interaction effects and one might think that the results are equivalent to their t-test version. This is, however, not the case as will be explained below and it will finally be recommended to use the t statistic wherever possible in order to maintain the statistical properties of the test (in terms of power).

## The decisive step in cluster-based permutation testing: computing the cluster mass

Cluster-based permutation testing involves calculating the test statistic (t-value, F-value, etc.) on so-called random partitions of the data (for details see [Cluster-based permutation tests on event related fields](/tutorial/cluster_permutation_timelock)). Calculating the test statistic for a cluster involves the step of computing the summary statistic for the whole cluster, which usually is the _cluster mass_, but could in theory be any other way of summarising the test statistics across contiguous points of your data in time and space that are above a certain threshold value. The cluster mass is simply the sum of all the statistic values across the cluster. The concept has been introduced in work with structural MRI data (Bullmore et al., 1999, in IEEE Transactions on Medical Imaging).

## The cluster mass destroys the equivalence between t and F distributions and makes them lead to different p-values

The p-value is the proportion of the null distribution with a _more extreme_ stats value than the obtained one (in the case of one-tailed tests it is about _larger_ or _smaller_ values). Creating the null distribution from the random participants usually involves calculating the cluster mass which consists in summing up the statistic values of each point in time and space for a cluster. For a single value, ```t^2 = F```. However, the sum of a set of t-values taken to the power of two does not correspond anymore to the same set of F values, because ```(sum(t_1, t_2, ..., t_n))^2 != sum(t_1^2, t_2^2, ..., t_n^2) == sum(F_1, F_2, ..., F_n)```. Thus, the null distribution based on t-values is different from the null distribution based on F-values. This difference can lead to a significant result for the t-value version but not for the F-value version. The result from the F-value version will usually be more conservative, i.e. you will be less likely to conclude that your experimental conditions differ significantly from each other.

## Conclusion: Use the t values or make the F values equivalent

Obtaining different p-values in two procedures which are supposed to be mathematically equivalent and lead to different results only because of the behaviour of an arbitrary summary function, such as the cluster mass, leads to the question of which the two procedures is to be preferred. Given that cluster-based permutation testing has originally been used with t-values and most of the studies have used the cluster mass with t-values, it is highly recommended to stick to the t-test version in order to maintain comparability to previous studies. In practice, this recommendation means:

- Compute statistics as t-tests between differences (or in the case of interactions, differences of differences) instead of F-test from an Anova on the full experimental design.
- If you compute statistics with an Anova, adjust the cluster-based permutation algorithm to take the square root of the F-value before computing the cluster mass. Some functions might provide this option already.

Slides with more detailed explanations and graphs can be found here:
[Christoph-cluster_test_answer-2023-03-06.pptx](https://github.com/chsquare/website/files/11469147/Christoph-cluster_test_answer-2023-03-06.pptx)
