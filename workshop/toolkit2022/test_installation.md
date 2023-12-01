---
title: Test your MATLAB and FieldTrip installation in advance
tags: [toolkit2022]
---

# Test your MATLAB and FieldTrip installation in advance

Prior to the hands-on sessions, we want you to provide us with some information with respect to the computational setup you have on your end. This is needed for us to anticipate (and ideally fix) any restrictions on your end. Also, it is needed to avoid a lot of time to be spent during the first session to get everybody up-and-running.

    fprintf('################################################################\n');
    fprintf('computer: %s\n', computer);
    ver('MATLAB');

    [ftver, ftpath] = ft_version;
    fprintf('FieldTrip path is at: %s\n', ftpath);
    fprintf('FieldTrip version is: %s\n', ftver);
    fprintf('ttest is:        %s\n', which('ttest'))
    fprintf('imdilate is:     %s\n', which('imdilate'));
    fprintf('dpss is:         %s\n', which('dpss'));
    fprintf('fminunc is:      %s\n', which('fminunc'));
    fprintf('ft_read_data is: %s\n', which('ft_read_data'));
    fprintf('runica is:       %s\n', which('runica'));  % should not be found yet, or the fieldtrip version
    fprintf('spm is:          %s\n', which('spm'));     % should not be found yet, or the fieldtrip version
    fprintf('################################################################\n');

If you get an error that says `Undefined function or variable 'ft_version'.` please add FieldTrip to the MATLAB path and try again. See [here](/faq/installation) for more information about adding FieldTrip to the MATLAB search path.
