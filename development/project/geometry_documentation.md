---
title: Clean up the documentation on head modeling, anatomical processing, etc.
---

{% include /shared/development/warning.md %}


there are now sections at

- https://www.fieldtriptoolbox.org/example/create_bem_headmodel_for_eeg -> has been deleted
- https://www.fieldtriptoolbox.org/example/headmodel -> has been deleted
- https://www.fieldtriptoolbox.org/example/make_leadfields_using_different_headmodels
- https://www.fieldtriptoolbox.org/tutorial/headmodel -> has been deleted
- https://www.fieldtriptoolbox.org/example/compute_leadfield
- https://www.fieldtriptoolbox.org/tutorial/forward -> has been deleted
- https://www.fieldtriptoolbox.org/development/bemmodel

These have to be merged if applicable, deleted if outdated/deprecated and improved if desired.

Please look at these links and replace any references to the old implementations with ft_prepare_headmodel

- https://www.fieldtriptoolbox.org/reference/ft_prepare_singleshell?do=backlink
- https://www.fieldtriptoolbox.org/reference/ft_prepare_concentricspheres?do=backlink
- https://www.fieldtriptoolbox.org/reference/ft_prepare_bemmodel?do=backlink
- https://www.fieldtriptoolbox.org/reference/ft_prepare_localspheres?do=backlink

It is done.
