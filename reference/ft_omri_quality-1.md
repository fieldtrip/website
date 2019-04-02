---
title: ft_omri_quality
---
```
 FT_OMRI_QUALITY implements an online fMRI quality assurance stack

 Use as
   ft_omri_quality(cfg)
 where cfg is a structure with configuration settings.

 Configuration options are
   cfg.input            = FieldTrip buffer containing raw scans (default='buffer://localhost:1972')
   cfg.numDummy         = how many scans to ignore initially    (default=0)
   cfg.showRawVariation = 1 to show variation in raw scans (default), 0 to show var. in processed scans
   cfg.clipVar          = threshold to clip variation plot with as a fraction of signal magnitude (default=0.2)
   cfg.lambda           = forgetting factor for the variaton plot (default=0.9)
   cfg.serial           = serial port (default = /dev/ttyS0), set [] to disable motion reporting
   cfg.baudrate         = serial port baudrate (default = 19200)
   cfg.maxAbs           = threshold (mm) for absolute motion before 'A' is sent to serial port, default = Inf
   cfg.maxRel           = threshold (mm) for relative motion before 'B' is sent to serial port, default = Inf
```
