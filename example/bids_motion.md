---
title: Converting an example motion tracking dataset for sharing in BIDS
tags: [example, bids, sharing, motion]
---

# Converting an example motion tracking dataset for sharing in BIDS

{% include markup/danger %}
BIDS does currently not specify how to represent motion tracking data. This example - and the support that is implemented in the **[data2bids](/reference/data2bids)** function - should be considered as a preliminary proposal to help researchers with their existing data. This example may also serve to start a discussion on whether and how this data type should be added to the [BIDS specification](http://bids-specification.readthedocs.io/).  
{% include markup/end %}

There are numerous companies that manufacture research-oriented motion capture systems, such as Polhemus, Qualisys, NDI Polaris, X-Sens, etc. Furthermore, there are multiple technologies that are used for motion tracking, such as optical cameras (often with IR markers), electromagnetic tracking, or using inertial measurement units (IMUs). Optical and electromagnetic tracking systems result in measurements that can directly be interpreted as the position of the marker, which changes over time. Systems based on IMUs record signals from multiple accelerometers, gyroscopes, and (sometimes) magnetometers; the raw data from these systems requires further processing before it can be interpreted as position.

Motion tracking data - optionally in relation to the presentation of stimulus material and responses (e.g. button presses) that are given by the subject - can be stored in the BIDS representation in line with the specification of [behavioral data](https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/07-behavioral-experiments.html). We store the continuously motion tracking data in tab-separated-value format (TSV) in the `_motion.tsv` file. The events corresponding to stimuli and responses are stored in the `_events.tsv` file, similar as for other types of data in BIDS.

{% include markup/info %}
Besides storing the output of the motion capture system, the position of the (optical) markers on the body, the frame of reference (coordinate system) and the units should be documented in the sidecar JSON file. This can be added to the `cfg.motion` field to **[data2bids](/reference/data2bids)** function, e.g. as `cfg.motion.MarkerPositions` and `cfg.motion.MotionCoordinateSystem`.
{% include markup/end %}

## Qualisys

[Qualisys](https://www.qualisys.com) consists of a camera-based motion capture system. _It would be nice to have some more details here on the system and corresponding software, please contribute your knowledge via [GitHub](https://github.com/fieldtrip/website)._

### Example

The example that we present here was recorded using a [Qualisys](https://www.qualisys.com) camera-based motion capture system. The data was exported from the proprietary Qualisys `.qtm` format to the standard biomechanics `.c3d` format (see [this link](https://www.c3d.org) for the standard) and to the `.tsv` (tab-separated-values) format; data in both exported formats can directly be read and processed by FieldTrip.

The original data for the following example and the converted BIDS representation are available from our [FTP server](ftp://ftp.fieldtriptoolbox.org/pub/fieldtrip/example/bids_motion/).

```
cfg = [];

cfg.InstitutionName             = 'Radboud University';
cfg.InstitutionalDepartmentName = 'Donders Institute for Brain, Cognition and Behaviour';
cfg.InstitutionAddress          = 'Kapittelweg 29, 6525 EN, Nijmegen, The Netherlands';

% required for dataset_description.json
cfg.dataset_description.Name                = 'Motion capture example';
cfg.dataset_description.BIDSVersion         = 'unofficial extension';

% optional for dataset_description.json
cfg.dataset_description.License             = 'n/a';
cfg.dataset_description.Authors             = 'n/a';
cfg.dataset_description.Acknowledgements    = 'n/a';
cfg.dataset_description.Funding             = 'n/a';
cfg.dataset_description.ReferencesAndLinks  = 'n/a';
cfg.dataset_description.DatasetDOI          = 'n/a';

cfg.dataset = './original/self_test_30April2015_ADA.c3d';  % exported from Qualisys
% cfg.dataset = './original/self_test_30April2015_ADA.tsv'; % alternative export format

cfg.bidsroot = './bids';  % write to the present working directory
cfg.datatype = 'motion';
cfg.sub = 'S01';

% these are general fields
cfg.Manufacturer           = 'Qualisys';
cfg.ManufacturersModelName = '6+';

cfg.TaskDescription = 'The subject was making some hand movements for a short test recording';
cfg.task = 'handmovement';

data2bids(cfg);
```

## Optotrak

The Optotrak software, NDI First Principles, automatically exports a collection file, an experiment file, a tool definition file, and two raw data files. One of the raw data files contains the Optotrak data, which consists of the 3D data from the attached markers, and the other raw data file contains the ODAU data. The ODAU is a separate unit of the Optotrak system that digitizes additional analog inputs, e.g. from analog inputs to synchronize the data to an external system. Additionally, the software can convert the data and export it in the following formats: NDI 3D, NDI Odau, C3D, AII to ASCII, or NDI 6D. The export format can be specified in the software prior to starting the recording, or the data can be converted offline.

Experimental events, such as the beginning of a trial or the onset of a stimulus, are usually captured by sending a signal to one of the analog channels of the ODAU unit of the Optotrak system. This can be done by sending for example a step function or a pulse with a given amplitude and duration. This analog signal differs from experimental events in for example the data from Presentation software, as it is saved as a continuous analog stream of data (similar to the 3D marker data) instead of saving the onset and offset of a certain event in a separate events file.
