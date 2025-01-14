---
title: How can I determine the onset of an effect?
category: faq
tags: [statistics]
redirect_from:
    - /faq/how_can_i_determine_the_onset_of_an_effect/
    - /faq/effectonset/
---

# How can I determine the onset of an effect?

{% include markup/skyblue %}
I received the following question:

_"If I am interested at the onset of an effect that is present in one condition and not another can I use the start time of a cluster (cluster-based permutation test) to represent the onset time of the effect?"_.

The answer below starts from the idea of cluster-based statistics, but applies to determining onset in general.
{% include markup/end %}

The cluster represents the thresholded uncorrected massive univariate statistics. The onset of where the uncorrected massive univariate statistics exceeds the threshold depends on the statistical sensitivity. e.g., consider that you use a [t-score](https://en.wikipedia.org/wiki/Student%27s_t-test) to quantify the condition difference

    t = sqrt(N) * (mean(x1) - mean(x2)) / std(x)

Given that the mean and standard deviation are unbiased estimators, they won't systematically change if you change the number of trials. But sqrt(N) changes with the number of trials. Hence the t-score increases with increasing number of trials.

Imagine the typical effect that starts weak and then increases over time until it peaks. The onset that you determine using the thresholded t-score depends on the number of trials, but it is always with finite N biased to being too late. If you have few trials, it will be much too late (close to the peak), if you have many trials it will only be a bit too late. The more trials, the closer it gets to the true onset. But you know that it will always be too late, and that it depends quite randomly on the amount of data that you happen to have.

Determining the onset of an effect that you know exists (i.e. you have rejected the H0 of no effect in favour of H1) is not a statistical question. There is an effect, it's as simple as that! So why use the value that you computed under the rejected null hypothesis to quantify a feature of the effect?

Of course it depends a lot on what you want to do with the onset. You could want to answer the question “what is the earliest time at which I can detect the effect?” Then it makes sense to use the thresholded statistic. But you can also just fit a line to the difference between x1 and x2 (at the rising flank) and see where that line crosses zero. Or fit a curved line to the whole bump.

So all in all it depends a bit on the precise question that you have. If you say “I want to quantify the onset of the (confirmed) effect”, then you should make a model of the effect (i.e. the bump) and determine the relevant model parameter (the zero crossing). But if you want to say “from this latency onward I am confident that the two lines differ”, you should quantify your confidence and use a thresholded statistic.
