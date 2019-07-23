---
title: Conditional Granger causality in the frequency domain
tags: [example, freq, connectivity, Granger]
---

# Conditional Granger causality in the frequency domain

Conditional Granger causality is a derivative of spectral Granger causality that is computed over a triplet of channels (or blocks of channels). It provides the advantage that for this triplet, it allows to differentiate between a delayed parallel drive from sources $A$ to be $B$ and $C$ and a sequential drive from $A$ to $B$ to $C$.

This example illustrates the simulation and base analysis of the paper **TODO**.

See also: [the connectivity tutorial](http://www.fieldtriptoolbox.org/tutorial/connectivity/).

First, define parameters under which samples should be simulated.

    simcfg             = [];
    simcfg.ntrials     = 500;
    simcfg.triallength = 1;
    simcfg.fsample     = 200;
    simcfg.nsignal     = 3;
    simcfg.method      = 'ar';

    % parmeters of the model itself
    mu                 = 0.5;
    absnoise           = [ 1.0   0.2   0.3 ];

First, we generate the sample for the case of sequential driving.

    % params(i,j,k): j -> i at t=k
    simcfg.params(:,:,1) = [   0      0      0;
                             1.0      0      0;
                               0    1.0     mu];

Note that the matrix representation for the covariance reads from columns to row, other than the MVAR-model is read intuitively.

    % paper defines stds, not cov:
    simcfg.noisecov      = diag(absnoise.^2);

data2           = ft_connectivitysimulation(simcfg);

Now create sample data for the case of differentially delayed driving.

    simcfg.params(:,:,1) = [   0      0      0;
                             1.0      0      0;
                               0      0     mu];
    simcfg.params(:,:,2) = [   0      0      0;
                               0      0      0;
                             1.0      0      0];

Build the actual MVAR-representation...

    data1           = ft_connectivitysimulation(simcfg);

... and have a first look at the data:

    figure
    plot(data.time{1}, data.trial{1})
    legend(data1.label)
    xlabel('time (s)')

%% --------------------------------------------------------
% 2.a) mvar model freq analysis
% ---------------------------------------------------------

    freq                   = [];
    freq.freqcfg           = [];
    freq.freqcfg.method    = 'mtmfft';
    freq.freqcfg.output    = 'fourier';
    freq.freqcfg.tapsmofrq = 2;
    freqdata1           = ft_freqanalysis(freq.freqcfg, data1);
    freqdata2           = ft_freqanalysis(freq.freqcfg, data2);

%% --------------------------------------------------------
% 3.) test regular granger causality
% ---------------------------------------------------------
% Standard granger causal analysis

    grangercfg = [];
    grangercfg.method  = 'granger';
    grangercfg.granger.conditional = 'no';

    gdata = [];

    gdata.g1_bivar_mvar     = ft_connectivityanalysis(grangercfg, mfreqdata1);
    gdata.g2_bivar_mvar     = ft_connectivityanalysis(grangercfg, mfreqdata2);

    grangercfg.granger.sfmethod = 'bivariate';
    gdata.g1_bivar_reg      = ft_connectivityanalysis(grangercfg, freqdata1);
    gdata.g2_bivar_reg      = ft_connectivityanalysis(grangercfg, freqdata2);

%% --------------------------------------------------------
% 4.a) Bivariate conditional
% ---------------------------------------------------------

    grangercfg.granger.conditional = 'yes';
    grangercfg.channelcmb  = {{'signal001'} {'signal002'} {'signal003'}};
    grangercfg.granger.sfmethod = 'multivariate';
    grangercfg.granger.conditional = 'yes';

    % block-wise causality
    grangercfg.granger.block(1).name   = freqdata1.label{1};
    grangercfg.granger.block(1).label  = freqdata1.label(1);
    grangercfg.granger.block(2).name   = freqdata1.label{2};
    grangercfg.granger.block(2).label  = freqdata1.label(2);
    grangercfg.granger.block(3).name   = freqdata1.label{3};
    grangercfg.granger.block(3).label  = freqdata1.label(3);

    gdata.g1_multi_reg_conditional = ft_connectivityanalysis(grangercfg, freqdata1);
    gdata.g2_multi_reg_conditional = ft_connectivityanalysis(grangercfg, freqdata2);

%% --------------------------------------------------------
% 5) Evaluate
% ---------------------------------------------------------
% The label combinations are 6x2 cell arrays, containing all 2-permutations
% tuplets from the channels. How to interpret this?
% Is the combination a b representing F a -> b given rest?
% Let's check this. In scenario 2, we should clearly see a higher causality
% from 1 -> 3 given 2 than in scenario 1 of the differentially delayed
% drive. This corresponds to row 4 in the
% gdata.g1_multi_reg_conditional.labelcmb.
% So, let's compare the labelcmb 1 3 in both scenarios:

    scenario1_mean = mean(gdata.g1_multi_reg_conditional.grangerspctrm(4, :));
    scenario2_mean = mean(gdata.g2_multi_reg_conditional.grangerspctrm(4, :));

% But scenario2_mean < scenario1_mean...