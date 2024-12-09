---
title: Can I create an artificial CTF dataset using MATLAB?
category: example
tags: [dataformat, ctf, meg]
redirect_from:
    - /example/writing_simulated_data_to_a_ctf_dataset/
---

{% include markup/red %}
This is a very old and outdated example page, the referenced code does not exist anymore
{% include markup/end %}

# Can I create an artificial CTF dataset using MATLAB?

Q: Is there a way to create an artificial CTF dataset using MATLAB or one of the CTF utilities, or alternatively take a real dataset and replace just the channel data with my simulated data?

A: Yes, there is, see below.

## Part of function ft_write_data, case ctf_meg4

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % function ft_write_data(filename, dat, varargin)

    % FT_WRITE_DATA exports electrophysiological data to a file
    %
    % Use as ft_write_data(filename, dat, ...)
    %
    % The specified filename can already contain the filename extention,
    % but that is not required since it will be added automatically.
    %
    % Additional options should be specified in key-value pairs and can be
    % 'header' header structure, see READ_FCDC_HEADER
    % 'dataformat' string, see below
    % 'chanindx' 1xN array

    % ...

    % get the options
    dataformat = keyval('dataformat', varargin); if isempty(dataformat), dataformat = ft_filetype(filename); end
    chanindx = keyval('chanindx', varargin);
    hdr = keyval('header', varargin);

    % determine the data size (input is dataformat as it is returned by preprocessing, should be in ntrials x nchannels x nsamples)
    [nchans, nsamples] = size(dat.trial{1});

    switch dataformat
    case 'ctf_ds'
    id = find(filename == '.');
    filename = [filename '/' filename(1:id) 'meg4'];
    dataformat = ft_filetype(filename);

        case 'ctf_meg4'

            % reshaping the data size
            if isfield(dat, 'trial'),
               for i = 1:size(dat.trial,2)
                  data(i,:,:) = dat.trial{i};
               end
            end

            ntrldat   = size(data,1);
            nsmpdat   = size(data,3);
            nchandat  = size(data,2);
            ntrlorig  = hdr.nTrials;
            nchanorig = hdr.nChans;
            nsmporig = hdr.nSamples;

            % In case more trials/channels/samples are present in data compared to
            % header, error message. No fix.
            if ntrldat>ntrlorig
                error('More trials in dataset than header indicates');
            elseif nchandat>nchanorig
                error('More channels in dataset than header indicates');
            elseif nsmpdat>nsmporig
                error('More samples in dataset than header indicates');
            end

            % compare label to orig.label
            [count, index] = vec_match(dat.label,hdr.label);
            if find(index == 0)
               error('Channelnames do not match');
            end

            % If the dat.label contains the same channels (no more), or a
            % subset of existing channels of orig.label, the order of the channels
            % should be checked, and if the nr of channels in the new dataset is
            % smaller than in the header, the rest will be zeropadded.

            NZ_index = nonzeros(index);
            AV = check_asc(NZ_index);
            if length(NZ_index) == length(hdr.label) && AZ == 1
                return
            else
                NewLabel = cell(length(hdr.label),1);
                NewDat = zeros(ntrlorig, nchanorig, nsmpdat);
                for i = 1:length(NZ_index)
                   NewLabel(NZ_index(i),:) = dat.label(i);
                   NewDat(1:ntrldat,NZ_index(i),:) = data(:,i,:);
                end
                if count < length(hdr.label)
                    fprintf('Less channels in dataset than header indicates, data padded with zeros');
                end
            end

            dat.label = NewLabel;
            data = NewDat;

            % Since the size of dat may have changed, new values for trl,smp and
            % chan should be defined
            ntrldat   = size(data,1);
            nsmpdat   = size(data,3);
            nchandat  = size(data,2);

            % Opening the filename and writing the header
            fid = fopen(filename, 'wb', 'ieee-be');
            buf = [77 69 71 52 49 67 80 0]; % 'MEG41CP', null-terminated
            fwrite(fid, buf, 'char');

            if isempty(chanindx) && length(hdr.label)==nchandat
               chanindx = 1:nchandat;
            end

            % Check number of bytes needed to write the data
            nr_bytes = 8 + (ntrldat*nsmpdat*nchandat*4);
            if nr_bytes > 1e9
               error ('this code is not capable of writing datasets larger than 1Gb')
            end

            for i=1:ntrldat
               datorig = zeros(nchanorig,nsmporig); % size 'original' = header data
               if i<=ntrldat
                 datorig(chanindx,1:nsmpdat) = data(i,:,:); % Padding with zeros in case nsmpdat<nsmporig
                 datorig = transpose(sparse(diag(1./hdr.orig.gainV)) * datorig);
                 if any(datorig(:)>intmax('int32')) || any(datorig(:)<intmin('int32'))
                    warning('Data reaches limits int32, border values are clipped');
                    datorig(datorig>intmax('int32')) = intmax('int32');
                    datorig(datorig<intmin('int32')) = intmin('int32');
                 end
                 datorig = int32(datorig);
               else
                  datorig = int32(transpose(datorig));
               end
               fwrite(fid, datorig, 'int32');
            end

            fclose(fid);

        end % switch dataformat

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Function vec_match
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    function [count, index] = vec_match(vec1, vec2)

    count = 0;
    for i = 1:size(vec1,1)
    id = strmatch(vec1(i,:), vec2);
    if size(id,1) == 0
    continue
    else
    count = count + 1;
    index(i) = id;
    end
    end

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % Function check_asc
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    function AZ = check_asc(index)

    max = 0;
    for i = 1:length(index)
    if max < index(i)
    max = index(i);
    AZ = 1;
    else
    AZ = 0;
    break;
    end
    end
