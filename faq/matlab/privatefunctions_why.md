---
title: Why are so many of the interesting functions in the private directories?
category: faq
tags: [function, matlab]
redirect_from:
    - /faq/why_are_so_many_of_the_interesting_functions_in_the_private_directories/
    - /faq/privatefunctions_why/
---

In the FieldTrip code, we make a distinction between functions that the end-user should call, and helper functions that are called by other functions. Most functions that the end-user calls are prefixed with `ft_xxx` and are present in the main directory. The functions that the end-user should _not_ call are mainly in the private directory. The reason for the private directory is that we can maintain backward compatibility for the main functions, but not for **all** functions. We want to be able to make changes in these helper functions (i.e. the private functions) without worrying about whether any of the end-users is affected by the change.

The main functions have a **stable user-interface** (this also applies to the functions in the [modules](/development/architecture)), the private helper functions don't have a stable interface. We want people to use FieldTrip as a stable package, without having to worry that the update from one version to the next version breaks their own analysis scripts. If you would start using the private helper functions (which is not trivial due to the way that MATLAB hides the private functions), they are themselves responsible for their scripts breaking due to changes in these helper functions.

See also this FAQ that explains why [MATLAB does not see the functions in the "private" directory](/faq/matlab/matlab_privatefunctions).
