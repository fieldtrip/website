---
title: MATLAB does not see the functions in the "private" directory
category: faq
tags: [function, matlab]
redirect_from:
    - /faq/matlab_does_not_see_the_functions_in_the_private_directory/
---

# MATLAB does not see the functions in the "private" directory

The functions in the fieldtrip/private directory are only available for functions that are located in fieldtrip. You cannot call them from the command line, and you cannot call them from functions (or scripts) that are located outside the FieldTrip directory.

See this this [Mathworks documentation](https://nl.mathworks.com/help/matlab/matlab_prog/private-functions.html) for more general information.

The private directory provides a convenient way of separating the high-level functions that a normal user would call (i.e. the user interface to the toolbox) and the low-level functions. However, if you are a "power user" and also want to directly call the low-level functions, you can do the following:

(on the Linux/macOS command line, or using a Windows equivalent)

    cd /your/path/to/fieldtrip
    mv private ../fieldtrip_private

(or alternatively on the Linux/macOS command line)

    cd /your/path/to/
    ln -s fieldtrip/private fieldtrip_private

(on the MATLAB prompt)

    addpath /your/path/to/fieldtrip
    addpath /your/path/to/fieldtrip_private

See also this FAQ that explains [why so many of the interesting functions are in the private directories](/faq/why_are_so_many_of_the_interesting_functions_in_the_private_directories).
