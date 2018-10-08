---
layout: default
---

`<note warning>`
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

This has been resolved with http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=1114 and test_bug1114.m

	
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


