---
title: How NOT to interpret results from a cluster-based permutation test
tags: [faq, statistics]
---

# How NOT to interpret results from a cluster-based permutation test

## The correct interpretation

The permutation test as implemented in **[ft_statistics_montecarlo](/reference/ft_statistics_montecarlo)** serves to test the null hypothesis (H0) that the data in the experimental conditions come from (are drawn from) the same probability distribution. In specialised statistics books, one sometimes reads the technical term that the probability distributions are **exchangeable**. Getting a significant result means that we can reject the null hypothesis (H0) that the data come from the same probability distribution in favour of the alternative hypothesis (H1) that the data come from different distributions. Based on a significant test result, you therefore can report that **"there is a significant difference between condition A and condition B"**.

{% include markup/red %}
H0: The data in the experimental conditions come from the same probability distribution, i.e. the data in the conditions cannot be distinguished.

H1: The data in the experimental conditions do **not** come from the same probability distributions, i.e. the data are different.
{% include markup/end %}

## What the test DOES NOT show

However, you cannot report a significant outcome of a permutation test as **"there is a significant cluster ..."**. This is because the significance in the test only speaks to the null hypothesis and not to the "where" or "when" of this difference. The binary test result (H0 is rejected: yes or no) by itself does not provide information on the exact spatial or temporal extent of the effect.

After you have made the decision that you reject H0 in favour of H1, you may want to interpret the difference in the data. Here is where the cluster might be useful because it points you to the feature(s) on the basis of which you came to the conclusion to believe in H1 over H0.

{% include markup/skyblue %}
If you test that the physical dimensions of male bodies are different from those of female bodies, you will likely find that the H0 (the physical dimensions of male and female bodies come from the same probability distribution) will be rejected in favour of the alternative (they come from different distributions).

However, from this result, one cannot conclude that men and women have different foot sizes. In fact, it may be that the test statistic that was used to compare male and female bodies was sensitive to other aspects than foot size.

Finding **a significant effect** using some test statistic (with some sensitivity profile) does **not mean that it tells the complete story**. Making a decision of H1 over H0 still requires that you interpret the result using your understanding of the (processed) data and the sensitivity profile of the test statistic (i.e., which between-condition differences will be reflected by the statistic). The decision and the interpretation are two separate steps.
{% include markup/end %}

## The extent of a cluster depends on multiple factors

Keep in mind that the extent of the cluster depends on multiple factor

- The signal to noise ratio in the data
- The length of the sliding time window (when calculating frequency data)
- The chosen time bins or brain regions on which to perform the statistical test
- The threshold chosen to select samples to belong to a cluster (choosing a stringent threshold will lead to a focal effect, while a liberal threshold will produce a widespread effect.
- Coverage of the head, i.e. the sensor arrangement.

You could imagine that with a dipolar scalp topography, one of the poles of the dipole would be above threshold and included in a cluster, whereas the other pole is below threshold and hence not represented in a cluster.

You could also imagine that the moment at which you can distinguish an ERP from the zero-baseline depends on the number of trials. The more trials, the more sensitive you will be in deciding that it starts to be different from the baseline. That does not mean that the ERP starts earlier if you have more trials, only that you are able to detect the effect earlier.

## What if I preselect a latency range and a spatial region?

If you a-priori select a certain time window and some scalp location in which to do the cluster-based permutation test, then you can say that there is a difference in the specific latency range and specific area.

However, this does not necessarily represent the entire true effect in the data.

{% include markup/skyblue %}
Here is what NOT to write:

"We found a significant cluster in area X, between time point A and B"
{% include markup/end %}

{% include markup/skyblue %}
Here are some examples of what you CAN write

"After selecting the a-priori time and region of interest in our data, the cluster-based permutation tests revealed a difference between the fully congruent and fully incongruent condition."

or if you would only select a latency range

"Testing for an N400 effect in the latency range from 350 to 500 ms post-stimulus, the cluster-based permutation test revealed a significant difference between the fully congruent and fully incongruent condition (p<0.05). In this latency range, the difference was most pronounced over left frontotemporal sensors."
{% include markup/end %}

## Is there a paper on this topic?

Yes, a paper has been written by Maris E., Oostenveld R. _[Nonparametric statistical testing of EEG- and MEG-data.](http://www.ncbi.nlm.nih.gov/pubmed/17517438)_ J Neurosci Methods, 2007. Furthermore, we recommend you to read _[Statistical testing in electrophysiological studies](http://www.ncbi.nlm.nih.gov/pubmed/22176204)_ Maris E, Psychophysiology, 2011. An additional worthwile read is _[Cluster‐based permutation tests of MEG/EEG data do not establish significance of effect latency or location](https://doi.org/10.1111/psyp.13335)_ Sassenhagen J., Dejan D., Psychophysiology 2019.
