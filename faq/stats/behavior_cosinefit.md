---
title: How can I test whether a behavioral measure is phasic?
parent: Statistical analysis
grand_parent: Frequently asked questions
category: faq
tags: [statistics, freq]
redirect_from:
    - /faq/how_can_i_test_whether_a_behavioral_measure_is_phasic/
    - /faq/behavior_cosinefit/
---

# How can I test whether a behavioral measure is phasic?

Some experimental hypotheses address the question: *Is my measure-of-interest systematically modulated by the phase of an underlying process?*

For instance, you may wish to quantify the effect of the phase of a band-limited neuronal oscillation on behavioral accuracy or reaction time. Alternatively, you may wish to quantify the effect of pre-stimulus phase on the amplitude of a stimulus-evoked transient in the neuronal signal. One way to evaluate this is to fit a sine/cosine function to the dependent variable, which (according to the hypothesis) modulates as a function of phase. Subsequently, you test the probability of observing the outcome of this fit (typically expressed as the amplitude, or modulation depth) under some null hypothesis.

Here, we demonstrate how this can be achieved in a generic way, using a binning approach. Conceptually, the dependent data consists of a set of observations (typically trials), consisting of categorical variables (e.g., hit/miss) or of continuous variables (e.g., reaction time, signal amplitude). For each of these observations, there is a corresponding 'phase' of the underlying independent variable of interest. Using least-squares regression, it is possible to estimate the amplitude (and phase) of the best fitting cosine-wave to the data. A binning approach can be used to improve the sensitivity, and to better appreciate the underlying structure in the data (particularly for categorical data). The code snippet below demonstrates this approach, and provides a statfun that efficiently computes the cosinefit for multiple signals at once.

    function [s, s_unbinned, x_binned, y_binned] = demo_phasicfit

    nchan = 200;
    nobs  = 500;

    % ground truth
    A   = rand(nchan,1).*0.4; % amplitude
    phi = 2.*pi.*rand(nchan,1); % phase shift


    % create some data, consisting of 0's and 1's
    n = 500;
    ix = 2.*pi.*rand(1,nobs);

    x = exp(1i.*ix);
    xshift = exp(1i.*(ix+phi));
    y = round(rand(nchan,nobs)+A.*real(xshift));


    % bin the data, this is not efficient, but does the trick
    nbin     = 20;
    binwidth = pi/6;

    stepsize = (2.*pi)./nbin;
    steps    = -pi:stepsize:pi;

    x_binned = zeros(1, numel(steps));
    y_binned = zeros(nchan, numel(steps));

    for m = 1:size(y,1)

      for k = 1:numel(steps)
        x_binned(1,k) = steps(k);
        thisbin       = steps(k)+ [-1 1]/(binwidth*2);
        angles        = angle(x);
        if thisbin(1)<-pi
          shift = (angles>(pi-binwidth/2));
          angles(shift) = angles(shift) - 2.*pi;

        end
        if thisbin(1)>pi
          shift = (angles<(-pi+binwidth/2));
          angles(shift) = angles(shift) + 2.*pi;
        end
        sel           = find(angles>thisbin(1) & angles<thisbin(2));
        y_binned(m,k) = mean(y(m,sel));
      end

    end

    figure;plot(x_binned,y_binned, 'o');


    s = ft_statfun_cosinefit([], y_binned, x_binned);

    s_unbinned = ft_statfun_cosinefit([], y, angle(x));

    figure;plot(A, [s_unbinned.stat,s.stat],'o');
    hold on;plot([0 0.5],[0 0.5],'k');
    xlabel = 'actual';
    ylabel = 'estimate';
    legend({'unbinned';'binned'});


The relevant function that computes the cosine fit is provided below:

    function [s, cfg] = ft_statfun_cosinefit(cfg, dat, design)

    % STATFUN_xxx is a function for computing a statistic for the relation
    % between biological data and a design vector containing trial
    % classifications or another independent variable
    %
    % This function is called by STATISTICS_MONTECARLO, where you can specify
    % cfg.statistic = 'xxx' which will be evaluated as statfun_xxx.
    %
    % The external interface of this function has to be
    %   [s] = statfun_xxx(cfg, dat, design);
    % where
    %   dat    contains the biological data, Nvoxels x Nreplications
    %   design contains the independent variable,  1 x Nreplications
    %
    % Additional settings can be passed through to this function using
    % the cfg structure.
    %
    % STATFUN_COSINEFIT fits a cosine to the data dat. the independent
    % variable design should contain angular values, bounded by -pi and pi.
    %
    % the output s is a structure containing the statistic, as specified by
    %  cfg.cosinefit.statistic. this can either be the amplitude (default) of the fit, angle   (giving the preferred angle), complex (giving both angle and amplitude in a complex number), or fit (giving the percentage of explained variance).
    % additional fields in the output=structure are:
    %  s.r      percentage of explained variance.
    %  s.offset the DC-component of the fit.
    %
    % Additional cfg-options are:
    %  cfg.cosinefit.phi = [] (default) or angular value between -pi and pi, estimates the amplitude of a cosine at a given angle.

    % Copyright (C) 2006 Jan-Mathijs Schoffelen

    if ~isfield(cfg, 'cosinefit'),           cfg.cosinefit           = [];          end
    if ~isfield(cfg.cosinefit, 'phi'),       cfg.cosinefit.phi       = [];          end
    if ~isfield(cfg.cosinefit, 'statistic'), cfg.cosinefit.statistic = 'amplitude'; end

    %---create and check independent variable
    if size(design, 2) ~= size(dat,2), error('design is incompatible with input-data'); end
    if size(design, 1) ~= size(dat,1) && size(design,1)==1
      quickflag = 1;
      repdim    = [size(dat,1) 1];
    else
      quickflag = 0;
      repdim    = [1 1];
    end

    %---estimate offset
    offset = mean(dat,2);

    %---do cosinefitting based on a least-square fit
    y = dat - repmat(offset, [1 size(dat,2)]);

    n  = size(design,2);
    if quickflag
      S  = y*sin(design(:));
      C  = y*cos(design(:));
      dS = repmat(sum(sin(2.*design)), repdim);
      dC = repmat(sum(cos(2.*design)), repdim);
    else
      S  = sum(y.*sin(design),2);
      C  = sum(y.*cos(design),2);
      dS = sum(sin(2.*design),2);
      dC = sum(cos(2.*design),2);
    end

    if isempty(cfg.cosinefit.phi)
      nom   = S.*n + S.*dC - C.*dS;
      denom = C.*n - S.*dS - C.*dC;
      b(denom > 0,1) = atan(nom(denom > 0)./denom(denom > 0));
      b(denom < 0,1) = atan(nom(denom < 0)./denom(denom < 0)) + pi;
      b(denom ==0,1) = 0.5 .* pi;
    else
      b = ones(size(design,1),1).*cfg.cosinefit.phi;
    end

    A    = 2 .* (C.*cos(b)+S.*sin(b)) ./ (dS.*cos(2.*b)+dC.*sin(2.*b)+n);
    sse  = sum( (y - repmat(A, [1 n]).*cos(repmat(design,repdim)-repmat(b, [1 n]))).^2, 2); %sum of squared errors
    sTot = sum(y.^2, 2);
    sA   = sqrt( (sse./(n-3)) ./ sum( (design - repmat(mean(design,2), [1 n])).^2, 2) );  %standard deviation of estimator
    r    = 1 - sse ./ sTot; %proportion of explained variance
    phi  = b;

    %---create output-structure
    if strcmp(cfg.cosinefit.statistic, 'complex')
      s.stat = A.*exp(1i.*phi);
    elseif strcmp(cfg.cosinefit.statistic, 'amplitude')
      s.stat = A;
    elseif strcmp(cfg.cosinefit.statistic, 'angle')
      s.stat = phi;
    elseif strcmp(cfg.cosinefit.statistic, 'fit')
      s.stat = r;
    elseif strcmp(cfg.cosinefit.statistic, 'tstat')
      s.stat = A./sA;
    %elseif strcmp(cfg.cosinefit.statistic, 'fstat'),
    %  s.stat = sse./(sTot./(n-3));
    elseif strcmp(cfg.cosinefit.statistic, 'ratio')
      s.stat = A./offset;
    end
    s.r      = r;
    %s.s      = sA;
    s.offset = offset;
