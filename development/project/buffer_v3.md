---
title: Clean up the buffer implementation
---

{% include /shared/development/warning.md %}

The public interface should consist of

- ft_read_header
- ft_read_event, should have option blocking=0/1, timeout=number
- ft_read_data, should have option blocking=0/1, timeout=number

The ft_read_data and event functions can make use of ft_poll_buffer (which is currently public, but eventually should be moved to fileio/private)

fileformat in ft_read_xxx should only be one type of fcdc_buffer, what is offline/online?

ft_read_header should be made faster by smarter handling of the additional data that does not change over subsequent calls (i.e the chunks). Use a persistent representation of the chunks (and hdr.orig, hdr.label, hdr.grad).

Stuff that is worth implementing in the next version of the buffer is

- Better error reporting, see proposed v2
- GET_HDR_WITHOUT_CHUNKS
