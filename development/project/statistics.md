---
title: Redesign and implement a common statistical backend for various data types
---

{% include /shared/development/warning.md %}

## Objectives

- Add support for each major statistical method to each of the data objects (source, freq, timelock)
- Clarify the conceptial structure of the parametric and non-parametric statistical tests to the end-user
- Ensure that new statistical ideas can easily be implemented and made available to the end-user

## Step 1: verify the implementations on simulated data

The purpose is to examine the correctness and completeness of the currently implemented methods. Backward compatibility with existing scripts has to be maintained, therefore the current implementation can serve as reference implementation.

Besides showing that the current implementations are correct, this also reveals the different output formats that are presented to the end user.

## Step 2: implement a new structure

The current structure consists of a collection of stand-alone functions which do not fit into a common framework

- sourcestatistics_randomization, sourcestatistics_randcluster
- clusterrandanalysis, sourcestatistics_parametric, sourcestatistics_shiftpredict, freqstatistics_shiftpredict (\*)
- timelockstatistics, freqstatistics, sourcestatistics

The timelockstatistics, freqstatistics and sourcestatistics functions provide the user interface to the common statistics structure. Each of these functions calls the general statistics_wrapper, which subsequently dispatches the computation to a dataformat independent statistics function. The functionality provided by the functions marked by (\*) can be merged into the common framework.

The suggested structure is

{% include image src="/assets/img/development/project/statistics/statistics_structure.png" %}

An alternative to this structure with a more clear separation between the massive univariate single-sample (time-freq-channel element, or voxel) is given below

Implementing a new structure requires that

1.  existing statistical tests have to be refitted under the common structure
2.  handling of critical values has to be implemented consistently (required for parametric tests and clustering)
3.  missing values have to be dealt with (if possible)
4.  multiple comparison corrections have to be implemented consistently, (not only maxStat and clusterSum, but also Bonferroni and FDR)

## Step 3: ensure that the efficiency of the implementation is adequate for real-world use

Without optimization it is approximately a factor of 2x slower than clusterrandanalysis, which is acceptable.

## Step 4: document and release

### Supported and allowed permutations of the design matrix

{% include image src="/assets/img/development/project/statistics/perm1.png" %}
Independent samples design, ivar=A

{% include image src="/assets/img/development/project/statistics/perm2.png" %}
Dependent samples design, uvar=A, ivar=B

{% include image src="/assets/img/development/project/statistics/perm3.png" %}
Independent samples design with a control variable, ivar=A, cvar=B

{% include image src="/assets/img/development/project/statistics/perm4.png" %}
Mixed design, uvar=A, ivar=B, cvar=C
