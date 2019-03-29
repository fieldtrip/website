---
title: ft_realtime_headlocalizer
---
```
 FT_REALTIME_HEADLOCALIZER is a real-time application for online visualization of
 the head position for the CTF275 and the Elekta/Neuromag systems. This uses the
 continuous head localization (in CTF terminology, i.e. CHL) or position indicator
 (in Elekta terminology, i.e. cHPI) information.

 Repositioning the subject to a previous recording session can be done by specifying
 the previous dataset as cfg.template = 'subject01xxx.ds', or by pointing to a text
 file created during a previous recording; e.g. cfg.template = '29-Apr-2013-xxx.txt'.
 The latter textfile is written automatically to disk with each 'Update' buttonpress.

 The online visualization shows the displacement of the head relative to the start
 of the recording. The timepoint (i.e. position) relative to which the displacement
 is shown can be updated can be achieved by marking the HPI at an arbitrary moment
 by clicking the 'Update' button. This allows for repositioning within a recording
 session. Black unfilled markers should appear which indicate the positions of the
 coils at the moment of buttonpress. Distance to these marked positions then become
 colorcoded, i.e. green, orange, or red.

 Use as
   ft_realtime_headlocalizer(cfg)
 with the following configuration options
   cfg.dataset         = string, name or location of a dataset/buffer (default = 'buffer://odin:1972')
   cfg.template        = string, name of a template dataset for between-session repositioning (default = [])
   cfg.bufferdata      = whether to start on the 'first or 'last' data that is available (default = 'last')
   cfg.xlim            = [min max], range in cm to plot (default = [-15 15])
   cfg.ylim            = [min max], range in cm to plot (default = [-15 15])
   cfg.zlim            = [min max], range in cm to plot (default is automatic)
   cfg.blocksize       = number, size of the blocks/chuncks that are processed (default = 1 second)
   cfg.accuracy_green  = distance from fiducial coordinate; green when within limits (default = 0.15 cm)
   cfg.accuracy_orange = orange when within limits, red when out (default = 0.3 cm)
   cfg.dewar           = filename or mesh, description of the dewar shape (default is automatic)
   cfg.polhemus        = filename or mesh, description of the head shape recorded with the Polhemus (default is automatic)
   cfg.headshape       = filename or mesh, description of the head shape recorded with the Structure Sensor

 The following options only apply to data from the Elekta/Neuromag system
   cfg.headmovement    = string, name or location of the .pos file created by MaxFilter which describes the location of the head relative to the dewar
   cfg.coilfreq        = single number in Hz or list of numbers (default = [293, 307, 314, 321, 328])

 This method is described in Stolk A, Todorovic A, Schoffelen JM, Oostenveld R.
 "Online and offline tools for head movement compensation in MEG."
 Neuroimage. 2013 Mar;68:39-48. doi: 10.1016/j.neuroimage.2012.11.047.
```
