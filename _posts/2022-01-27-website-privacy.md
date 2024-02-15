---
title: 27 January 2022 - Website privacy improvements
categories: [news]
tweet: We have improved the FieldTrip website privacy by implementing @DuckDuckGo as search engine and @PlausibleHQ for statistics. No more cookies to count visitors! See http://www.fieldtriptoolbox.org/#27-january-2022 for some background.
---

### 27 January 2022

For a long time we used Google Analytics to collect website usage statistics. This allowed us to see how many visitors we have, which is important to convince funding agencies and directors of FieldTrip's impact, and which pages were the most visited, which helps to guide our efforts in improving documentation.

In the summer of 2020 we introduced a "cookie banner" with the opportunity to disable third-party cookies. The number of unique visitors that was _counted_ subsequently dropped 85%, from approximately 3500 to 500 per week (with a short glitch in 2021 due to a bug). This indicates that you don't like cookies; which we understand.

{% include image src="/assets/img/posts/cookie-effect.png" width="500" %}

For website usage statistics we have now implemented [Plausible](https://plausible.io), an open source web analytics solution without tracking cookies that is fully compliant with GDPR, CCPA and PECR. It only stores _that_ you have visited, not _who you are_, and it does not share any information across websites to build user profiles. Plausible allows us to get the minimal information that we need, but none of your personal information.

Furthermore, we have updated the search functionality. If you are fine with third-party cookies, it will continue to use Google Search. If you reject third-party cookies, it will now use DuckDuckGo, which does not track you.
