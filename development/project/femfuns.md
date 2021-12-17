---
title: Implemention of realistic electrode properties in forward volume conduction models
---

{% include /shared/development/warning.md %}

# Implemention of realistic electrode properties in forward volume conduction models

## Description

In applications like epilepsy and brain-computer interface, electrocorticography electrode grids are often implanted in patients to detect normal and abnormal brain activity. For both applications, there is the need for assessing the sensitivity of current or newly-designed ECoG grids, whether the sensitivity could be improved, and how to eventually optimize the grid. These investigations can be conducted numerically, with adequate and adapted volume conduction models.

Commonly, in such models, electrodes are considered to record the potential in just a single point. However, we have [shown](https://iopscience.iop.org/article/10.1088/1741-2552/abb11d/meta) the importance of explicitly including electrode properties in volume conduction models for accurately interpreting ECoG measurements. To achieve this type of simulation, the Finite Element Method for useful neuroscience simulations ([FEMfuns](https://github.com/meronvermaas/FEMfuns)) was developed, which allows knowledgeable neuroscientists to solve the forward problem in a variety of different geometrical domains, including various types of source models and electrode properties, such as resistive and capacitive materials, and the double layer that exists at the electrode-tissue interface. Here, as part of the project Into the Brain, we will incorporate FEMfuns into FieldTrip.

## Organization of FEMfuns in FieldTrip

FEMfuns is a python based open-source pipeline and will be called externally from FieldTrip. Within FieldTrip, the headmodel and electrode positions are created, after which the forward solution is found using FEMfuns code under the hood. We split incorporating FEMfuns into Fieldtrip in three steps:

- integrate complex meshing routines in FieldTrip
- test on sphere: compute the forward solutions in FieldTrip using a compiled binary of FEMfuns
- test on real dataset: compute forward solution in a realistically shaped head model (test the interaction of forward solutions computed with FEMfuns and pre-processing/source analysis routines implemented in FieldTrip)

{% include image src="/assets/img/development/project/femfuns/workflow.jpg" width="500" %}

The workflow consists of calling many subroutines (comparable to a Russian doll), start-ing within the toolbox FieldTrip. First, a FieldTrip script in MATLAB loads data and calls the routine to compute the forward solution. Via this routine, a shell script is written and executed under the hood. This shell script sets up the required version of Python and associated packages (using Anaconda), passes the volume conduction parameters (e.g., mesh, tissue and electrode type, source model), and launches FEMfuns. Then, FEMfuns runs the forward simulation. Finally, the lead field matrices are imported back into FieldTrip for further analysis, e.g., source reconstruction analysis.

Currently (September 2021), the MATLAB fuctions to add electrodes to an existing finite element head model are available [here](https://github.com/meronvermaas/fieldtrip/tree/femfuns/external/femfuns)

## Running a simulation with FieldTrip and FEMfuns combined
The following section illustrates an example where the FEMfuns pipeline is embedded in FieldTrip. The geometry, electrodes and source-model are created in FieldTrip. These are used in FEMfuns to calculate lead fields by means of FEM with optional properties such as an electrode surface conductance and stimulating electrodes. For the simplest case, a 2-sphere geometry is used with several realistic electrodes on the upper half of the sphere.

Before starting with FieldTrip, it is important that you set up your [MATLAB path](https://www.fieldtriptoolbox.org/faq/should_i_add_fieldtrip_with_all_subdirectories_to_my_matlab_path) properly.

    cd PATH_TO_FIELDTRIP
    ft_defaults

Then surfaces of two spheres can be created using FieldTrip:

    % Create a spherical volume conductor with two spheres of radius 7 and 10 at the origin
    csvol.o = [0, 0,0];
    csvol.r = [7 10];
    cfg = [];
    cfg.numvertices = 1000;
    csbnd = ft_prepare_mesh(cfg, csvol);

Realistic intracranial electrode surfaces are added to the inner sphere (representing the brain) at a few locations on the top half of the sphere.

    %pick a few electrode positions on top of the sphere
    sel = find(csbnd(1).pos(:,3)>0); sel = sel(1:100:end);
    elec = [];
    elec.elecpos = csbnd(1).pos(sel,:);
    for i=1:length(sel)
      elec.label{i} = sprintf('elec%d', i);
    end
    elec.unit = 'cm';
    % update the electrode sets to the latest standards
    elec = ft_datatype_sens(elec);
    
    % combine the brain surface with electrode surfaces and get inner points of the electrodes
    dp_elec = 0.5; %height  of the electrode cylinder
    rad_elec = 0.2; %radius of the electrode cylinder
     [dented_elsurf,elecmarkers] = add_electrodes(csbnd(1), elec.elecpos, rad_elec, dp_elec);
    merged_surfs = add_surf(dented_elsurf,csbnd(2)); %combine with the scalp
    
    %create volumetric tetrahedral mesh
     [tet_node,tet_elem] = s2m(merged_surfs.pos,merged_surfs.tri, 1, 1, 'tetgen', [point_in_surf(csbnd(1));point_in_surf(csbnd(2));elecmarkers]);
    %label the electrode surfaces where they make contact with the brain
    el_faces = label_surf(tet_elem, 3:7, 1);

Currently volumes and surfaces are not combined in FieldTrip mesh structures. This is being integrated at this moment. For now, a FieldTrip mesh structure is created separately including both volume and surface information:

    %Construct the FT mesh structure
    mesh.unit = 'cm';
    mesh.pos = tet_node;
    mesh.tet = tet_elem(:,1:4);
    mesh.tri = el_faces(:,1:3);
    mesh.boundary = el_faces(:,4);
    mesh.boundarylabel = elec.label;
    mesh.tissue = tet_elem(:,5);
    mesh.tissuelabel = [{'brain'}, {'skull'},elec.label(:)'];

Next the FieldTrip sourcemodel is created:

    % construct a vol to create the FT sourcemodel
    vol.pos = mesh.pos;
    vol.tet = mesh.tet;
    vol.tissue = mesh.tissue;
    vol.tissuelabel = mesh.tissuelabel;
    vol.unit = mesh.unit;
    vol.type = 'simbio';
    
    cfg                 = [];
    cfg.resolution      = 5; %in mm
    cfg.headmodel       = vol;
    cfg.inwardshift     = 1; %shifts dipoles away from surfaces
    sourcemodel         = ft_prepare_sourcemodel(cfg);

Finally, the geometry and parameters are used by FEMfuns externally. The resulting leadfield is imported back into matlab after which they can be used by FieldTrip:

    % conductivities for brain, scalp and metal electrodes are set
    conductivities = [0.33 0.01 1e10 1e10 1e10 1e10 1e10];
    lf_rec = femfuns_leadfield(mesh,conductivities,sourcemodel,elec);
    filename = fullfile(tempname, 'femfuns_leadfield');
    ft_headmodel_interpolate(filename, elec, lf_rec, 'smooth', false);

Alternatively, stimulating electrodes can be used:

    % Instead dipole sources, a stimulating and ground electrode is set.
    % For boundary options, look for example here https://github.com/meronvermaas/FEMfuns/blob/master/separability/parameters_discelecins.py
    sourcemodel.inside(:) = false;
    elec.label{1} = ['stim_' elec.label{1}];
    elec.label{2} = ['ground_' elec.label{2}];
    mesh.boundarylabel = elec.label;
    elec.params{1} = {1, 100, 'int'};
    elec.params{2} = {0, 100, 'int'};
    conductivities = [0.33 0.01 0 0 0 0 0];
    lf_stim = femfuns_leadfield(mesh,conductivities,sourcemodel,elec);



This work is supported by a grant from stichting IT projecten ([StITPro](https://stitpro.nl/)).
