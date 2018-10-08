---
layout: default
---

{{tag>realtime workshop}}

#  Realtime MEG BCI hands-on session


To set up MATLAB, you should do

    restoredefaultpath
    addpath h:\common\matlab\fieldtrip
    addpath h:\common\matlab\fieldtrip\realtime\example
    addpath h:\common\matlab\fieldtrip\realtime\online_eeg
    addpath h:\common\matlab\fieldtrip\realtime\online_meg
    ft_defaults

Relevant locations on the network driv

*  h:\common\matlab\fieldtrip
*  h:\common\matlab\fieldtrip\data


Acquisition computer 131.174.44.180

    hdr = ft_read_header('buffer://odin:1972')


Relevant link

*  http://www.fieldtriptoolbox.org/development/realtime

*  http://www.nici.ru.nl/brainstream/twiki/bin/view/BrainStreamDocs/WebHome

*  https://intranet.donders.ru.nl/index.php?id=4231

*  https://intranet.donders.ru.nl/index.php?id=4438 including channel layout
    
