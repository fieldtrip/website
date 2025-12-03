---
title: Convert the EEG sedation dataset for sharing in BIDS
tags: [bids, eeg-sedation, madrid2019]
---

The following MATLAB script shows how the EEG data supporting [Brain connectivity during propofol sedation](https://doi.org/10.1371/journal.pcbi.1004669)
by Chennu et al. (2015) was converted to the Brain Imaging Data Structure (BIDS). The original data has been made available on the [Cambridge data repository](https://www.repository.cam.ac.uk/handle/1810/252736).

The BIDS background is explained on <http://bids.neuroimaging.io>, details on the specification can be found on <https://bids-specification.readthedocs.io/>.

This conversion makes use of the **[data2bids](/reference/data2bids)** function to convert the data and to write the associated metadata to the accompanying TSV and JSON files. The converted data in the BIDS organization is available from our [download server](https://download.fieldtriptoolbox.org/workshop/madrid2019/extra/complete_resting_data).

```` matlab
sourcedata = '/Volumes/Samsung T3/data/eeg-sedation/sourcedata';
bidsroot   = '/Volumes/Samsung T3/data/eeg-sedation/bids';

cd(sourcedata)

load datainfo

% For each dataset, there is an entry in the "datainfo" table with the following content
% 1) the name of the dataset
% 2) the level of sedation at which the dataset was acquired (1 = baseline, 2 = mild sedation, 3 = moderate sedation, 4 = recovery)
% 3) the concentration of propofol measured in blood plasma at that level (in microgram/litre)
% 4) the average reaction time measured in a speeded two-choice response task administered at that level (in milliseconds)
% 5) the number of correct responses in that task (out of a max of 40)

% use full descriptions rather than 1, 2, 3, 4
level = {
  'baseline'
  'mild sedation'
  'moderate sedation'
  'recovery'
  };

for i=1:length(datainfo)

  filename          = datainfo{i,1};
  sedation          = datainfo{i,2};
  concentration     = datainfo{i,3};
  reactiontime      = datainfo{i,4};
  correctresponses  = datainfo{i,5};

  cfg = [];
  cfg.dataset = fullfile(sourcedata, [filename '.set']);
  cfg.suffix = 'eeg';

  % copying would have also been an option, but the BrainVision format is more widely supported
  cfg.method = 'convert';

  % what to do with existing files, e.g., on re-runs of this script
  cfg.eeg.writesidecar            = 'replace';
  cfg.channels.writesidecar       = 'replace';
  cfg.events.writesidecar         = 'replace';
  cfg.dataset_description.writesidecar = 'replace';

  % this is used for the output file name
  cfg.bidsroot  = bidsroot;
  cfg.sub       = filename(1:2);
  cfg.task      = 'resting';
  cfg.run       = sedation; % this is a number

  % general information for the eeg.json file
  cfg.InstitutionName             = 'University of Cambridge';
  cfg.InstitutionalDepartmentName = 'Department of Clinical Neurosciences';
  cfg.InstitutionAddress          = 'Cambridge, United Kingdom';
  cfg.TaskDescription             = 'resting state, eyes closed';

  % these are EEG specific
  cfg.eeg.PowerLineFrequency      = 50;
  cfg.eeg.EEGReference            ='average';
  cfg.eeg.SoftwareFilters         = nan;

  % all 91 channels in the original recording are of the same type
  cfg.channels.type  = repmat({'eeg'}, 91, 1);
  cfg.channels.units = repmat({'uV'}, 91, 1);

  % these details should go in the scans.tsv file
  cfg.scans.sedationlevel    = level{sedation}; % convert number into string
  cfg.scans.concentration    = concentration;
  cfg.scans.reactiontime     = reactiontime;
  cfg.scans.correctresponses = correctresponses;

  % these details should go in the participants.tsv file
  cfg.participants.age = nan;
  cfg.participants.sex = nan;

  % these details should go in the dataset_description.json file
  cfg.dataset_description.Name                = 'Research data supporting ''Brain connectivity during propofol sedation''';
  cfg.dataset_description.Authors             = {'Chennu, S.', 'O'Connor, S.', 'Adapa, R.', 'Menon, D. K.', 'Bekinschtein, T. A.'};
  cfg.dataset_description.KeyWords            = {'Consciousness', 'Electroencephalography', 'Sedation', 'Propofol', 'Brain Connectivity'};
  cfg.dataset_description.ReferencesAndLinks  = {'http://dx.doi.org/10.1371/journal.pcbi.1004669', 'https://www.repository.cam.ac.uk/handle/1810/252736'};
  cfg.dataset_description.Abstract            = 'Accurately measuring the neural correlates of consciousness is a grand challenge for neuroscience. Despite theoretical advances, developing reliable brain measures to track the loss of reportable consciousness during sedation is hampered by significant individual variability in susceptibility to anaesthetics. We addressed this challenge using high-density electroencephalography to characterise changes in brain networks during propofol sedation. Assessments of spectral connectivity networks before, during and after sedation were combined with measurements of behavioural responsiveness and drug concentrations in blood. Strikingly, we found that participants who had weaker alpha band networks at baseline were more likely to become unresponsive during sedation, despite registering similar levels of drug in blood. In contrast, phase-amplitude coupling between slow and alpha oscillations correlated with drug concentrations in blood. Our findings highlight novel markers that prognosticate individual differences in susceptibility to propofol and track drug exposure. These advances could inform accurate drug titration and brain state monitoring during anaesthesia.';
  cfg.dataset_description.Sponsorship         = 'This work was supported by grants from the James S. McDonnell Foundation, the Wellcome Trust [WT093811MA to TAB], and the British Oxygen Professorship from the Royal College of Anaesthetists [to DKM]. The research was also supported by the NIHR Brain Injury Healthcare Technology Co-operative based at Cambridge University Hospitals NHS Foundation Trust and University of Cambridge. The views expressed are those of the authors and not necessarily those of the UK National Health Service, the NIHR or the UK Department of Health. The funders had no role in study design, data collection and analysis, decision to publish, or preparation of the manuscript.';
  cfg.dataset_description.License             = 'Attribution 2.0 UK: England & Wales, see http://creativecommons.org/licenses/by/2.0/uk/';
  cfg.dataset_description.BIDSVersion         = '1.2';

  data2bids(cfg);

end

````
