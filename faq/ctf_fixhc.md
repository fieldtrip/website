---
title: I am having problems reading the CTF .hc headcoordinates file
category: faq
tags: [ctf, raw]
redirect_from:
    - /faq/i_am_having_problems_reading_the_ctf_.hc_headcoordinates_file/
---

# I am having problems reading the CTF .hc headcoordinates file

The most likely problem that you have with your CTF dataset is due to a bug in the dataset itself. Old versions of the CTF acquisition software would write the .hc file with a typo in the file. The file itself is an ASCII file which you can open (and edit) in any text editor.

The 5th line in the file is

'' stadard left ear coil position relative to dewar (cm):''

but should be

'' standard left ear coil position relative to dewar (cm):''

Note the missing "n" in the problematic .hc headcoordinates file.
