    % remove the trials that have artifacts from the trl
    cfg.trl([2, 5, 6, 8, 9, 10, 12, 39, 43, 46, 49, 52, 58, 84, 102, 107, 114, 115, 116, 119, 121, 123, 126, 127, 128, 133, 137, 143, 144, 147, 149, 158, 181, 229, 230, 233, 241, 243, 245, 250, 254, 260],:) = [];


    % preprocess the data
    cfg.channel   = {'MEG', '-MLP31', '-MLO12'};        % read all MEG channels except MLP31 and MLO12
    cfg.demean    = 'yes';                              % do baseline correction with the complete trial

    data_all = ft_preprocessing(cfg);

These data have been cleaned from artifacts by removing several trials and two channels; see the [visual artifact rejection tutorial](/tutorial/visual_artifact_rejection).
