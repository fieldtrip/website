---
title: Ensemble methods
---

{% include /shared/development/warning.md %}

At the moment the ft_mv_gridsearch class produces the classifier of all
candidate classifiers, which are defined in the input, with the best performance.

The extension which is currently implemented and under investigation is a class that finds an ensemble of all candidate classifiers.

The input to this alternative grid superclassifier class is the same as for
the grid search and produces an ensemble classifier using arbitrary many of the
candidate configuration as ensemble members.

contact: karch-spam(at)mpib-berlin(dot)mpg(dot)de without -spam
