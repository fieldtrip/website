---
layout: default
---

##  FT_VOLUMELOOKUP

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_volumelookup".

`<html>``<pre>`
    `<a href=/reference/ft_volumelookup>``<font color=green>`FT_VOLUMELOOKUP`</font>``</a>` can be used in to combine an anatomical or functional
    atlas with the source reconstruction results. You can use it for forward
    and reverse lookup.
 
    Given the region of interest (ROI) as anatomical or functional label, it
    looks up the locations and creates a mask (as a binary volume) based on
    the label. Given the ROI as point in the brain, it creates a sphere or
    box around that point. In these two case the function is to be used a
    mask = ft_volumelookup(cfg, volume)
 
    Given a binary volume that indicates a ROI or a point of interest (POI),
    it looks up the corresponding anatomical or functional labels from the
    atlas. In this case the function is to be used a
     labels = ft_volumelookup(cfg, volume)
 
    In both cases the input volume can b
    mri    is the output of `<a href=/reference/ft_read_mri>``<font color=green>`FT_READ_MRI`</font>``</a>` source is the output of `<a href=/reference/ft_sourceanalysis>``<font color=green>`FT_SOURCEANALYSIS`</font>``</a>`
    stat   is the output of `<a href=/reference/ft_sourcestatistics>``<font color=green>`FT_SOURCESTATISTICS`</font>``</a>`
 
    The configuration options for a mask according to an atla
    cfg.inputcoord          = 'mni' or 'tal', coordinate system of the mri/source/stat
    cfg.atlas               = string, filename of atlas to use, see `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>`
    cfg.roi                 = string or cell-array of strings, ROI from anatomical atlas
 
    The configuration options for a spherical/box mask around a PO
    cfg.roi                 = Nx3 vector, coordinates of the POI
    cfg.sphere              = radius of each sphere in cm/mm dep on unit of input
    cfg.box                 = Nx3 vector, size of each box in cm/mm dep on unit of input
    cfg.round2nearestvoxel  = 'yes' or 'no' (default = 'no'), voxel closest to point of interest is calculated
                              and box/sphere is centered around coordinates of that voxel
 
    The configuration options for labels from a mas
    cfg.inputcoord          = 'mni' or 'tal', coordinate system of the mri/source/stat
    cfg.atlas               = string, filename of atlas to use, see `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>`
    cfg.maskparameter       = string, field in volume to be looked up, data in field should be logical
    cfg.minqueryrange       = number, should be odd and &lt;= to maxqueryrange (default = 1)
    cfg.maxqueryrange       = number, should be odd and &gt;= to minqueryrange (default = 1)
 
    The configuration options for labels around PO
    cfg.output              = 'single' always outputs one label; if several POI are provided, they are considered together as describing a ROI (default)
                              'multiple' outputs one label per POI (e.g., choose to get labels for different electrodes)
    cfg.roi                 = Nx3 vector, coordinates of the POI
    cfg.inputcoord          = 'mni' or 'tal', coordinate system of the mri/source/stat
    cfg.atlas               = string, filename of atlas to use, see `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>`
    cfg.minqueryrange       = number, should be odd and &lt;= to maxqueryrange (default = 1)
    cfg.maxqueryrange       = number, should be odd and &gt;= to minqueryrange (default = 1)
    cfg.querymethod         = 'sphere' searches voxels around the ROI in a sphere (default)
                            = 'cube' searches voxels around the ROI in a cube
    cfg.round2nearestvoxel  = 'yes' or 'no', voxel closest to POI is calculated (default = 'yes')
 
    The label output has a field "names", a field "count" and a field "usedqueryrange".
    To get a list of areas of the given mask you can do for instanc
       [tmp ind] = sort(labels.count,1,'descend');
       sel = find(tmp);
       for j = 1:length(sel)
         found_areas{j,1} = [num2str(labels.count(ind(j))) ': ' labels.name{ind(j)}];
       end
    In the "found_areas" variable you can then see how many times which labels are
    found. Note that in the AFNI brick one location can have 2 labels.
 
    Dependent on the input coordinates and the coordinates of the atlas, the
    input MRI is transformed betweem MNI and Talairach-Tournoux coordinates
    See http://www.mrc-cbu.cam.ac.uk/Imaging/Common/mnispace.shtml for more details.
 
    See http://www.fieldtriptoolbox.org/template/atlas for a list of templates and
    atlasses that are included in the FieldTrip release.
 
    See also `<a href=/reference/ft_read_atlas>``<font color=green>`FT_READ_ATLAS`</font>``</a>`, `<a href=/reference/ft_sourceplot>``<font color=green>`FT_SOURCEPLOT`</font>``</a>`
`</pre>``</html>`

