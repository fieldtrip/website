---
title: Integration with NUTMEG
redirect_from:
  - /development/nutmeg/
---

{% include /shared/development/warning.md %}

    1) Identify pieces of code in common and avoid replication
    2) NUTMEG can call FieldTrip's fileio
    3) NUTMEG can call FieldTrip's forward (including the change to treating reference electrodes as separate)
    4) What does NM do that does not exist (or done well) in FT? place in fieldtrip/external/nutmeg
    5) What does FT do that does not exist (or done well) in NM?
    6) create nutmeg/external/fieldtrip for functions other than fileio or forward (call to sites.google for this code)
    7) changes to FieldTrip to be compatible with running in Nutmeg
    8) conversion functions
    9) examples of switching between toolboxes
    10) try Subject01.ds in NM and/or MEGSIM dataset in both toolboxes.

See [/development/compat](/development/project/compat) for mydepfun example

## 2) fileio questions

- How is it recommended to deal with datasets larger than one's RAM? i.e. is there a recommended pipeline to follow? (e.g., load in trials individually, do separate filtering computations, then bring it all together to compute an inverse weight, apply weights to trials separately again, etc).
- BTi_UCSF support? (No)
- Can all data formats be read in as single?  
   _ CTF can, not sure with other formats. (file bug if not true for all formats)
  _ Would help if could be done at line ''data.trial = cutdat;'' in ft_preprocessing. \* write a subfunction ft_single that loops over trials and singles each
- ft_chantype(data.label) 'unknown' in test case for neuromag.
- Issue of clearing a data variable in MATLAB but it still takes up memory (with FT but not with NM).

## 3) Forward modelling

- ft_prepare_localspheres should not call 'clf' and 'cla' as this will mess with the Nutmeg figures. Can it instead call: hfig=figure; and then use hfig handle for plotting?
- ft_volumesegment sufficient (which calls SPM), or prefer other software/method? \* Can't do 'skull' yet.

## 4) NM ideas missing from FT

- nut*filter2:  
   * 'firls' (rather than fir1) filter
  * demean time-domain filtering (in ft_preproc*\*filter), do filter, then add mean back if it was non-zero. (file bug)
- nut_results_viewer
- ft_sourceanalysis allow for multiple time and multiple frequency windows? (regardless of whether LCMV, DICS, or covariances from wavelet transform)
- nut_beamforming_gui
- rumour has it that some people prefer the interactive fiducial selection in NM over FT.
- simplified pipeline for OpenMEEG with BrainVisa segmentations (Sarang to write wiki on BrainVisa use, then OM creates BEM, then import to MATLAB
- single precision used as long as double not needed (e.g., initial loading single but covariance computation double)
- how does FT reduce/display data computed with vector inverse method and therefore the source data has 3 components per voxel?
  _ Specifically, can the s_perp (1 or 2 extra components not of primary direction) be displayed or further manipulated (e.g., in statistics)?
  _ How is s_perp computed 'on the fly' after weights and/or leadfield not present anymore? \* (see email correspondence with Sarang called '3-dim orientation' in 2008)
- option of when in pipeline to normalise leadfield (specific to scalar LCMV)
- Wilcoxon ranksum test in NM: uses single trial info per time-freq bin on the fly to compute Z/p values, but then only saves these averages, not save out single-trial info for each time-freq bin (assuming 20000 voxels, 100 time, 10 freq, that would be too large!)
- weight normalisation? (rather than leadfield norm)? (could be better for EEG data, whereas leadfield norm better for MEG...just hearsay at the moment)

### 4a) overlap/comparison of functional connectivity metrics between NM and FT

- [Nutmeg page comparison of FC metrics and options in both NM and FT](http://nutmeg.berkeley.edu/index.php?title=Comparison_of_connectivity_options) (especially Adrian's FCM toolbox)

## 5) FT ideas missing from NM

1.  NM directly call FT artifact reject, databrowser, topoplots, etc. Remove this from nut_beamforming_gui
2.  NM can call ft_freqanalysis and ft_sourceanalysis(DICS)
3.  How are continuous head-tracking coils dealt with? Ideally separate leadfield per trial?
4.  Units setting (default should be fT for MEG not T to avoid numerical issues)

## 7) Changes to FT for compatibility with NM

- any function/tool that plots should 'play nice' with Nutmeg figures concurrently open \* Specifically, can FT plotting tools call 'figure' prior to the plot, to avoid plotting over an existing open figure (e.g., Nutmeg GUI figures)

## 8) Conversion functions

The conversion from FieldTrip to NUTMEG is done with the following functions inside NUTMEG sv
Please see: http://nutmeg.berkeley.edu/index.php?title=Reading_FieldTrip_processed_data

- nut_ft2nuts
- nut_ft2beam
- nut_ftgrid2nutsLpvox
- nut_ftmriN2coreg.m

The conversion from NUTMEG to FieldTrip is done with the following functions inside FieldTrip sv

- nutmegBeam2fieldtripSource
- nutmegNuts2fieldtrip

## 9) Examples of why/how to switch between toolboxes

### 9.1 Load data not supported by NM (e.g., Yokogawa), then do source-loc in NM

### 9.2 Preprocess data in FT (e.g., ft_rejectvisual) then do source-loc in NM

### 9.3 ft_freqanalysis and DICS in FT, then view results in NM

    nuts=load('jz_alldsallstim5s_both.mat');
    [raw,grid,mri]=nutmegNuts2fieldtrip(nuts);
    raw.vol.r=9*size(raw.vol.o);

    cfg=[];
    cfg.method='mtmconvol';
    cfg.output='powandcsd';
    cfg.keeptrials='yes';
    cfg.foi=18;
    cfg.taper='hanning';
    cfg.t_ftimwin=7./cfg.foi;
    cfg.toi=0.3;
    freq18=ft_freqanalysis(cfg, raw);

    cfg=[];
    cfg.method='dics';
    cfg.grid=grid;
    cfg.headmodel=raw.vol;
    cfg.grad=raw.grad;
    cfg.keepfilter='yes';
    cfg.latency=.1;
    cfg.frequency=18;
    cfg.rawtrial='no';
    source18=ft_sourceanalysis(cfg, freq18);

    filter=source18.avg.filter;
    clear source18
    cfg=[];
    cfg.method='dics';
    cfg.grid=grid;
    cfg.sourcemodel.filter=filter;
    cfg.headmodel=raw.vol;
    cfg.grad=raw.grad;
    cfg.keepfilter='no';
    cfg.latency=.3;
    cfg.frequency=18;
    cfg.rawtrial='yes';
    source18=ft_sourceanalysis(cfg, freq18);

    fiducials=double(nuts.coreg.fiducials_mri_mm);
    save('fiducial','-ascii','fiducials');
    flags.avetime=0;flags.mmvoxflag=1;
    beam=nut_ft2beam(source18,[],[],[],flags);
    beam.coreg=nuts.coreg;
    save('s_beam_both_ftDICS.mat','-struct','beam')

### 9.4 Time-freq LCMV in NM, keeptrials (in tfZ), then further stats in ft_sourcestatistics

    tfbf(['nuts_sim.mat'],'actconwindows',2,80,'firlsbp200cn.mat');
    params.keeptrials=1;save('firlsbp200cn.mat,'params,'filt');
    tfZ(['nuts_sim.mat'],'actconwindows',2,80,'firlsbp200cn.mat');
    beam=load('s_beamtf_nuts_sim_firlsbp200cn_SAMcn_2to80Hz_0to713ms_SAM');
    cfg=[];
    cfg.out='trial';
    cfg.keepvol=1;
    source = nutmegBeam2fieldtripSource(cfg,beam);

    cfg=[];
    cfg.method='montecarlo';
    cfg.numrandomization=100;
    cfg.alpha=.05;
    cfg.parameter='pow';
    cfg.statistic   = 'indepsamplesT';
    cfg.correctm='fdr';
    cfg.repmeas='no';
    tmp=[source{1}.trial.pow].^.5;
    for jj=1:size(tmp,2)
     source{1}.trial(jj).pow=1e15*tmp(:,jj); % we want sqrt of power as thing tested.
    end
    cfg.design(1,:)=tmp(570,:)./max(tmp(570,:));
    cfg.design(2,:)=tmp(4261,:)./max(tmp(4261,:));
    cfg.design(3,:)=tmp(2363,:)./max(tmp(2363,:));
    cfg.design(4,:)=tmp(2075,:)./max(tmp(2075,:));
    cfg.design(5,:)=ones(1,size(tmp,2));
    cfg.ivar=1:5;
    stat=ft_sourcestatistics(cfg,source{1});
