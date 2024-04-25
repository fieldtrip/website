---
title: Converting an example audio dataset for sharing in BIDS
tags: [example, bids, sharing, audio]
---

# Converting an example audio dataset for sharing in BIDS

{% include markup/red %}
The [BIDS standard](https://bids.neuroimaging.io)  does currently not specify how to represent audio recordings. This example - and the support that is implemented in the **[data2bids](/reference/data2bids)** function - should be considered as a preliminary proposal to help researchers with their existing data. This example may also serve to start a discussion on whether and how this data type should be added to the [BIDS specification](http://bids-specification.readthedocs.io).  
{% include markup/end %}

In language studies, and especially speech production experiments, audio might be recorded on itself or along with other measurements, e.g., physiological signals from the brain. The audio can be used to monitor the subjects responses to a task, or can be off-line annotated/segmented in sentences, words or phonemes. Neither the audio recording (which can be considered as raw data), nor the annotations (which can be considered as derived data) are currently formally part of BIDS, although it is not so difficult to come up with a way that these can be represented in a BIDS-like fashion.

## Example

{% include markup/green %}
The example data is available from our [download server](https://download.fieldtriptoolbox.org/example/bids_audio/).
{% include markup/end %}

The example is a short recording of someone speaking into a microphone. In the example there is no specific task involved, but task details and events could in principle be coded/represented similar to how they are represented for other data types.

The example includes the audio recording under the “original” directory. It also has a copy of the script to do the conversion under “code”. The reorganized data is under the “bids” directory. According to [the documentation](https://bids-specification.readthedocs.io/en/stable/02-common-principles.html#source-vs-raw-vs-derived-data) the original data can be added to the BIDS dataset under the “sourcedata” directory and code can be added to the “code” directory. This way no information is lost and the conversion/reorganization is fully reproducible.

In general: if your original data is in a different format than the BIDS representation (e.g., DICOM instead of NIFTI), you probably want to keep a copy of the original data, e.g., on a data acquisition collection on the Donders Repository. If it is in the same format like here - since we are not converting the audio file but only copying and renaming it, you could simply delete the original files after conversion. In either case - your own analyses and the shared data would be based on the BIDS representation.

```
cfg = [];

cfg.InstitutionName             = 'Radboud University';
cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
cfg.InstitutionAddress          = 'Kapittelweg 29, 6525 EN, Nijmegen, The Netherlands';

% this is required for dataset_description.json
cfg.dataset_description.Name                = 'Audio example';
cfg.dataset_description.BIDSVersion         = 'unofficial extension';

% this is optional for dataset_description.json
cfg.dataset_description.License             = 'n/a';
cfg.dataset_description.Authors             = 'n/a';
cfg.dataset_description.Acknowledgements    = 'n/a';
cfg.dataset_description.Funding             = 'n/a';
cfg.dataset_description.ReferencesAndLinks  = 'n/a';
cfg.dataset_description.DatasetDOI          = 'n/a';

% provide some metadata about the task that was performed
cfg.TaskDescription = 'The subject was instructed to speak a random sentence into the microphone';

cfg.method    = 'copy'; % the audio should simply be copied, not converted
cfg.dataset   = './original/short_sentence.mp3';
cfg.bidsroot  = './bids';
cfg.datatype  = 'audio';
cfg.sub       = '01';
cfg.task      = 'speech';

data2bids(cfg);
```
