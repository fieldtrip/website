---
title: Why should I set cfg.continuous = 'yes' when preprocessing CTF trial-based data?
tags: [faq, ctf, preprocessing]
---

# Why should I set cfg.continuous = 'yes' when preprocessing CTF trial-based data?

When storing a continuous CTF recording in disk, the CTF acquisition software automatically adds a trigger every 10 seconds alongside your custom triggers. To virtually stitch together these 10-second segments into one continuous recording , you must set cfg.continuous = 'yes' in **[ft_preprocessing](/reference/ft_preprocessing)**. That way you can perform trial-based MEG analysis using your custom triggers. This is also done in the [Preprocessing - Segmenting and reading trial-based EEG and MEG data](tutorial/preprocessing) tutorial.

