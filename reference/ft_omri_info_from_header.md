---
layout: default
---

##  FT_OMRI_INFO_FROM_HEADER

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_omri_info_from_header".

`<html>``<pre>`
    function S = ft_omri_info_from_header(hdr)
 
    Convenience function to retrieve most important MR information
    from a given header (H) as retrieved from a FieldTrip buffer.
    Will look at both NIFTI-1 and SiemensAP fields, if present, and
    give preference to SiemensAP info.
 
    Returns empty array if no information could be found.
`</pre>``</html>`

