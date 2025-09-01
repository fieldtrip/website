---
title: Lessons learned
tags: [toolkit2020]
---

If you ask all participants to do something online (such as answer a poll, or provide information about their MATLAB version), only 50% of them will actually do it, which might go up to 75% after asking repeatedly. So you cannot check explicitly with everyone, only get some statistics.

Even if you give participants explicit instructions on downloading and installing a “recent version” of FieldTrip, quite some do not (or consider a 1 or 2 year version recent enough). Perspectives on “recent” apparently differ.

Some people will use a MATLAB version that is 5 years old, whereas some other people will use the latest MATLAB version (released last month) that has not been tested thoroughly yet.

Also beware of the YEARa versions. These are in my experience somewhat more buggy than the YEARb versions.

People that get the error “DPSS, Signal Processing toolbox not found” do not have a license for the signal toolbox and can use the drop-in replacement for the dpss function (for spectral analysis with multitapers). This will not be automatically detected by FieldTrip, so users need to manually add `<path-to-fieldtrip>/external/signal/dpss_hack` to their path.

Switching between Zoom breakout rooms (to allow participants to self-organize) requires that all participants are assigned as co-host. This needs to be done every time they log in. People have to be aware of this, and ask the host to be reassigned if needed.

The host and the co-hosts in Zoom cannot raise their hands.

Co-hosts can mute anyone, including the host.

General announcements in Zoom (that span over all breakout rooms) are easily missed.

Once people spread out over two pages of webcam thumbnails in Zoom, you cannot look at them any more like you normally would do when scanning the audience in a physical meeting/lecture.

Besides a lecturer or presenter, you need a moderator or sidekick in large online meetings. While the lecturer presents or answers questions, the assistant keeps an eye on the audience (e.g., checking the Slack channel, raising hands in the Zoom, new additions to the google doc). So the “lecturer” focuses on the content, whereas the “assistant” acts as moderator.  The lecturer needs his full attention (and his full screen) for the content, whereas the assistant keeps an eye on the different communication channels.

During the hands-on sessions all people move to Zoom breakout rooms. At that moment it is helpful to have a single tutor that stays in the general (starting) room. Participants occasionally leave the Zoom meeting or drop out of it (Zoom crashes, network interruptions, laptop battery empty) which means that the later join again. The "doorman" can welcome them and ensure that hey become co-host again and get assigned to a breakout room. The doorman could in principle also act as the bouncer, but luckily that was not needed.

Shared google docs to collect questions during the talks works fine. The majority of people online on Zoom also have the google doc in front of them (as visible by the number of anonymous viewers on the google doc).

Having the shared Q&A documents makes people take the exercises in the tutorials more serious than they are actually meant to be. People really want an answer, and sometimes they just serve to activate the people but don’t have clear answers.

If - as presenter on Zoom - you want to share a link, you can just ask someone to post it on Slack or in the comments. There is always someone (e.g., a tutor) available who know what you mean and who will post it for you.

When people want to share their screen, MATLAB code is often too small to be visible to others. Instead, ask participants to copy-paste it into their personal Q&A document. This way, tutors can easy see it and even provide (copy-paste) their own code below it.
Alternatively, ask participants to copy-paste their code into a .txt file (minimal formatting) and increase font size.
