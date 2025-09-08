---
title: Fixing a missing channel
tags: [meg, preprocessing, ctf, neighbours]
category: example
redirect_from:
    - /example/fixing_a_missing_sensor/
---

Use this script when one or more channels in the 275 channel CTF system are dead. It identifies the missing sensors and uses **[ft_channelrepair](/reference/ft_channelrepair)** to fix the problem, so you can compare or average this handicapped dataset with complete datasets. Use this function after preprocessing. This snippet of code works if you have loaded into memory (in addition to the data structure you would like to fix,) a full list of labels (let's call this label), and a gradiometer description (a grad-structure) describing all the sensors.

    [notmissing, dummy] = match_str(label, data.label);
    newtrial = cell(size(data.trial));
    for k = 1:numel(data.trial)
      newtrial{k} = zeros(numel(label), size(data.trial{k},2));
      newtrial{k}(notmissing,:) = data.trial{k};
    end
    goodchans   = false(numel(label),1);
    goodchans(notmissing) = true;
    badchanindx = find(goodchans==0);

    data.trial = newtrial; clear newtrial;
    data.label = label;
    warning('Inserting grad that does not actually belong to this dataset!')
    data.grad  = grad;

Subsequently you can use **[ft_channelrepair](/reference/ft_channelrepair)** for nearest neighbourhood averaging. This replaces the zeros in the broken channel with more appropriate values.

    cfg               = []
    cfg.badchannel    = data.label(badchanindx);
    cfg.neighbourdist = 4;
    data = ft_channelrepair(cfg, data);
