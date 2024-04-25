---
title: Convert the EEG language dataset for sharing in BIDS
tags: [bids, eeg-language, cuttingeeg2021]
---

# Convert the EEG sedation dataset for sharing in BIDS

The following MATLAB script shows how the EEG data supporting [Identifying Object Categories from Event-Related EEG: Toward Decoding of Conceptual Representations](https://doi.org/10.1371/journal.pone.0014465) by Simanova et al. (2010) was converted to the Brain Imaging Data Structure (BIDS). The original data is available from the [archive of the MPI for Psycholinguistics](https://hdl.handle.net/1839/00-0000-0000-001B-860D-8). More details on the experiment and data can be found [here](/tutorial/eeg_language).

The BIDS background is explained on <http://bids.neuroimaging.io>, details on the specification can be found on <https://bids-specification.readthedocs.io/>.

This conversion makes use of the **[data2bids](/reference/data2bids)** function to convert the data and to write the associated metadata to the accompanying TSV and JSON files. The converted data in the BIDS organization is available from our [download server](https://download.fieldtriptoolbox.org/workshop/cuttingeeg2021/).

{% include markup/skyblue %}
The conversion here only includes the "pilot" subjects numbered 0, 1, 2, 3, 4, which were used for the (non-blind) optimization of the analysis pipeline in the original paper. The optimized pipeline was subsequently used (blind) on all other subjects. This ensures that the optimization of the processing does not bias the results of the analysis.
{% include markup/end %}

```` matlab
% this script converts the original data to a BIDS representation

originaldir = '/Volumes/SamsungT3/data/eeg-language/pilot';
rawdir = 'bids';

originalid = {
  'subj0'
  'subj1'
  'subj2'
  'subj3'
  'subj4'
  };

for i=1:length(originalid)
  % keep the original number as the identifier, but zero pad it to two digits (e.g., 01, 02, ...)
  number = sscanf(originalid{i}, 'subj%d');
  newid = sprintf('%02d', number);
  
  cfg = [];
  cfg.sub = newid;
  cfg.bidsroot = rawdir;
  cfg.datatype = 'eeg';
  cfg.dataset = fullfile(originaldir, [originalid{i} '.vhdr']);
  cfg.task = 'language';
  cfg.method = 'copy'; % it is already in the right format
  
  % this goes into dataset_description.json
  % see https://bids-specification.readthedocs.io/en/stable/03-modality-agnostic-files.html#dataset_descriptionjson
  cfg.dataset_description.Name                = 'Identifying Object Categories from Event-Related EEG: Toward Decoding of Conceptual Representations';
  cfg.dataset_description.BIDSVersion         = '1.6.0';
  cfg.dataset_description.Authors             = {'Irina Simanova', 'Marcel van Gerven', 'Robert Oostenveld', 'Peter Hagoort'};
  cfg.dataset_description.ReferencesAndLinks  = {'https://doi.org/10.1371/journal.pone.0014465', 'https://hdl.handle.net/1839/00-0000-0000-001B-860D-8'};
  
  hdr = ft_read_header(cfg.dataset);
  nchan = hdr.nChans;
  
  % this goes into eeg.json
  cfg.InstitutionName                 = 'Radboud University';
  cfg.InstitutionalDepartmentName     = 'Donders Institute for Brain, Cognition and Behaviour';
  cfg.InstitutionAddress              = 'Kapittelweg 29, 6525 EN, Nijmegen, The Netherlands';
  
  cfg.TaskDescription = 'The study investigated semantic processing of stimuli presented as pictures (black line drawings on white background), visually displayed text or as auditory presented words. Stimuli consisted of concepts from three semantic categories: two relevant categories (animals, tools) and a task category that varied across subjects, either clothing or vegetables.';
  
  cfg.eeg.Manufacturer = 'BrainProducts';
  cfg.eeg.ManufacturersModelName= 'BrainAmp with ActiCap';
  cfg.eeg.CapManufacturer = 'Easycap';
  cfg.eeg.CapManufacturersModelName= 'M10';
  cfg.eeg.PowerLineFrequency = 50;
  cfg.eeg.HardwareFilters.lowpass = 1000;
  cfg.eeg.HardwareFilters.highpass = 1/10;
  cfg.eeg.SoftwareFilters.lowpass = 200;
  cfg.eeg.SoftwareFilters.highpass = 1/10;
  cfg.eeg.EEGChannelCount = 62;
  cfg.eeg.EOGChannelCount = 2;
  
  % this goes in channels.tsv
  cfg.channels.name               = hdr.label;
  cfg.channels.type               = repmat({'EEG'}, nchan, 1);  % Type of channel
  cfg.channels.units              = repmat({'uV'}, nchan, 1);% Physical unit of the data values recorded by this channel in SI
  cfg.channels.sampling_frequency = repmat(hdr.Fs, nchan, 1); % Sampling rate of the channel in Hz.
  
  % add a human-interpretable event table
  event = ft_read_event(cfg.dataset);
  nevent = length(event);
  
  onset     = ([event.sample]' - 1)/hdr.Fs; % starting at t=0
  duration  = zeros(size(onset));
  sample    = [event.sample]'; % starting at sample 1
  type      = {event.type}';
  value     = {event.value}';
  
  % these are the required columns, i.e. the technical description of the events
  % see https://bids-specification.readthedocs.io/en/stable/04-modality-specific-files/05-task-events.html
  required = table(onset, sample, duration, type, value);
  
  % The first digit codes task/no task: 1 for the non-target semantic categories:
  % animals, tools and 2 for the target semantic category: clothing. The subjects’ task
  % was to press the button in response to clothing items, these targets were not
  % analyzed in the main study.
  %
  % The second digit codes the items, 1 to 4 for animals (cow, bear, lion, ape) and 5
  % to 8 for tools (ax, scissors, comb, pen). There were also 4 target items
  % (clothing).
  %
  % The third digit codes the stimulus modality: 1 for written words, 2 for pictures, 3
  % for spoken words.
  
  task      = cell(nevent,1);  % nontarget, target
  category  = cell(nevent,1);  % animals, tools
  item      = cell(nevent,1);  % cow, bear, lion, ape, ax, scissors, comb, pen
  modality  = cell(nevent,1);  % written, picture, spoken
  
  for i=1:nevent
    if strcmp(event(i).type, 'Stimulus')
      digit1 = str2double(event(i).value(2));
      digit2 = str2double(event(i).value(3));
      digit3 = str2double(event(i).value(4));
      
      if isnan(digit1) || isnan(digit1) || isnan(digit1)
        task{i}     = 'unknown';
        category{i} = 'unknown';
        item{i}     = 'unknown';
        modality{i} = 'unknown';
        continue
      end
      
      switch digit1
        case 1
          task{i} = 'notarget';
        case 2
          task{i} = 'target';
      end
      
      if strcmp(task{i}, 'target')
        % the interpretation of digit2 is not given for targets
        category{i} = 'target'; % clothes or vegetables
        item{i}     = 'target'; % we don't know the actual items

      else
        % the following only applies to nontargets
        switch digit2
          case {1, 2, 3, 4}
            category{i} = 'animals';
          case {5, 6, 7, 8}
            category{i} = 'tools';
        end

        switch digit2
          case 1
            item{i} = 'cow';
          case 2
            item{i} = 'bear';
          case 3
            item{i} = 'lion';
          case 4
            item{i} = 'ape';
          case 5
            item{i} = 'ax';
          case 6
            item{i} = 'scissors';
          case 7
            item{i} = 'comb';
          case 8
            item{i} = 'pen';
        end
        
      end % target or non-target

      switch digit3
        case 1
          modality{i} = 'written';
        case 2
          modality{i} = 'picture';
        case 3
          modality{i} = 'spoken';
      end
      
    elseif strcmp(event(i).type, 'Response')
      task{i}     = 'response';
      category{i} = 'response';
      item{i}     = 'response';
      modality{i} = 'response';
      
    else
      task{i}     = 'unknown';
      category{i} = 'unknown';
      item{i}     = 'unknown';
      modality{i} = 'unknown';
      
    end % stimulus or response
  end % for
  
  % these are the interpretation of the events
  interpretation = table(task, category, item, modality);
  
  % this is for events.tsv, note that it is with an "s"
  cfg.events = cat(2, required, interpretation);
  
  % this is for participants.tsv, note that it is with an "s"
  cfg.participants.age = nan;
  cfg.participants.gender = nan;
  cfg.participants.handedness = nan;
  
  % convert the dataset to BIDS
  data2bids(cfg);
  
end % for each subject
````
