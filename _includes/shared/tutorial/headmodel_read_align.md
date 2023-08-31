### Reading in the anatomical data

Before starting with FieldTrip, it is important that you set up your [MATLAB path](/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

    cd <path_to_fieldtrip>
    ft_defaults

Then, you can read in the anatomical MRI data.

    mri = ft_read_mri('Subject01.mri');

    save mri mri

    disp(mri)
              dim: [256 256 256]
          anatomy: [256x256x256 int16]
              hdr: [1x1 struct]
        transform: [4x4 double]
              fid: [1x1 struct]
              unit: 'mm'
          coordsys: 'ctf'

The structure of the `mri` variable contains the following fields:

-   `dim` gives information on the size (i.e. the number of voxels) of the anatomical volume into each direction
-   `anatomy` is a matrix (with the size and number of dimensions specified in `dim`) that contains the anatomical information
-   `hdr` contains the detailed header information from the original file, it contents vary, depending on the file format
-   `transform` is a homogenous [transformation matrix](/faq/homogenous) that allows expressing the voxel positions (in the field `anatomy`) in a certain coordinate system
-   `fid` is an optional structure with fiducial information, this will in general not be present
-   `coordsys` specifies the coordinate system
-   `unit` specifies the units of distance

You can see that in the data we just read in the `coordsys` specifies that it is already aligned to the [CTF coordinate system](/faq/coordsys#details-of-the-ctf-coordinate-system). This MRI was not read from the original DICOM images, but was in the past already processed using the CTF MRIConverter tool. We will get back to this in the next section.

We can check the overall quality of the MRI image using **[ft_sourceplot](/reference/ft_sourceplot)**, which allows us to browse through the whole volume.

    cfg = [];
    cfg.method = 'ortho';
    ft_sourceplot(cfg, mri)

In case your MRI appears [upside down](/faq/my_mri_is_upside_down_is_this_a_problem), don't worry. This is common and we will address it in the next section.

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure2.png" width="600" %}

_Figure; Using ft_sourceplot to asses the MRI quality_

Things to pay attention to when judging the quality of the MRI are

- is the MRI image of good quality overall?
- is the coverage complete, including the tip of the nose, back and top of the head and the ears? Complete coverage is especially important for EEG, as the headmodel includes the scalp.
- is the MRI contrast homogenous over the whole volume? If not, consider **[ft_volumebiascorrect](/reference/ft_volumebiascorrect)**.
- do you see the fiducials that you expect, such as vitamine-E capsules? In this case there are [earmold markers](/faq/how_are_the_lpa_and_rpa_points_defined/#the-lparpa-in-the-donders-meg-and-mri-labs) along the ear canals, and a marker behind the right ear (for a left/right check).
- is the part of the MRI outside the head (i.e., the air) uniform and black? If not, you might be able to clean it up with  **[ft_defacevolume](/reference/ft_defacevolume)**.
- are the anatomical landmarks at the expected coordinates? In this case the nasion is at (116,0,0) mm, the left ear at (0,72,0) mm, the right ear at (0,-71,0) mm, in line with the CTF convention. If not, you will have to realign the MRI to the desired coordinate system (see next section).

### Align the MRI to the head coordinate system

The EEG head model needs to be expressed in the same coordinate system as the electrodes and the source model. It is not really relevant which specific coordinate system is used, as long as all are consistently [aligned](/faq/how_to_coregister_an_anatomical_mri_with_the_gradiometer_or_electrode_positions).

Using **[ft_sourceplot](/reference/ft_sourceplot)** we can check the orientation of the axes and the position of the origin by looking at the numbers taht are printed on screen. Alternatively, we can make a 3D image with **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)**. In the command window it will print that the positive x-axis is pointing towards "anterior", the positive y-axis is pointing towards the "left" and the positive z-axis is pointing towards "superior", in line with the CTF convention. You can also see this in the figure, which has the x-axis (red), y-axis (green) and z-axis (blue) pointing in these three directions of the head. The figure also reveals that the y-axis passes through both ears, consistent with the [convention](/faq/how_are_the_lpa_and_rpa_points_defined/#the-lparpa-in-the-donders-meg-and-mri-labs) at the Donders Centre for Cognitive Neuroimaging (DCCN).

    ft_determine_coordsys(mri)
    % rotate the anatomical MRI around and pay attention to the labels along the axes
    % press "n" and "return" in the command window

{% include image src="/assets/img/tutorial/headmodel_eeg_bem/figure3.png" width="600" %}

_Figure; Determine the coordinate system in which the original MRI is expressed_

You might read your anatomical MRI data from DICOM files, from a NIFTI file, or [other formats](/faq/dataformat), with data that is possibly defined in [a different coordinate system](/faq/coordsys). In that case it may not give information on the coordinate system in which the anatomical data is expressed. You can check and update the coordinate-system with the **[ft_determine_coordsys](/reference/utilities/ft_determine_coordsys)** function by specifying in which direction eax axis points and where the origin is relative to the head.

In general following the reading of the MRI, we use **[ft_volumerealign](/reference/ft_volumerealign)** to align the anatomical MRI to the desired coordinate system. For the CTF coordinate system - as for most coordinate systems used in EEG and MEG - you have to specify the anatomical landmarks (LPA, RPA and nasion). Knowing the voxel indices of these landmarks allows the MRI to be translated and rotated such that the axes of the coordinate systems pass through these landmarks. Following the coregistration or realignment of the MRI, the output of any later processing step on the MRI (reslicing, segmentation, mesh, headmodel) will be expressed in the same coordinate system. Once all anatomical processing of the MRI is done, you can also align the electrodes to the same anatomical landmarks and/or you can fit the electrodes interactively on the scalp surface of your head model.

In this specific case the anatomical MRI is already aligned to the CTF coordinate system. Therefore, we do not need to align the anatomical MRI to any other convention. But if needed, we could have used the previous **[ft_sourceplot](/reference/ft_sourceplot)** step to identify and write down the voxel indices of the nasion, LPA and RPA.

Using the fiducial locations (in voxels) written down in the previous step, we would do

    cfg = [];
    cfg.method = 'fiducial';
    cfg.fiducial.nas = [ 87   60  116];
    cfg.fiducial.lpa = [ 29  145  155];
    cfg.fiducial.rpa = [144  142  158];
    cfg.coordsys = 'ctf'; % the desired coordinate system
    mri_realigned = ft_volumerealign(cfg, mri)

    save mri_realigned mri_realigned

If we did not pay attention to the anatomical landmarks when looking at **[ft_sourceplot](/reference/ft_sourceplot)**, we could also use **[ft_volumerealign](/reference/ft_volumerealign)** to find them.

    cfg = [];
    cfg.method = 'interactive'
    cfg.coordsys = 'ctf'; % the desired coordinate system
    mri_realigned = ft_volumerealign(cfg, mri)

Identifying the nasion is easy. However, it is difficult, if not impossible, to visually distinguish the left and right side from the anatomical MRI. That is why at the DCCN (where this scan was made) we _always_ include a vitamine-E capsule at the right side of the head. Sometimes the vitamine-E capsule is taped on the right mastoid, sometimes it is taped into the right earshell of the protective headphones. To determine the rpa in this specific MRI, you first search for the vitamine-E capsule and then search for the fiducial that marks the right ear canal. Once the rpa been determined, you can move on to the lpa. Other labs might use vitamine-E capsules at the anatomical landmarks themselves, or might not use any fiducials, so please update your own coregistration procedure accordingly.
