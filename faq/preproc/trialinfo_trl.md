---
title: I used to work with trl-matrices that have more than 3 columns. Why is this not supported anymore?
category: faq
tags: [trialinfo, trialdef, trialfun]
redirect_from:
    - /faq/i_used_to_work_with_trl-matrices_that_have_more_than_3_columns._why_is_this_not_supported_anymore/
    - /faq/trialinfo_trl/
---

# I used to work with trl-matrices that have more than 3 columns. Why is this not supported anymore?

In the past, it was not straightforward to keep track of trial-specific information throughout the analysis pipeline. Some users actually knew how to work around this by coding trial-specific information in the `trl` matrix (by building it from a custom-defined function, which was called by ft_definetrial). Subsequently, since the `trl` matrix percolated into cfg.previous.previous.previous and so on, information about conditions, reaction times etc. could be recovered. However, this approach was far from straightforward, because some FieldTrip functions actually affect the `trl` matrix (such as ft-redefinetrial, but also all function which have an option cfg.trials, allowing for doing the computation on just a subset of trials in the input). Therefore, it was important to keep track of changing trial boundaries, changing number of trials etc.

In addition, some FieldTrip function implicitly relied on information present in this nested trl-matrix, in order to function properly. We encountered a few problems related to this implicit assumption, e.g., when working on data-structures consisting of the output of ft_appenddata, where the original data structures were obtained from different recording sessions. In such case, the first 2 columns of the `trl` matrix do not uniquely refer to some absolute sample numbers anymore. This caused some problems. Another example is related to data which has been resampled. Also, in such case, the first 3 columns of the `trl` matrix lose the connection to the data stored in data.trial.

In summary, to address these problems, and to make the functionality more transparent, we changed the way in which trial-specific information can be handled throughout the analysis pipeline.

See also [this](/faq/is_it_possible_to_keep_track_of_trial-specific_information_in_my_fieldtrip_analysis_pipeline) frequently asked question.
