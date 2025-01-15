---
title: Fourier analysis of neuronal oscillations and synchronization
parent: Spectral analysis
grand_parent: Examples
category: example
tags: [freq]
redirect_from:
    - /tutorial/fourier/
    - /example/fourier/
---

# Fourier analysis of neuronal oscillations and synchronization

## Background

EEG and MEG measure brain activity as a so called time series, i.e. they measure electric voltage or
magnetic field strength as a function of time. In those time series, there are often clearly visible
oscillations like the alpha oscillations over occipital cortex or the beta oscillations over
sensorimotor cortex during rest. However, in the time series, the information about those
oscillations is distributed over many samples: We observe an oscillation through the fact that there
are peaks in the time series that recur at regular intervals. Since the information about the
oscillations is distributed over many samples, it cannot be used immediately. We can e.g., not tell
directly the main frequency of such an oscillation. In order to concentrate all information about an
oscillation, we use spectral analysis. Any signal that is measured as a function of time can also be
expressed as a function of frequency. The transformation from the so-called time-domain into the
frequency-domain is the Fourier transform. This part of the course tries to give an
easy-to-understand, but nevertheless correct, explanation of what the Fourier transform does and how
we can use its outputs to compute power-spectra and cross-spectral densities.

## Procedure

In this tutorial the following steps will be demonstrate

- Spectral analysis using the **Fast Fourier Transform** (FFT).
- Computation of the **power spectrum** from the Fourier transformed data.
- Computation of the **coherence spectrum** from the Fourier transformed data of two signals.

## The concept of spectral analysis using the Fourier Transform

To get to the concept of spectral analysis, we first construct a sine-wave and a cosine wave of
known frequency. (While in this course, we will use sine waves for reasons of simplicity and
clarity, please bear in mind that biological signals are never sine waves but extend over a
frequency range. This is important for the appropriate way of analyzing them.) We then calculate the
Fourier transform of those signals using the Fast Fourier Transform (FFT) function of MATLAB. The
Fourier transform decomposes the time series signals into the cosine and sine components at all
frequencies. The result of the Fourier transform is complex, containing, for each frequency, the
cosine component of the signal as the real component and the sine component of the signal as the
imaginary component. It is straightforward to compute those components by hand. For any given
frequency, one can therefore think of a vector, representing the signal component at that frequency.
This vector has an amplitude and a phase (phase relative to the begin of the time series). The
amplitude is of interest when we later compute the power spectrum of a signal and the phase is
particularly important when we later compute the coherence spectrum between two signals.

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % The Fourier Transform
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    clear all
    close all

    % get a sine and cosine wave of equal frequency and plot them
    frq = 20; % Hz
    len = 1; % seconds
    smpfrq = 1000; % Hz
    phs = 0;
    ind = ((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+(phs.*2.*pi);
    sinwav = sin(ind);
    coswav = cos(ind);
    figure;
    plot(sinwav);
    hold on;
    plot(coswav,'r');

    % get the FFT of the waves and plot the real and imaginary components
    fftsin = fft(sinwav);
    figure;
    subplot(2,1,1);
    plot(real(fftsin));
    subplot(2,1,2);
    plot(imag(fftsin),'r');

    fftcos = fft(coswav);
    figure;
    subplot(2,1,1);
    plot(real(fftcos));
    subplot(2,1,2);
    plot(imag(fftcos),'r');

{% include image src="/assets/img/example/fourier/figure1.png" %}

_Figure: The Fourier transform of the sine wave. The result of the Fourier transform is complex, containing, for each frequency, the cosine component of the signal as the real component (upper panel) and the sine component of the signal as the imaginary component (lower panel)._

{% include image src="/assets/img/example/fourier/figure2.png" %}

_Figure: The Fourier transform of the cosine wave. The result of the Fourier transform is complex, containing, for each frequency, the cosine component of the signal as the real component (upper panel) and the sine component of the signal as the imaginary component (lower panel)._

    % calculate the FFT results at the signal frequency "by hand" and plot the result as a vector
    figure;
    subplot(2,1,1);
    sigsinwav = sinwav;
    plot(sigsinwav .* coswav)
    subplot(2,1,2);
    plot(sigsinwav .* sinwav)
    coscmpsin = sum(sigsinwav .* coswav)
    sincmpsin = sum(sigsinwav .* sinwav)
    figure;
    plot([0,coscmpsin],[0,sincmpsin]);
    set(gca,'xlim',[-600 600],'ylim',[-600 600])

    figure;
    subplot(2,1,1);
    plot(coswav .* coswav)
    subplot(2,1,2);
    plot(coswav .* sinwav)
    coscmpcos = sum(coswav .* coswav)
    sincmpcos = sum(coswav .* sinwav)
    figure;
    plot([0,coscmpcos],[0,sincmpcos]);
    set(gca,'xlim',[-600 600],'ylim',[-600 600])

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % generate a cosine wave that is shifted by 45 degrees
    frq = 20; % Hz
    len = 1; % seconds
    smpfrq = 1000; % Hz
    phs = 45 ./360; % the relative phase advance in fraction of radiants
    ind = ((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+(phs.*2.*pi);
    wav = sin(ind);
    figure;
    plot(wav);

{% include image src="/assets/img/example/fourier/figure3.png" %}

_Figure: A 20 Hz cosine wave shifted 45 degrees._

    % get the FFT of the wave
    fftwav = fft(wav);
    figure;
    subplot(2,1,1);
    plot(real(fftwav));
    subplot(2,1,2);
    plot(imag(fftwav),'r');

{% include image src="/assets/img/example/fourier/figure4.png" %}

_Figure: The FFT of a 20 Hz cosine wave shifted 45 degrees._

    % calculate the FFT results at the signal frequency "by hand" and plot the result as a vector
    figure;
    subplot(2,1,1);
    plot(wav .* coswav)
    subplot(2,1,2);
    plot(wav .* sinwav)
    coscmpwav = sum(wav .* coswav)
    sincmpwav = sum(wav .* sinwav)
    figure;
    plot([0,coscmpwav],[0,sincmpwav]);
    set(gca,'xlim',[-600 600],'ylim',[-600 600])

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % generate a wave of a different frequency
    frq = 10; % Hz
    len = 1; % seconds
    smpfrq = 1000; % Hz
    phs = 0; % the relative phase advance in fraction of radiants
    ind = ((0 : (len.*smpfrq -1))./(smpfrq).*(frq.*2.*pi))+(phs.*2.*pi);
    wav = sin(ind);
    figure;
    plot(wav);

    % get the FFT of the wave
    fftwav = fft(wav);
    figure;
    subplot(2,1,1);
    plot(real(fftwav));
    subplot(2,1,2);
    plot(imag(fftwav),'r');

    % calculate the FFT result OF THE SIGNAL FREQUENCY "by hand"
    figure;
    subplot(2,1,1);
    plot(wav .* coswav)
    subplot(2,1,2);
    plot(wav .* sinwav)

    coscmpwav = sum(wav .* coswav)
    sincmpwav = sum(wav .* sinwav)

## The power spectrum

When we have only one signal, we might want to know the amplitude of the different
frequency components. This can be directly obtained through the power spectrum, the
squared absolute of the Fourier transform (plus appropriate normalisation that will not be
covered in detail here). The power spectrum no longer contains the phase
information. Thus, the power spectra of our sine and cosine waves are identical!

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % The Power spectrum
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % calculate the power spectrum
    clear all
    close all

    % get a sine and cosine wave of equal frequency and plot them
    frq = 10; % Hz
    len = 1; % seconds
    smpfrq = 1000; % Hz
    phs = 0;
    ind = ((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+(phs.*2.*pi);
    sinwav = sin(ind);
    coswav = cos(ind);
    figure('name','sin&cos');
    plot(sinwav);
    hold on;
    plot(coswav,'r');

{% include image src="/assets/img/example/fourier/figure5.png" %}

_Figure: A sine (blue) and cosine wave (red) of equal frequency (10 Hz)._

    % get the FFT of the waves
    fftsin = fft(sinwav);
    figure('name','fft sin');
    subplot(2,1,1);
    plot(real(fftsin));
    subplot(2,1,2);
    plot(imag(fftsin),'r');

    fftcos = fft(coswav);
    figure('name','fft cos');
    subplot(2,1,1);
    plot(real(fftcos));
    subplot(2,1,2);
    plot(imag(fftcos),'r');

    numsmp = length(sinwav);
    psdsin = 2 .* abs(fftsin) .^ 2 ./ (numsmp .^2);
    figure('name','power sin');
    plot(psdsin);
    psdcos = 2 .* abs(fftcos) .^ 2 ./ (numsmp .^2);
    figure('name','power cos');
    plot(psdcos);

{% include image src="/assets/img/example/fourier/figure6.png" %}

_Figure: The power spectrum of a 10 Hz sine wave. The power spectrum of the 10 Hz cosine wave is identical._

## The coherence spectrum

When we have two signals, we might want to know whether they are related. One way of addressing this
is to quantify whether there is a consistent phase relation between two signals. We have learned
that the Fourier transform gives, for each frequency component, the amplitude and the phase of the
signal. Thus, in order to determine whether there is a consistent phase relationship between two
signal, we could e.g., analyze the difference in phases between two signals.

If two signals are related, there should be a consistent phase difference between them – or in other
words, the phase difference should not be random. It turns out that the phase difference between two
signals is easily obtained if one has the Fourier transform of the two signals. The product of the
Fourier transform of one signal with the conjugate of the Fourier Transform of the signal gives the
Cross-Spectral density (CSD). We will not go into the detail what the conjugate actually is and why
this multiplication gives this particular results. Let's simply accept this for now as a fact.

The CSD is complex and a function of frequency, just like the Fourier Transforms. The amplitude of
the CSD is the product of the amplitudes of the Fourier Transforms of the two signals. The
interesting component is the phase of the CSD: It corresponds to the difference in the phase of the
two Fourier transforms of the two signals. Just like the Fourier Transform itself, we can think of
the CSD at one frequency as a vector. If we have multiple measurements from two signals and the CSD
for each of those measurements, then we can analyze the distribution of those vectors. If there is
some consistency in the phase difference, those vectors should not be pointing in random directions,
but they should be bundled around one main direction.

In order to quantify how much those vectors are bundled, one simply sums up all the vectors. Vector
summation works by simply appending one vector to the end of the other. If the CSD vectors from
multiple measurements point into random directions, the sum of those vectors will approximate a
vector of no length. If however, the CSD vectors all point into one and the same direction, then
they will optimally add up and form the longest possible sum vector. "Coherence" as a measure of
signal relatedness uses this fact. It is a ratio of two sums: The numerator is the sum of the CSDs
of multiple measurements. The denominator is the sum of the products of the power spectra. This
denominator is necessary in order to make direct comparisons possible between signal pairs of very
different amplitudes. Coherence is then normalized between 0 – random phase difference – and 1 –
constant phase difference.

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % The Coherence spectrum
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % get many repetitions of two signals with random phase difference
    clear all
    close all

    frq = 10; % Hz
    len = 1; % seconds
    smpfrq = 100; % Hz
    numrpt = 1000;
    ranphs = rand(2.*numrpt,2);
    phsdif = 45 ./ 360;
    noifac = 1./50;
    for rptlop = 1:numrpt
      wav(:,rptlop,1) = sin(((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+(ranphs(rptlop,1).*2.*pi)) + ...
        randn(1,len.*smpfrq).*noifac;
      wav(:,rptlop,2) = sin(((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+((ranphs(rptlop,2)+phsdif).*2.*pi)) + ...
        randn(1,len.*smpfrq).*noifac;
    end

    % get the FFT of the waves
    for rptlop = 1:numrpt
      fftwav(:,rptlop,1) = fft(wav(:,rptlop,1));
      fftwav(:,rptlop,2) = fft(wav(:,rptlop,2));
    end

    % calculate the power-spectral densities (psd) and the cross-spectral
    % densities (csd) and sum them over repetitions
    numsmp = length(wav);
    psd = 2.*abs(fftwav).^2./(numsmp.^2);
    csd = 2.*(fftwav(:,:,1).*conj(fftwav(:,:,2)))./(numsmp.^2);
    sumpsd = squeeze(sum(psd,2));
    sumcsd = squeeze(sum(csd,2));

    % calculate coherence
    coh = abs(sumcsd ./ sqrt(sumpsd(:,1) .* sumpsd(:,2)));

    figure;
    plot(squeeze(wav(:,:,1)));
    figure;
    plot(squeeze(wav(:,:,2)));
    figure;
    plot(coh);

{% include image src="/assets/img/example/fourier/figure7.png" %}

_Figure: Coherence spectrum for two 10 Hz signals with a random phase difference._

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % get many repetitions of two signals with somewhat consistent phase difference
    clear all
    close all

    frq = 10; % Hz
    len = 1; % seconds
    smpfrq = 100; % Hz
    numrpt = 1000;
    phsspreadfac = 0.5;
    circulran = mod(randn(2.*numrpt,2).*phsspreadfac + pi, 2.* pi) - pi;
    ranphs = circulran ./ (2 .* pi);
    phsdif = 45 ./ 360;
    noifac = 1./50;
    for rptlop = 1:numrpt
      wav(:,rptlop,1) = sin(((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+(ranphs(rptlop,1).*2.*pi)) + ...
        randn(1,len.*smpfrq).*noifac;
      wav(:,rptlop,2) = sin(((0:(len.*smpfrq-1))./(smpfrq).*(frq.*2.*pi))+((ranphs(rptlop,2)+phsdif).*2.*pi)) + ...
        randn(1,len.*smpfrq).*noifac;
    end

    % get the FFT of the waves
    for rptlop = 1:numrpt
      fftwav(:,rptlop,1) = fft(wav(:,rptlop,1));
      fftwav(:,rptlop,2) = fft(wav(:,rptlop,2));
    end

    % calculate the power-spectral densities (psd) and the cross-spectral
    % densities (csd) and sum them over repetitions
    numsmp = length(wav);
    psd = 2.*abs(fftwav).^2./(numsmp.^2);
    csd = 2.*(fftwav(:,:,1).*conj(fftwav(:,:,2)))./(numsmp.^2);
    sumpsd = squeeze(sum(psd,2));
    sumcsd = squeeze(sum(csd,2));

    % calculate coherence
    coh = abs(sumcsd ./ sqrt(sumpsd(:,1) .* sumpsd(:,2)));

    figure;
    plot(squeeze(wav(:,:,1)));
    figure;
    plot(squeeze(wav(:,:,2)));
    figure;
    plot(coh);

{% include image src="/assets/img/example/fourier/figure8.png" %}

_Figure: Coherence spectrum for two 10 Hz signals with a somewhat consistent phase difference._

### Exercise

{% include markup/skyblue %}
Change the phase spread factor (phsspreadfac) in the coherence analysis and see what the outcome is.
{% include markup/end %}
