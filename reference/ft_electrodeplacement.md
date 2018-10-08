---
layout: default
---

##  FT_ELECTRODEPLACEMENT

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_electrodeplacement".

`<html>``<pre>`
    `<a href=/reference/ft_electrodeplacement>``<font color=green>`FT_ELECTRODEPLACEMENT`</font>``</a>` allows manual placement of electrodes on a MRI scan, CT scan
    or on a triangulated surface of the head. This function supports different methods.
 
    VOLUME - Navigate an orthographic display of a volume (e.g. CT or MRI scan), and
    assign an electrode label to the current crosshair location by clicking on a label
    in the eletrode list. You can undo the selection by clicking on the same label
    again. The electrode labels shown in the list can be prespecified using cfg.channel
    when calling ft_electrodeplacement. The zoom slider allows zooming in at the
    location of the crosshair. The intensity sliders allow thresholding the image's low
    and high values. The magnet feature transports the crosshair to the nearest peak
    intensity voxel, within a certain voxel radius of the selected location. The labels
    feature displays the labels of the selected electrodes within the orthoplot. The
    global feature allows toggling the view between all and near-crosshair
    markers. The scan feature allows toggling between scans when another scan
    is given as input.
 
    HEADSHAPE - Navigate a triangulated scalp (for EEG) or brain (for ECoG) surface,
    and assign an electrode location by clicking on the surface. The electrode is
    placed on the triangulation itself.
 
    1020 - Starting from a triangulated scalp surface and the nasion, inion, left and
    right pre-auricular points, this automatically constructs and follows contours over
    the surface according to the 5% system. Electrodes are placed at certain relative
    distances along these countours. This is an extension of the 10-20 standard
    electrode placement system and includes the 20%, 10% and 5% locations. See
    "Oostenveld R, Praamstra P. The five percent electrode system for high-resolution
    EEG and ERP measurements. Clin Neurophysiol. 2001 Apr;112(4):713-9" for details.
 
    Use as
    [elec] = ft_electrodeplacement(cfg, ct)
    [elec] = ft_electrodeplacement(cfg, ct, mri, ..)
    where the input mri should be an anatomical CT or MRI volume, or
    [elec] = ft_electrodeplacement(cfg, headshape)
    where the input headshape should be a surface triangulation.
 
    The configuration can contain the following options
    cfg.method         = string representing the method for placing the electrodes
                         'volume'          interactively locate electrodes on three orthogonal slices of a volumetric MRI or CT scan
                         'headshape'       interactively locate electrodes on a head surface
                         '1020'            automatically locate electrodes on a head surface according to the 10-20 system
 
    The following options apply to the mri method
    cfg.parameter      = string, field in data (default = 'anatomy' if present in data)
    cfg.channel        = Nx1 cell-array with selection of channels (default = {'1' '2' ...})
    cfg.elec           = struct containing previously placed electrodes (this overwrites cfg.channel)
    cfg.clim           = color range of the data (default = [0 1], i.e. the full range)
    cfg.magtype        = string representing the 'magnet' type used for placing the electrodes
                         'peakweighted'    place electrodes at weighted peak intensity voxel (default)
                         'troughweighted'  place electrodes at weighted trough intensity voxel
                         'peak'            place electrodes at peak intensity voxel (default)
                         'trough'          place electrodes at trough intensity voxel
                         'weighted'        place electrodes at center-of-mass
    cfg.magradius      = number representing the radius for the cfg.magtype based search (default = 3)
 
    The following options apply to the 1020 method
    cfg.fiducial.nas   = 1x3 vector with coordinates
    cfg.fiducial.ini   = 1x3 vector with coordinates
    cfg.fiducial.lpa   = 1x3 vector with coordinates
    cfg.fiducial.rpa   = 1x3 vector with coordinates
    cfg.feedback       = string, can be 'yes' or 'no' for detailled feedback (default = 'yes')
 
    See also `<a href=/reference/ft_electroderealign>``<font color=green>`FT_ELECTRODEREALIGN`</font>``</a>`, `<a href=/reference/ft_volumerealign>``<font color=green>`FT_VOLUMEREALIGN`</font>``</a>`, `<a href=/reference/ft_volumesegment>``<font color=green>`FT_VOLUMESEGMENT`</font>``</a>`, `<a href=/reference/ft_prepare_mesh>``<font color=green>`FT_PREPARE_MESH`</font>``</a>`
`</pre>``</html>`

