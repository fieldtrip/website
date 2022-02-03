---
title: Privacy Policy
tags: [support]
redirect_from:
  - /faq/tracking/
---

# Privacy Policy

This website is hosted on a server of the [Donders Centre for Cognitive Neuroimaging](https://www.ru.nl/donders/), [Radboud University](https://www.ru.nl/english/), Nijmegen, the Netherlands. The web server logs web page access and IP addresses for technical and security reasons, but does not retain information about individual users.

## How we process your personal data on this website

This website by itself does not use cookies, except for a single cookie which specifies whether third party cookies and scripts can be used. We also link to content and documentation on external websites, these are not covered here.

If you do not allow third party cookies and scripts to be used on this website, the search functionality will default to DuckDuckGo. If you do allow third party cookies, it will default to Google Search.

Regardless of your permission for third party cookies, the embedded YouTube and Vimeo videos on this website are displayed in a way that does not place cookies on your computer.

We do not use external tools to collect website statistics. We use a self-hosted instance of [plausible](https://plausible.io), an open source web analytics solution without tracking cookies that is fully compliant with GDPR, CCPA and PECR. It only stores _that_ you have visited, not _who you are_, and it does not share any information across different websites which could be used to build a user profile.

### External third-party cookies

If you approve third-party cookies and scripts, this website will use custom Google search forms to search this website and the email discussion list. Furthermore, it will embed videos from Youtube and Vimeo on the [video](/video) overview page and on some [tutorials](/tutorial). By loading and displaying content from these external services, these may place cookies on your computer and track your personal information.

### Reset the permission for third party cookies and scripts

Click here to reset the permission for third party cookies and scripts:

<p><button name="button" onclick="eraseCookie('allow-external-cookies');location.reload()" class="btn btn-primary btn-sm">Reset cookie permission</button></p>

## How we process your personal data when you download the FieldTrip toolbox

You can download FieldTrip from an FTP server that is hosted on a server of the Donders Centre for Cognitive Neuroimaging, Radboud University Nijmegen. The FTP server allows anonymous logins, it tracks the downloads and IP addresses for technical and security reasons, but does not retain information about individual users. We do store the information that you provide in the download form. Note that you are not required to use the download form, you can also go to the FTP server directly.

Alternatively, you can download and contribute to FieldTrip from GitHub, which is an external service. The processing of your data by GitHub is explained in its [privacy policy](https://github.com/site/privacy).

## How we process your personal data when you use the FieldTrip toolbox

The FieldTrip toolbox itself includes the **[ft_trackusage](https://github.com/fieldtrip/fieldtrip/blob/release/utilities/ft_trackusage.m)** function. This function is called once in every new MATLAB session from within **[ft_defaults](https://github.com/fieldtrip/fieldtrip/blob/release/ft_defaults.m)** at the moment that you start using the first high-level FieldTrip function. The first time ever that you start FieldTrip, you will see a warning message in your MATLAB command window about this.

The reason for tracking is to gather information about the number of users, how often FieldTrip is used, which versions of FieldTrip are used, and which versions of MATLAB are used. This information helps us in deciding where to focus our attention in continued development. Furthermore, this information is used to inform our funding sources about the success. We do not store any directly identifyable information about your login name or computer name, but encrypt it with a [random salt](https://en.wikipedia.org/wiki/Salt_(cryptography)) that is unique to your computer and not shared with us.

You can disable usage tracking at startup by specifying

    global ft_default
    ft_default.trackusage = 'no';

prior to calling **[ft_defaults](https://github.com/fieldtrip/fieldtrip/blob/release/ft_defaults.m)** for the first time in your MATLAB session. We recommend that you do this in your `startup.m` file. Alternatively you can do

    prefs = load(fullfile(prefdir, 'fieldtripprefs.mat'))
    prefs.trackusage = 'no';
    save(fullfile(prefdir, 'fieldtripprefs.mat'), '-struct', 'prefs')

You can also store other global defaults this way: the content of the `fieldtripprefs.mat` file is merged with the global `ft_default` variable, which in turn is merged with the `cfg` variable that each high-level FieldTrip function uses.
