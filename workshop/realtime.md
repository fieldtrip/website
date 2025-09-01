---
title: Realtime MEG BCI hands-on session in Nijmegen
tags: [realtime]
---

To set up MATLAB, you should do

    restoredefaultpath
    addpath h:\common\matlab\fieldtrip
    addpath h:\common\matlab\fieldtrip\realtime\example
    addpath h:\common\matlab\fieldtrip\realtime\online_eeg
    addpath h:\common\matlab\fieldtrip\realtime\online_meg
    ft_defaults

## Relevant locations on the network drive

- h:\\common\\matlab\\fieldtrip
- h:\\common\\matlab\\fieldtrip\\data

Connect to the MEG acquisition computer at 131.174.44.180 with

    hdr = ft_read_header('buffer://odin:1972')

## Relevant links

- <https://www.fieldtriptoolbox.org/development/realtime>
- <http://www.nici.ru.nl/brainstream/twiki/bin/view/BrainStreamDocs/WebHome>
- <https://intranet.donders.ru.nl/index.php?id=4231>
- <https://intranet.donders.ru.nl/index.php?id=4438> including channel layout
