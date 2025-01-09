---
title: How can I fix a corrupt CTF meg4 file?
parent: Specific data formats
category: faq
tags: [corrupt, ctf, raw]
redirect_from:
    - /faq/how_can_i_fix_a_corrupt_ctf_meg4_data_file/
---

# How can I fix a corrupt CTF meg4 file?

A corrupt .meg4 file can occur if your recording did not end properly. In this case, the size of your .meg4 file will not obey the demands of a regular .meg4 file. The CTF system records 'trials' of pre-specified length, usually 10s chunks of data. Note that this triallength has nothing to do with your experiment, it is just a convention! Any .meg4 file must contain a full number of trials, and the corresponding headerfile must contain these number of trials as well.

If your datafile is corrupt, maybe due to incomplete storing or because the acquisition machine showed an error, you can still repair this file and use it. You can use the following script written by Ivar Clemens to fix both the datafile and the header:

    function repair_ctf_size(dataset)
    %
    % REPAIR_CTF_SIZE recalculates the amount of trials in
    % a CTF MEG dataset and writes this value to the header
    % file (res4). If partial trials are present, this function will
    % remove them from the last meg4 file.
    %
    % Use as
    %   repair_ctf_size(dataset)
    %
    %   dataset     The dataset to repair
    %
    % Made by Ivar Clemens

    % convert CTF dataset into filenames
    [path, file, ext] = fileparts(dataset);
    headerfile = fullfile(dataset, [file '.res4']);
    datafile   = fullfile(dataset, [file '.meg4']);

    hdr = ft_read_header(headerfile, 'headerformat', 'ctf_old');

    % Find datafiles and determine their size
    dot = find(datafile == '.');
    prefix = datafile(1:dot(end));
    suffix = datafile(dot(end)+1:end);

    current_file = datafile;
    counter = 1;

    while(exist(current_file))
        datafiles(counter).name = current_file;
        fileinfo = dir(current_file);
        datafiles(counter).size = fileinfo.bytes;
        current_file = [prefix num2str(counter) '_' suffix];
        counter = counter + 1;
    end

    % Find and move empty datafiles (other than the first one)
    backup_location = [dataset '/backup'];
    if(~exist(backup_location, 'dir')), mkdir(backup_location); end;

    for counter = length(datafiles):-1:2
        if(datafiles(counter).size == 8)
            disp(['Removing datafile ' num2str(counter) ' because it does not contain data.']);
            movefile(datafiles(counter).name, backup_location);
            datafiles(counter) = [];
        end
    end

    % Calculate maximum number of trials based on
    %  amount of data recorded

    bytes_recorded = 0;

    for file = datafiles
        bytes_recorded = bytes_recorded + file.size - 8;
    end

    if(bytes_recorded == 0)
        error('Repair failed, no data recorded');
    end

    number_of_trials = bytes_recorded / 4 / hdr.nChans / hdr.nSamples;

    % Write correct number of trials to header
    fid = fopen(headerfile, 'r+', 'ieee-be');
    fseek(fid, 1312, 'bof');
    val = fread(fid, 1, 'int16');
    disp(['Recorded amount of trials (previous): ' num2str(val)]);
    fseek(fid, 1312, 'bof');
    fwrite(fid, number_of_trials, 'int16');
    disp(['Recorded amount of trials (current): ' num2str(number_of_trials)]);
    fclose(fid);

    % Remove partial trials (if present)
    if(number_of_trials ~= floor(number_of_trials))
        disp('Removing partially recorded trial.');

        number_of_trials = floor(number_of_trials);

        bytes_to_copy = number_of_trials * 4 * hdr.nChans * hdr.nSamples;

        for file = datafiles(1:end-1)
            bytes_to_copy = bytes_to_copy - file.size + 8;
        end

        bytes_to_copy = bytes_to_copy + 8;

        backup_name = [backup_location '/original.meg4'];
        if(~exist(backup_name)), movefile(datafiles(end).name, backup_name); end;

        infile = fopen(backup_name, 'r+');
        outfile = fopen(datafiles(end).name, 'w+');

        val = fread(infile, 8, 'uint8');
        fwrite(outfile, val, 'uint8');

        for i = 1:((bytes_to_copy - 8) / hdr.nChans / 4)
            val = fread(infile, hdr.nChans * 4, 'uchar');
            fwrite(outfile, val, 'uchar');
        end

        fclose(outfile);
        fclose(infile);
    end

{% include markup/yellow %}
This script will backup your data by appending the extension '.old'. Your newly obtained set of files might be truncated by a few bytes, so you might loose a little bit of data.
{% include markup/end %}
