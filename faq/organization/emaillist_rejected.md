---
title: Why is my message rejected from the email discussion list?
tags: [email]
category: faq
redirect_from:
    - /faq/why_is_my_message_rejected_from_the_email_discussion_list/
    - /faq/emaillist_rejected/
---

It might be that you receive the following message when you try to post a question to the email discussion list.

    You are not allowed to post to this mailing list, and your message
    has been automatically rejected.  If you think that your messages are
    being rejected in error, contact the mailing list owner at
    fieldtrip-owner@xxx.xxx.xx.

The most frequent cause is that the email address from which you are **sending** your email is different from the one that you used when you **subscribed** to the email list.

For example, you might use _john.doe@example.com_ to send messages, and _j.doe@example.com_ to receive them. On your side it might appear that both email addresses are the same as messages to both would end up at the same location on your computer, but to the email list server they are different.

To ensure that your email reaches the email discussion list, you have to ensure that the address configured in your email client as the "from" address is the same as the one you used to register. I.e., you should register with the same address as the one you have in your "from" field.

Alternatively, you can also register with both addresses and then use the [web interface](http://mailman.science.ru.nl/mailman/listinfo/fieldtrip) to configure one of the email addresses not to receive emails. That allows you to send from both, but you won't be receiving messages twice.
