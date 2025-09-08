---
title: How can I find out what eventvalues and eventtypes there are in my data?
tags: [preprocessing, raw, trigger, event, values, type, eventvalue, eventtype]
category: faq
redirect_from:
    - /faq/how_can_i_find_out_what_eventvalues_and_eventtypes_there_are_in_my_data/
    - /faq/inspect_events/
---

If you recorded data and do not know what eventvalues or eventtypes there are in your data or if the expected values or types do not show up in your data, there is an easy way in FieldTrip to find out what actually _is_ in your data. You need to call **[ft_definetrial](/reference/ft_definetrial)** with `cfg.dataset` as you are interested in and `cfg.eventtype` set to '?':

    cfg = [];
    cfg.dataset            = 'yourfile.ext';
    cfg.trialdef.eventtype = '?';
    ft_definetrial(cfg);

This will print in the command window an overview of all eventtypes with associated eventvalues for subsequent trigger-based trial selection.

Another way to find out eventvalues is to use **[ft_databrowser](/reference/ft_databrowser)**. When calling the databrowser in mode `cfg.continuous = 'yes'` and with not resampled-data (e.g., with the raw dataset), vertical lines will indicate the onset time of the triggers (and text will indicate the associated value

    cfg = [];
    cfg.dataset    = 'yourfile.ext';
    cfg.continuous = 'yes';
    ft_databrowser(cfg);

{% include markup/skyblue %}
Each recording environment (lab/system/program) has a very specific way of naming the eventtype and labelling the triggers. For example, BrainVision recorder marks stimulus triggers by having them start with an 'S' and response triggers with an 'R'. Further, all trigger-values have a length of four characters. For example, the response trigger 100 will be 'R100', and stimulus trigger 15 will be 'S 15' (note the blank!). As another example that the eventtype also depends on the recording environment, we at the DCCN MEG lab have event-types that can be named 'frontpanel trigger' or 'backpanel trigger' (and this depends whether the device sending the trigger is connected to the front- or to the backside).
{% include markup/end %}
