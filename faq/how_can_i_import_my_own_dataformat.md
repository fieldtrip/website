---
title: How can I import my own dataformat?
tags: [faq, dataformat, preprocessing]
---

## How can I import my own dataformat?

There are two approaches for importing data from an unsupported format: you can extend FieldTrip with new code, or you can circumvent the import procedure.

### Extend the FieldTrip reading functions

The first and preferred way of implementing a new dataformat is by extending the **[ft_read_header](/reference/ft_read_header)**, **[ft_read_data](/reference/ft_read_data)** and **[ft_read_event](/reference/ft_read_event)** functions. These functions are wrappers around many different fileformats and provide a common interface. Probably you will also have to add your fileformat to fileformat function so that the files are properly recognized. You could even replace the ft_read_xxx functions completely by your own functions, as long as their interface stays the same. Depending on the complexity of your experimental design (e.g. conditional trigger sequences), you might want to write a custom function for the trial definition. 

Contact us if you need help.

#### Using your own low-level reading functions when calling ft_read_header/data/event

You may be in the situation that you wish use ft_read_header/data/event for reading in your data, but your dataformat is very atypical and used only by your lab. In such a case, in order to prevent cluttering, it is preferential to not add the dataformat to FieldTrip. However, there is a simple way you can still use your own reading functions. To do so, make your read_XXX_header/data/event functions, and be sure they are on the path. Then, when e.g. calling ft_preprocessing, specify headerformat/dataformat/eventformat as the name of your specific function. 

 For exampl

    cfg = [];
    cfg.headerfile   = 'SOMEFILENAME'
    cfg.headerformat = 'MYHEADERFUNCTION'
    cfg.datafile     = 'SOMEFILENAME'
    cfg.dataformat   = 'MYDATAFUNCTION'
    cfg.eventfile    = 'SOMEFILENAME'
    cfg.eventformat  = 'MYEVENTFUNCTION'
    ...
    data = ft_preprocessing(cfg)
    
Keep in mind that your reading functions have to follow the following input/output format.  
    hdr   = myheaderfunction(filename)
    dat   = mydatafunction(filename, hdr, begsample, endsample, chanindx)
    event = myeventfunction(filename)  
See ft_read_header/data/event to find details of each of these variables are.

### Circumvent the FieldTrip reading functions

Alternatively, if you already are able to read the data into MATLAB somehow, you can reformat that data within Matlab into a datastructure that is compatible with FieldTrip. Raw data that is comparable with the output of preprocessing should consist of a structure with the fields

    data.label      % cell-array containing strings, Nchan*1
    data.fsample    % sampling frequency in Hz, single number
    data.trial      % cell-array containing a data matrix for each 
                  % trial (1 X Ntrial), each data matrix is a Nchan*Nsamples matrix 
    data.time       % cell-array containing a time axis for each 
                  % trial (1 X Ntrial), each time axis is a 1*Nsamples vector 
    data.trialinfo  % this field is optional, but can be used to store 
                  % trial-specific information, such as condition numbers, 
                  % reaction times, correct responses etc. The dimensionality 
                  % is Ntrial*M, where M is an arbitrary number of columns

Each trial can have a different number of samples (i.e. variable length), that is why each trial needs an individual time axis. If your data consists of trials with a fixed length, then each vector data.time{i} is equal to data.time{1}. If your data consists of a single trial, e.g. when it is a continuous recording, there is only a single data.time{1} and single data.trial{1}. The data format is described in more detail in **[/reference/ft_datatype_raw](/reference/ft_datatype_raw)**. The main FieldTrip data structures are jointly described in [this FAQ](/faq/how_are_the_various_data_structures_defined).  

If your data represents a continuous recording, you can also consider taking a simple two-step approach by first representing your data into *one long trial* as described above, and then cutting it up into individual trials using **[ft_redefinetrial](/reference/ft_redefinetrial)**.

Note that to do so you need to enter another field that makes the data recognizable as a long tria
    data.sampleinfo % array containing [startsample endsample] of data

Note also that if you want to add trial-specific information related to the short trials that are going to be created in the next step, you need to create the trialinfo field only after your call to ft_redefinetrial

Now you simply call **[ft_redefinetrial](/reference/ft_redefinetrial)**, supplying a trialstructure in the config, e.g
    
    cfg.trl = [1    100 -10;
             101  200 -10;
             201  300 -10];
    newdata = ft_redefinetrial(cfg,data);

The second approach for importing data is relevant if you do not want to read the raw data from file, i.e. you do not want to do everything (starting with preprocessing) using FieldTrip, but only the final stages of your analysis. This is the approach for example taken in the **[besa2fieldtrip](/reference/besa2fieldtrip)** and **[spm2fieldtrip](/reference/spm2fieldtrip)** functions.
