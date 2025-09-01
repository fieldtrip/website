---
title: Why am I receiving warnings about too many bouncing emails?
category: faq
tags: [email]
redirect_from:
    - /faq/why_am_i_receiving_warnings_about_too_many_bouncing_emails/
    - /faq/emaillist_bounces/
---

A "bounce" means that the email from the mailing list cannot be delivered to your email server.

Please see http://www.list.org/mailman-member/node25.html and note the section

_If your mail provider "bounces" too many messages (that is, it tells Mailman that the message could not be delivered) Mailman eventually stops trying to send you mail. This feature allows Mailman to gracefully handle addresses which no longer exist (for example, the subscriber has found a new internet service provider and forgot to unsubscribe the old address), as well as addresses which are temporarily out-of-service (for example, the subscriber has used up all of the allotted space for his or her email account, or the subscriber's mail provider is experiencing difficulties)._

We are using the mailman list server of the Radboud University and cannot check the logs for the reason why your mailserver is bouncing the mails from the list. It might be that your server is unavailable, that your email address does not exist any more, or that your inbox is full.

However, every time your mail server bounces (i.e. returns because of an error) an email to our server, our server gets the extra load to deal with it. It will accept a few occasional bounces, but if there are more you will receive a warning you of frequent bounces. If there are too many bounces, your email address will be automatically disabled.

You can consider switching to a more robust mail provider and re-register on the list with a new email address.
