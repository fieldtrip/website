---
title: How can I anonymize data processed in FieldTrip?
parent: Various other questions
category: faq
tags: [sharing, anonymize]
redirect_from:
    - /faq/how_can_i_anonymize_fieldtrip_data/
---

# How can I anonymize data processed in FieldTrip?

If you share your MATLAB files with others, you should be aware that the [provenance](https://en.wikipedia.org/wiki/Provenance) information might contain identifying information about your subjects.

FieldTrip keeps track of the analyses in the `data.cfg.previous` field. This is something you can exploit using **[ft_analysispipeline](/reference/ft_analysispipeline)** to look up details of the processing that you might not be able to find in your analysis scripts any more.

However, the consequence might also be that original file name are present which might identify the subject. For example, after calling **[ft_prepare_headmodel](/reference/ft_prepare_headmodel)** the provenance of the input data is saved in the output `headmodel.cfg.previous`). You can use the **[ft_anonymizedata](/reference/ft_anonymizedata)** function to scrub unwanted information from the provenance.

Better is not to use the subject's name, date of birth or other identifying information as the filename if you acquire the data. If you - or the person from whom you received the data - nevertheless did use identifying information in the file name: the earlier you rename it, the better. Have a look here to learn [how to rename and anonymize a CTF dataset](/faq/how_can_i_anonymize_a_ctf_dataset), i.e. the `.ds` directory with all files in it.

Another concern for subject confidentiality is the anatomical MRI, which might include facial details. Please see this frequently asked question on [how to anonymize an anatomical MRI](/faq/how_can_i_anonymize_an_anatomical_mri).

Furthermore, depending on how strict you want to be, the date at which a subject is recorded or the data at which a subject's data was processed might also contain clues about identifying the subject.

{% include markup/skyblue %}
In the [Human Connectome Project](http://www.humanconnectome.org) (HCP) we decided that the date at which the subject was scanned (i.e. date of acquisition) should not be revealed, as it would mean that not only the participant him/herself, but potentially also family members, friends and other people that were informed about the subject participating would be able to identify the individual subject in the database. This is one of the reasons for releasing subjects in the HCP in larger batches and not continuously.

You may want to review the [elements](http://www.humanconnectome.org/data/data-use-terms/restricted-data-reference.html) of the HCP related to the gradual sensitivity of human data and the [data use terms](http://www.humanconnectome.org/data/data-use-terms/) for the open and restricted access elements of the HCP data.

Note that the important difference between e.g., the [Creative Commons](http://creativecommons.org/licenses/) licenses and the data use terms that were designed for the HCP is that the latter ones explicitly deal with identifying the data subjects.
{% include markup/end %}
