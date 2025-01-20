---
title: How can I anonymize or deidentify a CTF dataset?
parent: Various other questions
grand_parent: Frequently asked questions
category: faq
tags: [ctf, raw, anonymize, sharing]
redirect_from:
    - /faq/how_can_i_anonymize_a_ctf_dataset/
    - /faq/anonymization_ctf/
---

# How can I anonymize or deidentify a CTF dataset?

## Determining whether a dataset contains identifiers

If you have a dataset from a subject with a known name, you can search on the Linux or macOS command line whether that name occurs in any of the text or binary files.

    find SubjectXX.ds -type f -exec grep -l KnownSubjectName {} \;

## Using MATLAB

George O'Neill from the FIl shared the following code to scrub identifying information from a CTF dataset.

```
function go_anonymiseDs(input,output)
% Note// input and output filenames must include filepaths

% Add path to CTF functions
ft_hastoolbox('ctf', 1);

fprintf('Anonymising dataset ******.ds: ');

hdr = readCTFds(input);
data = getCTFdata(hdr,[],[],'fT');

hdr_anon = hdr;

% Remove identifiable information
% RES4
hdr_anon.res4.data_time=' ';
hdr_anon.res4.data_date=' ';
hdr_anon.res4.nf_run_name=' ';
hdr_anon.res4.nf_instruments=' ';
hdr_anon.res4.nf_collect_descriptor=' ';
hdr_anon.res4.nf_subject_id=' ';
hdr_anon.res4.nf_operator=' ';
hdr_anon.res4.nf_sensorFileName=' ';

% INFODS - loop through all fields which say patient/procedure/dataset
for ii = 1:length(hdr_anon.infods);
    if ~isempty(strfind(hdr.infods(ii).name,'PATIENT'))
        hdr_anon.infods(ii).data = '';
        % the sex field requires a number, just set to 2
        if ~isempty(strfind(hdr.infods(ii).name,'SEX'))
            hdr_anon.infods(ii).data = 2;
        end
    end
end
for ii = 1:length(hdr_anon.infods);
    if ~isempty(strfind(hdr.infods(ii).name,'PROCEDURE'))
        if hdr_anon.infods(ii).type == 10;
        hdr_anon.infods(ii).data = '';
        end
    end
end
for ii = 1:length(hdr_anon.infods);
    if ~isempty(strfind(hdr.infods(ii).name,'DATASET'))
        if hdr_anon.infods(ii).type == 10;
        hdr_anon.infods(ii).data = '';
        end
    end
end

% Remove dataset history too to make sure scan date is gone.
hdr_anon.hist = 'REDACTED';
hdr_anon.processing = 'REDACTED';

% Write out file with new anonymised header file
writeCTFds([output],hdr_anon,data,'fT');

fprintf('COMPLETE\n');
```


## Using CTF command-line tools on Linux

Using the CTF command line tool "newDs" with the "-anon" option. To keep all other aspects of the dataset as it is, you should specify some option

    newDs -anon -includeBadChannels -includeBadSegments -includeBad <dataset> <savePath>

Otherwise, bad channels, bad segments (in the continuous data) and bad trials (in segmented data) will be thrown away.

Make sure the savePath has an unambiguous name, so that you don't mix up your data.

Fields that are blanked out: purpose, site, institute, operator name, run title and description, collection description. The subject ID is set to Anon-1. The collection date and time are changed to 11/11/1911, 11:11.

{% include markup/red %}
The CTF newDs version 5.4.0-linux-20061212 (and possibly also other versions) is known to have a bug that causes the collection date and time not to be cleared. To remove these from your recording, you can use the remove_ctf_datetime script available [here](https://github.com/robertoostenveld/bids-tools).
{% include markup/end %}

For example

    newDs -anon -includeBadChannels -includeBadSegments -includeBad /home/common/matlab/fieldtrip/data/Subject01.ds        ./Subject01_anon.ds
    newDs -anon -includeBadChannels -includeBadSegments -includeBad /home/common/matlab/fieldtrip/data/Subject01.ds/hz.ds  ./Subject01_anon.ds/hz.ds
    newDs -anon -includeBadChannels -includeBadSegments -includeBad /home/common/matlab/fieldtrip/data/Subject01.ds/hz2.ds ./Subject01_anon.ds/hz2.ds

    rm ~/anon/Subject01.ds/defaults.de
    rm ~/anon/Subject01.ds/hz.ds/defaults.de
    rm ~/anon/Subject01.ds/hz2.ds/defaults.de

See also this frequently asked question on [how to anonymize an anatomical MRI](/faq/how_can_i_anonymize_an_anatomical_mri).

## Additional notes

It is advisable to also convert the head localizer datasets, which are inside the `SubjectXX.ds` and are named `hz.ds`, `hz2.ds`, etc.

After creating the anonymous dataset, you should delete the `defaults.de` ASCII file that might be present in the output dataset. That file contains some information that might be traced back to the original file location on disk, which may include your name or the name of the subject. You should also delete the `SubjectXX.acq` file, which contains a copy of some potentially identifying header information.
