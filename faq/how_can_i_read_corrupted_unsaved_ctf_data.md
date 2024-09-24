---
title: How can I read corrupted (unsaved) CTF data?
category: faq
tags: [raw, corrupt, preprocessing, ctf]
---

# How can I read corrupted (unsaved) CTF data?

When during recording a system failure occurs, the dataset may not be (properly) saved. This may have its problematic consequences with respect to the offline reading of the data. Because prior to recording the CTF system is set up to record 1000 10-second trials, and subsequently corrected during saving of the actually recorded trials, there is a mismatch between the headerinformation and the datafile.

You can check with the following command whether this is the case or not:

    read_ctf_meg4('/home/arjsto/MEG/subjectx.ds/subjectx.res4')

    ans =
               Fs: 1200
           nChans: 356
         nSamples: 12000
      nSamplesPre: 0
          timeVec: [1x12000 double]
          nTrials: 1000 <--- here
            gainV: [356x1 double]
           ioGain: [356x1 double]
            qGain: [356x1 double]
         sensGain: [356x1 double]
         sensType: [356x1 double]
            label: {356x1 cell}
          nameALL: [356x32 char]
             Chan: [1x356 struct]

See whether you can find the correct number of trials.

     ft_read_header('/home/arjsto/MEG/subjectx.ds/subjectx.res4')

     readCTFds: This dataset has multiple meg4 files.

     readCTFds: Data set error : size of meg4 file(s)
    1298676928 bytes (from dir command)
    1.708800e+10 bytes (from res4 file)

      ans =
             Fs: 1200
         nChans: 356
       nSamples: 12000
    nSamplesPre: 0
        nTrials: 75          <--- here
          label: {356x1 cell}
           grad: [1x1 struct]
           orig: [1x1 struct]

Now re-read the res4 file again and correct for the number of trials. Then read the raw data with the low-level function.

         hdr = read_ctf_meg4('/home/arjsto/MEG/subjectx.ds/subjectx.res4');
         hdr.nTrials = 75;

         data = read_ctf_meg4('/home/arjsto/MEG/subjectx/subjectx.meg4', hdr, 1, hdr.nTrials*12000);


If you want to do the same with high-level FieldTrip functions, invoke the above mentioned low-level functions by specifying the 'ctf_old' header- and dataformat. In your trialfunction:

    hdr   = ft_read_header(cfg.dataset,'headerformat','ctf_old','dataformat','ctf_old');
    hdr.nTrials = 75;
    event = ft_read_event(cfg.dataset,'eventformat','ctf_old','header',hdr);

Before preprocessing:

    cfg.dataformat = 'ctf_old';
    cfg.headerformat = 'ctf_old';

You may then append data using ft_appenddata. The grad structure may be lost with the procedure above. You may want to copy it from another dataset.
