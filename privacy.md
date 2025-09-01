---
title: Privacy Policy
tags: [support]
redirect_from:
  - /faq/tracking/
---

This website is hosted on a server of the [Donders Centre for Cognitive Neuroimaging](https://www.ru.nl/donders/), [Radboud University](https://www.ru.nl/english/), Nijmegen, the Netherlands. The web server logs web page access and IP addresses for technical and security reasons, but does not retain information about individual users.

## How we process your personal data on this website

This website does not use cookies and does not include content from external commercial services like Google, Facebook or Twitter that would track users and collect statistics. We do use a self-hosted instance of [plausible](https://plausible.io), an open-source web analytics solution without tracking cookies that is fully compliant with GDPR, CCPA and PECR. It only stores _that_ you have visited, not _who you are_, and it does not share any information across different websites which could be used to build a user profile.

The embedded YouTube and Vimeo videos on this website are displayed in a way that does not place cookies on your computer. We use the [anonymous crossorigin](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/crossorigin) attribute for resources that are loaded from external services, such as javascript libraries.

When you use the search functionality, you will be redirected to Google, which may track your internet usage.

## How we process your personal data when you download the FieldTrip toolbox

You can download FieldTrip from a download server that is hosted on a server of the Donders Centre for Cognitive Neuroimaging, Radboud University Nijmegen. The download server tracks the downloads and IP addresses for technical and security reasons, but does not retain information about individual users. We do store the information that you provide in the download form. Note that you are not required to use the download form, you can also go to the download server directly.

Alternatively, you can download and contribute to FieldTrip from GitHub, which is an external service. The processing of your data by GitHub is explained in its [privacy policy](https://github.com/site/privacy).

## How we process your personal data when you use the FieldTrip toolbox

The FieldTrip toolbox itself includes the **[ft_trackusage](/reference/utilities/ft_trackusage)** function. This function is called once in every new MATLAB session from within **[ft_defaults](/reference/ft_defaults)** at the moment that you start using the first high-level FieldTrip function. The first time ever that you start FieldTrip, you will see a warning message in your MATLAB command window about this.

The reason for tracking is to gather information about the number of users, how often FieldTrip is used, which versions of FieldTrip are used, and which versions of MATLAB are used. This information helps us in deciding where to focus our attention in continued development. Furthermore, this information is used to inform our funding sources about the success. We do not store any directly identifiable information about your login name or computer name, but encrypt it with a [random salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) that is unique to your computer and not shared with us.

You can disable usage tracking at startup by specifying

    global ft_default
    ft_default.trackusage = 'no';

prior to calling **[ft_defaults](/reference/ft_defaults)** for the first time in your MATLAB session. We recommend that you do this in your `startup.m` file. Alternatively you can do

    prefs = load(fullfile(prefdir, 'fieldtripprefs.mat'))
    prefs.trackusage = 'no';
    save(fullfile(prefdir, 'fieldtripprefs.mat'), '-struct', 'prefs')

You can also store other global defaults this way: the content of the `fieldtripprefs.mat` file is merged with the global `ft_default` variable, which in turn is merged with the `cfg` variable that each high-level FieldTrip function uses.
