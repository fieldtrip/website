---
title: Making your own trialfun for conditional trial definition
tags: [example, raw, preprocessing, trialfun, trialdef]
redirect_from:
- /example/making_your_own_trialfun_for_conditional_trial_definition/
---

# Making your own trialfun for conditional trial definition

The **[ft_definetrial](/reference/ft_definetrial)** function allows you to specify your own MATLAB function for conditional selection of data segments or trials of interest. That is done using the `cfg.trialfun` option. Using a trial-function you can use an arbitrary complex conditional sequence of events to select data, e.g., only correct responses, or only responses that happened between 300 and 750 ms after the presentation of the stimulus. You can also use your own reading function to obtain the events, or you can read the data from an EMG channel to detect the onset of muscle activity.

This trial-function should be a MATLAB function with the following function definition

    function [trl, event] = your_trialfun_name(cfg);

The configuration structure will contain the fields cfg.dataset, cfg.headerfile and cfg.datafile. If you want to pass additional information (e.g., trigger value), then you should do that in the sub-structure cfg.trialdef.xxx. The second output argument of the trialfun is optional, it will be added to the configuration if present (i.e. for later reference).

Ensure that your trial function is available on the MATLAB path for it to be found by MATLAB and invoked by the call to **[ft_definetrial](/reference/ft_definetrial)**. 

{% include markup/skyblue %}
In the [fieldtrip/trialfun](https://github.com/fieldtrip/fieldtrip/tree/master/trialfun) directory you can find a number of example trial functions.
{% include markup/end %}

## Examples

### Conditional on the trigger sequence

This is an example for a trial function that detects trigger code 7, followed by trigger code 64. 

    function [trl, event] = trialfun_conditionaltrigger(cfg);

    % TRIALFUN_CONDITIONALTRIGGER requires the following configuration settings
    %   cfg.dataset         = filename
    %   cfg.trialdef.pre    = pre-trigger time, in seconds
    %   cfg.trialdef.post   = post-trigger time, in seconds

    % read the header information and the events from the data
    hdr   = ft_read_header(cfg.dataset);
    event = ft_read_event(cfg.dataset);

    % search for "trigger" events
    value  = [event(find(strcmp('trigger', {event.type}))).value]';
    sample = [event(find(strcmp('trigger', {event.type}))).sample]';

    % determine the number of samples before and after the trigger
    pretrig  = -round(cfg.trialdef.pre  * hdr.Fs);
    posttrig =  round(cfg.trialdef.post * hdr.Fs);

    % look for the combination of a trigger "7" followed by a trigger "64"
    % for each trigger except the last one
    trl = [];
    for j = 1:(length(value)-1)
    trg1 = value(j);
    trg2 = value(j+1);
    if trg1==7 && trg2==64
      trlbegin = sample(j) + pretrig;
      trlend   = sample(j) + posttrig;
      offset   = pretrig;
      newtrl   = [trlbegin trlend offset];
      trl      = [trl; newtrl];
    end
    end

When calling **[ft_definetrial](/reference/ft_definetrial)**, you would specify

    cfg = ...
    cfg.trialfun = 'trialfun_conditionaltrigger';
    cfg.trialdef.pre  = 0.5;
    cfg.trialdef.post = 1.0;

and you would call

    cfg = ft_definetrial(cfg);

followed by

    data = ft_preprocessing(cfg);

You could of course also make the trigger value (which are hard-coded here) configurable by passing them in the cfg structure.

### Conditional on stimulus and response

Let's say that your EEG acquisition system has separate inputs for the stimulus and the response and that ft_read_event represents them as a "stimulus" and as a "response", then the following trialfun could be used to select trials time-locked to the stimulus but conditional to the response.

    function [trl, event] = trialfun_stimulusresponse(cfg);
 
    % TRIALFUN_STIMULUSRESPONSE requires the following configuration settings
    %   cfg.dataset         = filename
    %   cfg.trialdef.pre    = pre-trigger time, in seconds
    %   cfg.trialdef.post   = post-trigger time, in seconds

    % read the header information and the events from the data
    hdr   = ft_read_header(cfg.dataset);
    event = ft_read_event(cfg.dataset);

    % determine the number of samples before and after the trigger
    pretrig  = -round(cfg.trialdef.pre  * hdr.Fs);
    posttrig =  round(cfg.trialdef.post * hdr.Fs);

    % search for "stimulus" events
    stimulus_value  = [event(find(strcmp('stimulus', {event.type}))).value]';
    stimulus_sample = [event(find(strcmp('stimulus', {event.type}))).sample]';

    % search for "response" events
    response_value  = [event(find(strcmp('response', {event.type}))).value]';
    response_sample = [event(find(strcmp('response', {event.type}))).sample]';

    if length(stimulus_sample)~=length(response_sample)
    error('the number of stimuli and responses is different');
    end

    if any((response_sample-stimulus_sample)<=0)
    error('there is a response prior to a stimulus');
    end

    reaction_time = (response_sample-stimulus_sample)/hdr.Fs;

    % define the trials
    trl(:,1) = stimulus_sample + pretrig;  % start of segment
    trl(:,2) = stimulus_sample + posttrig; % end of segment
    trl(:,3) = pretrig;                    % how many samples prestimulus

    % add the other information
    % these columns will be represented after ft_preprocessing in "data.trialinfo"
    % the last column in this example contains a "correct" boolean flag for each trial
    trl(:,4) = stimulus_value;
    trl(:,5) = response_value;
    trl(:,6) = reaction_time;
    trl(:,7) = (stimulus_value==3 & response_value==103) | (stimulus_value==4 & response_value==104);

When calling **[ft_definetrial](/reference/ft_definetrial)**, you would specify

    cfg = ...
    cfg.trialfun = 'trialfun_stimulusresponse';
    cfg.trialdef.pre  = 0.5;
    cfg.trialdef.post = 1.0;

and you would call

    cfg = ft_definetrial(cfg);

followed by

    data = ft_preprocessing(cfg);

### Rising flank of a TTL trigger

The example scripts assume that the event is marked by an 'up' flank in the recorded signal (e.g., by virtue of an increase in light on the photodiode transducer). Downward going flanks can also be detected by specifying cfg.detectflank = 'down'. The trigger threshold can be a hard threshold, i.e., numeric, or flexibly defined by an executable string, for example to calculate the 'median' of the analog signal. 

In this example, we define a 'segment' or 'trial' as one second preceding this trigger until 2 seconds thereafter:

    function [trl, event] = trialfun_ttl(cfg)

    % TRIALFUN_TTL requires the following configuration settings
    %   cfg.dataset         = filename
    % The trigger channel index and the length of the window around the trigger are hard-coded below.

    % read the header information
    hdr           = ft_read_header(cfg.dataset);

    detectflank   = 'up'; % detect rising flanks
    threshold     = 'midrange'; % or for example '0.7*max'
    chanindx      = 1;

    % when the event channel index is unknown, but its name or a part thereof (e.g., 'Trig') is known, you can use
    % chanindx = find(ismember(hdr.label, ft_channelselection('Trig*', hdr.label)));

    % read the events from the data
    event         = ft_read_event(cfg.dataset, 'chanindx', chanindx, 'detectflank', detectflank, 'threshold', threshold);

    % define trials around the events
    trl           = [];
    pretrig       = round(1 * hdr.Fs); % e.g., 1 sec before trigger
    posttrig      = round(2 * hdr.Fs); % e.g., 2 sec after trigger
    for i = 1:numel(event)
      offset    = -pretrig;  % number of samples prior to the trigger
      trlbegin  = event(i).sample - pretrig;
      trlend    = event(i).sample + posttrig;
      newtrl    = [trlbegin trlend offset];
      trl       = [trl; newtrl]; % store in the trl matrix
    end

### While the trigger is on

In this example, we define a data segment as the whole period during which the trigger was on, i.e., from the 'up' flank until the 'down' flank.

    function [trl, event] = trialfun_updown(cfg)

    % TRIALFUN_UPDOWN requires the following configuration settings
    %   cfg.dataset         = filename
    % The trigger channel index and the length of the window around the trigger are hard-coded below.

    % read the header information
    hdr           = ft_read_header(cfg.dataset);

    detectflank   = 'both'; % detect up and down flanks
    threshold     = 'midrange'; % or for example '0.7*max'
    chanindx      = 1;

    % when the event channel index is unknown, but its name or a part thereof (e.g., 'Trig') is known, you can use
    % chanindx = find(ismember(hdr.label, ft_channelselection('Trig*', hdr.label)));

    % read the events from the data
    event         = ft_read_event(cfg.dataset, 'chanindx', chanindx, 'detectflank', detectflank, 'threshold', threshold);

    % look for up events that are followed by down events (peaks in the analog signal)
    trl           = [];
    waitfordown   = false;
    for i = 1:numel(event)
        if ~isempty(strfind(event(i).type, 'up')) % up event
            uptrl       = i;
            waitfordown = true;
        elseif ~isempty(strfind(event(i).type, 'down')) && waitfordown % down event
            trlbegin  = event(uptrl).sample;
            trlend    = event(i).sample;
            newtrl    = [trlbegin trlend 0];
            trl       = [trl; newtrl]; % store in the trl matrix
            waitfordown = false;
        end
    end

## Finding out which trigger codes are used

You can use a code snippet like this to see which trigger codes are used in your recording.

    event = ft_read_event(filename);
    plot([event.sample], [event.value], '.')

In case the triggers are of different types, e.g., like here

    disp(unique({event.type}))
    'CM_in_range'    'Epoch'    'STATUS'

you can use this to select only the events of a particular type

    % select only the trigger codes, not the CM_in_range and Epoch events
    sel = find(strcmp({event.type}, 'STATUS'));
    event = event(sel);

## See also

{% include seealso tag="trialfun" %}