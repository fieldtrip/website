---
title: How should I share example data with the email list or developers?
category: faq
tags: [email, development, git]
---

# How should I share example data with the email list or developers?

In general it is not a good idea to send data as email attachment to the email discussion list. You should consider that your data file will end up in ~1000 email inboxes of all other people that are subscribed. I.e. your 10 MB attachment would result in 10 GB of storage requirements. Also when sending example data to one of the developers, you should not send large data files as email attachments.

If the data that you want to send is too large for an email attachment, you can use one of the file sharing methods below:

- <https://wetransfer.com>
- <https://www.dropbox.com>
- <https://www.google.com/drive/>
- <https://www.hightail.com>
- <https://www.sendspace.com>

So instead of sending the large file as attachment, you would just include the download link in your email.

## Using GitHub and Git Large File Storage

You can also share example data by storing it in a GitHub hosted repository using [Git LFS](https://git-lfs.github.com/). In addition to sharing a snapshot of a file's state, this also lets you track changes to the files over time, control access to the shared data, easily sync it between multiple machines, and collaborate by allowing multiple users to write changes to the file set.

{% include markup/red %}
If this is confidential data, remember that by default, GitHub repositories are public and visible to everyone. To keep your data private, you must make it a private repo, and selectively grant access to the users you wish to see it.
{% include markup/end %}

To share files via Git LFS on GitHub:

- Install [Git LFS](https://git-lfs.github.com/) on your computer
- On GitHub, [Create a new repository](https://github.com/new)
  - Name it `example-<description>-yyyy-mm` or something similar; this is just example data, so you do not need a memorable name
- Clone the repository to your local machine
- Run `git lfs install` inside the cloned local repo
- Copy your example data files into the local repo
- Use `git lfs track` to make sure the files you have added are tracked by Git LFS instead of committed as regular files
- `git add` the files, `git commit`, and `git push`
