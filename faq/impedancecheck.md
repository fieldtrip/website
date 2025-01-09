---
title: How can I inspect the electrode impedances of my data?
parent: Reading and preprocessing data
category: faq
tags: [eeg, electrode]
redirect_from:
    - /faq/how_can_i_inspect_the_electrode_impedances_of_my_data/
---

# How can I inspect the electrode impedances of my data?

The quality of EEG signals depends for a large part on how well the electrodes make contact to the skin. Currents flow from the head across the skin-gel-electrode interface and through wires to the amplifier. Along this path the current will face some resistance, often called impedance. Impedance is related to voltage and current by Ohm's law (I = V/R).

In general, the higher the impedance of an electrode, the lower the signal-to-noise ratio of the EEG signal. Importantly, recording EEG with a lower signal-to-noise ratio may increase noise levels and decrease the probability of obtaining statistically signifcant effects.

Most modern EEG systems are capable of measuring the impedance at each electrode, and save these values in the header file. The following example script can be used to visualize the impedance values at the start of the recording of your EEG dataset.

This example reads the impedance values from an EEG dataset recorded with [BrainVision PyCorder](http://www.brainvision.com/pycorder.html).

## Read impedance values

    % Read header file
    fid = fopen('PP01.vhdr', 'r');
    C = textscan(fid, '%s', 'Delimiter', '\n');
    fclose(fid);

    C=C{1,1};

    %F ind the line containing 'Impedance'
    D = strfind(C, 'Impedance');
    rows = find(~cellfun('isempty', D));

    %Read channelnames and impedance
    temp = {};
    for i = rows+1:length(C)-1
      temp = [temp; textscan(char(C(i)),'%d%s%d')];
    end
    temp = [temp; [cell(1) textscan(char(C(length(C))),'%s%d')]];

    % Remove colon from channel name
    chantemp = temp(:,2);
    for j = 1:length(chantemp)
      chan = char(chantemp{j});
      chantemp{j} = chan(1:end-1);
    end

    imp             = [];
    imp.label       = chantemp;
    imp.imp         = cell2mat(temp(:,3));
    imp.time        = 1;
    imp.dimord      = 'chan_time';

## Plot impedance values

Make a plot of the ''imp'' structure containing the impedance values using a custom colormap (green, yellow and red)

    cfg             = [];
    cfg.parameter   = 'imp';
    cfg.layout      = 'EEG1010.lay';
    cfg.max_imp     = 20;

    % Create a custom colormap
    T = [  0, 255,   0        % green
       255, 255,   0        % yellow
       255,   0,   0]./255; % red

    x = [0
      cfg.max_imp/2
      cfg.max_imp];

    map = interp1(x/cfg.max_imp,T,linspace(0,1,cfg.max_imp));

    cfg.style               = 'blank';
    cfg.marker              = 'labels';
    cfg.markersize          = 7;
    cfg.markerfontsize      = 12;

    cfg.highlight           = repmat({'labels'},1,numel(imp.label));

    chans = cell(1,numel(imp.label));
    for nchan = 1:numel(imp.label)
      chans{nchan} = imp.label(nchan);
    end

    cfg.highlightchannel    = chans;
    cfg.highlightsymbol     = repmat({'.'},1,numel(imp.label));
    cfg.highlightsize       = repmat({50},1,numel(imp.label));

    test                    = map(round(imp.(cfg.parameter)),:);
    cfg.highlightcolor      = mat2cell(test, ones(1, size(test, 1)), size(test, 2))';
    cfg.highlightfontsize   = repmat({8},1,numel(imp.label));

    cfg.comment             = 'no';
    cfg.labeloffset         = 0;

    cfg.colorbar            = 'yes';
    cfg.contournum          = 10;
    cfg.colormap            = map;
    cfg.zlim                = [0 cfg.max_imp];

    % figure
    ft_topoplotER(cfg, imp)

{% include image src="/assets/img/faq/impedancecheck/impedance.png" %}
