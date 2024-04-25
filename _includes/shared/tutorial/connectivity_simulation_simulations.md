We will first simulate some data with a known connectivity structure built in. This way we know what to expect in terms of connectivity. To simulate data we use **[ft_connectivitysimulation](/reference/ft_connectivitysimulation)**. We will use an order 2 multivariate autoregressive model. The necessary ingredients are a set of NxN coefficient matrices, one matrix for each time lag. These coefficients need to be stored in the cfg.param field. Next to the coefficients we have to specify the NxN covariance matrix of the innovation noise. This matrix needs to be stored in the cfg.noisecov field.

The model we are going to use to simulate the data is as follow

x(t) = 0.8*x(t-1) - 0.5*x(t-2)

y(t) = 0.9*y(t-1) + 0.5*z(t-1) - 0.8*y(t-2)

z(t) = 0.5*z(t-1) + 0.4*x(t-1) - 0.2*z(t-2)

which is done using

    % always start with the same random numbers to make the figures reproducible
    rng default
    rng(50)

    cfg             = [];
    cfg.ntrials     = 500;
    cfg.triallength = 1;
    cfg.fsample     = 200;
    cfg.nsignal     = 3;
    cfg.method      = 'ar';

    cfg.params(:,:,1) = [ 0.8    0    0 ;
                            0  0.9  0.5 ;
                          0.4    0  0.5];

    cfg.params(:,:,2) = [-0.5    0    0 ;
                            0 -0.8    0 ;
                            0    0 -0.2];

    cfg.noisecov      = [ 0.3    0    0 ;
                            0    1    0 ;
                            0    0  0.2];

    data              = ft_connectivitysimulation(cfg);

The simulated data consists of 3 channels (cfg.nsignal) in 500 trials (cfg.ntrials). You can easily visualize the data for example in the first trial using

    figure
    plot(data.time{1}, data.trial{1})
    legend(data.label)
    xlabel('time (s)')

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_simulations/figure1.png" width="400" %}

or browse through the complete data using

    cfg = [];
    cfg.viewmode = 'vertical';  % you can also specify 'butterfly'
    ft_databrowser(cfg, data);

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_simulations/figure2.png" width="400" %}

### Computation of the multivariate autoregressive model

To be able to compute spectrally resolved [Granger causality](https://en.wikipedia.org/wiki/Granger_causality), or other frequency-domain directional measures of connectivity, we need to estimate two quantities: the spectral transfer matrix and the covariance of an autoregressive model's residuals. We fit an autoregressive model to the data using the **[ft_mvaranalysis](/reference/ft_mvaranalysis)** function.

For the actual computation of the autoregressive coefficients FieldTrip makes use of an implementation from third party toolboxes. At present **[ft_mvaranalysis](/reference/ft_mvaranalysis)** supports the [biosig](http://biosig.sourceforge.net) and [bsmart](http://www.brain-smart.org) toolboxes for these computations.

In this tutorial we will use the bsmart toolbox. The relevant functions have been included in the FieldTrip release in the fieldtrip/external/bsmart directory. Although the exact implementations within the toolboxes differ, their outputs are comparable.

    cfg         = [];
    cfg.order   = 5;
    cfg.toolbox = 'bsmart';
    mdata       = ft_mvaranalysis(cfg, data);

    mdata =
             dimord: 'chan_chan_lag'
              label: {3x1 cell}
             coeffs: [3x3x5 double]
           noisecov: [3x3 double]
                dof: 500
        fsampleorig: 200
                cfg: [1x1 struct]

The resulting variable **mdata** contains a description of the data in terms of a multivariate autoregressive model. For each time-lag up to the model order (cfg.order), a 3x3 matrix of coefficients is outputted. The noisecov-field contains covariance matrix of the model's residuals.

{% include markup/yellow %}
Here, we know the model order a priori because we simulated the data and we choose a slightly higher model order (five instead of two) to get more interesting results in the output. For real data the appropriate model order for fitting the autoregressive model can vary depending on subject, experimental task, quality and complexity of the data, and model estimation technique that is used. You can estimate the optimal model order for your data by relying on information criteria methods such as the Akaike information criterion or the Bayesian information criterion. Alternatively, you can choose to use a non-parametric approach without having to decide on model order at all (see next section on [Non-parametric computation of the cross-spectral density matrix](/tutorial/connectivity#non-parametric-computation-of-the-cross-spectral-density-matrix))
{% include markup/end %}

#### Exercise 1

{% include markup/blue %}
Compare the parameters specified for the simulation with the estimated coefficients and discuss.
{% include markup/end %}

### Computation of the spectral transfer function

From the autoregressive coefficients it is now possible to compute the spectral transfer matrix, for which we use **[ft_freqanalysis](/reference/ft_freqanalysis)**. There are several ways of computing the spectral transfer function, the parametric and the non-parametric way. We will first illustrate the parametric route:

    cfg        = [];
    cfg.method = 'mvar';
    mfreq      = ft_freqanalysis(cfg, mdata);

    mfreq =

            freq: [1x101 double]
        transfer: [3x3x101 double]
        noisecov: [3x3 double]
       crsspctrm: [3x3x101 double]
             dof: 500
            label: {3x1 cell}
           dimord: 'chan_chan_freq'
              cfg: [1x1 struct]

The resulting **mfreq** data structure contains the pairwise transfer function between the 3 channels for 101 frequencies.

It is also possible to compute the spectral transfer function using non-parametric spectral factorization of the cross-spectral density matrix. For this, we need a Fourier decomposition of the data. This is done in the following section.

### Non-parametric computation of the cross-spectral density matrix

Some connectivity metrics can be computed from a non-parametric spectral estimate (i.e. after the application of the FFT-algorithm and conjugate multiplication to get cross-spectral densities), such as coherence, phase-locking value and phase slope index. The following part computes the Fourier-representation of the data using **[ft_freqanalysis](/reference/ft_freqanalysis)**.

    cfg           = [];
    cfg.method    = 'mtmfft';
    cfg.taper     = 'dpss';
    cfg.output    = 'fourier';
    cfg.tapsmofrq = 2;
    freq          = ft_freqanalysis(cfg, data);

    freq =
                label: {3x1 cell}
               dimord: 'rpttap_chan_freq'
                 freq: [1x101 double]
        fourierspctrm: [1500x3x101 double]
            cumsumcnt: [500x1 double]
            cumtapcnt: [500x1 double]
                  cfg: [1x1 struct]

The resulting **freq** structure contains the spectral estimate for 3 tapers in each of the 500 trials (hence 1500 estimates), for each of the 3 channels and for 101 frequencies. It is not necessary to compute the cross-spectral density at this stage, because the function used in the next step, **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)**, contains functionality to compute the cross-spectral density from the Fourier coefficients.

{% include markup/yellow %}
We apply frequency smoothing of 2Hz. The tapsmofrq parameter should already be familiar to you from the [multitapers section of the frequency analysis tutorial](/tutorial/timefrequencyanalysis/#multitapers). How much smoothing is desired will depend on your research question (i.e. frequency band of interest) but also on whether you decide to use the parametric or non-parametric estimation methods for connectivity analysis:

Parametric and non-parametric estimation of Granger causality yield very comparable results, particularly in well-behaved simulated data. The main advantage in calculating Granger causality using the non-parametric technique is that it does not require the determination of the model order for the autoregressive model. When relying on the non-parametric factorization approach more data is required as well as some smoothing for the algorithm to converge to a stable result. Thus the choice of parametric vs. non-paramteric estimation of Granger causality will depend on your data and your certainty of model order.
(find this information and more in [Bastos and Schoffelen 2016](http://journal.frontiersin.org/article/10.3389/fnsys.2015.00175/full))
{% include markup/end %}

### Computation and inspection of the connectivity measures

The actual computation of the connectivity metric is done by **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)**. This function is transparent to the type of input data, i.e. provided the input data allows the requested metric to be computed, the metric will be calculated. Here, we provide an example for the computation and visualization of the coherence coefficient.

    cfg           = [];
    cfg.method    = 'coh';
    coh           = ft_connectivityanalysis(cfg, freq);
    cohm          = ft_connectivityanalysis(cfg, mfreq);

Subsequently, the data can be visualized using **[ft_connectivityplot](/reference/ft_connectivityplot)**.

    cfg           = [];
    cfg.parameter = 'cohspctrm';
    cfg.zlim      = [0 1];
    ft_connectivityplot(cfg, coh, cohm);

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_simulations/figure3.png" width="400" %}

The coherence measure is a symmetric measure, which means that it does not provide information regarding the direction of information flow between any pair of signals. In order to analyze directionality in interactions, measures based on the concept of granger causality can be computed. These measures are based on an estimate of the spectral transfer matrix, which can be computed in a straightforward way from the multivariate autoregressive model fitted to the data.

    cfg           = [];
    cfg.method    = 'granger';
    granger       = ft_connectivityanalysis(cfg, mfreq);

    cfg           = [];
    cfg.parameter = 'grangerspctrm';
    cfg.zlim      = [0 1];
    ft_connectivityplot(cfg, granger);

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_simulations/figure4.png" width="400" %}

#### Exercise 2

{% include markup/blue %}
Compute the granger output using instead the 'freq' data structure. Plot them side-by-side using ft_connectivityplot.
{% include markup/end %}

Instead of plotting it with **[ft_connectivityplot](/reference/ft_connectivityplot)**, you can use the following low-level MATLAB plotting code which gives a better understanding of the numerical representation of the results.

    figure
    for row=1:3
    for col=1:3
      subplot(3,3,(row-1)*3+col);
      plot(granger.freq, squeeze(granger.grangerspctrm(row,col,:)))
      ylim([0 1])
    end
    end

{% include image src="/assets/img/shared/tutorial/connectivity_simulation_simulations/figure5.png" width="400" %}

#### Exercise 3

{% include markup/blue %}
Discuss the differences between the granger causality spectra, and the coherence spectra.
{% include markup/end %}

#### Exercise 4

{% include markup/blue %}
Compute the following connectivity measures from the **mfreq** data, and visualize and discuss the results: partial directed coherence (pdc), directed transfer function (dtf), phase slope index (psi). (Note that psi will require specifying cfg.bandwidth. What is the meaning of this parameter?)
{% include markup/end %}
