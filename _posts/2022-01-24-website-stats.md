---
title: 24 January 2022 - Website privacy improvements
categories: [news]
tweet: We have improved the FieldTrip website privacy by implementing @PlausibleHQ. No more cookies to count visitors! See http://www.fieldtriptoolbox.org/#24-january-2022 for some background.
---

### 24 January, 2022

For a long time we used using Google Analytics to collect website usage statistics. This allowed us to see how many visitors we have, which is important to convince funding agencies and directors of FieldTrip's impact, and which pages were the most visited, which helps to guide our efforts in improving documentation.

In the summer of 2020 we introduced a "cookie banner" with the opportunity to disable all cookies (and consequently disaable google analytics, as well as search and inline youtube and vimeo content). The number of unique visitors that was counted subsequently dropped 85%, from ~3500 per week to ~500 per week. This indicates that you don't like cookies; which we understand.

{% include image src="/assets/img/posts/cookie-effect.png" width="500" %}

We have now implemented [plausible](https://plausible.io), an open source web analytics solution without tracking cookies that is fully compliant with GDPR, CCPA and PECR. It does only stores _that_ you have visited (on a private server), not who you are, and it does not share any information over websites to build (advertisment) profiles. This allows us to get the information that we need, and gives the website visitors to worry about.

In the near future we hope to also realize a privacy-friendly alternative for google search, which is now disabled for most of you anyway.
