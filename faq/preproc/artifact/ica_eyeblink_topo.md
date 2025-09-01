---
title: Why does my ICA eyeblink component look strange?
category: faq
tags: [ica, brainvision]
redirect_from:
    - /faq/ica_eyeblink_topo/
---

Using 64-channel Brainvision data, it could happen that a IC, which in its timecourse clearly presents as an eyeblink component, shows a topographical mixing matrix that looks strange. 

{% include image src="/assets/img/faq/ica_eyeblink_topo/topo_strange01.png" width="600" %}

In a slightly other visualization it becomes clear that there's something off with the mixing. 
For instance, the Iz electrode at the back gets a very high mixing weight. 

{% include image src="/assets/img/faq/ica_eyeblink_topo/topo_strange02.png" width="400" %}

The most likely cause for this is that something has gone wrong with the labelling of the electrodes during the recording, resulting in a mismatch between the layout used for plotting, and the way that the electrode labels ended up in the data. This, for instance, could result from plugging the electrodes into the 'wrong' sockets at the control boxes (which would be very difficult to debug), or from accidentally swapping the 2 fiber optic connector cables (each of which connecting to a 32-channel box). To check whether the latter has been the case, you can evaluate whether swapping the ```topolabel``` around fixes the plotted topography, i.e. by doing something like: ```comp.topolabel = comp.topolabel([33:64 1:32]);```. Having done this for the data used for the above figures, we can generate a new set of topographies.

{% include image src="/assets/img/faq/ica_eyeblink_topo/topo_fixed.png" width="600" %}

Based on this, we can conclude that indeed the connector cables were accidentally swapped during the recording. This means that there is a mismatch in how the electrodes are labeled in the ```.vhdr``` file. This could - in principle - be solved by manually updating the header file (it's a text-file anyway. Alternatively - and perhaps preferred - you can/need to rename the channels, either after reading the data using **[ft_preprocessing](/reference/ft_preprocessing)**, or by directly using a [montage](/faq/preproc/datahandling/rename_channels) in the cfg for **[ft_preprocessing](/reference/ft_preprocessing)**.

