---
title: MATLAB complains that mexmaci64 cannot be opened because the developer cannot be verified
tags: [matlab, mex]
category: faq
redirect_from:
    - /faq/mexmaci64_cannot_be_opened_because_the_developer_cannot_be_verified/
    - /faq/mex_osx/
---

When you try to use FieldTrip on macOS Catalina or later, you may get an error like

```matlab
"ft_getopt.mexmaci64" cannot be opened because the developer cannot be verified.
macOS cannot verify that this app is free from malware.
```

{% include image src="/assets/img/faq/mex_osx/screenshot.png" width="400" %}

or a similar error for another mex file that is included with FieldTrip.

This problem is due to additional security measures implemented in macOS. MATLAB mex files are small dynamically linked libraries (comparable to `.dll` files on Windows), that are loaded and linked to the MATLAB executable as soon as you execute the function implemented in the mex file. The problem is discussed in more detail [here](https://osxdaily.com/2015/07/15/add-remove-gatekeeper-app-command-line-mac-os-x/), which also provides a solution.

If you trust the source where you have downloaded FieldTrip, you can resolve these errors for all mex files at once by opening a terminal and typing the following if you have Apple Silicon (M1, M2, M3, etc) mac

```bash
sudo xattr -r -d com.apple.quarantine LOCATION_OF_FIELDTRIP

sudo find 'LOCATION_OF_FIELDTRIP' -name \*.mexmaca64 -exec spctl --add {} \;
```

or if you have an older Intel mac

```bash
sudo xattr -r -d com.apple.quarantine LOCATION_OF_FIELDTRIP

sudo find 'LOCATION_OF_FIELDTRIP' -name \*.mexmaci64 -exec spctl --add {} \;
```

where `LOCATION_OF_FIELDTRIP` is the place where you have unzipped FieldTrip. If your mac is using the zsh shell (the default since macOS 10.15) rather than bash, it is important to include the quotes around the `LOCATION_OF_FIELDTRIP` as otherwise it will not find mex files in subdirectories.

Following `sudo` you will have to give your administrator password.

The first command removes all FieldTrip files from [quarantaine](https://derflounder.wordpress.com/2012/11/20/clearing-the-quarantine-extended-attribute-from-downloaded-applications/).

The second command adds a [Gatekeeper exception](https://osxdaily.com/2015/07/15/add-remove-gatekeeper-app-command-line-mac-os-x/) to all mex files.

See also this documentation on the [Apple website](https://support.apple.com/en-gb/guide/mac-help/mchleab3a043/mac).
