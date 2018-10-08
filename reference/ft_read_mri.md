---
layout: default
---

##  FT_READ_MRI

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_read_mri".

`<html>``<pre>`
    `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>` reads anatomical and functional MRI data from different file formats.
    The output data is structured in such a way that it is compatible with
    `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`.
 
    Use as
    [mri] = ft_read_mri(filename)
 
    Additional options should be specified in key-value pairs and can be
    'dataformat' = string specifying the file format, determining the low-
                   level reading routine to be used. If no explicit format
                   is given, it is determined automatically from the filename.
 
    The following values apply for the dataformat
    'afni_head'/'afni_brik'      uses AFNI code
    'analyze_img'/'analyze_hdr'  uses SPM code
    'analyze_old'                uses Darren Webber's code
    'asa_mri'
    'ctf_mri'
    'ctf_mri4'
    'ctf_svl'
    'dicom'                      uses FreeSurfer code
    'dicom_old'                  uses own code
    'freesurfer_mgh'             uses FreeSurfer code
    'freesurfer_mgz'             uses FreeSurfer code
    'matlab'                     assumes a MATLAB *.mat file containing a mri structure according to `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
    'minc'                       uses SPM (&lt;= version SPM5)
    'neuromag_fif'               uses MNE toolbox
    'neuromag_fif_old'           uses meg-pd toolbox
    'nifti'                      uses FreeSurfer code
    'nifti_fsl'                  uses FreeSurfer code
    'nifti_spm'                  uses SPM
    'yokogawa_mri'
 
    The following MRI file formats are supported
    CTF - VSM MedTech (*.svl, *.mri version 4 and 5)
    NIFTi (*.nii) and zipped NIFTi (*.nii.gz)
    Analyze (*.img, *.hdr)
    DICOM (*.dcm, *.ima)
    AFNI (*.head, *.brik)
    FreeSurfer (*.mgz, *.mgh)
    MINC (*.mnc)
    Neuromag - Elekta (*.fif)
    ANT - Advanced Neuro Technology (*.mri)
    Yokogawa (*.mrk, incomplete)
 
    If you have a series of DICOM files, please provide the name of any of the files
    in the series (e.g. the first one). The other files will be found automatically.
 
    The output MRI may have a homogenous transformation matrix that converts
    the coordinates of each voxel (in xgrid/ygrid/zgrid) into head
    coordinates.
 
    See also `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`, `<a href=/reference/ft_write_mri>``<font color=green>`FT_WRITE_MRI`</font>``</a>`, `<a href=/reference/ft_read_data>``<font color=green>`FT_READ_DATA`</font>``</a>`, `<a href=/reference/ft_read_header>``<font color=green>`FT_READ_HEADER`</font>``</a>`, `<a href=/reference/ft_read_event>``<font color=green>`FT_READ_EVENT`</font>``</a>`
`</pre>``</html>`

