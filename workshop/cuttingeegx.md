---
title: CuttingEEG X workshop at the Donders
tags: [cuttingeegx]
---

# CuttingEEG X workshop at the Donders

CuttingEEG is turning 10 years old! This milestone calls for a special edition, looking back at the EEG and MEG fields of the past 10 years and looking ahead at the next 10 years and beyond! Alongside the [CuttingEEG X](https://cuttingeegx.org) conference we are organizing a number of local workshops that will take place in the morning. This specific page describes the content and practicalities for the FieldTrip OPM workshop, but there is also the MNE-Python workshop (presented by Britta Westner and Tilman Stephani) and the Git/GitHub workshop (presented by Julia Chauvet, Jan-Mathijs and Robert).

- Who: Konstantinos Tsilimparis, Robert Oostenveld, Jan-Mathijs Schoffelen
- When: 31 October 2024
- Where: Nijmegen
- See <https://cuttingeegx.org/registration/#Nijmegen> for the timetable and more details

## The tutorial

We will run a tutorial on [preprocessing and coregistration of SQUID-based and OPM-based data](/workshop/cuttingeegx/squids_vs_opms). We will explore the differences in data analysis between the two MEG systems.

## Getting started with the hands-on session

In this workshop you will work on your own laptop computer. It will be an in-person event with no possibilities for hybrid or online attendance.

### Wifi access

If you don't have a eduroam account through your institution, it is possible to get a visitor access. Please let us know if you need a visitor access at the day of the workshop.

### MATLAB

For the hands-on sessions we assume that you have a computer with a relatively recent version of MATLAB installed (preferably < 5 years old, so >= 2019a/b).

### FieldTrip

To get the most recent copy of FieldTrip, you can follow this [link](https://github.com/fieldtrip/fieldtrip/releases/tag/20241025), download the zip-file, and unzip it at a convenient location on your laptop's hard drive. Alternatively, you can do the following in the MATLAB command window (less work and more robust):

```
% create a folder that will contain the code and the data, and change directory
mkdir('cuttingeegx');
cd('cuttingeegx');

% download and unzip fieldtrip into the newly created folder
url_fieldtrip = 'https://github.com/fieldtrip/fieldtrip/archive/refs/tags/20241025.zip';
unzip(url_fieldtrip);
```

Upon completion of this step, the folder structure should look something like this:

```bash
cuttingeegx/
└── fieldtrip-20241025
    ├── bin
    ├── compat
    ├── connectivity
    ├── contrib
    ├── external
    ├── fileio
    ├── forward
    ├── inverse
    ├── plotting
    ├── preproc
    ├── private
    ├── qsub
    ├── realtime
    ├── specest
    ├── src
    ├── statfun
    ├── template
    ├── test
    ├── trialfun
    └── utilities
```

{% include markup/red %}
Downloading and unzipping can take up to ~10 minutes, so please download and unzip FieldTrip prior to the workshop.
{% include markup/end %}

{% include markup/red %}
If you have downloaded and unzipped by hand on a Windows computer, it could be that there's an 'extra folder layer' in your directory structure and that it appears as `fieldtrip-20241025/fieldtrip-20241025`. We recommend that you remove this extra layer, i.e., move all content one level up.
{% include markup/end %}

### Test your installation in advance

To have a smooth experience - and to avoid having to spend precious debugging time during the hands-on sessions - we recommend that you [test your MATLAB and FieldTrip installation in advance](/workshop/cuttingeegx/test_installation).

## The data used in this tutorial

Next, we proceed with downloading the relevant data from the FieldTrip [download server](https://download.fieldtriptoolbox.org/workshop/cuttingeegx). The data are approximately 1.3 Gb. You can either ‘click around’ using your web browser and/or windows explorer to grab the data that are needed, or instead (less work and more robust) execute the MATLAB code below.

Please do ensure that your present working directory is the `cuttingeegx` which you created in the previous step. Open a new m-file in the MATLAB editor, copy-and-paste the following code and run the whole script. Note: to properly run the function `recursive_download`, do not paste this code into the command line window and do not run the code line-by-line:

```
% Create a folder (within cuttingeegx) to contain the data
mkdir('data');
cd('data');

% Download the SQUID and OPM dataset
url = 'https://download.fieldtriptoolbox.org/workshop/cuttingeegx';
recursive_download(url, pwd)


function recursive_download(webLocation, localFolder)

    % RECURSIVE_DOWNLOAD downloads a complete directory from a RESTful web service
    %
    % Use as
    %   recursive_download(webLocation, localFolder)
    %
    % See also WEBREAD, WEBSAVE, UNTAR, UNZIP, GUNZIP
    
    % Copyright (C) 2023, Konstantinos Tsilimparis
    %
    % This file is part of FieldTrip, see http://www.fieldtriptoolbox.org
    % for the documentation and details.
    %
    %    FieldTrip is free software: you can redistribute it and/or modify
    %    it under the terms of the GNU General Public License as published by
    %    the Free Software Foundation, either version 3 of the License, or
    %    (at your option) any later version.
    %
    %    FieldTrip is distributed in the hope that it will be useful,
    %    but WITHOUT ANY WARRANTY; without even the implied warranty of
    %    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    %    GNU General Public License for more details.
    %
    %    You should have received a copy of the GNU General Public License
    %    along with FieldTrip. If not, see <http://www.gnu.org/licenses/>.
    %
    % $Id$
    
    % Read the HTML content of the URL
    htmlContent = webread(webLocation);
    pattern = '<a href="([^"]+)">';
    matches = regexp(htmlContent, pattern, 'tokens');
    
    % Iterate over the matches
    for i = 2:numel(matches) % Ignore i=1, which is the parent directory link: '../'
      item = matches{i}{1};
    
      if endsWith(item, '/') % It is a folder
        % Create the necessary directories if they do not exist
        subfolder = fullfile(localFolder, item);
        if ~isfolder(subfolder)
          mkdir(subfolder);
        end
    
        % Recursively download the subfolder
        subWebLocation = strcat(webLocation, '/', item);
        recursive_download(subWebLocation, subfolder);
    
      else % It is a file
        % Create the necessary directories if they do not exist
        if ~isfolder(localFolder)
          mkdir(localFolder);
        end
    
        % Download the file
        fileUrl = strcat(webLocation, '/', item);
        localFilePath = fullfile(localFolder, item);
        websave(localFilePath, fileUrl);
      end
    end
end
```

At this stage, you should have a directory structure like this:

```bash
cuttingeegx/data/
└── sub-01
│   ├── anat
│   └── meg
│       ├── opm
│       └── squid
└── fieldtrip-20241025
    ├── bin
    ├── compat
    ├── connectivity
    ├── contrib
    ├── external
    ├── fileio
    ├── forward
    ├── inverse
    ├── plotting
    ├── preproc
    ├── private
    ├── qsub
    ├── realtime
    ├── specest
    ├── src
    ├── statfun
    ├── template
    ├── test
    ├── trialfun
    └── utilities
```

Whenever starting a fresh MATLAB session, to configure the right FieldTrip paths, execute the following:

```
% change into the 'cuttingeegx' folder and then do the following
restoredefaultpath
addpath('fieldtrip-20241025')
addpath(genpath('data'))
ft_defaults
```

The `restoredefaultpath` command sets the path to the MATLAB default, clearing any custom toolboxes that you may have but that we don't need today. The `ft_defaults` command ensures that all of FieldTrip's required subdirectories are added to the path.

{% include markup/red %}
Furthermore, please do NOT add FieldTrip with all subdirectories, subdirectories will be added automatically when needed, and only when needed (see this [FAQ](/faq/matlab/installation)).
{% include markup/end %}
