---
title: Why are the fileio functions stateless, does the fseek not make them very slow?
category: faq
tags: [memory, matlab]
redirect_from:
    - /faq/why_are_the_fileio_functions_stateless_does_the_fseek_not_make_them_very_slow/
---

# Why are the fileio functions stateless, does the fseek not make them very slow?

The **[ft_read_data](/reference/fileio/ft_read_data)** function in the fileio module is used to read the data into MATLAB from all supported EEG and MEG data formats. However, between multiple read operations the file is closed. This "stateless" handling of the read operations makes the interface simpler, i.e. in between read operations there is no state to be remembered (the state being the file pointer). It being stateless means that you don't have to keep track of the file-pointer and facilitates error handling. However, developers that started programming on the DOS operating system might know from experience that fseek operations are slow, which would impact reading performance.

This belief that fopen and fseek are slow certainly applied to old-fashioned file systems, such as FAT16, which was used in the MS-DOS era. The reason for that was that on every fseek the File Allocation Table (FAT) had to be read from disk to determine the physical block on disk to which the fseek should be made. Modern file systems don't seem to have this problem any more, and there are only small differences in stateless versus stateful read operations. The MATLAB code below demonstrates this.

    filename = 'test.bin';

    nchan    = 256;
    fsample  = 1024;
    duration = 600;      % seconds
    dtype    = 'int32';
    dsize    = 4;        % bytes

    dat = zeros(nchan, fsample*duration, dtype);
    fprintf('the total size of the data is %g MB\n', nchan*fsample*duration*dsize/(1024*1024));

    tic
    fid = fopen(filename, 'wb');
    fwrite(fid, dat, dtype);
    fclose(fid);
    fprintf('writing the data to file took %g seconds\n', toc);

    tic
    for i=1:duration
    fid = fopen(filename, 'rb');
    fseek(fid, (i-1)*nchan*fsample*dsize, 'bof');
    dat = fread(fid, [nchan fsample], dtype);
    fclose(fid);
    end
    fprintf('reading the data with    fopen and fseek took %g seconds\n', toc);

    tic
    fid = fopen(filename, 'rb');
    for i=1:duration
    dat = fread(fid, [nchan fsample], dtype);
    end
    fclose(fid);
    fprintf('reading the data without fopen and fseek took %g seconds\n', toc);

On my MacPro desktop computer with 2GB RAM, it results in

    the total size of the data is 600 MB
    writing the data to file took 17.2062 seconds
    reading the data with    fopen and fseek took 4.4741 seconds
    reading the data without fopen and fseek took 3.83829 seconds

Note that there are some potential caching effects that might influence these results. That is why I first do the stateless (i.e. with fopen and fseek for every block), and then the stateful read operations. If any caching effect is present, then the stateful read operation will have more benefit from it.

The example above shows that reading segments of one second with fseek and fopen is 10% slower than continuous reading. Depending on the file size and how well the file can be cached by the operating system, the difference will even be smaller. Note that my MacPro only has 2GB of memory, which leaves little space for caching this 600MB example file, because I have MATLAB, Safari, Mail, Word quite a few other small programs open, which means that the memory is more or less full.

You can try the code above on your own computer. Please post the results here, including your computer specs.
