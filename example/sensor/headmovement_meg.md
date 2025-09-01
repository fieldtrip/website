---
title: How to incorporate head movements in MEG analysis
category: example
tags: [artifact, meg, glm, regression, confound]
redirect_from:
    - /example/how_to_incorporate_head_movements_in_meg_analysis/
    - /example/regressing_out_headposition_confounds_in_a_ctf275_dataset/
    - /example/headmovement_meg/
---

# How to incorporate head movements in MEG analysis

## Description

Changes in the subject's position of the head during MEG recordings may cause a significant error in the source localization. Besides, the mixture of different head positions over time adds variance to the data that is not accounted for by the experimental manipulation. Thus head movements may deteriorate statistical sensitivity when analyzing MEG on both sensor and source levels. It is therefore recommended to incorporate head movements in the offline MEG analysis, see [Stolk et al., NeuroImage 2013](https://doi.org/10.1016/j.neuroimage.2012.11.047).

In the CTF MEG system the continuous head localization is represented in HLC (Head Localization Coil) channels. Information from these channels can be used to [track the head position](/faq/how_can_i_monitor_a_subject_s_head_position_during_a_meg_session) in real time. The example script here shows how to read these channels for offline analysis and to estimate the amount of movement. This example script uses [an example dataset](https://download.fieldtriptoolbox.org/example/regressconfound/TacStimRegressConfound.zip) that you can download from our download server.

In general there are various ways that you can use the continuous head localization information.

1. you can discard a subject or trial(s) from subsequent analysis if he/she moved too much
2. you can regress out the movements from the processed data
3. you can compensate the raw data for the movements
4. you can correct the forward model (i.e., the leadfield) for the spatial blurring that is due to the movements

The first way of dealing with the movements requires that you visualize and decide on the movements. This is demonstrated in the first half of the example script.

The second way of dealing with the movements means that you perform **[ft_timelockanalysis](/reference/ft_timelockanalysis)**, **[ft_freqanalysis](/reference/ft_freqanalysis)** or **[ft_sourceanalysis](/reference/ft_sourceanalysis)** with the option `cfg.keeptrials='yes'`. This will give trial estimates of the ERF, the power or the source strength for each trial. The effect that the variable head position has on those single-trial estimates can be estimated and removed from the data using **[ft_regressconfound](/reference/ft_regressconfound)**. This method has been found to significantly improve statistical sensitivity following head movements up to 30% (see [Stolk et al. 2013](https://doi.org/10.1016/j.neuroimage.2012.11.047)) and is demonstrated in the second half of the example script.

The third way of dealing with the movements requires that you make a spatial interpolation of the raw MEG data at each moment in time, in which you correct for the movements. In principle this could be done using the **[ft_megrealign](/reference/ft_megrealign)** function, but at this moment (May 2012) that function cannot yet deal with within-session movements.

The fourth way of dealing with the movements is implemented in the **[ft_headmovement](/reference/ft_headmovement)** function. It is not explained in further detail on this example page.

{% include markup/yellow %}
Please cite the following paper when you have used the offline head movement compensation in your study:

Stolk A, Todorovic A, Schoffelen JM, Oostenveld R. **[Online and offline tools for head movement compensation in MEG.](https://doi.org/10.1016/j.neuroimage.2012.11.047)** Neuroimage, 2013. doi: 10.1016/j.neuroimage.2012.11.047.
{% include markup/end %}

## Reading-in and visualizing the head localization

Prepare configuration to define a single continuous data segment:

    cfg                         = [];
    cfg.dataset                 = 'TacStimRegressConfound.ds';
    cfg.trialdef.ntrials        = 1;
    cfg.trialdef.length         = inf; 
    cfg.continuous              = 'yes';
    cfg = ft_definetrial(cfg);

Read the data with the following HLC channels:

- HLC00n1 is the X coordinate relative to the dewar (in meters) of the nth head localization coil
- HLC00n2 is the Y coordinate relative to the dewar (in meters) of the nth head localization coil
- HLC00n3 is the Z coordinate relative to the dewar (in meters) of the nth head localization coil

Here we have three HLC coils

    cfg.channel = { ...
      'HLC0011', 'HLC0012', 'HLC0013', ...
      'HLC0021', 'HLC0022', 'HLC0023', ...
      'HLC0031', 'HLC0032', 'HLC0033'
    };

    headpos = ft_preprocessing(cfg);

Determine the mean (per trial) circumcenter (the center of the circumscribed circle) of the three headcoils and its orientation. For this we use the helper function that you can find at the bottom of this page.

    % get the position of each of the three coils over time
    coil1 = headpos.trial{1,t}([1 2 3], :);
    coil2 = headpos.trial{1,t}([4 5 6], :);
    coil3 = headpos.trial{1,t}([7 8 9], :);

    % calculate the headposition and orientation per trial (for function see bottom page)
    cc = circumcenter(coil1, coil2, coil3);

Now you can plot the head position relative to the first sample, and compute the maximal position change.

    cc_rel = cc - repmat(cc(:,1), 1, size(cc,2));

    figure

    % plot translations
    subplot(2,1,1)
    plot(headpos.time{1}, cc_rel(1:3,:)*1000) % in mm
    title('Translations')

    % plot rotations
    subplot(2,1,2)
    plot(headpos.time{1}, cc_rel(4:6,:))
    title('Rotations')

    maxposchange = max(abs(cc_rel(1:3,:)), [], 'all')*1000 % in mm

{% include image src="/assets/img/example/headmovement_meg/headmovementexample.png" %}

The figure illustrates the change in head position during the 200 seconds of this short example MEG recording. In a longer and more typical MEG recording you are likely to see some structure over time that relates to the experimental blocks and the breaks in-between.

You may decide to exclude a subject from the subsequent analysis if the head movement exceeds a certain threshold.

## Regressing out headposition confounds

MEG experiments typically involve repeated trials of an evoked or induced brain response. A mixture of different head positions over time adds variance to the data that is not accounted for by the experimental manipulation, thus potentially deteriorating statistical sensitivity. By using a general linear model, head movement related trial-by-trial variance can be removed from the data, both at the sensor- and source level. This procedure involves 3 steps:

1. Preprocess the MEG data, for instance pertaining to an ERF analysis at the sensor level. Note the `cfg.keeptrials='yes'` option when calling **[ft_timelockanalysis](/reference/ft_timelockanalysis)**.

    ```matlab
    % define trials
    cfg = [];
    cfg.dataset = 'TacStimRegressConfound.ds';
    cfg.trialdef.eventtype = 'UPPT001';
    cfg.trialdef.eventvalue = 4;
    cfg.trialdef.prestim = 0.2;
    cfg.trialdef.poststim = 0.3;
    cfg.continuous = 'yes'; % see https://www.fieldtriptoolbox.org/faq/continuous/
    cfg = ft_definetrial(cfg);

    % preprocess the MEG data
    cfg.channel = {'MEG'};
    cfg.demean = 'yes';
    cfg.baselinewindow = [-0.2 0];
    cfg.dftfilter = 'yes'; % notch filter to filter out 50Hz
    data = ft_preprocessing(cfg);

    % timelock analysis
    cfg = [];
    cfg.keeptrials = 'yes';
    timelock = ft_timelockanalysis(cfg, data);
    ````

2. Create trial-by-trial estimates of head movement. Here one may assume that the head is a rigid body that can be described by 6 parameters (3 translations and 3 rotations). The circumcenter function (see below at the end of this page) gives us these parameters. By demeaning we obtain the deviations relative to the average head position and orientation.

    ```matlab
    % define the same trials, now for the HLC channels
    cfg = [];
    cfg.dataset = 'TacStimRegressConfound.ds';
    cfg.trialdef.eventtype = 'UPPT001';
    cfg.trialdef.eventvalue = 4;
    cfg.trialdef.prestim = 0.2;
    cfg.trialdef.poststim = 0.3;
    cfg.continuous = 'yes'; % see https://www.fieldtriptoolbox.org/faq/continuous/
    cfg = ft_definetrial(cfg);

    % preprocess the headposition data
    cfg.channel = { ...
      'HLC0011', 'HLC0012', 'HLC0013', ...
      'HLC0021', 'HLC0022', 'HLC0023', ...
      'HLC0031', 'HLC0032', 'HLC0033'
    };
    headpos = ft_preprocessing(cfg);

    % calculate the mean coil position per trial
    ntrials = size(headpos.sampleinfo,1);
    for t = 1:ntrials
        coil1(:,t) = [mean(headpos.trial{1,t}(1,:)); mean(headpos.trial{1,t}(2,:)); mean(headpos.trial{1,t}(3,:))];
        coil2(:,t) = [mean(headpos.trial{1,t}(4,:)); mean(headpos.trial{1,t}(5,:)); mean(headpos.trial{1,t}(6,:))];
        coil3(:,t) = [mean(headpos.trial{1,t}(7,:)); mean(headpos.trial{1,t}(8,:)); mean(headpos.trial{1,t}(9,:))];
    end

    % calculate the headposition and orientation per trial
    cc = circumcenter(coil1, coil2, coil3)

    % demean to obtain translations and rotations from the average position and orientation
    % transpose to construct a nsamples-by-nregressors matrix 
    cc_dem = [cc - repmat(mean(cc,2),1,size(cc,2))]';
    ```

3. Fit the head movement regressors to the data and remove the variance that can be explained by these confounds.

    ```matlab
    % add head movements to the regressorlist. also add the constant (at the end; column 7)
    confound = [cc_dem ones(size(cc_dem,1),1)];

    % regress out headposition confounds
    cfg = [];
    cfg.confound = confound;
    cfg.reject = [1:6]; % keeping the constant (nr 7)
    regr = ft_regressconfound(cfg, timelock);
    ```

The following figure from the [Stolk et al. 2013](https://doi.org/10.1016/j.neuroimage.2012.11.047) paper shows the statistical results in a single-subject analysis of baseline vs. task activity contrasts. With **[ft_regressconfound](/reference/ft_regressconfound)**, the sensor-level statistical sensitivity was increased after tactile stimulation (40-50 ms; note the more extreme t-scores in the upper panel). Similarly, the source-level statistical sensitivity was increased after visual stimulation (0-500 ms; 65Hz; lower panel).

{% include image src="/assets/img/example/headmovement_meg/regr_ftwiki.png" width="300" %}

_Figure taken from [Stolk et al., NeuroImage 2013](https://doi.org/10.1016/j.neuroimage.2012.11.047)._

## Practical issues

Some features of this GLM-based compensation method need emphasizing. These points are described in more detail in the 'Testing the offline GLM-based head movement compensation' section of [Stolk et al. 2013](https://doi.org/10.1016/j.neuroimage.2012.11.047).

First, **[ft_regressconfound](/reference/ft_regressconfound)** can be applied to timelock, freq, and source data. The estimation of regression coefficients (beta weights of the head position data) is performed separately for each channel and each latency, in the case of timelock data. Consequently, after compensation, the sensor level data cannot be used anymore for source modeling. To employ the GLM based compensation on the source level, single trial estimates for the cortical locations of interest have to be made from the original sensor level data, preferably using a common spatial filter based on all trials. The beta weights are subsequently estimated for each cortical location and the variance in source amplitude over trials that is explained by the head movement is removed. It is therefore recommended to use **[ft_regressconfound](/reference/ft_regressconfound)** as **the final step prior to** calling **[ft_timelockstatistics](/reference/ft_timelockstatistics)**, **[ft_freqstatistics](/reference/ft_freqstatistics)**, or **[ft_sourcestatistics](/reference/ft_sourcestatistics)**.

Second, the same trials in the headposition data have to be selected as those present in the MEG data since these two will be fitted. And more or less related; this general linear modeling (GLM) approach only **affects the signal variance and not the signal mean over trials** (because the constant remains in the data). So when performing a group study, taking the subject mean to the group level statistics will not change these statistics. To benefit from improved statistical sensitivity after using **[ft_regressconfound](/reference/ft_regressconfound)**, it is advised to take a measure that incorporates the consistency (over trials) of a neural effect to the group level. For instance, the t-descriptive, as obtained using an independent samples t-test on trials of one condition versus that of another. These t-values can then be tested at the group level for rejecting the null-hypothesis of no difference between conditions (T=0).

Finally, note that the circumcenter function is a helper function that calculates the position (geometrical center of the three localizer coils) and orientation of the head. This saves some **degrees of freedom** (df=6) as compared to taking into account the x,y,z-coordinates of each coil separately (n=3) as regressors (df=9). If you want to also use the squares, cubes, and derivatives as regressors (to account for non-linear effects of head motion on the MEG signal), this can save quite a bit of degrees. However, too large a number of covariates can reduce statistical efficiency for procedures. In that case, MATLAB will produce the warning that the matrix is "Rank deficient". A rule of thumb is to roughly have 10% of the sample size (based on chapter 8 of Tabachnick & Fidell (1996)).

## Appendix: circumcenter

    function [cc] = circumcenter(coil1,coil2,coil3)

    % CIRCUMCENTER determines the position and orientation of the circumcenter
    % of the three fiducial markers (MEG headposition coils).
    %
    % Input: x,y,z-coordinates of the 3 coils [3 X N],[3 X N],[3 X N] where N
    % is timesamples/trials.
    %
    % Output: x,y,z-coordinates of the circumcenter [1-3 X N], and the
    % orientations to the x,y,z-axes [4-6 X N].
    %
    % A. Stolk, 2012

    % number of timesamples/trials
    N = size(coil1,2);

    %% x-, y-, and z-coordinates of the circumcenter
    % use coordinates relative to point "a" of the triangle
    xba = coil2(1,:) - coil1(1,:);
    yba = coil2(2,:) - coil1(2,:);
    zba = coil2(3,:) - coil1(3,:);
    xca = coil3(1,:) - coil1(1,:);
    yca = coil3(2,:) - coil1(2,:);
    zca = coil3(3,:) - coil1(3,:);

    % squares of lengths of the edges incident to point "a"
    balength = xba .* xba + yba .* yba + zba .* zba;
    calength = xca .* xca + yca .* yca + zca .* zca;

    % cross product of these edges
    xcrossbc = yba .* zca - yca .* zba;
    ycrossbc = zba .* xca - zca .* xba;
    zcrossbc = xba .* yca - xca .* yba;

    % calculate the denominator of the formulae
    denominator = 0.5 ./ (xcrossbc .* xcrossbc + ycrossbc .* ycrossbc + zcrossbc .* zcrossbc);

    % calculate offset (from point "a") of circumcenter
    xcirca = ((balength .* yca - calength .* yba) .* zcrossbc - (balength .* zca - calength .* zba) .* ycrossbc) .* denominator;
    ycirca = ((balength .* zca - calength .* zba) .* xcrossbc - (balength .* xca - calength .* xba) .* zcrossbc) .* denominator;
    zcirca = ((balength .* xca - calength .* xba) .* ycrossbc - (balength .* yca - calength .* yba) .* xcrossbc) .* denominator;

    cc(1,:) = xcirca + coil1(1,:);
    cc(2,:) = ycirca + coil1(2,:);
    cc(3,:) = zcirca + coil1(3,:);

    %% orientation of the circumcenter with respect to the x-, y-, and z-axis coordinates
    v = [cc(1,:)', cc(2,:)', cc(3,:)'];
    vx = [zeros(1,N)', cc(2,:)', cc(3,:)']; % on the x-axis
    vy = [cc(1,:)', zeros(1,N)', cc(3,:)']; % on the y-axis
    vz = [cc(1,:)', cc(2,:)', zeros(1,N)']; % on the z-axis

    for j = 1:N
      % find the angles of two vectors opposing the axes
      thetax(j) = acos(dot(v(j,:),vx(j,:))/(norm(v(j,:))*norm(vx(j,:))));
      thetay(j) = acos(dot(v(j,:),vy(j,:))/(norm(v(j,:))*norm(vy(j,:))));
      thetaz(j) = acos(dot(v(j,:),vz(j,:))/(norm(v(j,:))*norm(vz(j,:))));

      % convert to degrees
      cc(4,j) = (thetax(j) * (180/pi));
      cc(5,j) = (thetay(j) * (180/pi));
      cc(6,j) = (thetaz(j) * (180/pi));
    end
