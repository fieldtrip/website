---
title: Clean up the documentation on head modeling, anatomical processing, etc.
---

{% include /shared/development/warning.md %}

##  Clean up the documentation on head modeling, anatomical processing, etc. 

there are now sections at

*  http://fieldtrip.fcdonders.nl/example/create_bem_headmodel_for_eeg -> has been deleted
*  http://fieldtrip.fcdonders.nl/example/headmodel -> has been deleted
*  http://fieldtrip.fcdonders.nl/example/make_leadfields_using_different_headmodels
*  http://fieldtrip.fcdonders.nl/tutorial/headmodel -> has been deleted
*  http://fieldtrip.fcdonders.nl/example/compute_leadfield
*  http://fieldtrip.fcdonders.nl/tutorial/forward -> has been deleted
*  http://fieldtrip.fcdonders.nl/development/bemmodel

These have to be merged if applicable, deleted if outdated/deprecated and improved if desired.

Please look at these links and replace any references to the old implementations with ft_prepare_headmodel

*  http://fieldtrip.fcdonders.nl/reference/ft_prepare_singleshell?do=backlink
*  http://fieldtrip.fcdonders.nl/reference/ft_prepare_concentricspheres?do=backlink
*  http://fieldtrip.fcdonders.nl/reference/ft_prepare_bemmodel?do=backlink
*  http://fieldtrip.fcdonders.nl/reference/ft_prepare_localspheres?do=backlink

It is done.

