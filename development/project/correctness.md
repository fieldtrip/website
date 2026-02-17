---
title: Check the correctness of the implementation of the algorithms
---

{% include /shared/development/warning.md %}

## Objectives

The functions should be tested regularly on correctness, therefore test scripts are needed. These scripts should cover

- the correctness of the implemented algorithms
- proper parsing of configuration options, including backward compatibility
- support for the normal data structures, also backward compatible

**Method A:** If possible, the scripts should check against an internal reference solution, i.e., the outcome of the algorithm on particular ideal data is known, therefore the correctness of the algorithm can be tested using simulated data.

**Method B:** If that is not possible or difficult, the scripts should check the consistency of one implementation with another implementation.

**Method C:** If that is also not possible, the result of the algorithm on a particular real-world dataset has to be interpreted as being correct, and that solution should be reused as reference solution (i.e. regression testing).

## Step 1

Create testscripts for:

- different headmodels (method B, hanvdgei: done )
- frequency analysis (method A, hanvdgei: work in progress)
- statistical analysis (method A, erimar & roboos: work in progress)
- use the scripts of the toolkit 2004 as test (method C)
- use the scripts of the toolkit 2005 as test (method C)
- use the scripts of the toolkit 2006 as test (method C)

Frequency Analysis progress:

- data of 10 Hz oscillations
  - Tested amplitudes of mtmfft, mtmconvol, mtmwelch, wltconvol and tfr;
  - tfr and wltconvol have different amplitudes then the other methods.
  - tfr and wltconvol averages have the same shape.
  - mtmwelch and mtmfft are the same when taking t_ftimwin the length of total timewindow (/hanvdgei/test_HD_002/freq002_a).
  - mtmwelch and mtmconvol give the same results when taking t_ftimwin the same lengths (/hanvdgei/test_HD_002/freq002_b).
  - tfr and wltconvol increase amplitude when cfg.waveletwidth or cfg.width (is same: expresse the width of the wavelets in nr of cycles) is increased from 5 to 7. (/hanvdgei/test_HD_002/freq002_c).
  - More cycles increase the amplitudes more. 6 cycles is closest (Maybe should be default?, /hanvdgei/test_HD_002/freq002_d).
  - tested taper smoothing for mtmfft with 10, 20, 30 and 40 Hz smoothing (/hanvdgei/test_HD_002/freq002_e).
- data of delta function
  - tested the freqanalysis methods on a delta function (/hanvdgei/test_HD_002/freq002_f).
  - tapersmoothing or extending timewindow doesn't make a difference.
  - visualizing wavelets see figure freq002_h.
- tjirp data
  - tested the methods for analyzing 'tjirp' data. Results shown in freq002_g (/hanvdgei/test_HD_002/freq002_g). When t_ftimwin is big (I took one second before) the read curve has peaks like wltconvol but the amplitudes are similar over time (they don't decrease like wltconvol).
  - tested mtmfft and mtmwelch for the same timewindow (cfg.t_ftimwin=10 for mtmwelch and mtmconvol). Amplitudes are now close to each other. (5.6039 e -8 (mtmfft) and 5.6051 e -8 (mtmwelch and mtmconvol)).

**freq002_a**
{% include image src="/assets/img/development/project/correctness/averagesfreq.png" %}
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_b**
{% include image src="/assets/img/development/project/correctness/freq002_b.png" %}
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_c**
{% include image src="/assets/img/development/project/correctness/freq002_c.png" %}
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_d**
{% include image src="/assets/img/development/project/correctness/freq002_d.png" %}
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_e**
{% include image src="/assets/img/development/project/correctness/tapsmo.png" %}

**freq002_f**
{% include image src="/assets/img/development/project/correctness/delta_freqs.png" %}

**freq002_g**
{% include image src="/assets/img/development/project/correctness/tjirptfr.png" %}

{% include image src="/assets/img/development/project/correctness/tjirp.png" %}
legend: blue = mtmfft; red = mtmconvol; cyaan = wltconvol; black = tfr; green = mtmwelch;

**freq002_h**
{% include image src="/assets/img/development/project/correctness/waveletstfrdelta.png" %}
