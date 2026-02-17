---
title: Clean up inside_vol and similar functions
---

{% include /shared/development/warning.md %}

The functions prepare_dipole_grid/find_inside_vol/headsurface should all be merged with the inside_vol function, which is part of the public interface of forwinv. Furthermore, all FT use of those functions should be updated.
