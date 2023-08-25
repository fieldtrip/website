---
title: Communication guidelines
tags: [guidelines, development]
---

# Communication guidelines

To communicate with and reach a wide audience, we use the following channels

- this website, for documentation
- the email [discussion list](/discussion_list), for interactions among users to help each other out
- [GitHub](https://github.com/fieldtrip), for interaction between developpers
- [Mastodon](https://fosstodon.org/@fieldtriptoolbox), for release announcements and news items

With each of these we reach out to a specific group FieldTrip stakeholders but - although they are partially overlapping - there is none through which we reach everyone.

## News items and releases

These are to be announced on the website and on Mastodon.

To add a news item to the website, please file a pull request adding a new file to the [\_posts folder on the website](https://github.com/fieldtrip/website/tree/master/_posts). See example files there for how these (markdown) files should be structured. The latest files flagged as `categories: [news]` will, when merged, appear on the homepage.

Whenever a new release is made following automatic code [testing](/development/testing), a news item is automatically made that is flagged as `categories: [release]` in the header, and sent as pull request to the [website repository](https://github.com/fieldtrip/website/pulls). This PR has to be reviewed and summarized for human readability by one of the website editors. If merged, the "latest release" section on the homepage will automatically be updated to reflect this.

All news items (both "manually created" and those corresponding to new releases) can contain a `tweet` element in the header. This can contain up to 280 characters for the tweet/toot that is automatically sent once the news item is merged with the website repository. At that moment the news item appears on the website, and a tweet/toot is sent out.

If you only want to send a tweet/toot, you can make a news item without either `news` or `release` as category in the page header (or without any `categories` line at all), but with a `tweet` in the header. Idem for a news item for the website without a tweet: just leave out the `tweet` in the page header and only add the relevant category.

## Code changes and commits

People that are interested in following the details of the development can follow these on their own initiative on GitHub by "watching" the [fieldtrip/fieldtrip](https://github.com/fieldtrip/fieldtrip) or [fieldtrip/website](https://github.com/fieldtrip/website) repository.
