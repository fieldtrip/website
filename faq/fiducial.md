---
layout: default
tags: faq eeg fiducial
---

##  How should I specify the fiducials for electrode realignment?

Sensor locations are described by the elec structure and it can contain fewer or more channels that present in the data. Depending on the system we use, fiducials are digitized and represented just like electrodes, and in other systems the fiducials are represented separately from the sensors.

In **[ft_electroderealign](/reference/ft_electroderealign)** the fiducials are never obtained from the elec structure, but they always have to be explicitly specified in the cf

	fid.chanpos       = [nas; lpa; rpa];       % ctf-coordinates of fiducials
	fid.elecpos       = [nas; lpa; rpa];       % Nx3, where N includes the fiducials
	fid.label         = {'Nz','LPA','RPA'};    % same labels as in elec
	fid.unit          = 'mm';                  % same units as mri

	cfg               = [];
	cfg.method        = 'fiducial';            
	cfg.template      = fid;                   % see above
	cfg.elec          = elec;
	cfg.fiducial      = {'Nz', 'LPA', 'RPA'};  % labels of fiducials in fid and in elec
	elec_aligned      = ft_electroderealign(cfg);

In case fiducials are present in the elec structure, they will simply be removed at the time of forward modelling. Just like channels such as “trigger” and “EOG” are removed from the data prior to forward modelling.

See also the FAQ about [how are electrodes, magnetometers or gradiometers described?](/how_are_electrodes_magnetometers_or_gradiometers_described).
