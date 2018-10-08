---
layout: default
---

##  FT_DATATYPE_HEADMODEL

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_datatype_headmodel".

`<html>``<pre>`
    `<a href=/reference/ft_datatype_headmodel>``<font color=green>`FT_DATATYPE_HEADMODEL`</font>``</a>` describes the FieldTrip MATLAB structure for a volume
    conduction model of the head that can be used for forward computations of
    the EEG potentials or the MEG fields. The volume conduction model represents
    the geometrical and the conductive properties of the head. These determine
    how the secondary (or impressed) currents flow and how these contribute to
    the model potential or field.
 
    A large number of forward solutions for the EEG and MEG are supported
    in FieldTrip, each with its own specification of the MATLAB structure that
    describes the volume conduction model of th ehead. It would be difficult to
    list all the possibilities here. One common feature is that the volume
    conduction model should specify its type, and that preferably it should
    specify the geometrical units in which it is expressed (e.g. mm, cm or m).
 
    An example of an EEG volume conduction model with 4 concentric spheres i
 
    headmodel =
         r: [86 88 94 100]
         c: [0.33 1.00 0.042 0.33]
         o: [0 0 0]
      type: 'concentricspheres'
      unit: 'mm'
 
    An example of an MEG volume conduction model with a single sphere fitted to
    the scalp with its center 4 cm above the line connecting the ears i
 
    headmodel =
         r: [12]
         o: [0 0 4]
      type: 'singlesphere'
      unit: 'cm'
 
    For each of the methods XXX for the volume conduction model, a corresponding
    function FT_HEADMODEL_XXX exists that contains all specific details and
    references to literature that describes the implementation.
 
    Required field
    - type
 
    Optional field
    - unit
 
    Deprecated field
    - inner_skull_surface, source_surface, skin_surface, source, skin
 
    Obsoleted field
    - &lt;none specified&gt;
 
    Revision histor
 
    (2015/latest) Use the field name "pos" instead of "pnt" for vertex positions.
 
    (2014) All numeric values are represented in double precision.
 
    (2013) Always use the field "cond" for conductivity.
 
    (2012) Use consistent names for the volume conductor type in the structure, the
    documentation and for the actual implementation, e.g. bem_openmeeg -&gt; openmeeg,
    fem_simbio -&gt; simbio, concentric -&gt; concentricspheres. Deprecated the fields
    that indicate the index of the innermost and outermost surfaces.
 
    See also `<a href=/reference/ft_datatype>``<font color=green>`FT_DATATYPE`</font>``</a>`, `<a href=/reference/ft_datatype_comp>``<font color=green>`FT_DATATYPE_COMP`</font>``</a>`, `<a href=/reference/ft_datatype_dip>``<font color=green>`FT_DATATYPE_DIP`</font>``</a>`, `<a href=/reference/ft_datatype_freq>``<font color=green>`FT_DATATYPE_FREQ`</font>``</a>`,
    `<a href=/reference/ft_datatype_mvar>``<font color=green>`FT_DATATYPE_MVAR`</font>``</a>`, `<a href=/reference/ft_datatype_raw>``<font color=green>`FT_DATATYPE_RAW`</font>``</a>`, `<a href=/reference/ft_datatype_source>``<font color=green>`FT_DATATYPE_SOURCE`</font>``</a>`, `<a href=/reference/ft_datatype_spike>``<font color=green>`FT_DATATYPE_SPIKE`</font>``</a>`,
    `<a href=/reference/ft_datatype_timelock>``<font color=green>`FT_DATATYPE_TIMELOCK`</font>``</a>`, `<a href=/reference/ft_datatype_volume>``<font color=green>`FT_DATATYPE_VOLUME`</font>``</a>`
`</pre>``</html>`

