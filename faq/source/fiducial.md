---
title: How should I specify the fiducials for electrode realignment?
tags: [electrode, eeg, fiducial]
category: faq
redirect_from:
    - /faq/fiducial/
---

Sensor locations are described by the `elec` structure and can contain fewer or more electrodes than channels actually present in the data, e.g., the electrode positions for the EOG or ECG channels might not be represented.

Depending on the system from which the data originates, fiducials are either digitized and represented just like electrodes, or fiducials are represented separately from the electrodes.

In **[ft_electroderealign](/reference/ft_electroderealign)** the fiducials are never obtained from the `elec` structure, but they always have to be explicitly specified in the configuration:

    fid.chanpos       = [nas; lpa; rpa];       % CTF coordinates of the fiducials
    fid.elecpos       = [nas; lpa; rpa];       % just like electrode positions
    fid.label         = {'Nz','LPA','RPA'};    % same labels as in elec
    fid.unit          = 'mm';                  % same units as mri

    cfg               = [];
    cfg.method        = 'fiducial';
    cfg.template      = fid;                   % see above
    cfg.elec          = elec;
    cfg.fiducial      = {'Nz', 'LPA', 'RPA'};  % labels of fiducials in fid and in elec
    elec_aligned      = ft_electroderealign(cfg);

In case fiducials are present in the `elec` structure, they will simply be removed at the time of forward modeling. Just like channels such as “trigger” and “EOG” are removed from the data prior to forward modeling.

See also the related documentation that explains [how electrodes, magnetometers or gradiometers are described](/faq/source/sensors_definition) and that explains [how to report the positions of the fiducial points on the head](/faq/source/fiducials_definition).
