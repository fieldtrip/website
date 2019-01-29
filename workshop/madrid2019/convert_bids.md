---
title: Convert to BIDS
tags: [bids, eeg-chennu]
---

```
% Research data supporting "Brain connectivity during propofol sedation"
% Chennu, S., O’ Connor, S., Adapa, R., Menon, D. K., & Bekinschtein, T. A. (2015).
%
% https://www.repository.cam.ac.uk/handle/1810/252736
% https://doi.org/10.1371/journal.pcbi.1004669
%
% This script converts the shared data to the BIDS organization.
%
% BIDS is documented on http://bids.neuroimaging.io
% The general details can be found on http://bids.neuroimaging.io/bids_spec.pdf
% The EEG specific details can be found on https://psyarxiv.com/63a4y
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

bidsroot = '/Volumes/128GB/data/Sedation-RestingState/bids';

load datainfo

% For each dataset, there is an entry in the "datainfo" table with the following meaning
% 1) the name of the dataset
% 2) the level of sedation at which the dataset was acquired (1 = baseline, 2 = mild sedation, 3 = moderate sedation, 4 = recovery)
% 3) the concentration of propofol measured in blood plasma at that level (in microgram/litre)
% 4) the average reaction times measured in a speeded two-choice response task administered at that level (in milliseconds)
% 5) the number of correct responses in that task (out of a max of 40)

subject = {
  '02'
  '03'
  '05'
  '06'
  '07'
  '08'
  '09'
  '10'
  '13'
  '14'
  '18'
  '20'
  '22'
  '23'
  '24'
  '25'
  '26'
  '27'
  '28'
  '29'
  };

level = {
  'baseline'
  'mild sedation'
  'moderate sedation'
  'recovery'
  };


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% PART 1
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

for isub=1:numel(subject)

  % find the 4 datasets for this subject
  sel = find(startsWith(datainfo(:,1), subject{isub}));
  num = numel(sel);

  dataset           = datainfo(sel,1);    % keep this as cell-array with strings
  sedation          = [datainfo{sel,2}];  % convert this to a numeric array
  concentration     = [datainfo{sel,3}];
  reactiontime      = [datainfo{sel,4}];
  correctresponses  = [datainfo{sel,5}];

  if num~=4
    error('inconsistent number of datasets for subject %s', subject{isub});
  end

  for i=1:4

    % construct the output file name
    sub       = sprintf('sub-%s', subject{isub});
    task      = 'task-rest';
    run       = sprintf('run-%d', i);
    filename  = [sub '_' task '_' run '_eeg.vhdr'];

    mkdir(fullfile(bidsroot, sub, 'eeg'));

    cfg = [];
    cfg.dataset                     = [dataset{i} '.set'];
    cfg.outputfile                  = fullfile(bidsroot, sub, 'eeg', filename);

    cfg.eeg.writesidecar            = 'replace';
    cfg.channels.writesidecar       = 'replace';
    cfg.events.writesidecar         = 'replace';

    cfg.InstitutionName             = 'University of Cambridge';
    cfg.InstitutionalDepartmentName = 'Department of Clinical Neurosciences';
    cfg.InstitutionAddress          = 'Cambridge, United Kingdom';

    % provide the long rescription of the task
    cfg.TaskName = 'resting state, eyes closed';

    % these are EEG specific
    cfg.eeg.PowerLineFrequency      = 50;
    cfg.eeg.EEGReference            ='average';

    cfg.channels.type = repmat({'eeg'}, 91, 1);
    cfg.channels.units = repmat({'uV'}, 91, 1);

    % further down I will also put these in the scans.tsv file
    cfg.SedationLevel = level{sedation(i)}; % pick it from a descriptive list
    cfg.Concentration = concentration(i);
    cfg.ReactionTime = reactiontime(i);
    cfg.CorrectResponses = correctresponses(i);

    data2bids(cfg)

  end % for 1 to 4

end


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% PART 2
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


% After the initial conversion of the EEG data files, I used
% https://github.com/robertoostenveld/bids-tools to make the additional metadata
% files and used the following code to update the scans.tsv files

for isub=1:numel(subject)

  % find the 4 datasets for this subject
  sel = find(startsWith(datainfo(:,1), subject{isub}));
  num = numel(sel);

  dataset           = datainfo(sel,1);    % keep this as cell-array with strings
  sedation          = [datainfo{sel,2}];  % convert this to a numeric array
  concentration     = [datainfo{sel,3}];
  reactiontime      = [datainfo{sel,4}];
  correctresponses  = [datainfo{sel,5}];

  sub       = sprintf('sub-%s', subject{isub});
  filename = fullfile(bidsroot, sub, [sub '_scans.tsv']);

  t = readtable(filename, 'FileType', 'text', 'Delimiter', '\t');

  % add the subject-specific information
  t.sedation       = level(sedation);
  t.concentration  = concentration(:);
  t.reactiontime  = reactiontime(:);
  t.correctresponses = correctresponses(:);

  writetable(t, filename, 'FileType', 'text', 'Delimiter', '\t');

end

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% PART 3
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% Then I used an editor to check and copy some general fields into the metadata
% sidecar files.
```
