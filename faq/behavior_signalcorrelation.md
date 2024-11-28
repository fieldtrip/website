---
title: How can I test for correlations between neuronal data and quantitative stimulus and behavioral variables?
category: faq
tags: [statistics]
redirect_from:
    - /faq/how_can_i_test_for_correlations_between_neuronal_data_and_quantitative_stimulus_and_behavioural_variables/
---

# How can I test for correlations between neuronal data and quantitative stimulus and behavioral variables?

## Dependent versus Independent Variables

A common perspective on the statistical testing starts from the distinction between dependent and independent variables. When analyzing neurobiological signals, these are typically considered to be the dependent variable. In these studies, the independent variable can be the experimental conditions, as defined by task instructions, stimulus type, learning history, etc. The label _independent variable_ suggests that it must be under the experimenter's control. However, this is not necessarily the case, and this is exemplified by response accuracy, which may very well serve as the independent variable in a study in which the relation is investigated between behavior (actually, one aspect of it, accuracy) and neural activity. Because neither of these variables (accuracy and neural activity) is under experimental control, it is arbitrary how the roles of dependent and independent variable are assigned. In FieldTrip, we use the convention that the variable with the smallest dimensionality is assigned the role of independent variable. For our example, this implies that accuracy is assigned the role of independent and the neurobiological signal the role of dependent variable. In fact, accuracy is represented by a single number, whereas the neurobiological signal often has a spatial (the channels), a temporal (the time points), and a spectral (the frequencies) dimension.

## Categorical versus Quantitative Independent Variables

It is important to make a distinction between categorical and quantitative independent variables, because these are associated with different test statistics. Categorical variables have values in a number of unordered categories (e.g., left-versus-right, patient-versus-control, old-versus-new) whereas quantitative variables have ordered values that typically express some quantity (e.g., response time, blood pressure, pupil diameter, working memory capacity).

When deciding on the statistical test to be used, besides the distinction between categorical and quantitative independent variables, one also has to distinguish between two types of design:

1.  A design in which there is only a single observation for every unit-of-observation (UO). This is called a **between-UO** design.
2.  A design in which every UO is observed in the multiple conditions that one wants to compare. This is called a **within-UO** design.
    (Note: In a single-subject study, the UOs are the trials; in a multi-subject study, the UOs are the subjects.) There are studies with multiple independent variables, and all combinations of _between_ and _within_ are possible (all _between_, all _within_, and mixed _between-within_). For simplicity, in this FAQ, we only consider studies with a single independent variable.

Now, for studies with a between-UO design and a categorical independent variable, we can use the following test statistic

- The _independent-_ or _between-samples T-statistic_ when the number of categories is equal to 2. In FieldTrip, this is implemented as **ft_statfun_indepsamplesT**.
- The _independent-_ or _between-samples F-statistic_ when the number of categories is larger than 2. In FieldTrip, this is implemented as **ft_statfun_indepsamplesF**.

And for studies with a within-UO design and a categorical independent variable, we can use the following test statistic

- The _dependent-_ or _paired-samples T-statistic_ when the number of categories is equal to 2. In FieldTrip, this is implemented as **ft_statfun_depsamplesT**.
- The _dependent-_ or _repeated-measures F-statistic_ when the number of categories is larger than 2. In FieldTrip, this is implemented as **ft_statfun_depsamplesF**.

For quantitative independent variables, we have two test statistics, one for a between-UO and one for a within-UO design. In both cases, the test statistic is based on a regression of the dependent on the quantitative independent variable. In fact, the test statistic is a function of the regression coefficient and its standard error. The two test statistics are the following:

- In a between-UO design we use the _independent samples regression T-statistic_. In FieldTrip, this is implemented as **ft_statfun_indepsamplesregrT**.
- In a within-UO design we use the _dependent samples regression T-statistic_. In FieldTrip, this is implemented as **ft_statfun_depsamplesregrT**.

It turns out that the independent samples regression T-statistic only depends on the Pearson correlation between the dependent and the independent variable. The formula that expresses the independent samples regression T-statistic as a function of this correlation is implemented in the FieldTrip function **ft_statfun_correlationT**.

## The Permutation Distribution Results From Breaking the Association Between Dependent and Independent Variable

The null hypothesis that is tested by a permutation test involves that the probability distribution of the dependent variable is identical for all possible values of the independent variable. Categorical independent variables typically have a finite number of categories, and the probability distributions implied in the null hypothesis are distributions of the dependent variable within each of these categories. Quantitative independent variables, on the other hand, may have an infinite number of values, and in this case it is more difficult to conceptualise the probability distributions within each of these values. However, there is a null hypothesis for quantitative independent variables that is equivalent to the one for categorical independent variables: **statistical independence** between the dependent and the independent variable. Testing for this statistical independence is possible in the same way for categorical as for quantitative independent variables: breaking the association between dependent and independent variable by randomly permuting the values of the independent variable. In a between-UO design, these values are permuted across the UOs, and in a within-UO design, they are permuted across the conditions in which the UO has been observed.

It is important to point out that the hypothesis of statistical independence rules out _all possible_ relations between the dependent and a quantitative independent variable, and not only the linear relation. This contrasts with the three test statistics for quantitative independent variables that are implemented in FieldTrip: these are only sensitive to deviations from statistical independence that can be captured as a **linear** relation between the dependent and the independent variable. Of course, new test statistics can be formulated (and implemented as statfuns) with a sensitivity profile that is optimised for particular non-linear deviations from statistical independence.

## Statistical Testing of the Relation Between a Neurobiological and a Behavioural Variable

Sometimes, the statistical testing of the relation with a quantitative variable is confused with the testing of the relation with a behavioral variable. This is understandable, as several interesting behavioral variables are quantitative (e.g., response time, scores on a questionnaire or ability test, accuracy as quantified in the proportion correct). However, from a statistical point of view, the two issues are unrelated. This can be demonstrated using an example: in a single-subject study, one can test for a relation between behavior and the measured neurobiological signal by means of an independent samples T-statistic that compares the signal between correct and incorrect trials.

## Examples

In the following some example codes are provided that illustrate the use of various statfuns that can be used to test for a relationship between our independent and dependent variable.

### Quantitative Independent Variable

In the following example we will consider a design in which we want to test if there is a relationship between a **quantitative independent variable** (e.g., mean reaction time per subject) and their time-frequency data which is the dependent variable.

First, we will consider testing if there is a relationship between our **independent** and **dependent** variable using the **ft_statfun_indepsamplesregrT** function.

    % compute statistics with ft_statfun_indepsamplesregrT
    cfg = [];
    cfg.statistic        = 'ft_statfun_indepsamplesregrT';
    cfg.method           = 'montecarlo';
    cfg.numrandomization = 1000;

    n1 = 3;    % n1 is the number of subjects
    design(1,1:n1)       = [0.6 0.9 0.1]; %here we insert our independent variable (behavioral data) in the cfg.design matrix, in this case reaction times of 3 subjects.

    cfg.design           = design;
    cfg.ivar             = 1;

    stat = ft_freqstatistics(cfg, data_brain{:});

In order to test for a correlation between the **independent** and **dependent** variable using Pearson we can use the **ft_statfun_correlationT** function.

    % compute statistics with correlationT
    cfg = [];
    cfg.statistic        = 'ft_statfun_correlationT';
    cfg.method           = 'montecarlo';
    cfg.numrandomization = 1000;

    n1 = 3;    % n1 is the number of subjects
    design(1,1:n1)       = [0.6 0.9 0.1]; %here we insert our independent variable (behavioral data) in the cfg.design matrix, in this case reaction times of 3 subjects.

    cfg.design           = design;
    cfg.ivar             = 1;

    stat = ft_freqstatistics(cfg, data_brain{:});

### Categorical Independent Variable

In the next example we will consider a design in which we want to test if there is a relationship between a **categorical independent variable** (e.g., accuracy coded as 1 or 2 per trial for a subject) and the time-frequency data of one subject, which is the dependent variable.

We will consider testing if there is a relationship between our **independent** and **dependent** variable using the **ft_statfun_indepsamplesT** function.

    % compute statistics with ft_statfun_indepsamleT
    cfg = [];
    cfg.statistic        = 'ft_statfun_indepsamplesT';
    cfg.method           = 'montecarlo';
    cfg.numrandomization = 1000;

    n1 = 20;    % n1 is the number of trials
    design(1,1:n1)       = [1;2;2;1;1;1;1;1;2;1;1;1;2;2;2;1;2;1;2;2]; %here we insert our independent variable (behavioral data) in the cfg.design matrix, in this case accuracy per trial of 1 subject.

    cfg.design           = design;
    cfg.ivar             = 1;

    stat = ft_freqstatistics(cfg, data_brain);
