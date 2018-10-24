---
layout: default
---

`<note warning>`
The purpose of this page is just to serve as todo or scratch pad for the development project and to list and share some ideas. 

After making changes to the code and/or documentation, this page should remain on the wiki as a reminder of what was done and how it was done. However, there is no guarantee that this page is updated in the end to reflect the final state of the project

So chances are that this page is considerably outdated and irrelevant. The notes here might not reflect the current state of the code, and you should **not use this as serious documentation**.
`</note>`

# Check the correctness of the implementation of the algorithms


## Objectives

The functions should be tested regularly on correctness, therefore test scripts are needed. These scripts should cover


*  the correctness of the implemented algorithms

*  proper parsing of configuration options, including backward compatibility

*  support for the normal data structures, also backward compatible


**Method A:** If possible, the scripts should check against an internal reference solution, i.e., the outcome of the algorithm on  particular ideal data is known, therefore the correctness of the algorithm can be tested using simulated data.

**Method B:** If that is not possible or difficult, the scripts should check the consistency of one implementation with another implementation. 

**Method C:** If that is also not possible, the result of the algorithm on a particular real-world dataset has to be interpreted as being correct, and that solution should be reused as reference solution (i.e. regression testing). 

## Step 1

Create testscripts fo

*  different headmodels (method B, hanvdgei: done )

*  frequency analysis (method A, hanvdgei: work in progress)

*  statistical analysis (method A, erimar & roboos: work in progress)

*  use the scripts of the toolkit 2004 as test (method C)

*  use the scripts of the toolkit 2005 as test (method C)

*  use the scripts of the toolkit 2006 as test (method C)



Frequency Analysis progres

      * data of 10 Hz oscillations;
      - Tested amplitudes of mtmfft, mtmconvol, mtmwelch, wltconvol and tfr;
      - tfr and wltconvol have different amplitudes then the other methods.
      - tfr and wltconvol averages have the same shape.
      - mtmwelch and mtmfft are the same when taking t_ftimwin the length of total timewindow (/hanvdgei/test_HD_002/freq002_a).
      - mtmwelch and mtmconvol give the same results when taking t_ftimwin the same lengthes (/hanvdgei/test_HD_002/freq002_b).
      - tfr and wltconvol increase amplitude when cfg.waveletwidth or cfg.width (is same: expresse the width of the wavelets in nr of cycles) is increased from 5 to 7. (/hanvdgei/test_HD_002/freq002_c). 
      - More cycles increase the amplitudes more. 6 cycles is closest (Maybe should be default?, /hanvdgei/test_HD_002/freq002_d).
      - tested taper smoothing for mtmfft with 10, 20, 30 and 40 Hz smoothing.(/hanvdgei/test_HD_002/freq002_e).

      * data of delta function;
      - tested the freqanalysis methods on a delta function.(/hanvdgei/test_HD_002/freq002_f).
      - tapersmoothing or extending timewindow doesn't make a difference.
      - visualizing wavelets see figure freq002_h.

      * tjirp data
      - tested the methods for analysing 'tjirp' data. Results shown in freq002_g. (/hanvdgei/test_HD_002/freq002_g). When t_ftimwin is big (I took one second before) the read curve has peaks like wltconvol but the amplitudes are similar over time (they don't decrease like wltconvol).
      - tested mtmfft and mtmwelch for the same timewindow (cfg.t_ftimwin=10 for mtmwelch and mtmconvol). Amplitudes are now close to eachother. (5.6039 e -8 (mtmfft) and 5.6051 e -8 (mtmwelch and mtmconvol)).



**freq002_a**
![image](/media/wiki/averagesfreq.png)
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_b**
![image](/media/wiki/freq002_b.png)
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_c**
![image](/media/wiki/freq002_c.png)
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_d**
![image](/media/wiki/freq002_d.png)
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_e**
![image](/media/wiki/tapsmo.png)

**freq002_f**
![image](/media/wiki/delta_freqs.png)

**freq002_g**
![image](/media/wiki/tjirptfr.png)

![image](/media/wiki/tjirp.png)
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_h**
![image](/media/wiki/waveletstfrdelta.png)



