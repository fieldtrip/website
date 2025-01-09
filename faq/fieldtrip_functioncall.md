---
title: What does a typical call to a FieldTrip function look like?
parent: Code and development questions
category: faq
tags: [datatype, function]
redirect_from:
    - /faq/what_does_a_typical_call_to_a_fieldtrip_function_look_like/
---

# What does a typical call to a FieldTrip function look like?

All high-level FieldTrip functions take a configuration input structure as first input argument. The FieldTrip functions in general work like this

    dataout = functionname(cfg);               % e.g., ft_preprocessing
    dataout = functionname(cfg, datain, ...);  % e.g., ft_freqanalysis
    functionname(cfg, datain, ...);            % e.g., plotting functions

Type `help functionname` to see which input arguments (cfg.xxx) ought to be defined before calling the function. The _datain_ and _dataout_ arguments to all FieldTrip main functions can be categorized in a limited number of data types, all of which are structures with a characteristic set of fields. The different datatypes are described [here](/faq/how_are_the_various_data_structures_defined).
