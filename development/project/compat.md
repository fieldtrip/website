---
title: Ensure that the compat directories are NOT called by FieldTrip itself
---

{% include /shared/development/warning.md %}

This has been resolved with <http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1114> and test_bug1114.m

    a = dir('*.m');   % a = dir('ft_*.m')
    inlist = {a.name}
    inlist = {a.name}'
    [outlist, mat] = mydepfun(inlist)
    sel2 = find(~cellfun(@isempty, strfind(outlist, 'compat')))

    % these compat functions are called
    outlist(sel2)

    find(any(mat(:,sel2), 2))
    sel1 = find(any(mat(:,sel2), 2))

    % these are the calling fucntions
    inlist(sel1)

    % this shows the call details, i.e. which function calls which
    mat(sel1,sel2)
