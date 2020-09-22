---
title: Communication guidelines
tags: [guidelines, development]
---

# Communication guidelines

To communicate with and reach a wide audience, we use the following channels

- this website, for documentation
- the email [discussion list](/discussion_list), for interactions between users and support
- [GitHub](http://github.com/fieldtrip), for interaction between developpers
- [Twitter](http://twitter.com/fieldtriptoolbx), for announcements and news
- [FaceBook](http://facebook.com/fieldtriptoolbox), which we are not actively using at the moment

With each of these we reach out to a specific group FieldTrip stakeholders but - alhough they are partially overlapping - there is none of them through which we reach everyone.

## News items and releases

These are to be announced on the website and on twitter.

Whenever a new release is made following automatic code [testing](http://www.fieldtriptoolbox.org/development/testing/), a news item is automatically made that is flagged as `category` release in the header, and send as pull request to the [website repository](https://github.com/fieldtrip/website/pulls). This PR has to be reviewed and summarized for human readability by one of the website editors. The news item for the release also contains a `tweet` element in the header, which can contain up to 280 characters for the tweet that is automatically send once the news item is merged with the website repository. At that moment the news item appears on the website, and a tweet is send out.

If you only want to send a tweet, you can make a news item without the `category` line in the page header, but with a `tweet` in the header. Idem for a news item for the website without a tweet: just leave out the `tweet` in the page header and only add the relevant category.  

## Code changes and commits

People that are interested in following the details of the development can follow these on their own initiative on GitHub by "watching" the [fieldtrip/fieldtrip](https://github.com/fieldtrip/fieldtrip) or [fieldtrip/website](https://github.com/fieldtrip/website) repository.
