---
title: Simulating and estimating, what about model (mis)match?
tags: [chieti, freq, connectivity, coherence, granger, dtf, pdc]
---

## Introduction

{% include markup/skyblue %}
This tutorial contains hands-on material that we use for the [MEG connectivity workshop in Chieti](/workshop/chieti2015).
{% include markup/end %}

## Background

{% include /shared/tutorial/connectivity_simulation_background.md %}

## Procedure

We will simulate (virtual) channel-data and use it to compute various connectivity metrics. As a generative model of the data we will use a multivariate autoregressive model and we will use **[ft_connectivitysimulation](/reference/ft_connectivitysimulation)** for this. Subsequently, we will estimate the multivariate autoregressive model and the spectral transfer function, and the cross-spectral density matrix using the functions **[ft_mvaranalysis](/reference/ft_mvaranalysis)** and **[ft_freqanalysis](/reference/ft_freqanalysis)**. In the next step we will compute and inspect various measures of connectivity with **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** and **[ft_connectivityplot](/reference/ft_connectivityplot)**.

## Simulated data with directed connections

{% include /shared/tutorial/connectivity_simulation_simulations.md %}
