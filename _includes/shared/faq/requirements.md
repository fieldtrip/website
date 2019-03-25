## MATLAB version

We try to develop FieldTrip in such a way that it works with the latest MATLAB release on the most popular operating system platforms, but at the same time we try to have it work with as many older MATLAB versions as possible.

However, the MATLAB syntax and the availability of functions in the standard MathWorks toolboxes [changes over time](http://www.mathworks.com/help/matlab/release-notes.html). Consequently, sometimes we will use MATLAB code that is only supported from a certain version upwards. In general we attempt to support MATLAB versions up to 5 years old.

An online poll in April 2011 showed that a large proportion (>98%) of our users access the FieldTrip toolbox with a MATLAB version younger than 2006 (<5 years). The full results can be found [here](http://bugzilla.fieldtriptoolbox.org/attachment.cgi?id=45).

## MathWorks toolboxes

MATLAB includes a large number of functions in standard toolboxes that come with every installation, but certain functions are included in additional (commercial) toolboxes from MathWorks, such as the Signal Processing or the Statistics toolbox. Whether you need to buy these toolboxes depends on whether you want to use specific functionality in FieldTrip. We try to avoid using these additional MathWorks toolboxes to the extent that we will look for alternatives (e.g. from [GNU Octave](https://www.gnu.org/software/octave)) or use drop-in replacement functions for certain functions, as long as the time required to implement these alternatives is not too large.

The following functions depend on the MathWorks [Image Processing Toolbox](https://www.mathworks.com/products/image.html)

- ft_sourceplot
- ft_volumesegment
- ft_read_mri

The following functions depend on the MathWorks [Optimization Toolbox](https://www.mathworks.com/products/optimization.html)

- warp_optim
- dipole_fit

The following functions depend on the MathWorks [Signal Processing Toolbox](https://www.mathworks.com/products/signal.html)

- ft_mvaranalysis
- ft_resampledata
- ft_preproc_bandpassfilter
- ft_preproc_bandstopfilter
- ft_preproc_denoise
- ft_preproc_highpassfilter
- ft_preproc_hilbert
- ft_preproc_lowpassfilter
- ft_preproc_medianfilter
- ft_preproc_resample
- ft_specest_hilbert
- ft_specest_mtmconvol
- ft_specest_mtmfft
- ft_spiketriggeredspectrum_convol
- ft_spiketriggeredspectrum_fft

The following functions depend on the MathWorks [Statistics and Machine Learning Toolbox](https://www.mathworks.com/products/statistics.html)

- ft_connectivitysimulation
- ft_headmovement
- ft_qualitycheck
- ft_regressconfound
- ft_sourcedescriptives
- ft_statistics_stats
- ft_stratify
- ft_datatype_spike
- ft_statfun_depsamplesFmultivariate
- ft_statfun_indepsamplesF
- ft_statfun_indepsamplesZcoh
- ft_spike_isi
- ft_spike_plot_isi
- ft_spike_plot_isireturn
- ft_spike_plot_jpsth
- ft_spike_plot_raster
- ft_spike_waveform
- ft_spike_xcorr
- ft_spikesorting
- ft_spiketriggeredspectrum_convol
