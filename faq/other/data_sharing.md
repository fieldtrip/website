---
title: How can I share my MEG data?
category: faq
tags: [dataset, sharing]
redirect_from:
    - /faq/data_sharing/
---

Sharing data along with published results is a vital step towards better reproducibility of MEG/EEG research; furthermore, it supports the ongoing development and validation of new analysis methods such as those implemented in FieldTrip.

Funding agencies and journals are more frequently requiring that data is being shared along with publications.

## Where can I share my data?

You may have an institutional data repository or a national data repository. Alternatively, you can consider using a generic data repository such as [Zenodo](http://zenodo.org/), [Harvard DataVerse](https://thedata.harvard.edu), or [OpenFMRI](http://openfmri.org/), which all accept raw and minimally processed MEG or EEG data.

## How can others cite my data?

Most data repositories will create a persistent identifier linked to your dataset, such as a DOI or Handle. The dataset can be cited using the title, list of authors and this persistent identifier.

Even better than only sharing the data is to write a accompanying publication that describes the dataset in detail and upload the data with the publication. There are dedicated peer-reviewed journals for data publications, among others [Scientific Data (Nature)](http://www.nature.com/sdata/), [GigaScience](http://www.gigasciencejournal.com/). See [here](https://www.wiki.ed.ac.uk/display/datashare/Sources+of+dataset+peer+review) and [here](http://proj.badc.rl.ac.uk/preparde/blog/DataJournalsList) for some lists of data journals.

## What should I share?

There is not a simple answer to this, but ideally you would share:

- raw MEG data in the original vendor-specific format
- details on the task and a specification of the trigger codes
- defaced anatomical MRI with the coregistration information between the MRI and MEG
- if applicable the mapping of trigger codes on experimental conditions (stimuli and responses) and presentation log files
- demographics (age, sex)

Furthermore, you can consider sharing the following:

- minimally processed data
- specification of bad channels and bad segments
- cortical sheet source models (e.g., obtained from FreeSurfer)
- volume conduction models (e.g., the boundaries that define brain, skull and scalp)

## How should I deidentify the data?

Here it helps to clarify some often used terminology:

- The identity of the subject relates to [personally identifiable information](https://en.wikipedia.org/wiki/Personally_identifiable_information) that is stored in, or linked to the (biological, structural and behavioral) research data.
- Anonymous means that the data itself is not linked to the identity of the subject in any way.
- Pseudonomized means that the link between data and subject identity is provided as a (symbolic) identifier, where the key that links the pseudonym to actual identity is only known to the original researcher that acquired the data.
- Deidentified means that identifying features have been removed.

The MEG and corresponding imaging data should be pseudonomized (i.e. using subject codes instead of names) and deidentified (i.e. no personal identifiable information contained in the files or data). For both MEG and MRI that means that the subject name and exact date of birth should not be stored in the header of the MEG dataset. For the MRI, the identifiable features of the imaging data (i.e. the face) should be removed.

For CTF data, you can look in this [FAQ on anonymizing a CTF dataset](/faq/other/anonymization_ctf).

{% include markup/red %}
Note that "anonymous" or "pseudonomized" does not imply that it is impossible to link the data, just that the link is not directly provided with the data. e.g., am photo of a participant without its name or social security number is anonymous, but could nevertheless still be linked to the participants identity using Google reverse image search. That is why you should also consider to use deidentification methods.
{% include markup/end %}

See [this presentation](http://slideshare.net/RobertOostenveld/cuttingeeg-open-science-open-data-and-bids-for-eeg) with a conceptual explanation of how to deal with directly and indirectly identifying personal data.

## How should I organize the data?

There is not per se a perfect format for sharing the dataset, so you have to **be pragmatic** and where needed consider the peculiarities of your dataset. However, we strongly recommend that you follow the [Brain Imaging Data Structure](http://bids.neuroimaging.io/) (BIDS), for which an MRI oriented introduction has been published [here](http://www.nature.com/articles/sdata201644), the MEG version has been published [here](https://www.nature.com/articles/sdata2018110).

BIDS is an active project; the [specification](https://bids-specification.readthedocs.io/en/stable/) is still expanding through so-called BIDS extension proposals (BEPs). Also tools to create and work with BIDS datasets are under active development. FieldTrip includes the **[data2bids](/reference/data2bids)** function to help you organize your data in BIDS. Under the examples section you can find multiple example scripts:

{% include seealso category="example" tag1="bids" %}
