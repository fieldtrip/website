---
title: Restructure the directory layout
---

{% include /shared/development/warning.md %}


The directory layout has been changed per 23 September 2008. The new layout makes the FieldTrip modules explicit (i.e. fileio, forwinv, preproc) and allows external toolboxes to be included in the release/zipfile without confusion about the different licenses and/or contributors to the external code.

The new layout also makes the use of templates (for layout and cortical surfaces), statfuns and trialfuns explicit by putting them in their own directories.

    fieldtrip/preprocessing.m
    fieldtrip/freqanalysis.m
    fieldtrip/private/…

    fieldtrip/fileio/read_header.m
    fieldtrip/fileio/read_data.m
    fieldtrip/fileio/…
    fieldtrip/fileio/private/…

    fieldtrip/forwinv/compute_leadfield.m
    fieldtrip/forwinv/…
    fieldtrip/forwinv/private/…

    fieldtrip/external/toolbox1/…
    fieldtrip/external/toolbox2/…
    fieldtrip/external/toolbox3/…

All changes have been made with backward compatibility in mind. This is achieved through "hastoolbox" and the use of a "fixpath" module, where for the time being most code that used to be in fieldtrip/private still can be found. Furthermore, there is a "ft_defaults" script which is now included in all FieldTrip main functions.

## What still needs to be done is

- remove files from private that are unused

- remove files from fixpath that are unused

- resolve the dependencies on the remaining functions in fixpath and try to fix the dependency structure

## Known problems that should be fixed

using the MATLAB "depfun" function

    FUNCTION dipolefitting
    /home/common/matlab/fieldtrip/fixpath/rv.m

    FUNCTION megrealign
    /home/common/matlab/fieldtrip/fixpath/rv.m

    FUNCTION headmodelplot
    /home/common/matlab/fieldtrip/fixpath/headsurface.m
    /home/common/matlab/fieldtrip/fixpath/project_elec.m

    FUNCTION bciagent
    /home/common/matlab/fieldtrip/fixpath/appendevent.m

    FUNCTION prepare_layout
    /home/common/matlab/fieldtrip/fixpath/filetype.m

    FUNCTION volumenormalise
    /home/common/matlab/fieldtrip/fixpath/filetype.m

    FUNCTION megplanar
    /home/common/matlab/fieldtrip/fixpath/headsurface.m

    FUNCTION read_spike
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/read_plexon_nex.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_nse.m
    /home/common/matlab/fieldtrip/fixpath/read_plexon_plx.m
    /home/common/matlab/fieldtrip/fixpath/timestamp_plexon.m
    /home/common/matlab/fieldtrip/fixpath/LoadSpikes.m
    /home/common/matlab/fieldtrip/fixpath/ReadHeader.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_nst.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_ntt.m

    FUNCTION scalpcurrentdensity
    /home/common/matlab/fieldtrip/fixpath/lapcal.m
    /home/common/matlab/fieldtrip/fixpath/splint.m

    FUNCTION volumewrite
    /home/common/matlab/fieldtrip/fixpath/avw_hdr_make.m
    /home/common/matlab/fieldtrip/fixpath/avw_img_write.m

    FUNCTION headmovement
    /home/common/matlab/fieldtrip/fixpath/ctf2grad.m
    /home/common/matlab/fieldtrip/fixpath/read_ctf_hc.m

    FUNCTION read_sens
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/read_asa_elc.m
    /home/common/matlab/fieldtrip/fixpath/read_brainvision_pos.m

    FUNCTION write_data
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/filetype_check_uri.m
    /home/common/matlab/fieldtrip/fixpath/read_plexon_nex.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_ncs.m
    /home/common/matlab/fieldtrip/fixpath/write_plexon_nex.m
    /home/common/matlab/fieldtrip/fixpath/write_brainvision_eeg.m
    /home/common/matlab/fieldtrip/fixpath/write_neuralynx_ncs.m

    FUNCTION write_fcdc_spike
    /home/common/matlab/fieldtrip/fixpath/read_plexon_nex.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_nse.m
    /home/common/matlab/fieldtrip/fixpath/write_plexon_nex.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_nts.m
    /home/common/matlab/fieldtrip/fixpath/write_neuralynx_nse.m
    /home/common/matlab/fieldtrip/fixpath/write_neuralynx_nts.m

    FUNCTION read_mri
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/avw_img_read.m
    /home/common/matlab/fieldtrip/fixpath/read_asa_mri.m
    /home/common/matlab/fieldtrip/fixpath/read_ctf_mri.m

    FUNCTION read_vol
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/ama2vol.m
    /home/common/matlab/fieldtrip/fixpath/loadama.m
    /home/common/matlab/fieldtrip/fixpath/read_asa_vol.m
    /home/common/matlab/fieldtrip/fixpath/read_ctf_hdm.m

    FUNCTION spikesplitting
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/read_neuralynx_dma.m

    FUNCTION volumesegment
    /home/common/matlab/fieldtrip/fixpath/filetype.m

    FUNCTION artifact_file
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/read_brainvision_marker.m
    /home/common/matlab/fieldtrip/fixpath/read_eep_rej.m

    FUNCTION bciinput
    /home/common/matlab/fieldtrip/fixpath/filetype.m

    FUNCTION prepare_bemmodel
    /home/common/matlab/fieldtrip/fixpath/ama2vol.m
    /home/common/matlab/fieldtrip/fixpath/loadama.m

    FUNCTION channelselection
    /home/common/matlab/fieldtrip/fixpath/senslabel.m

    FUNCTION write_event
    /home/common/matlab/fieldtrip/fixpath/filetype.m
    /home/common/matlab/fieldtrip/fixpath/filetype_check_uri.m
    /home/common/matlab/fieldtrip/fixpath/appendevent.m
    /home/common/matlab/fieldtrip/fixpath/filetype_check_extension.m

    FUNCTION definetrial
    /home/common/matlab/fieldtrip/fixpath/filetype.m

    FUNCTION loreta2fieldtrip
    /home/common/matlab/fieldtrip/fixpath/filetype.m

    FUNCTION spass2fieldtrip
    /home/common/matlab/fieldtrip/fixpath/read_labview_dtlg.m
