---
title: How can I determine the anatomical label of a source or electrode?
tags: [source]
category: faq
redirect_from:
    - /faq/how_can_i_determine_the_anatomical_label_of_a_source/
    - /faq/label_lookup/
---

## Determine the label of a source that you localized

FieldTrip supports the use of an anatomical atlas to look up the anatomical label of a source that you have localized. Vice versa you can also first look up the location of an anatomical region and subsequently use that in source analysis, e.g., as region of interest for beamforming or as starting point for dipole fitting.

The function **[ft_read_atlas](/reference/fileio/ft_read_atlas)** reads in a specified atlas with coordinates and anatomical labels. It either uses the [AFNI brik file](https://www.google.com/search?q=afni+brik+file+format), or it uses one of the [WFU atlases](http://fmri.wfubmc.edu) (see also https://www.nitrc.org/projects/wfu_pickatlas). The following example code shows a simple demonstration:

    atlas = ft_read_atlas('ROI_MNI_V4.nii');

    cfg              = [];
    cfg.method       = 'ortho';
    cfg.funparameter = 'brick0';
    cfg.funcolormap  = 'jet';
    ft_sourceplot(cfg, atlas)

Atlases can be used in several FieldTrip functions. For instance in the **[ft_sourceplot](/reference/ft_sourceplot)** function if you specify cfg.atlas and cfg.atlascoordinates you can click on a voxel in the interactive mode (cfg.method = 'ortho') and the label of that voxel according to the specified atlas is given.

The most important function for using an atlas is **[ft_volumelookup](/reference/ft_volumelookup)**. It can be used in two approaches.

1. Given the anatomical or functional label, it looks up the locations and creates a mask (as a binary volume) based on the label, or creates a sphere or box around a point of interest.
2. Given a binary volume that indicates a region of interest, it looks up the corresponding anatomical or functional labels from a given atlas.

## Determine the label of an (intracranial) electrode

In the context of intracranial EEG recordings, FieldTrip supports looking up the anatomical or functional labels corresponding to electrodes in a number of atlases, including the AFNI Talairach Tournoux atlas, the AAL atlas, the BrainWeb data set, the JuBrain cytoarchitectonic atlas, the VTPM atlas, the Brainnetome atlas, and the Yeo atlases, in addition to the subject-tailored Desikan-Killiany and Destrieux atlases produced by FreeSurfer (for details of each atlas, see the [template atlas documentation](/template/atlas)). Given that no two electrodes end up in the exact same location across subjects due to inter-individual variability in electrode coverage and brain anatomy, atlases are particularly useful for the systematic combination of neural activity from different subjects in a so-called region of interest (ROI) analysis. With exception of the above FreeSurfer-based atlases, the atlases are in MNI coordinate space and require the electrodes to be spatially normalized (Steps 26 through 27 of the [human iEEG tutorial](/tutorial/intracranial/human_ecog)). First, import an atlas of interest, e.g., the AAL atlas, into the MATLAB workspace.

    [ftver, ftpath] = ft_version;
    atlas = ft_read_atlas([ftpath filesep 'template/atlas/aal/ROI_MNI_V4.nii']);

Next, look up the corresponding anatomical label of an electrode of interest, e.g., electrode LHH1 of the iEEG tutorial dataset, targeting the left hemisphere's hippocampus.

    cfg            = [];
    cfg.roi        = elec_mni_frv.chanpos(match_str(elec_mni_frv.label,'LHH1'),:);
    cfg.atlas      = atlas;
    cfg.inputcoord = 'mni';
    cfg.output     = 'label';
    labels = ft_volumelookup(cfg, atlas);

    [~, indx] = max(labels.count);
    labels.name(indx)
    ans =

    'ParaHippocampal_L'

The function below represents a tool that automatically overlays all channels in an electrode structure with all of the above atlases and stores the resulting anatomical labels in an excel table.

    function generate_electable_v3(filename, varargin)

    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    % GENERATE_ELECTABLE_V3 writes an electrode anatomy and annotation table
    %
    % Use as:
    %   generate_electable(filename, ...)
    % where filename has an .xlsx file extension,
    %
    % and at least one of the following sets of key-value pairs is
    % specified:
    %   elec_mni    = electrode structure, with positions in MNI space
    %
    %   elec_nat    = electrode structure, with positions in native space
    %   fsdir       = string, path to freesurfer directory for the subject
    %                 (e.g., 'SubjectUCI29/freesurfer')
    %
    % Ensure FieldTrip is correcty added to the MATLAB path:
    %   addpath <path to fieldtrip home directory>
    %   ft_defaults
    %
    % On Mac and Linux, the freely available xlwrite plugin is needed,
    % hosted at: http://www.mathworks.com/matlabcentral/fileexchange/38591
    %   xldir       = string, path to xlwrite dir (e.g., 'MATLAB/xlwrite')
    %
    % This function is part of Stolk, Griffin et al., Integrated analysis
    % of anatomical and electrophysiological human intracranial data
    %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

    % get the optional input arguments
    elec_mni        = ft_getopt(varargin, 'elec_mni');
    elec_nat        = ft_getopt(varargin, 'elec_nat');
    fsdir           = ft_getopt(varargin, 'fsdir');
    xldir           = ft_getopt(varargin, 'xldir');

    if isunix % on mac and linux
      % add java-based xlwrite to overcome windows-only xlswrite
      addpath(xldir);
      javaaddpath([xldir '/poi_library/poi-3.8-20120326.jar']);
      javaaddpath([xldir '/poi_library/poi-ooxml-3.8-20120326.jar']);
      javaaddpath([xldir ...
        '/poi_library/poi-ooxml-schemas-3.8-20120326.jar']);
      javaaddpath([xldir '/poi_library/xmlbeans-2.3.0.jar']);
      javaaddpath([xldir '/poi_library/dom4j-1.6.1.jar']);
      javaaddpath([xldir '/poi_library/stax-api-1.0.1.jar']);
    end

    % prepare the atlases and elec structure
    atlas = {};
    name = {};
    elec = [];
    if ~isempty(elec_mni) % mni-based atlases
      [~, ftpath]       = ft_version;
      atlas{end+1}      = ft_read_atlas([ftpath ...
        '/template/atlas/afni/TTatlas+tlrc.HEAD']); % AFNI
      name{end+1}       = 'AFNI';
      atlas{end+1}      = ft_read_atlas([ftpath ...
        '/template/atlas/aal/ROI_MNI_V4.nii']); % AAL
      name{end+1}       = 'AAL';
      brainweb = load([ftpath ...
        '/template/atlas/brainweb/brainweb_discrete.mat']);
      atlas{end+1}      = brainweb.atlas; clear brainweb; % BrainWeb
      name{end+1}       = 'BrainWeb';
      atlas{end+1}      = ft_read_atlas([ftpath ...
        '/template/atlas/spm_anatomy/AllAreas_v18_MPM']); % JuBrain
      name{end+1}       = 'JuBrain';
      load([ftpath '/template/atlas/vtpm/vtpm.mat']);
      atlas{end+1}      = vtpm; % VTPM
      name{end+1}       = 'VTPM';
      atlas{end+1}      = ft_read_atlas([ftpath ... % Brainnetome
        '/template/atlas/brainnetome/BNA_MPM_thr25_1.25mm.nii']);
      name{end+1}       = 'Brainnetome';
      atlas{end+1}      = ft_read_atlas([ftpath ... % Yeo7
       '/template/atlas/yeo/Yeo2011_7Networks_MNI152_FreeSurferConformed1mm_LiberalMask_colin27.nii']);
      name{end+1}       = 'Yeo7';
      atlas{end+1}      = ft_read_atlas([ftpath ... % Yeo17
       '/template/atlas/yeo/Yeo2011_17Networks_MNI152_FreeSurferConformed1mm_LiberalMask_colin27.nii']);
      name{end+1}       = 'Yeo17';
      elec              = elec_mni;
    end
    if ~isempty(elec_nat) && ~isempty(fsdir) % freesurfer-based atlases
      atlas{end+1}      = ft_read_atlas([fsdir ...
        '/mri/aparc+aseg.mgz']); % Desikan-Killiany (+volumetric)
      atlas{end}.coordsys = 'acpc';
      name{end+1}       = 'Desikan-Killiany';
      atlas{end+1}      = ft_read_atlas([fsdir ...
        '/mri/aparc.a2009s+aseg.mgz']); % Destrieux (+volumetric)
      atlas{end}.coordsys = 'acpc';
      name{end+1}       = 'Destrieux';
      if isempty(elec) % elec_mni not present
        elec              = elec_nat;
      else
        if ~isequal(elec_nat.label, elec_mni.label)
          error('inconsistent order or number of channel labels')
        end
      end
      elec.chanpos_fs   = elec_nat.chanpos;
    end

    % generate the table
    table = {'Electrode','Coordinates','Discard','Epileptic', ...
      'Out of Brain','Notes','Loc Meeting',name{:}};

    for a = 1:numel(atlas) % atlas loop

      % search anatomical labels
      cfg               = [];
      if strcmp(name{a}, 'Desikan-Killiany') || ...
          strcmp(name{a}, 'Destrieux') % freesurfer-based atlases
        cfg.roi           = elec.chanpos_fs; % from elec_nat
        cfg.inputcoord    = 'acpc';
      else
        cfg.roi           = elec.chanpos; % from elec_mni
        cfg.inputcoord    = 'mni';
      end
      cfg.atlas         = atlas{a};
      cfg.minqueryrange = 11;
      cfg.maxqueryrange = 11;
      cfg.output        = 'multiple'; % since v2
      labels = ft_volumelookup(cfg, atlas{a});

      for e = 1:numel(elec.label) % electrode loop

        % enter electrode information
        table{e+1,1} = elec.label{e}; % Electrode
        table{e+1,2} = num2str(elec.chanpos(e,:)); % Coordinates
        table{e+1,3} = 0; % Discard
        table{e+1,4} = 0; % Epileptic
        table{e+1,5} = 0; % Out of Brain
        table{e+1,6} = ''; % Notes
        table{e+1,7} = ''; % Localization Meeting

        % enter anatomical labels and lookup stats
        [cnt, idx] = max(labels(e).count);
        voxinr = [1 7 33 99 209 383 697 ...
          1071 1581 2255 3089 4135 5353]; % 1, 3, 5, .., 25 qrange
        nvox = voxinr(cfg.minqueryrange/2+.5); % n vox searchlight
        prob = round((cnt/nvox)*100); % probability
        lab  = char(labels(e).name(idx)); % anatomical label
        if ~isequal(lab, 'no_label_found')
          table{e+1,7+a} = [lab ' (' num2str(prob) '%)']; % label (%)
        else
          table{e+1,7+a} = lab; % no_label_found
        end
        clear cnt idx prob
        fprintf(['>> electrode ' elec.label{e} ': ' lab  ...
          ' (' table{1,7+a} ' atlas) <<\n'])

      end % end of electrode loop
      clear labels
    end % end of atlas loop

    % write table to excel file
    if isunix
      xlwrite(filename, table);
    else
      xlswrite(filename, table);
    end
