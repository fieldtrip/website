---
title: Test your MATLAB and FieldTrip installation in advance
tags: [cuttingeegx]
---

# Test your MATLAB and FieldTrip installation in advance

Prior to the hands-on sessions, you need to check the functionality of the computational setup you have on your end. This is needed to hit the ground running, and to avoid to spend time on debugging the MATLAB environment during the hands on session. We recommend to use a clean install of a [recent version](https://github.com/fieldtrip/fieldtrip/releases/tag/20241025) of the toolbox. Once you have set this up, please execute the code below, and check the output.

    fprintf('################################################################\n');
    fprintf('computer: %s\n', computer);
    ver('MATLAB');

    cd('fieldtrip-20241025')
    ft_defaults; % sets the required paths to use fieldtrip

    [ftver, ftpath] = ft_version;
    fprintf('FieldTrip path is at: %s\n', ftpath);
    fprintf('FieldTrip version is: %s\n', ftver);
    fprintf('ttest is:             %s\n', which('ttest'))
    fprintf('imdilate is:          %s\n', which('imdilate'));
    fprintf('dpss is:              %s\n', which('dpss'));
    fprintf('fminunc is:           %s\n', which('fminunc'));
    fprintf('ft_read_data is:      %s\n', which('ft_read_data'));
    fprintf('runica is:            %s\n', which('runica'));  % don't worry if this path is not be found yet
    fprintf('spm is:               %s\n', which('spm'));     % don't worry if this path is not be found yet
    fprintf('################################################################\n');

    cd .. % go back to the 'cuttingeegx' directory
