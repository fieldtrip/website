---
title: How can I transform trigger values from bits to decimal representation with a trialfun?
category: faq
tags: [trialfun]
---

# How can I transform trigger values from bits to decimal representation with a trialfun?

Some EEG acquisition systems allow users to represent trigger values in bits (see [NETSTATION acquisition manual](http://cb3.unl.edu/dbrainlab/wp-content/uploads/sites/2/2013/12/Acquisition_Manual.pdf) pages 62-72). At some point, the user might be also interested to transform the binary representation to decimal. You can archive a smooth conversion writing your own custom function for the trial definition (see also the [preprocessing tutorial](/tutorial/preprocessing#use_your_own_function_for_trial_selection), the [example1](/example/detect_the_muscle_activity_in_an_emg_channel_and_use_that_as_trial_definition) and [example2](/example/trialfun) to explore other approaches)

The following code transforms bits to decimal numbers in a \*.RAW fileformat from NETSTATION EEG system whos trigger channels are named as "DIN". For example the number 11 is represented with the following trigger sequence: DIN1 + DIN8 + DIN2. The trigger channel name can be changed and it is then LAB SPECIFIC. However you can follow the logic of the code and try to adapt it to a specific system

    function trl = trialfun_bit2dec(cfg)

    % TRIALFUN_BIT2DEC is a trialfun example function that illustrates how to
    % convert trigger values from bits to decimal representation.
    %
    % To know more about how to extract events from a continuous trigger
    % channel that have one or multiple continuously sampled TTL channels in
    % the data see the private function READ_TRIGGER.M (trunk/fileo/private/)
    %
    % The trialdef structure can contain the following specifications
    % cfg.dataset cfg.trialdef.eventtype cfg.trialdef.eventvalue
    % cfg.trialdef.prestim cfg.trialdef.poststim

    %%
    hdr   = ft_read_header(cfg.dataset);
    event = ft_read_event(cfg.dataset);

    % bit to decimal conversion
    for i=1:length(event);
    switch event(i).value
      case 'DIN1'
        bit = 1;
      case 'DIN2'
        bit = 2;
      case 'DIN4'
        bit = 3;
      case 'DIN8'
        bit = 4;
      case 'DI16'
        bit = 5;
      otherwise
        error('weird');
    end % switch

    binarydata(bit, event(i).sample) = 1;
    end

    decimaldata = zeros(1,size(binarydata,2));
    for i=1:size(binarydata,1)
    decimaldata = decimaldata + binarydata(i,:) *(i-1)^2;
    end

    % reinsert them as decimal values
    for i=1:length(event)
    event(i).value = decimaldata(event(i).sample);
    end

    % define trials
    trl = [];

    for i=1:length(event)
    if strcmp(event(i).type, cfg.trialdef.eventtype)
      % it is a trigger, see whether it has the right value
      if ismember(event(i).value, cfg.trialdef.eventvalue)
        % add this to the trl definition
        begsample     = event(i).sample - cfg.trialdef.prestim*hdr.Fs;
        endsample     = event(i).sample + cfg.trialdef.poststim*hdr.Fs - 1;
        offset        = -cfg.trialdef.prestim*hdr.Fs;
        trigger       = event(i).value; % remember the trigger (=condition) for each trial
        trl(end+1, :) = [round([begsample endsample offset])  trigger];
      end
    end
    end

    % discard the repeated values
    idx = any(diff(trl(:,1),1,1),2);
    trl = trl(idx,:);
