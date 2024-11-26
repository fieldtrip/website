---
title: How to test an interaction effect using cluster-based permutation tests?
tags: [faq, statistics]
---

# How to test an interaction effect using cluster-based permutation tests?

You can use cluster-based permutation tests for some but not for all interaction effects. This FAQ section covers how to test interaction effects based on corresponding t-values. You can also test interaction effects based on F-values. For a comparison of both procedures, see [Should I use t or F values for cluster-based permutation tests](/faq/should_I_use_t_or_F_values_for_cluster-based_permutation_tests).

## A 2-by-2 factorial design

I first consider the situation of a 2-by-2 factorial design. The four cells in this design are denoted by (1,1), (1,2), (2,1) and (2,2) (the first number in every pair denotes the level of the first factor; the second number denotes the level of the second factor). At some point in my explanation, it will be important to distinguish between a full within-subjects design and a mixed between-within subjects design. Now, in a full within-subjects design, every subject has participated in each of the four cells of the design; in a mixed between-within-subjects design, there are two groups of subjects (e.g., old and young, patients and controls) and each of these subjects has participated in two conditions (the within-subjects conditions). In the following, I assume that the first factor is the between-subjects factor.

I assume you have the output of your time-locked or frequency analysis for each of the 4 conditions. This output should be produced by, respectively, **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**, **[ft_freqgrandaverage](/reference/ft_freqgrandaverage)** or **[ft_sourcegrandaverage](/reference/ft_sourcegrandaverage)** with the field keepindividual set to 'yes'. We will denote these 4 data structures as follows: GA11, GA 12, GA21 and GA22.

From these 4 data structures, you now make 2 difference data structures in the following way:

- Copy GA11 to GAdiff11_12 and perform the assignment GAdiff11_12.individual=GA11.individual-GA12.individual.
- Copy GA21 to GAdiff21_22 and perform the assignment GAdiff21_22.individual=GA21.individual-GA22.individual.

The objective is now to statistically compare GAdiff11_12 and GAdiff21_22. Because we will be comparing two differences, we will be testing an interaction effect. Using a cluster-based permutation test, we have to choose the appropriate statfun, depending on whether this comparison involves a within-subjects or a between-subjects factor. In a full within-subjects design, it involves a within-subject factor, and in a mixed between-within-subjects design, it involves a between-subjects factor (remember that the first factor in the design is the between-subjects factor). In the form of a recip

- In a full within-subjects design, compare GAdiff11_12 and GAdiff21_22 using the statfun depsamplesT.
- In a mixed between-within-subjects design, compare GAdiff11_12 and GAdiff21_22 using the statfun indepsamplesT.

Following this rationale, you can also construct statistical tests for interaction effects that involve factors with more than 2 levels. However, especially with neurobiological data, it is almost never wise to statistically test interaction effects in designs more complicated than the 2-by-2 factorial design. In these more complicated designs, you always end up with F-tests, and these do not inform you about the pattern in the data that is responsible for the interaction effect. Nevertheless, for those of you that cannot resist the temptation(-;), I now describe the analysis steps for a general K-by-L factorial design (with K and L being positive integer >=2).

## The general K-by-L factorial design

I assume you have the output of your time-locked or frequency analysis for each of the KL conditions. This output should be produced by, respectively, ft_timelockgrandaverage or ft_freqgrandaverage with the field keepindividual set to 'yes'. We will denote these KL data structures as follows: GA11, GA12, ... GA1L, GA21, GA22, ... GAKL.

From these KL data structures, you now make K(L-1) difference data structures in the following wa

For k=1,...,K and l=2,...,L

- Copy GAk1 to GAdiffk1_kl and perform the assignment GAdiffk1_kl.individual=GAk1.individual-GAkl.individual.

The objective is now to statistically compare the K difference arrays GAdiffk1_kl. Because we will be comparing differences, we will be testing an interaction effect. Using a cluster-based permutation test, we have to choose the appropriate statfun, depending on whether this comparison involves a within-subjects or a between-subjects factor. In a full within-subjects design, it involves a within-subject factor, and in a mixed between-within-subjects design, it involves a between-subjects factor (remember that the first factor in the design is the between-subjects factor).

In the form of a recipe:

1.  In a full within-subjects design with K=2, compare the array [GAdiff11_12, GAdiff11_13, ... , GAdiff11_1L] with the array [GAdiff21_22, GAdiff21_23, ... , GAdiff21_2L] using the statfun depsamplesHotTsqr (which does not exist yet, but can be implemented in a straightforward way).
2.  In a mixed between-within-subjects design with K=2, compare the array [GAdiff11_12, GAdiff11_13, ... , GAdiff11_1L] with the array [GAdiff21_22, GAdiff21_23, ... , GAdiff21_2L] using the statfun indepsamplesHotTsqr (which does not exist yet, but can be implemented in a straightforward way).
3.  In a mixed between-within-subjects design with K>2, compare the K arrays [GAdiffk1_k2, GAdiffk1_k3, ... , GAdiffk1_kL] (k=1, ..., K) using the statfun indepsamplesWilksLambda (which does not exist yet, but can be implemented in a straightforward way).
