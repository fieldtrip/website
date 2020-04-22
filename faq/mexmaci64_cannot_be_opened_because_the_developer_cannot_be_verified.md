---
title: MATLAB complains that mexmaci64 cannot be opened because the developer cannot be verified
tags: [faq, matlab]
---

# MATLAB complains that mexmaci64 cannot be opened because the developer cannot be verified

When you try to use FieldTrip on macOS Catalina, you may get the error

```matlab
"ft_getopt.mexmaci64" cannot be opened because the developer cannot be verified.
macOS cannot verify that this app is free from malware.
```

{% include image src="/assets/img/faq/mexmaci64_cannot_be_opened_because_the_developer_cannot_be_verified/screenshot.png" width="400" %}

or a similar error for another mex file that is included with FieldTrip.

This problem is due to additional security measures implemented in macOS. MATLAB mex files are small dynamically linked libraries (comparable to `.dll` files on Windows), that are loaded and linked to the MATLAB executable as soon as you execute the function implemented in the mex file. The problem is discussed in more detail [here](https://osxdaily.com/2015/07/15/add-remove-gatekeeper-app-command-line-mac-os-x/), which also provides a solution.

If you trust the source where you have downloaded FieldTrip, you can resolve these errors for all mex files at once by opening a terminal and typing

```bash
find LOCATION_OF_FIELDTRIP -name “.mex” -exec spctl --add {} \;
```

where `LOCATION_OF_FIELDTRIP` is the place where you have unzipped FieldTrip.
