---
title: I used ICA on my MEG data from before 2012 and now FieldTrip crashes, why is that?
category: faq
tags: [ica, data, crash]
---

# I used ICA on my MEG data from before 2012 and now FieldTrip crashes, why is that?

In recent FieldTrip versions we changed the behavior for ft_componentanalysis to remove the balancing-matrix from the gradiometer structure. Accordingly we also changed the behavior of other functions. If you have done an ICA before this change was introduced your data will most likely still contain the balancing-matrix, which will lead to crashes in certain functions pertaining to inferring the position of the channels. If you want to keep using your old data without redoing the ICA, a workaround for you is to to remove the balancing-matrix from your gradiometer structure:
data.grad = rmfield(data.grad, 'balance');

If you have done this, everything should work fine again.
