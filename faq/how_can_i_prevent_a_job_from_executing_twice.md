---
layout: default
tags: [faq, peer]
---

## How can I prevent a job from executing twice?

Jobs that fail to finish in the expected amount of time (1), or jobs that fail to start properly (2) are by default automatically resubmitted by **[peercellfun](/reference/peercellfun)**. In general this is desired behavior, becaus

 1.  peers in generals come and go, and a colleague of yours might have switched of a peer that was busy on your job
 2.  an idle peerslave might accept your job, and only then find out that it cannot get a MATLAB license

However, if your jobs involve reading and especially writing to files, then having two jobs working at the same time on the same file might be problematic. 

To deal with the first case (resubmission because "job takes too long"), you can set the 'ResubmitTime' option to peercellfun to inf. Jobs sent to peerslaves that do not start will still be resubmitted. 

If you also want to prevent case two, you can modify your jobs such that they are guaranteed to run only once. Given that your job reads and writes files, it will probably look something like the following.

	
	function jobfunction(id)
	switch id
	case 1
	  infile  = 'subject01.mat'
	  outfile = 'subject01.mat'
	case 2
	  infile  = 'subject02.mat'
	  outfile = 'subject02.mat'
	case 3
	   ...
	otherwise
	  error('unknown subject ID');
	end
	
	load(infile);
	% do computation
	... 
	save(outfile);

Prior to reading the data, starting the computations and writing the results to disk, you can use a lockfile to prevent the job from being executed twice, e.g. change the job into

	
	function jobfunction(id)
	switch id
	case 1
	  infile  = 'subject01.mat'
	  outfile = 'subject01.mat'
	case 2
	  infile  = 'subject02.mat'
	  outfile = 'subject02.mat'
	case 3
	   ...
	otherwise
	  error('unknown subject ID');
	end
	
	lockfile = [outfile '.lock'];
	if ~exist(lockfile, 'file')
	  % create the lockfile
	  fclose(fopen(lockfile, 'wb'));
	else
	  warning('lockfile %s exists, not starting the job a second time', lockfile);
	  return
	end
	
	load(infile);
	% do computation
	... 
	save(outfile);

