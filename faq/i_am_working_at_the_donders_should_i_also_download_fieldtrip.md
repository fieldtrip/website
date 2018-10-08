---
layout: default
---

{{tag>faq path download}}

## I am working at the Donders, should I also download FieldTrip?

If you want to use FieldTrip inside the DCCN, you should **not use the ftp version**. Instead you should add h:\common\matlab\fieldtrip (on windows) or /home/common/matlab/fieldtrip (on linux) to your Matlab path. 

This common FieldTrip version on our network is automatically updated with each improvement to the code. That is also the reason why you should add that directory to your path, and not make your own copy (otherwise you would not benefit from the ongoing updates and improvements).

If you want to do your computations on your laptop or at home, i.e. if you cannot access the h: drive, you can use the ftp or git version.

See also this FAQ on [how to setup your FieldTrip path in MATLAB](/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path).
