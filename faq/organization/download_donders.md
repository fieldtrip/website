---
title: I am working at the Donders, should I also download FieldTrip?
parent: Organizational questions
grand_parent: Frequently asked questions
category: faq
tags: [path, download]
redirect_from:
    - /faq/i_am_working_at_the_donders_should_i_also_download_fieldtrip/
    - /faq/download_donders/
---

# I am working at the Donders, should I also download FieldTrip?

If you want to use FieldTrip at the Donders Centre for Cognitive Neuroimaging (DCCN) in Nijmegen, you do not have to download it. Instead you can add `h:\common\matlab\fieldtrip` (on Windows) or `/home/common/matlab/fieldtrip` (on Linux) to your MATLAB path.

{% include markup/yellow %}
To have precise control over the FieldTrip version that you are using in your analysis, we do recommend that you use the github version.
{% include markup/end %}

The common FieldTrip version on the shared network drive is automatically updated with each improvement to the code, which is why you should add that directory to your path, and not make your own copy (otherwise you would not benefit from the ongoing updates and improvements).

If you want to do your computations on your laptop or at home, you can use the download or github version.

See also this FAQ on [how to setup your FieldTrip path in MATLAB](/faq/installation).
