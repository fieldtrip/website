---
title: Implement trial selection option
---

{% include /shared/development/warning.md %}

Consistent implementation of option for trial selection in all relevant functions (such as plotting functions, functions that handle raw data, etc.).

## Objectives

- implement configuration option for doing trial selection in all relevant functions
- consistent implementation and documentation

## Step 1: get an overview of all functions for which this is relevant

- functions that use raw data
- functions that (could) use data with an 'rpt' dimension
- functions where this has already been implemented

---

### Functions that use raw data:

- preprocessing.m (when called with preprocessed data) -done-
- combineplanar.m -done-
- megplanar.m -done-
- megrealign.m -done-
- megrepair.m -done-
- scalpcurrentdensity.m -done-
- rejectvisual.m -done-
- redefinetrial.m -done-
- resampledata.m -done-
- timelockanalysis.m -done-
- freqanalysis.m -done-

### Functions that (could) use data with an 'rpt' dimension

- freqdescriptives.m -done-
- singleplotER.m -done-
- singleplotTFR.m -done-
- topoplotER.m -done-
- topoplotTFR.m -done-
- multiplotER.m -done-
- multiplotTFR.m -done-

### Functions where this has already been implemented

- componentanalysis.m -done-
- nonlinearassociation.m -done-

How it's currently implemented in these function

 % cfg.trials = 'all' or a selection like 1:10 (default = 'all')

    % set the defaults
    if ~isfield(cfg, 'trials'),   cfg.trials = 'all';  end

    % select trials of interest
    if ~strcmp(cfg.trials, 'all')
    fprintf('selecting %d trials\n', length(cfg.trials));
    data.trial  = data.trial(cfg.trials);
    data.time   = data.time(cfg.trials);
    end

## Step 2: develop and implement solution

- ensure consistency in solution
- relevant fields (trl) should be adjusted accordingly
- documentation

---

### Ensure consistency in solution

**For raw data input functions (implement before 'Ntrials=...' or equivalent):**

    % set the defaults
    if ~isfield(cfg, 'trials'),   cfg.trials = 'all';  end

    % select trials of interest
    if ~strcmp(cfg.trials, 'all')
      fprintf('selecting %d trials\n', length(cfg.trials));
      data.trial  = data.trial(cfg.trials);
      data.time   = data.time(cfg.trials);
    end

**For rpt data input functions:**

    % set the defaults
    if ~isfield(cfg, 'trials'),   cfg.trials = 'all';  end

- for topoplotE

  elseif strcmp(data.dimord, 'rpt_chan_time')
  tmpcfg = [];
  tmpcfg.trials = cfg.trials;
  data = timelockanalysis(tmpcfg, data);
  if ~isfield(cfg, 'xparam'), cfg.xparam='time'; end
  if ~isfield(cfg, 'yparam'), cfg.yparam=''; end
  if ~isfield(cfg, 'zparam'), cfg.zparam='avg'; end

- for singleplotER, multiplotER (varargin

  elseif strcmp(varargin{1}.dimord, 'rpt_chan_time')
  tmpcfg = [];
  tmpcfg.trials = cfg.trials;
  for i=1:(nargin-1)
  varargin{i} = timelockanalysis(tmpcfg, varargin{i});
  end
  if ~isfield(cfg, 'xparam'), cfg.xparam='time'; end
  if ~isfield(cfg, 'zparam'), cfg.zparam='avg'; end

- for topoplotER, singleplotTFR, multiplotTF

  elseif strcmp(data.dimord, 'rpt_chan_freq_time')
  tmpcfg = [];
  tmpcfg.trials = cfg.trials;
  tmpcfg.jackknife= 'no';
  data = freqdescriptives(tmpcfg, data);
  if ~isfield(cfg, 'xparam'), cfg.xparam='time'; end
  if ~isfield(cfg, 'yparam'), cfg.yparam='freq'; end
  if ~isfield(cfg, 'zparam'), cfg.zparam='powspctrm'; end

### Relevant fields (trl) should be adjusted accordingly

(note: when cfg.trials='all' this doesn't apply)

the code for adjusting the trl should look something like this:

finding the trl (see e.g., appenddata.m

    % adjust the trial definition (trl) in case of trial selection
    if ~strcmp(cfg.trials, 'all')
      % try to locate the trial definition (trl) in the nested configuration
      if isfield(data, 'cfg')
        trl = findcfg(data.cfg, 'trl');
      else
        trl = [];
      end
      if isempty(trl)
        % a trial definition is expected in each continuous data set
        warning('could not locate the trial definition ''trl'' in the data structure');
      else
        cfg.trl=trl(cfg.trials,:);
      end
    end

adjusting the tr

    % adjust the trial definition (trl)
    if ~isempty(trl) && ~strcmp(cfg.trials, 'all')
    cfg.trl=trl(cfg.trials,:);
    end

### Documentation

    %   cfg.trials       = 'all' or a selection given as a 1xN vector (default = 'all')

## Appendix: useful Linux commands

Find functions that use raw data:

    grep -n datatype.*raw *.m

Find functions that already have cfg.trials option:

    grep -n cfg.trials *.m
