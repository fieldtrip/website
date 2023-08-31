---
title: How to deal with the forward model units?
---

{% include /shared/development/warning.md %}

# How to deal with the forward model units?

See also [this small reminder](/development/project/units)

This refers to a bug submitted by V.Litvak, suggesting to give the lead field a default unit, or at least to have a default when the user wants to deal with the absolute values of the leadfields. (See also the [bug #686](http://bugzilla.fieldtriptoolbox.org/show_bug.cgi?id=686))

The discussed issues regard, among others, the following topic

- Units can be estimated by looking at the raw datasets, does the 'units' field have to be attached from the beginning?
- In case of absence of units, they can be recovered by looking at the header
- Default units could be assigned in case of standard datasets (MEG: T or fT, EEG: uV or V)
- The user should dispose of function to convert to the wanted units: i.e. I don't know what the units are but i want my data in microvolts

This topic is important and its implementation impacts both on FT and SPM users, so: BE CAREFUL!

## Some actions to take (Cristiano)

Here is the list of the functions in the module Forward (folders: \_fieldtrip/forward and \_fieldtrip/forward/private) that need the units to be documented in their help (this is necessary also for other modules, like e.g., the fileio module

### \_fieldtrip/forward

**UNITS are required for:**

    ft_compute_leadfield.m
    ft_convert_units.m
    ft_average_sens.m (?)
    ft_headmodel_bem_asa.m
    ft_headmodel_bem_cp.m
    ft_headmodel_concentricspheres.m
    ft_headmodel_dipoli.m
    ft_headmodel_fem_fns.m
    ft_headmodel_fem_simbio.m
    ft_headmodel_halfspace.m
    ft_headmodel_infinite.m
    ft_headmodel_localspheres.m
    ft_headmodel_openmeeg.m
    ft_headmodel_singleshell.m
    ft_headmodel_singlesphere.m
    ft_prepare_vol_sens.m
    ft_transform_headshape.m
    ft_transform_sens.m
    ft_transform_vol.m

**UNITS are NOT required for**

    ft_apply_montage.m
    ft_inside_vol.m
    ft_voltype.m
    ft_senstype.m
    ft_senslabel.m
    ft_sourcedepth.m (?)

### \_fieldtrip/forward/private

**UNITS are required for:**

    ama2vol.m
    eeg_halfspace_medium_leadfield.m
    eeg_halfspace_monopole.m
    eeg_leadfield1.m
    eeg_leadfield4.m
    eeg_leadfield4_prepare.m
    eeg_leadfieldb.m
    halfspace_medium_leadfield.m
    headcoordinates.m
    inf_medium_leadfield.m
    leadfield_fns.m
    leadfield_simbio.m
    leadsphere_all.m
    legs.m
    magnetic_dipole.m
    meg_forward.m
    meg_ini.m
    monopole_leadfield.m
    project_elec.m
    transfer_elec.m

**UNITS are NOT required for:**

    add_mex_source.m
    bounding_mesh.m
    compile_mex_list.m
    elproj.m
    find_innermost_boundary.m
    find_outermost_boundary.m
    fitsphere.m
    ft_hastoolbox.m
    get_dip_halfspace.m
    get_mirror_pos.m
    getsubfield.m
    hasyokogawa.m
    issubfield.m
    istrue.m
    keyval.m
    lmoutr.m
    loadama.m
    match_str.m
    normals.m
    plgndr.m
    ptriproj.m
    solid_angle.m
    triangle4pt.m
    warp_apply.m

**functions which have the .m file somewhere else (src folder?.m)**

    meg_leadfield1.mexa64
    routlm.mexa64
