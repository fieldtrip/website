---
title: Connectivity estimates for EEG/MEG time series data
tags: [development, connectivity]
---

# Connectivity estimates for EEG/MEG time series data

FieldTrip has a consistent set of low-level functions for the computation of connectivity, i.e. estimating a bivariate or multivariate quantity from electrophysiological data, both on the sensor level and on the source level.

The objective of supplying these low-level functions as a separate module/toolbox are to

1.  facilitate the reuse of these functions in other open source projects (e.g. EEGLAB, SPM)
2.  facilitate the implementation and support for new inverse methods, esp. for external users/contributors
3.  facilitate the implementation of advanced features

The low-level functions are in the [connectivity](/development/module/connectivity) module, which is released together with FieldTrip but can also be downloaded [here](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/modules/) as a separate toolbox.

Please note that if you are an end-user interested in analyzing experimental EEG/MEG/ECoG data, you will probably will want to use the high-level FieldTrip functions. The functions such as **[ft_preprocessing](https://github.com/fieldtrip/fieldtrip/blob/release/ft_preprocessing.m)**, **[ft_timelockanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_timelockanalysis.m)**, **[ft_sourceanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_sourceanalysis.m)**, **[ft_mvaranalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_mvaranalysis.m)**, **[ft_freqanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_freqanalysis.m)**, **[ft_connectivityanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_connectivityanalysis.m)** and **[ft_networkanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_networkanalysis.m)** provide a user-friendly interface that take care of all relevant analysis steps and the data bookkeeping.

## Supported connectivity metrics

1.  coherence
2.  correlation
3.  directed transfer function
4.  granger causality, spectrally resolved
5.  imaginary part of coherency
6.  instantaneous causality
7.  pairwise phase consistency
8.  partial coherence
9.  partial correlation
10. partial directed coherence
11. phase locking value
12. phase slope index
13. total interdependence
14. weighted phase lag index

## Definition of the function-calls (API)

The functions should be called as

    outputdata = ft_connectivity_bct (inputdata, 'key1', value1, 'key2', value2, ....);
    outputdata = ft_connectivity_corr(inputdata, 'key1', value1, 'key2', value2, ....);
    outputdata = ft_connectivity_dtf (inputdata, 'key1', value1, 'key2', value2, ....);
    outputdata = ft_connectivity_ppc (inputdata, 'key1', value1, 'key2', value2, ....);
    outputdata = ft_connectivity_psi (inputdata, 'key1', value1, 'key2', value2, ....);
    outputdata = ft_connectivity_wpli(inputdata, 'key1', value1, 'key2', value2, ....);

The inputdata consists of a matrix of one of the following dimensionalities:

1.  Nrpt x Nchan x Nchan (x Nfreq) (x Ntime)
2.  Nrpt x Nchancmb (x Nfreq) (x Ntime)

where Nrpt can be singleton. Additional arguments come in key-value pairs and depend on the function and the required functionality. The current functions only take inputdata which is already in a bivariate representation. In FieldTrip this is ensured by the calling function **[ft_connectivityanalysis](https://github.com/fieldtrip/fieldtrip/blob/release/ft_connectivityanalysis.m)**.

One exception to the API described above i

    outputdata = ft_connectivity_granger(H, Z, S, key1, value1, ...);

Spectrally resolved granger causality is a function of both the spectral transfer function (H) and the covariance of the noise (Z). For computational reasons, the cross-spectral density is also a required input argument for the function.

## Related documentation

The literature references to the implemented methods are given [here](/references_to_implemented_methods).

See also these tutorials:

{% include seealso tag1="tutorial" tag2="connectivity" %}
