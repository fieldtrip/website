---
layout: default
tags: faq artifact filter noise preprocessing
---

## Why is there a residual 50Hz line-noise component after applying a DFT filter?

It is due to the non-stationarity of the line noise component in the data. Imagine a trial in which the 50Hz line noise increases in amplitude over time (e.g. trial #3 in the first figure). 

![image](/media/faq/linenoise.png@600)

If you fit a constant sine wave, its amplitude will be the mean, i.e. at the begin of the trial it will be larger than the actual amplitude and towards the end it will be smaller (second figure, using a 5 Hz example sine).

    % sampling rate
    fs = 1000;
    % time
    t = (1:10000)/fs;
    % frequency (Hz)
    f = 5;         
    % increasing amplitude
    amp = (1:10000)/fs;

    % 5 Hz sine with increasing amplitude
    s1 = amp.*sin(2*pi*f*t);
    plot(t, s1, 'b');

    % dftfilter: fit 5 Hz sine (with constant amplitude)
    avgamp = mean(amp);
    s2 = avgamp.*sin(2*pi*f*t);
    hold on; plot(t, s2, 'r');

![image](/media/faq/dftfilter1.png@500)

Then imagine subtracting the estimated 5 Hz component. At the begin you subtract too much, causing a negative (sign-flipped) 50Hz signal remaining in the data, and towards the end of the trial you are not subtracting enough, causing a positive (non sign-flipped) 5 Hz signal remaining (black line in third figure). Computed over the whole time interval, the 5 Hz amplitude is zero. However, for a short time interval at the begin, there is non-zero amplitude at 5 Hz. In the middle the amplitude dips, but towards the end of the trial the amplitude increases and is again non-zero. I.e. the time-varying amplitude is V-shaped: large at the edges, small in the middle. Similarly, if you were to look at the power, it would be U-shaped.

    % subtract the 5 Hz fit
    s3 = s1-s2;
    figure; plot(t, s3, 'k'); 

    % bandstopfilter: remove 4.9 to 5.1 Hz 
    s4 = ft_preproc_bandpstopfilter(s1, fs, [4.9 5.1], 2);
    hold on; plot(t, s4, 'm');  

![image](/media/faq/dftfilter2.png@500)

After spectral estimation this would lead to a consistent decrease in 50 Hz towards the middle of the trials. Note that it depends on the spectral estimation technique and the data padding during filtering whether and how the residual line noise will express itself. An alternative approach would be to use a bandstop filter instead of the dftfilter (for result see magenta line in third figure).
