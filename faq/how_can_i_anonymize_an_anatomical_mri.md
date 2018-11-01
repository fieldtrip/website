---
title: How can I anonymize or deidentify an anatomical MRI?
layout: default
tags: [faq, mri, anonymize, sharing]
---

# How can I anonymize or deidentify an anatomical MRI?

{% include markup/info %}
This is something that in general you will want to do **after** the coregistration of the anatomical MRI with the MEG data (using **[ft_volumerealign](/reference/ft_volumerealign)**), as the coregistration often relies on facial landmarks.
{% include markup/end %}

You can deface an anatomical MRI using the FieldTrip **[ft_defacevolume](/reference/ft_defacevolume)** function. The default is to show a graphical user interface that allows you to scale, rotate and translate a box, such that it overlaps with the facial details that you want to be removed. Alternatively, you can use the cfg.method='spm' option to use an automated defacing procedure.

    mri = ft_read_mri('oostenveld_r.mri');

    cfg = [];
    mri_anon = ft_defacevolume(cfg, mri);

{% include image src="/assets/img/faq/defacevolume2.png" width="400" %}

You can use the standard MATLAB figure rotate button to look at the MRI from different angles.

{% include image src="/assets/img/faq/defacevolume1.png" width="400" %}

Once you are happy with the size and position of the box, you close the figure and the function returns the defaced anatomical MRI.

You can call **[ft_defacevolume](/reference/ft_defacevolume)** multiple times to sequentially mask out the identifying features. You might also want to remove the ears in two separate calls - one for each ear - as the ears are sometimes considered to be [potentially identifying](http://www.wired.com/2010/11/ears-biometric-identification/).

It is good practice to review the result of the defacing procedure using

    cfg = [];
    ft_sourceplot(cfg, mri_anon);

{% include image src="/assets/img/faq/defacevolume3.png" width="400" %}

Subsequently you can save it to a MATLAB file or to a NIFTI file usin

    ft_write_mri('subjectXX_anon.nii', mri_anon.anatomy, 'transform', mri_anon.transform, 'dataformat', 'nifti');

See also this frequently asked question on [how to anonimize a CTF MEG dataset](/how_can_i_anonymize_a_ctf_dataset).

{% include markup/danger %}
If you share your MATLAB files with others, note that there might also be identifying information in the [provenance](https://en.wikipedia.org/wiki/Provenance) information in the "cfg" field that is included in the FieldTrip data structure.

In principle FieldTrip keeps full track of all analyses that you do. The consequence might be that the original file name (identifying the subject) is included in the provenance information. You can use the **[ft_anonimizedata](/reference/ft_anonimizedata)** function to scrub the provenance from unwanted information.

Better is not to use the subject's name, date of birth or other identifying information as the filename if you acquire the data. If you - or the person from whom you received the data - nevertheless did use identifying information in the file name: the earlier you rename it, the better!   
{% include markup/end %}
