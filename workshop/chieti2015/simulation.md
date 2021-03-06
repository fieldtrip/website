---
title: Simulating and estimating, what about model (mis)match?
tags: [chieti, tutorial, freq, connectivity, coherence, granger, dtf, pdc]
---

# Simulating and estimating, what about model (mis)match?

## Introduction

{% include markup/info %}
This tutorial contains hands-on material that we use for the [MEG connectivity workshop in Chieti](/workshop/chieti2015).
{% include markup/end %}

## Background

{% include /shared/tutorial/connectivity_simulation_background.md %}

## Procedure

We will simulate (virtual) channel-data and use it to compute various connectivity metrics. As a generative model of the data we will use a multivariate autoregressive model and we will use **[ft_connectivitysimulation](https://github.com/fieldtrip/fieldtrip/blob/release/ft_connectivitysimulation.m)** for this. Subsequently, we will estimate the multivariate autoregressive model and the spectral transfer function, and the cross-spectral density matrix using the functions **[ft_mvaranalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_mvaranalysis.m)** and **[ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqanalysis.m)**. In the next step we will compute and inspect various measures of connectivity with **[ft_connectivityanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_connectivityanalysis.m)** and **[ft_connectivityplot](https://github.com/fieldtrip/fieldtrip/blob/release/ft_connectivityplot.m)**.

## Simulated data with directed connections

{% include /shared/tutorial/connectivity_simulation_simulations.md %}
