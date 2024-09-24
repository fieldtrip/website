---
title: How can I check or decipher the sequence of triggers in my data?
category: faq
tags: [trigger, trialfun, preprocessing]
---

# How can I check or decipher the sequence of triggers in my data?

Triggers, stimuli, responses, annotations, etcetera in the recording are in FieldTrip jointly represented as "events" and read from the dataset using **[ft_read_event](/reference/fileio/ft_read_event)**. The following code demonstrates how you can do a visual check of the triggers and export them to an excel file.

We start by reading the header (which we need for the sampling frequency) and the events. In case of Neuromag .fif data that was recorded with internal active shielding (IAS) and that has not been maxfiltered yet, you can disable the check for maxfilter.

    hdr   = ft_read_header(dataset, 'checkmaxfilter', 'no');
    event = ft_read_event(dataset, 'checkmaxfilter', 'no');

The "event" variable is a structure array, in which each element represent one event.

    >> event

    event =
    528x1 struct array with field
    type
    sample
    value
    offset
    duration

For convenience, you can represent the sample number (which is an integer), event type (which is a string) and the event value (which is usually an integer) like this

    smp = [event.sample];
    typ = {event.type};
    val = [event.value];

You can plot the events in a scatter plot. Along the horizontal axis is time, vertical is the value.

    figure
    plot(smp/hdr.Fs, val, '.');

{% include image src="/assets/img/faq/triggers/screen_shot_2017-09-20_at_17.50.53.png" width="400" %}

The visual inspection of the figure shows you the overall structure of the events in the recording. Often it allows you to decipher part of the experimental design.

## Neuromag/Elekta

The trigger coding in the Neuromag system is more complex than in most systems. One physical event gets coded in multiple trigger channels in the fif file and hence also in multiple FieldTrip events. There are STI101 and STI102 channels, which represent combined values; these are usually between 1 and 255. There are also STI00x with x running from 1 to 8, which represent the individual bits of the combined value. The STI00x channels are expressed in Volt and contain [TTL](https://en.wikipedia.org/wiki/Transistor–transistor_logic) level voltages.

The following code finds all unique events and aligns the individual bits in the STI00x channels with the combined value in a table.

    sample  = unique(smp)';
    latency = (sample-1)/hdr.Fs;
    type    = unique(typ)';

    trigarray = nan(length(sample), length(type));

    for i=1:numel(sample)
      sel = find(smp==sample(i));
      for j=1:numel(sel)
          trigarray(i, strcmp(type, typ{sel(j)})) = val(sel(j));
      end
    end

    trigtable = array2table(trigarray, 'VariableNames', type);
    trigtable = [table(sample, latency) trigtable];

    writetable(trigtable, 'trigger.xls');

The table can easily be exported to Excel or LibreOffice, where you can do additional checks on the columns.

{% include image src="/assets/img/faq/triggers/screen_shot_2017-09-20_at_17.50.22.png" width="600" %}

The STI101 channel represents stimuli, in STI102 you can see the response codes corresponding to button presses.

Note that the event type "Trigger" replicates the event type "STI101". We recommend that you use STI101 for consistency with Neuromag/Elekta/Megin and MNE software.
