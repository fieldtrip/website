---
title: Modularise ft_connectivityanalysis
---

{% include /shared/development/warning.md %}


Goal: convert ft_connectivityanalysis into a module, to facilitate collaboration with Tim Mullen's EEGLAB connectivity module.

Action plan (from the FT side):

- facilitate interaction with EEGLAB developers by providing more detailed information with respect to the datatypes (wiki)
- reorganise the code a bit such that univariate2bivariate moves to checkdata.
- move the connectivity computation subfunctions into subdirectory/module connectivity (done)
- standardize the api to the connectivity subfunctions (done)
- work with key/value pairs (done)
