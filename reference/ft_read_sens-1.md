---
title: ft_read_sens
---
```
 FT_READ_SENS read sensor positions from various manufacturer specific files. See
 further down for the list of file types that are supported.

 Use as
   grad = ft_read_sens(filename, ...)  % for gradiometers
   elec = ft_read_sens(filename, ...)  % for electrodes

 Additional options should be specified in key-value pairs and can be
   'fileformat'     = string, see the list of supported file formats (the default is determined automatically)
   'senstype'       = string, can be 'eeg', 'meg' or 'nirs', specifies which type of sensors to read from the file (default = 'eeg')
   'coordsys'       = string, 'head' or 'dewar' (default = 'head')
   'coilaccuracy'   = scalar, can be empty or a number (0, 1 or 2) to specify the accuracy (default = [])

 The electrode, gradiometer and optode structures are defined in more detail 
 in FT_DATATYPE_SENS.

 Files from the following acquisition systems and analysis platforms file formats
 are supported.
   asa_elc besa_elp besa_pos besa_sfp yokogawa_ave yokogawa_con yokogawa_raw 4d
   4d_pdf 4d_m4d 4d_xyz ctf_ds ctf_res4 itab_raw itab_mhd netmeg neuromag_fif
   neuromag_mne neuromag_mne_elec neuromag_mne_grad polhemus_fil polhemus_pos
   zebris_sfp spmeeg_mat eeglab_set localite_pos artinis_oxy3 artinis_oxyproj matlab

 See also FT_READ_HEADER, FT_DATATYPE_SENS, FT_PREPARE_VOL_SENS, FT_COMPUTE_LEADFIELD,
```
