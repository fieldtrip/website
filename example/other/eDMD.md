---
title: Extended dynamic mode decomposition (eDMD) over nonlinear dictionaries for neural data pipelines
tags: [eDMD, RFF, Koopman-operator, MEG, EEG]
category: example
redirect_from:
    - /example/eDMD/
---

This software provides a FieldTrip-integrated implementation of the Extended Dynamic Mode Decomposition (eDMD) algorithm for multi-channel neural data (MEG, EEG, and iEEG) analysis. eDMD is a data-driven method that generates an approximation to the Koopman operator over a set of observable functions. The **[project repository](https://github.com/DchavezGH/ft_edmdanalysis)**  contains additional information and the function code. 

The frequency content of the neural data is deduced from the eDMD modes. Power associated with these frequencies is also calculated. By binning the frequency content into relevant neural bands (alpha, beta, gamma...), peak frequencies per band are calculated, as well as total power per band. Through the mode decomposition inherent to eDMD, the user can reconstruct the data dynamics from the initial snapshot. The function offers several possibilities for the set of observable functions: Random Fourier features (RFF), Hermite polynomials, polynomial basis, and the identity observable. The package is meant to integrate with the user's FieldTrip pipeline, enabling them to incorporate nonlinear methods into existing workflows.

An overview of eDMD and its relation to the Koopman operator can be found in **[Matthew O. Williams' paper](https://link.springer.com/article/10.1007/s00332-015-9258-5)**. A manuscript on our own eDMD algorithm is still in preparation. 

## Installation

### Requirements

* MATLAB (R2021a or later recommended)

* FieldTrip toolbox (recent stable release recommended)

### Install This Package

* Clone the repository using Git:

`git clone https://github.com/DchavezGH/ft_edmdanalysis`

* Or download the ZIP file and extract it

* Add the repository folder to your MATLAB path:

`addpath(genpath('path_to_repo'))`

* Then ft_edmdanalysis can be called as any other FieldTrip function.

### Reproducibility

* For deterministic behavior when using random Fourier features:

`cfg.seed = 1;`

* Tested Configuration

   * MATLAB R2023b

   * FieldTrip (2024 stable release)

* Users are encouraged to report compatibility issues via the **[project repository](https://github.com/DchavezGH/ft_edmdanalysis)** 

NOTE:
The computational complexity of eDMD depends on dictionary size, data sampling, number of channels, and stacking depth. Users should adjust cfg.D, cfg.poly_degree, and cfg.nstacks carefully for large trials.

## Basic Usage

The function `ft_edmdanalysis` performs Extended Dynamic Mode Decomposition (eDMD) on FieldTrip raw data structures.  
The input data must be a valid FieldTrip **raw structure** containing time series data in `datain.trial`.

The function uses **`cfg.output`** to control the type of result produced.  
Three output modes are available:

- `'freq'` – interpolated spectrum derived from Koopman eigenvalues  (default)
- `'binned_peak_freq'` – power aggregated within frequency bins with peak frequency detection  
- `'raw'` – reconstructed time-domain signal using the Koopman model

---
### Using random Fourier features dictionary
```
cfg = [];
cfg.dictionary = 'rff';

dataout = ft_edmdanalysis(cfg, datain);
```
This runs eDMD using a random Fourier features dictionary on all trials in datain and returns a spectrum derived from Koopman eigenvalues. Random Fourier features are also the default dictionary.

### Using identity dictionary
```
cfg = [];
cfg.dictionary = 'identity';

dataout = ft_edmdanalysis(cfg, datain);
```
This runs classical DMD and returns a FieldTrip frequency structure containing the Koopman-derived spectrum.

### Using a Polynomial Dictionary
```
cfg = [];
cfg.dictionary = 'poly';
cfg.poly_degree = 3;

dataout = ft_edmdanalysis(cfg, datain);
```
This constructs a monomial polynomial dictionary up to degree 3.

### Using a Hermite Dictionary
```
cfg = [];
cfg.dictionary = 'hermite';
cfg.hermite_degree = 3;

dataout = ft_edmdanalysis(cfg, datain);
```
This applies probabilists’ Hermite polynomials independently to each channel.


## Function Output

As default, ft_edmdanalysis will output a FieldTrip freq structure, containing a spectrum generated from the Koopman decomposition. Details on the output structures are in the following section. Two other output options are available:  

### Binned Frequency Representation

To aggregate Koopman mode power into predefined frequency bands:
```
cfg = [];
cfg.output = 'binned_peak_freq';
cfg.freqEdges = [0 4 8 12 15 30 100];

dataout = ft_edmdanalysis(cfg, datain);
```

This returns a FieldTrip frequency structure where:

- power is summed within each frequency bin
- the dominant frequency per bin is stored separately

Peak frequencies per trial are stored in dataout.peakfreq

### State Reconstruction

To reconstruct the time-domain signal from Koopman modes:
```
cfg = [];
cfg.output = 'raw';

dataout = ft_edmdanalysis(cfg, datain);
```
This returns a FieldTrip raw structure containing reconstructed signals.

Optional normalization of the reconstruction can be enabled with `cfg.normalize_recon = true`

## Output Structures

The structure of `dataout` depends on `cfg.output`.


### 1. `cfg.output = 'freq'`

Returns a FieldTrip frequency structure representing the interpolated Koopman spectrum. This is the default output when `cfg.output` is empty (`[]`).

Fields:

* dataout.label = {'edmd'}
* dataout.freq = frequency vector (cfg.foi)
* dataout.powspctrm = [Ntrials x 1 x Nfreq]
* dataout.dimord = 'rpt_chan_freq'
* dataout.cfg

Additional diagnostics:

* dataout.modefreqs
* dataout.modepowers
* dataout.rank

Each entry corresponds to one trial.


### 2. `cfg.output = 'binned_peak_freq'`

Returns a FieldTrip frequency structure where power is aggregated in frequency bins.

Fields:

* dataout.label = {'edmd'}
* dataout.freq = bin centers
* dataout.powspctrm = [Ntrials x 1 x Nbins]
* dataout.dimord = 'rpt_chan_freq'
* dataout.cfg

Additional information:

* dataout.peakfreq


### 3. `cfg.output = 'raw'`

Returns a FieldTrip raw structure containing reconstructed signals.

Fields:

* dataout.label
* dataout.trial
* dataout.time
* dataout.fsample
* dataout.dimord
* dataout.cfg



## API

The main entry point of the package is:

`ft_edmdanalysis(cfg, datain)`


#### Inputs:

`cfg` – configuration structure controlling the decomposition

`datain` – FieldTrip raw data structure


#### Key Configuration Options


* Dictionary:  `cfg.dictionary`= `'identity'`, `'rff'`, `'poly'`, or `'hermite'`

*  Output selection: `cfg.output` = `'freq'`, `'binned_peak_freq'`, or `'raw'`
#### Dictionary parameters:

`cfg.D` number of random Fourier features
`cfg.gamma` RFF scaling parameter
`cfg.poly_degree` polynomial degree
`cfg.hermite_degree` Hermite polynomial degree

#### Algorithm parameters:

`cfg.nstacks` Hankel stacking depth  
`cfg.MA` moving average window 
`cfg.cut` rank truncation threshold
`cfg.seed` RNG seed for RFF reproducibility

#### Spectral parameters:

`cfg.foi` frequencies of interest
`cfg.freqEdges` frequency bin edges
`cfg.smooth` smoothing window for spectrum

#### Reconstruction normalization option:

`cfg.normalize_recon` true / false


## Running ft_edmdanalysis on a data example

We can generate an artificial dataset to showcase the configuration and outputs of ft_edmdanalysis.  
```
%Generate an artificial dataset:
fs = 500;                 % Sampling Frequency
T = 2;                    % Total time
t = 0:1/fs:T-1/fs;        % Time vector
rng(1);                    % Deterministic noise
nw = 0.03;                % Noise amplitude
wp_w=0.11;                % Transient width parameter
wp_c = [0.51 1 1.5 0.9];  % Transient center vector
f0 = [68 21 35 9];        % Transient frequency vector
index_f = [4 12 19 33];   % Transient channel vector
nchan = 40;               % Channel cardinality

% Background noise matrix:
X = nw .* randn(nchan, length(t)); 

% Introduce transient oscillations:
  for i = 1:size(f0,2)    
      X(index_f(i) ,:) = exp(-((t-wp_c(i))./(2.*wp_w)).^2).*sin(2*pi*f0(i)*t);
  end
```

Generate FieldTrip metadata for our artificial dataset:
```
data = [];
data.label = arrayfun(@(x) sprintf('chan%d', x), 1:nchan, 'UniformOutput', false);
data.fsample = fs;
data.trial = {X};
data.time = {t};
data.sampleinfo = [1 numel(t)];
```

Implement the eDMD algorithm with a Random Fourier Features dictionary:

```
cfg = [];
cfg.output = 'freq';         % A frequency structure as output
cfg.dictionary = 'rff';      % Dictionary choice
cfg.gamma = 9.8;             % Gamma parameter, related to RFFs
cfg.D = 4000;                % RFFs cardinality
cfg.foi = 0:0.5:100;         % Frequencies of interest
cfg.verbose = false;
freq = ft_edmdanalysis(cfg, data);
```
Plot the spectrum, marking the expected dominant frequencies

```
figure;
plot(squeeze(freq.freq), squeeze(freq.powspctrm), 'DisplayName', 'spectrum')
hold on
h = xline(f0);
set(h(2:end), 'HandleVisibility', 'off')
set(h(1), 'DisplayName', 'target frequencies')
legend('show')
title('eDMD Spectrum');
xlabel('frequency (Hz)');
ylabel('absolute power');
```

{% include image src="/assets/img/example/eDMD/Figure1.png" %}

Implement the eDMD algorithm with a reconstruction of the data as output. Note that besides cfg.output, all other options can stay the same:

```
cfg.output = 'raw';
raw = ft_edmdanalysis(cfg, data);
```

Plot the reconstruction next to the original data for comparison:
```
figure;
subplot(1,2,1)
surf(raw.trial{1,1}, 'EdgeColor','none')
title('eDMD reconstruction')
subplot(1,2,2)
surf(X, 'EdgeColor','none')
title('artificial dataset')
```

{% include image src="/assets/img/example/eDMD/Figure2.png" %}

Next, implement the eDMD algorithm with binned power as output. Custom frequency bins can be set, this is especially useful for analysis on specific bands (e.g., beta band activity in the dlPFC area shows correlation with the task...)

```
cfg.output = 'binned_peak_freq'; 
cfg.freqEdges = [0 4 8 12 20 40 100]; 
binned_peak = ft_edmdanalysis(cfg, data);
```

Plot binned power, marking the boundaries of the bins:

```
n = numel(binned_peak.freq);
x_centers = (1:n) + 0.5;
figure;
plot(x_centers, squeeze(binned_peak.powspctrm), '_', 'MarkerSize', 40)
hold on
edges = 1:(n+1);
h = xline(edges, 'k:');
set(h(2:end), 'HandleVisibility', 'off')
set(h(1))
xticks(edges)
xticklabels(round(cfg.freqEdges, 2))
xlabel('frequency (Hz)')
ylabel('binned power');
title('eDMD binned Spectrum');
```

{% include image src="/assets/img/example/eDMD/Figure3.png" %}


## Copyright

 Copyright (c) 2026, David Chavez-Huerta

 This program is free software: you can redistribute it and/or modify  it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.
