---
title: ft_connectivity_mutualinformation
---
```
 FT_CONNECTIVITY_MUTUALINFORMATION computes mutual information using the information
 breakdown toolbox (ibtb), as described in Magri et al., BMC Neuroscience 2009,
 1471-2202.

 Use as
   mi = ft_connectivity_mutualinformation(data, ...)

 The input data should be a Nchan x Nobservations matrix.

 Additional optional input arguments come as key-value pairs:
   histmethod = The way that histograms are generated from the data. Possible values
                are 'eqpop' (default), 'eqspace', 'ceqspace', 'gseqspace'.
                See the help of the 'binr' function in the ibtb toolbox for more information.
   numbin     = scalar value. The number of bins used to create the histograms needed for
                the entropy computations
   opts       = structure that is passed on to the 'information' function in the ibtb
                toolbox. See the help of that function for more information.
   refindx    = scalar value or 'all'. The channel that is used as 'reference channel'.
   refdata    = 1xNobservations vector, as an alternative to the refindx. Refdata takes precedence over refindx

 The output contains the estimated mutual information between all channels and the reference channel(s).

 See also FT_CONNECTIVITYANALYSIS
```
