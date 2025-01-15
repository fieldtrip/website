---
title: How can I deal with a discontinuous Neuralynx LFP recording?
parent: Specific data formats
grand_parent: Reading and preprocessing data
category: faq
tags: [neuralynx, corrupt, preprocessing]
redirect_from:
    - /faq/discontinuous_neuralynx/
---

# How can I deal with a discontinuous Neuralynx LFP recording?

It may occur that there are gaps in the continuous LFP recordings with the Neuralynx system, e.g., when the experimenter stops and re-starts the recording in the Cheetah acquisition software. The consequence is that the subsequent data samples in the recording do not form a continuous representation any more. This can be detected offline, as the time-stamps that are stored along with the data will show a gap or a jump at the moment of the break.

In case there are gaps in the recording, the default way of linking spike and event timestamps to LFP samples and vice versa will be incorrect. The default is to assume a linear relationship, i.e.

    timestamp = hdr.TimeStampPerSample * sample hdr.FirstTimeStamp

Due to the gaps in the LFP recording, the timestamps that relate to spikes and events cannot be mapped like this to the sample numbers. Furthermore, **[ft_read_header](/reference/fileio/ft_read_header)** computes the hdr.TimeStampPerSample without taking the gaps in the recording into account, so it will be incorrect.

The low-level `read_neuralynx_ncs` function detects the presence of gaps in the `.ncs` file and issues a warning. If you get this warning, the solution is to read in the raw timestamps for all individual samples rather than relying on the monotonous linear relationship. This is possible for a single channel, the procedure does not yet work when reading a whole dataset at once (i.e. a directory containing multiple `.ncs` files).

You can then construct a timestamp vector with all timestamps for all samples, interpolate missing samples, and set the values for missing samples (in the recording gap) to NaNs. This is demonstrated in the following code:

    % start with normal preprocessing of a single channel
    cfg         = [];
    cfg.dataset = 'CSC1.Ncs';
    data        = ft_preprocessing(cfg);

    Warning: discontinuous recording, predicted number of timestamps and observed number of timestamps differ by 1693523717.00
    Please consult https://www.fieldtriptoolbox.org/faq/discontinuous_neuralynx

    > In fileio/private/read_neuralynx_ncs at 94
    In ft_read_header at 1196
    In ft_preprocessing at 394

    >> disp(data)
             hdr: [1x1 struct]
           label: {'CSC1'}
            time: {[1x12902912 double]}
           trial: {[1x12902912 double]}
         fsample: 1893
      sampleinfo: [1 12902912]
             cfg: [1x1 struct]

    figure
    plot(data.time{1})
    xlabel('sample number')
    ylabel('time (s)')

This shows the default time axis of the data, which FieldTrip assumes to be continuous.

Now we continue with reading the actual timestamps and performing interpolation and gap-filling with NaNs across multiple channels. Your multiple channels can happen to have different start or end timestamps (which is another "feature" of the Cheetah acquisition software). This function then constructs a single timestamp-axis onto which all channels are represented.

```matlab
function [data_all] = ft_read_neuralynx_interp(fname)

% FT_READ_NEURALYNX_INTERP reads a cell-array of NCS files and performs interpolation
% and gap-filling of the timestamp axis to correct for potentially different offsets
% across channels, and potential gaps within the recordings. All samples are being
% read out.
%
% Input
%   The input FNAME is the list of CSC filenames, where all channels should have the
%   sample sampling frequency.
% Output
%   The output DATA_ALL is a raw data structure containing interpolated data and NaNs
%   at the gaps, based on all the available samples in a recording.
%
% Copyright (C) 2013, Martin Vinck, SILS, Center for Neuroscience, University of Amsterdam

% first check if these are indeed ncs files
ftype = zeros(length(fname), 1);
for i=1:length(fname)
  if ft_filetype(fname{i}, 'neuralynx_ncs')
    ftype(i) = 1;
  end
end
if ~all(ftype==1), error('some files do not correspond to ncs files'); end

% number of channels
nchans = length(fname);

% get the original headers
for i=1:nchans
  orig(i) = ft_read_header(fname{i});
end

% check if they all have the same sampling frequency, otherwise return error
for i=1:length(orig), SamplingFrequency(i) = orig(i).Fs; end
if any(SamplingFrequency~=SamplingFrequency(1))
  error('not all channels have the same sampling rate');
end

% get the minimum and maximum timestamp across all channels
for i = 1:nchans
  ts    = ft_read_data(fname{i}, 'timestamp', true);
  mn(i) = ts(1);
  mx(i) = ts(end);
  ts1   = ts(1);
  md(i) = mode(diff(double(ts-ts1)));

  % get the minimum and maximum across all channels
  if i>1 && mn(i)<min_all
    min_all = mn(i);
  else
    min_all = mn(i);
  end

  if i>1 && mx(i)>max_all
    max_all = mx(i);
  else
    max_all = mx(i);
  end
end

% issue some warning if channels don't start or end at the same time
startflag = 0; endflag = 0;
if any(mn~=mn(1)),
  warning('not all continuous channels start at the same time');
  startflag = 1;
end
if any(mx~=mx(1)),
  endflag = 1;
  warning('not all continuous channels end at the same time');
end
if any(md~=md(1)), warning('not all channels have same mode'); end

% take the mode of the modes and construct the interpolation axis
% the interpolation axis should be casted in doubles
mode_dts  = mode(md);
rng       = double(max_all-min_all); % this is small num, can be double
offset    = double(mn-min_all); % store the offset per channel
offsetmx  = double(max_all-mx);
tsinterp  = [0:mode_dts:rng]; % the timestamp interpolation axis

% loop over the channels if the channels have different timestamps
for i = 1:nchans
  cfg         = [];
  cfg.dataset = fname{i};
  data        = ft_preprocessing(cfg);
  ts          = ft_read_data(cfg.dataset, 'timestamp', true);

  % original timestamaps in doubles, with the minimum ts subtracted
  ts          = double(ts-ts(1)) + offset(i);

  % check if there are gaps to correct
  gaps     = find(diff(ts)>2*mode_dts); % skips at least a sample
  if isempty(gaps) && startflag==0 && endflag==0
    fprintf('there are no gaps and all channels start and end at same time, no interpolation performed\n');
  else
    % interpolate the data
    datinterp  = interp1(ts, data.trial{1}, tsinterp);

    % you can use NaN to replace the data in the gaps
    gaps = find(diff(ts)>2*mode_dts); % skips at least a sample
    for igap = 1:length(gaps)
      sel = tsinterp `< ts(gaps(igap)+1) & tsinterp >` ts(gaps(igap));
      datinterp(sel) = NaN;
    end

    % set data at the end and beginning to nans
    if startflag==1
      n = floor(offset(i)/mode_dts);
      if n>0
        datinterp(1:n) = NaN;
      end
    end

    % set data at the end and beginning to nans
    if endflag==1
      n = floor(offsetmx(i)/mode_dts);
      if n>0
        datinterp(end-n+1:end) = NaN;
      end
    end

    % update the FieldTrip data structure
    data.trial{1} = datinterp; clear datinterp
    data.time{1}  = [0:length(tsinterp)-1].*(1./data.hdr.Fs);
  end

  % append all the data
  if i==1
    data_all = data;
    clear data
  else
    data_all = ft_appenddata([], data_all, data);
    clear data
  end
end

% correct the header information and the sampling information
data_all.hdr.FirstTimeStamp     = min_all;
data_all.hdr.LastTimeStamp      = uint64(tsinterp(end)) + min_all;
data_all.hdr.TimeStampPerSample = mode_dts;
len = length(tsinterp);
data_all.hdr.nSamples           = len;
data_all.sampleinfo             = [1 len];
```
