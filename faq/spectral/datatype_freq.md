---
title: In what way can frequency domain data be represented in FieldTrip?
tags: [freq, connectivity, coherence]
category: faq
redirect_from:
    - /faq/in_what_way_can_frequency_domain_data_be_represented_in_fieldtrip/
    - /faq/datatype_freq/
---

## Different output options in ft_freqanalysis

When computing the frequency domain representation of your data using **[ft_freqanalysis](/reference/ft_freqanalysis)**, you can specify the cfg-option 'output'. This option determines the representation of your data:

    cfg.output = 'pow';

The output to **[ft_freqanalysis](/reference/ft_freqanalysis)** will look like this:

    freq =

          label: {2x1 cell}
         dimord: 'chan_freq'
           freq: [1x101 double]
      powspctrm: [2x101 double]
      cumtapcnt: [200x1 double]
            cfg: [1x1 struct]

The numeric data will be stored in the field called 'powspctrm', containing the (real-valued) power per channel and frequency bin (and time bin, depending on cfg.method). As per request, using the cfg.keeptrials and cfg.keeptapers options, you can get an estimate for each single trial and taper.

    cfg.output = 'powandcsd';

The output to **[ft_freqanalysis](/reference/ft_freqanalysis)** will look like this:

    freq =

          label: {2x1 cell}
         dimord: 'chan_freq'
           freq: [1x101 double]
      powspctrm: [2x101 double]
       labelcmb: {'signal002'  'signal001'}
      crsspctrm: [1x101 double]
      cumtapcnt: [200x1 double]
            cfg: [1x1 struct]

The numeric data will now be stored in two fields: the 'powspctrm' and the 'crsspctrm'. The 'powspctrm' is the same as above, and the 'crsspctrm' contains the (complex-valued) cross-spectral density between channel pairs, as indicated by the 'labelcmb' field. The cross-spectral density is the frequency domain analogue of the cross-covariance function. The default behavior of ft_freqanalysis is to return the cross-spectral density between all possible channel pairs, treating the channel pair {'a' 'b'} the same as channel pair {'b' 'a'}. This can be done because the cross-spectrum is a conjugate symmetric quantity. A subset of channel pairs can be specified by the cfg.channelcmb option. If the default number of channel pairs is created (cfg.channelcmb = {'all' 'all'}) the total number of cross-spectra will be n(n-1)/2 (n being the number of channels in the data). As per request, using the cfg.keeptrials and cfg.keeptapers options, you can get an estimate for each single trial / taper. The convention used in FieldTrip to obtain the cross-spectrum in relation to the labeled combination of channels is the following: C = Fa \* conj(Fb), where Fa and Fb are the Fourier transforms of channel a and channel b, and conj means the conjugate. The corresponding labelcmb will in this case be {'a' 'b'}, so the second column always represents the channel from which the conjugate was taken.

    cfg.output = 'fourier';

The output to **[ft_freqanalysis](/reference/ft_freqanalysis)** will look like this:

    freq =

              label: {2x1 cell}
             dimord: 'rpttap_chan_freq'
               freq: [1x101 double]
      fourierspctrm: [600x2x101 double]
          cumsumcnt: [200x1 double]
          cumtapcnt: [200x1 double]
                cfg: [1x1 struct]

The numeric data are now stored in the (complex-valued) 'fourierspctrm' field. It is important to realize that it is typically not a meaningful operation to average these across trials / tapers. Hence, the output will always contain the single trial / taper data. As such this representation is the most 'basic' of all three outputs because both power and cross spectra can be obtained from the fourier-representation of the data.

## Choosing the right output option for ft_freqanalysis

Which representation is most useful for your analysis depends very much on what you want to do with it, how big your data sets are, etc. The disadvantage of the Fourier representation is that it requires the single trial and tapers to be stored in memory, and if that is not needed, a representation containing the average across trials or tapers may be more memory efficient. On the other hand, a cross spectrum between all channel pairs and a lot of frequency bins (and time bins) can quickly become a very big matrix, and the more concise representation of fourier spectra may be more efficient.

## A historical note

Note that the 'powspctrm' is actually nothing else than the cross-spectrum between a channel and itself. As such, it can in principle be represented in a 'crsspctrm'-like way, i.e. having a labelcmb {'a' 'a'}, rather than a label. For historical reasons, the data representation in FieldTrip makes the distinction between the auto-spectra and the cross-spectra.

## Yet another representation

Using **[ft_connectivityanalysis](/reference/ft_connectivityanalysis)** on frequency domain data containing fourier-spectra, without specifying cfg.channelcmb will result in yet another representation of (bivariate) frequency domain data.

    coh =

          label: {2x1 cell}
         dimord: 'chan_chan_freq'
      cohspctrm: [2x2x101 double]
           freq: [1x101 double]
            dof: 600
            cfg: [1x1 struct]

Note that this representation lacks a 'labelcmb' field, and that the 'dimord' is 'chan_chan_freq'. This means that the numeric data now implicitly contains both the combinations {'a' 'b'} (in coh.cohspctrm(1,2,:) ) , and the combination {'b' 'a'} (in coh.cohspctrm(2,1,:) ). For a quantity like the coherence spectrum the values across the diagonal are symmetric, but for complex-valued quantities, as well as for directional measures of interaction, the values at the entries across the diagonal are typically different. The convention used by FieldTrip is that the row-channel 'causes' the column-channel.

## Toggling between the different representations

It is possible (but not recommended for non-expert users) to toggle between the different representations using **[ft_checkdata](/reference/utilities/ft_checkdata)** in combination with the key 'cmbrepresentation'. For example

    freq =

              label: {2x1 cell}
             dimord: 'rpttap_chan_freq'
               freq: [1x101 double]
      fourierspctrm: [600x2x101 double]
          cumsumcnt: [200x1 double]
          cumtapcnt: [200x1 double]
                cfg: [1x1 struct]

    >> freqnew=ft_checkdata(freq,'cmbrepresentation','full');
    >> freqnew

    freqnew =

          label: {2x1 cell}
         dimord: 'rpt_chan_chan_freq'
           freq: [1x101 double]
      cumsumcnt: [200x1 double]
      cumtapcnt: [200x1 double]
            cfg: [1x1 struct]
      crsspctrm: [4-D double]

or

    >> freqnew=ft_checkdata(freq,'cmbrepresentation','sparsewithpow');
    >> freqnew

    freqnew =

          label: {2x1 cell}
         dimord: 'rpt_chan_freq'
           freq: [1x101 double]
      cumsumcnt: [200x1 double]
      cumtapcnt: [200x1 double]
            cfg: [1x1 struct]
      powspctrm: [200x2x101 double]

or

    >> freqnew=ft_checkdata(freq,'cmbrepresentation','sparsewithpow','channelcmb',{'signal001' 'signal002'});
    >> freqnew

    freqnew =

          label: {2x1 cell}
         dimord: 'rpt_chan_freq'
           freq: [1x101 double]
      cumsumcnt: [200x1 double]
      cumtapcnt: [200x1 double]
            cfg: [1x1 struct]
      crsspctrm: [200x1x101 double]
       labelcmb: {'signal001'  'signal002'}
      powspctrm: [200x2x101 double]
