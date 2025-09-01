---
title: Restructure and rework all visualization functions
---

{% include /shared/development/warning.md %}


The current naming scheme is ambiguous and/or inefficient for end-users and developers. The goal of this page is to develop a new scheme for naming functions and structuring the underlying code.

## Goals of the new scheme

- be intuitive to the end-user
  - the name of any plotting function should be grouped by data-type (e.g., freq/timelock), followed by the intended plotting-mode (e.g., single/multi/topo/etc).
  - whether data is 2d or 3d should not determine in choosing which plotting function to call

- underlying code should be easy to distinguish functionality-wise
  - 2d/3d data should be plotted by the same underlying 2d or 3d code (irrespective of freq/timelock)
  - handling of options/data should be done in the higher-level functions.

## What is wrong with the current format

- Event-Related (ER) versus Time-Frequency-Representation (TFR) are not exclusive categories, but they are used as if they were

- chan_freq data is plotted by the end-user with xxxplotER (EventRelated), which (most often) has no relation what so ever to event-related vs induced (which are the common exclusive categories)

- topoplotER and topoplotTFR both depend on topoplotTFR, from a development perspective, there should be a third lower/intermediate level plotting function, and ER/TFR specific data-handling should be done by topoplotER/TFR (easier debugging, adding functionality) (same goes for movieplotER/TFR)

- inside single/multi/topoER/TFR a lot of data-handling is done to make the plotting code usable for different purposes, which is not ideal from a development perspective (debugging, adding features)

- ft_multiplotCC depends on ft_topoplotTFR, which is confusing for developers

## Existing implicated functions

- ft_singleplotER
- ft_singleplotTFR
- ft_topoplotER (wraps around ft_topoplotTFR)
- ft_topoplotIC (wraps around ft_topoplotTFR)
- ft_topoplotTFR
- ft_multiplotER
- ft_multiplotTFR
- ft_topomovie
- ft_sourcemovie
- ft_sourceplot
- ft_movieplotER (wraps around ft_movieplotTFR)
- ft_movieplotTFR
- ft_multiplotCC (wraps around ft_topoplotTFR)
- ft_topoplotCC

## Naming proposal

**Top-level functions**

- ft_freqplotsingle
- ft_freqplotmulti
- ft_freqplottopo
- ft_freqplotmovie
- ft_timelockplotsingle
- ft_timelockplotmulti
- ft_timelockplottopo
- ft_timelockplotmovie
- ft_componentplot (always topo's)
- ft_sourceplotsurf
- ft_sourceplotortho
- ft_sourceplotslice
- _ft_ccplotmulti...?_
- _ft_ccplottopo...?_
- _ft_statplotXXX....?_

**Extra Intermediate-level functions (to be located in trunk/private?.m)**

- ft_1dsingleplot
- ft_2dsingleplot
- ft_1dmultiplot
- ft_2dmultiplot
- ft_topoplot (DUM DUM DUMMMMMMMM.....) (whether 1d or 2d, frequency sel done at higher level)
- _ft_topomovieplot?_

_above naming scheme is ft_functionplot to avoid developer confusion with the low-level functions ft_plot_vector/matrix/lay/mesh/etc._

## See also

- <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=827>
