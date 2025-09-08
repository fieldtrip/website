---
title: How to test an interaction effect using cluster-based permutation tests?
tags: [statistics]
category: faq
redirect_from:
    - /faq/how_can_i_test_an_interaction_effect_using_cluster-based_permutation_tests/
    - /faq/clusterstats_interaction/
---

You can use cluster-based permutation tests for some but not for all interaction effects. This FAQ section covers how to test interaction effects based on corresponding t-values. You can also test interaction effects based on F-values. For a comparison of both procedures, see [Should I use t or F values for cluster-based permutation tests](/faq/stats/clusterstats_teststatistic).

## A 2-by-2 factorial design

First we consider the situation of a 2-by-2 factorial design. The four cells in this design are denoted by (1,1), (1,2), (2,1) and (2,2) (the first number in every pair denotes the level of the first factor; the second number denotes the level of the second factor). At some point in my explanation, it will be important to distinguish between a full within-subjects design and a mixed between-within subjects design. Now, in a full within-subjects design, every subject has participated in each of the four cells of the design; in a mixed between-within-subjects design, there are two groups of subjects (e.g., old and young, patients and controls) and each of these subjects has participated in two conditions (the within-subjects conditions). In the following, We assume that the first factor is the between-subjects factor.

We assume you have the output of your time-locked or frequency analysis for each of the 4 conditions. This output can be produced by, respectively, **[ft_timelockgrandaverage](/reference/ft_timelockgrandaverage)**, **[ft_freqgrandaverage](/reference/ft_freqgrandaverage)** or **[ft_sourcegrandaverage](/reference/ft_sourcegrandaverage)** with the cfg-field keepindividual set to 'yes'. We will denote these 4 data structures as follows: GA11, GA 12, GA21 and GA22. The functional parameter is then stored in the field 'individual'. Alternatively, you can use **[ft_appendtimelock](/reference/ft_appendtimelock)**, **[ft_appendfreq](/reference/ft_appendfreq)** or **[ft_appendsource](/reference/ft_appendsource)** with the cfg-field appenddim set to 'rpt', and the cfg-field parameter set appropriately. This results in data structure where the relevant numeric data is stored in fields with the original fieldname, e.g. 'trial', or 'powspctrm'. For the following example code, we assume that the data structures with the condition specific combined-across-subject data contain the relevant numbers in the 'powspctrm' field.

From these 4 data structures, you now make 2 difference data structures in the following way:

```
cfg = [];
cfg.parameter = 'powspctrm';
cfg.operation = 'subtract';
GAdiff11_12 = ft_math(cfg, GA11, GA12);
GAdiff21_22 = ft_math(cfg, GA21, GA22);
```

The objective is now to statistically compare GAdiff11_12 and GAdiff21_22. Because we will be comparing two differences, we will be testing an interaction effect. Using a cluster-based permutation test, we have to choose the appropriate statfun, depending on whether this comparison involves a within-subjects or a between-subjects factor. In a full within-subjects design, it involves a within-subject factor, and in a mixed between-within-subjects design, it involves a between-subjects factor (remember that the first factor in the design is the between-subjects factor). In the form of a recipe:

- In a full within-subjects design, compare GAdiff11_12 and GAdiff21_22 using the statfun depsamplesT.
- In a mixed between-within-subjects design, compare GAdiff11_12 and GAdiff21_22 using the statfun indepsamplesT.

Following this rationale, you can also construct statistical tests for interaction effects that involve factors with more than 2 levels. However, especially with neurobiological data, it is almost never wise to statistically test interaction effects in designs more complicated than the 2-by-2 factorial design. In these more complicated designs, you always end up with F-tests, and these do not inform you about the pattern in the data that is responsible for the interaction effect. Nevertheless, for those of you that cannot resist the temptation(-;), I now describe the analysis steps for a general K-by-L factorial design (with K and L being positive integer >=2).

## The general K-by-L factorial design

Here it is assumed that you have the output of your time-locked or frequency analysis for each of the KL conditions. This output should be produced by, respectively, ft_timelockgrandaverage or ft_freqgrandaverage with the field keepindividual set to 'yes' (or equivalently with the respective ft_append* functions). We could denote these KL data structures as follows: GA11, GA12, ... GA1L, GA21, GA22, ... GAKL, but alternatively store the data in a KxL cell-array GA, where the {k,l}'th cell reflects the condition-specific estimates.

From these KL data structures, you now could make K(L-1) difference data structures in the following way:

```
cfg = [];
cfg.operation = 'subtract';
cfg.parameter = 'powspctrm';
for k = 1:K
  for l = 2:L
    GAdiff{k,l-1} = ft_math(cfg, GA{k,l-1}, GA{k,l});
  end
end
```

The objective is now to statistically compare the K(L-1) difference arrays GAdiffk1_kl. Because we will be comparing differences, we will be testing an interaction effect. Using a cluster-based permutation test, we have to choose the appropriate test-statistic, implemented in a statfun, depending on whether this comparison involves a within-subjects or a between-subjects factor. In a full within-subjects design, it involves a within-subject factor, and in a mixed between-within-subjects design, it involves a between-subjects factor (remember that the first factor in the design is the between-subjects factor).

In the form of a recipe (note that the value for K is constrained to 2 if you want to employ a T-type of test statistic):

1.  In a full within-subjects design with K=2, compare the array [GAdiff11_12, GAdiff11_13, ... , GAdiff11_1L] with the array [GAdiff21_22, GAdiff21_23, ... , GAdiff21_2L] using the statfun depsamplesHotTsqr (which does not exist yet, but can be implemented in a straightforward way).
2.  In a mixed between-within-subjects design with K=2, compare the array [GAdiff11_12, GAdiff11_13, ... , GAdiff11_1L] with the array [GAdiff21_22, GAdiff21_23, ... , GAdiff21_2L] using the statfun indepsamplesHotTsqr (which does not exist yet, but can be implemented in a straightforward way).
3.  In a mixed between-within-subjects design with K>2, compare the K arrays [GAdiffk1_k2, GAdiffk1_k3, ... , GAdiffk1_kL] (k=1, ..., K) using the statfun indepsamplesWilksLambda (which does not exist yet, but can be implemented in a straightforward way).
