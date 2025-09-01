---
title: How can I visualize the Neuromag head position indicator coils?
category: faq
tags: [neuromag, head, localization]
redirect_from:
    - /faq/how_can_i_visualize_the_neuromag_head_position_indicator_coils/
    - /faq/neuromag_hpi/
---

It is common practice for an MEG experiment involving Neuromag systems to digitize the positions of head position indicator (HPI) coils, as well as other landmarks of the subject's head, prior to performing the experiment. The [real-time head localizer](/getting_started/realtime/headlocalizer) uses these digitized positions, which are stored in the Neuromag fif file, to perform the real time fitting of the actual HPI coil positions during the course of the experiment. It is therefore advised to check whether those digitized positions match the topographical magnetic field distribution of signals evoked by the HPI coils (each energized with a specific frequency).

The following code reads and visualizes the digitized positions of the HPI coils. See panel A for a photograph of the subject, and panel B for the digitized positions of the HPI coils in Neuromag device (dewar) space.

    % an example Neuromag dataset
    dataset = '/home/common/matlab/fieldtrip/data/test/bug1792/20130418_test_cHPI.fif';

    % visualize the known/fixed positions of the sensors
    hdr = ft_read_header(dataset, 'coordsys', 'dewar');
    ft_plot_sens(hdr.grad);

    % visualize the digitized positions of the head position indicator coils
    shape = ft_read_headshape(dataset, 'coordsys', 'dewar');
    for c = 1:size(shape.pnt,1)
      if ~isempty(strfind(shape.label{c},'hpi'))
          hold on;
          plot3(shape.pnt(c,1),shape.pnt(c,2),shape.pnt(c,3), 'ro', 'MarkerSize', 12, 'LineWidth', 3);
          hold on;
          text(shape.pnt(c,1),shape.pnt(c,2),shape.pnt(c,3), sscanf(shape.label{c},'hpi_%s'));
      end
    end

The following code reads and visualizes the topographical magnetic field distributions. This is done for specific frequency bands, known from the Neuromag documentation to contain signal evoked by the HPI coils (panel C).

    % preprocess the trials
    begsample = ([0 1 2 3 4 5 6 7 8 9 10]) * hdr.Fs+1;
    endsample = begsample + hdr.Fs-1;
    cfg = [];
    cfg.trl = [begsample(:) endsample(:)];
    cfg.trl(:,3) = 0;
    cfg.dataset = dataset;
    cfg.channel = 'MEGMAG';
    data = ft_preprocessing(cfg);

    % determine spectral content
    cfg = [];
    cfg.method = 'mtmfft';
    cfg.output = 'pow';
    cfg.foilim = [1 500];
    cfg.taper = 'hanning';
    freq = ft_freqanalysis(cfg, data);

    % plot topographical distribution of Neuromag coil frequencies
    figure; hold on;
    cfg = [];
    cfg.layout = 'neuromag306mag.lay';
    subplot(2,3,1); hold on;
    cfg.xlim = [293 293];
    cfg.comment = '293 Hz';
    ft_topoplotER(cfg, freq);
    subplot(2,3,2); hold on;
    cfg.xlim = [307 307];
    cfg.comment = '307 Hz';
    ft_topoplotER(cfg, freq);
    subplot(2,3,3); hold on;
    cfg.xlim = [314 314];
    cfg.comment = '314 Hz';
    ft_topoplotER(cfg, freq);
    subplot(2,3,4); hold on;
    cfg.xlim = [321 321];
    cfg.comment = '321 Hz';
    ft_topoplotER(cfg, freq);
    subplot(2,3,5); hold on;
    cfg.xlim = [328 328];
    cfg.comment = '328 Hz';
    ft_topoplotER(cfg, freq);

According to Neuromag documentation, frequencies of the HPI signals are 154, 158, 162, 166 and 170 Hz for the sampling rate of 600 Hz (low-pass filter at 200 Hz), or 293, 307, 314, 321
and 328 Hz for higher sampling rates.

Note that in this example dataset, the digitized position of HPI coil 5, energized with a frequency of 328 Hz, does not match the topographical distribution of recorded signal at that frequency. In order to optimize the fitting of those HPI coils during the experiment, it is recommended to exclude this coil from the real time analysis when [monitoring the subject's head](/faq/experiment/headlocalizer). For example, by specifying the frequencies of interest when calling **[ft_realtime_headlocalizer](/reference/realtime/online_meg/ft_realtime_headlocalizer)**:

    cfg.coilfreq = [293, 307, 314, 321]; % note 328 Hz is missing

{% include image src="/assets/img/faq/neuromag_hpi/neuromag_wikiexample.png" width="400" %}
