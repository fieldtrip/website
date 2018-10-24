---
layout: default
tags: [faq, peer]
---

## How can I read and write files if I use other people's peers?

If you want to use peerslaves that have been started by another person, you have to realize that the corresponding MATLAB sessions in which your computations will be evaluated under the account of **that other person**. 

The first consequence is that the functions you wish to evaluate on the peerslave have to readable by the other person's account. That involves giving the other person read-only access to the relevant directories and files. If the job that you want to evaluate also entails reading data from disk, then those data files should be accessible as well.

If your job also entails writing data to disk, then those files will be written by the other person's account, therefore you should write them at a location where you can easily manage the results. The most convenient is to create a "public" directory in yuor homedi

    mkdir $HOME/public
    chmod 777 $HOME/public

The chmod 777 will allow other people (including the other peerslave) to write in the public directory. You should see the "public" directory as a temporary scratch space. Once your computations have finished, you can move the results to their final location elsewhere in your home directory.

You can test the writing using the following function

    function testwrite(filename)
    a = randn(100);
    save(filename, "a");

and evaluate this function using

    filename = {
    fullfile(getenv('HOME'), 'public', 'testfile1.mat')
    fullfile(getenv('HOME'), 'public', 'testfile2.mat')
    fullfile(getenv('HOME'), 'public', 'testfile3.mat')
    fullfile(getenv('HOME'), 'public', 'testfile4.mat')
    };
    
    peercellfun(@testwrite, filename);

See also the FAQ on [debugging problematic jobs](/faq/how_can_i_debug_a_problematic_distributed_job).

 
