---
layout: default
---

##  FT_SENSINTERP_OPENMEEG

Note that this reference documentation is identical to the help that is displayed in MATLAB when you type "help ft_sensinterp_openmeeg".

`<html>``<pre>`
    `<a href=/reference/ft_sensinterp_openmeeg>``<font color=green>`FT_SENSINTERP_OPENMEEG`</font>``</a>` creates a volume conduction model of the
    head using the boundary element method (BEM). This function takes
    as input the triangulated surfaces that describe the boundaries and
    returns as output a volume conduction model which can be used to
    compute leadfields.
 
    This function implements
    Gramfort et al. OpenMEEG: opensource software for quasistatic
    bioelectromagnetics. Biomedical engineering online (2010) vol. 9 (1) pp. 45
    http://www.biomedical-engineering-online.com/content/9/1/45
    doi:10.1186/1475-925X-9-45
    and
    Kybic et al. Generalized head models for MEG/EEG: boundary element method
    beyond nested volumes. Phys. Med. Biol. (2006) vol. 51 pp. 1333-1346
    doi:10.1088/0031-9155/51/5/021
 
    This link with FieldTrip is derived from the OpenMEEG project
    with contributions from Daniel Wong and Sarang Dalal, and uses external
    command-line executables. See http://openmeeg.github.io/
 
    Use as
    headmodel = ft_headmodel_openmeeg(mesh, ...)
 
    Optional input arguments should be specified in key-value pairs and can
    include
    conductivity     = vector, conductivity of each compartment
    tissue           = tissue labels for each compartment
 
    See also `<a href=/reference/ft_headmodel_openmeeg>``<font color=green>`FT_HEADMODEL_OPENMEEG`</font>``</a>`, `<a href=/reference/ft_sysmat_openmeeg>``<font color=green>`FT_SYSMAT_OPENMEEG`</font>``</a>`, `<a href=/reference/ft_prepare_leadfield>``<font color=green>`FT_PREPARE_LEADFIELD`</font>``</a>`
`</pre>``</html>`

