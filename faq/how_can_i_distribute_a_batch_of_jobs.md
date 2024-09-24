---
title: How can I distribute a batch of jobs?
category: faq
tags: [distcomp]
---

# How can I distribute a batch of jobs?

Peer distributed computing allows to have multiple computers running the same analysis at the same time, efficiently speeding up your entire analysis. But how can I distribute my jobs?

Let's say we have an analysis script and we want to run that particular analysis for every subject, every condition (say we have 2), every event (again 2), and 5 different frequencies of interest. The analysis script should receive any of these parameters and then compute. For example, such an analysis script could look like this:

    myanalysis(input)

    % our study parameters
    myconds    = {'A','B'};
    myevents   = {'con','incon'};
    myfreqs    = [10:10:50]; % 10, 20, 30, 40, and 50 Hz

    % load the variable we need
    input = ['/home/mystorage/', input.subj,'_data.mat']; % the matfile which contains the variables
    variable = [myconds{input.cond}, '_', myevents{input.event}, '_' , num2str(myfreqs(input.freq))];
    load(input, variable);

    % perform analysis
    data = analyze(variable);

    % store data in a matfile with matching name
    output = ['/home/mystorage/', input.subj, '_newdata', variable, '_.mat'];
    save(output, data);
    clear

This script will simply perform 'analysis' on the parameters specified. Now we should effectively distribute this script and different parameters (we don't want multiple computers to do exactly the same of course). Here is an example of how such a job distribution (all subjects, 2 conditions, 2 events, 5 frequencies) script could look like. Basically in our example, we have 4 (2 conditions \* 2 events) different task-parameters repeated for 5 different frequencies:

     % our study parameters
     myconds    = {'A','B'};
     myevents   = {'con','incon'};
     myfreqs    = [10:10:50];

     % list subjects
     mysubjs = {'subject01', 'subject02', 'subject03'};
     nsub = 3;

     ctr = 0;
     for s = 1:nsub % all subjects

         for i = 1:20 % 2 conditions * 2 events * 5 frequencies

             % switch condition every 2 jobs
             if i >  2 && i `<=  4 || i >`  6 && i `<=  8 || i >` 10  && i <= 12 ...

| | i > 14 && i `<= 16 | | i >` 18 && i <= 20
| | ----------------- | | -----------------
cond = 2;
else
cond = 1;
end

             % switch event every job
             if floor(i/2) == i/2 % when i = equal number
                event = 2;
             else                 % when i = odd number
                event = 1;
             end

             % switch frequency every 4 jobs
             if i > 0 && i <= 4
                freq = 1;
             elseif i > 4 && i <= 8
                freq = 2;
             elseif i > 8 && i <= 12
                freq = 3;
             elseif i > 12 && i <= 16
                freq = 4;
             elseif i > 16 && i <= 20
                freq = 5;
             end

             % check for existence
             variable = [myconds{cond}, '_', myevents{event}, '_' , num2str(myfreqs(freq))];
             output = dir(['/home/mystorage/', mysubjs{s}, '_newdata', variable, '_.mat']);

             if isempty(output) % if the matfile does not yet exist, then add to the joblist
                ctr = ctr +1;
                input{ctr}.cond  = cond;
                input{ctr}.event = event;
                input{ctr}.freq  = freq;
                input{ctr}.subj  = mysubjs{s};
             end
             clear output;
         end
     end

     % distribute and assume one job requires 2 Gb of memory and 1 hour of CPU time
     % note: one should test with cellfun instead of peercellfun first
     peercellfun(@myanalysis, input, 'memreq', 2*(1024^3), 'timreq', 1*3600)

Our joblist (i.e. 'input') should now contain 60 jobs (20 different settings \* 3 subjects) which are distributed over the computer cluster. Having 'myanalysis' loading and saving the data is memory efficient. None of the output, namely, is sent to the workspace but instead stored on disk.
