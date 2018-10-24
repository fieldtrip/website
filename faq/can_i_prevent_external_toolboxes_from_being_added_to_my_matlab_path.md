---
layout: default
tags: faq matlab toolbox path
---


## Can I prevent "external" toolboxes from being added to my MATLAB path?

The recommended FieldTrip path settings are explained in this [frequently asked question](/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path).

The code in the **[ft_defaults](/reference/ft_defaults)** function will execute only once and preferably should be called by you in your startup.m file. The main FieldTrip functions will also call **[ft_defaults](/reference/ft_defaults)** to ensure that the subdirectories with teh code that they rely on are added to the path. 

The **[ft_defaults](/reference/ft_defaults)** will also add some toolboxes from external to your path, such as external/signal, external/stats and external/image. These contain drop-in [replacements for some MATLAB functions](/faq/matlab_replacements) to reduce the requirements on the (network) licenses, which are often available in a limited number.

If you don't want these replacement functions on your path, you should do the following in your startup.m file.

    ft_defaults
    [ftver, ftpath] = ft_version;
    rmpath(fullfile(ftver, 'external', 'signal'))
    rmpath(fullfile(ftver, 'external', 'stats'))
    rmpath(fullfile(ftver, 'external', 'image'))
 
    

   
