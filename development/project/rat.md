---
title: The rat beamformer
---

{% include /shared/development/warning.md %}

# The rat beamformer

## Introduction

The project deals with the source reconstruction of brain activity recorded by a polyimide grid placed in direct contact with the dura, and thus very close to the gray matter.
The step to generate a correct inverse solution are listed belo

### Creating a model for the rat inner skull

This is done already (George's work, here a part of his email...)

"The volume conductor is an STL file that represents a closed surface of
the inside of the skull. The front area (front of the olfactory bulb)
and the back area (where the spine comes out) are not closed in reality
so I had to close them manually. They are not too large holes and they
are far from where we collect data so I hope this won't interfere with
the model.
The 0,0,0 is the bregma point. I did my best to keep the triangles as isoskeles
as possible.
(...) So I have to take the original extruded object and put it through a
smoothing process that I do by eye. The resulting surface is much closer to
the real bone structure but the splines are not any more fully coincident
with this surface.
(...) I would use the stl file which is a very good overall fit to reality and
forget about the splines.
(...) I wanted in the area of functional interest my Loni atlas pictures to be
as close to the existing Paxinos atlas slices and Paxinos didn't do
every half a millimetre slices."

### Refine the model for the rat inner skull

This involves checking for uniqueness of the vertices and interpolation of the triangles in the area covered by the grid's leads. These functions are partly implemented in the 'surface' branch of FieldTrip <http://code.google.com/p/fieldtrip/source/browse/#svn%2Fbranches%2Fsurface>

Has to be completed and consists of:

- retriangulation of the mesh

  addpath ~/fieldtrip-dev/surface

  cfg = [];
  cfg.checkdoublevertices = 'yes';
  cfg.convert = 'yes';
  newshape = ft_surfacecheck(cfg,shape);

- interpolation of the triangles
- elastic repositioning (to create a regular grid triangles spacing)

Look at the Gram matrix of the leadfields to check for regularity, by looking at the sorted eigenvalues.

### Use the geometrical model to create a 'vol' structure

FieldTrip typically generated a volume conductor structure when dealing with Electrostatics/Magnetostatics forward solutions.
Here is the logi

    shape = ft_read_headshape('rat_dura','format','STL');
    cfg = [];
    cfg.method = 'dipoli';
    vol = ft_prepare_headmodel(cfg,shape);

where 'shape' is a structure defining the boundary for the Boundary Element model to be used in the next step. (shape.tri is the vertex connectivity for each triangle element, shape.pnt are all the vertices, a M points X 3 matrix).

### Use the 'vol' structure to create the leadfields

The electrodes are also given as a matrix of NX3 elements. They have to be put in a FieldTrip 'sensor' structure (see ). Given the electrodes and the volume conductor we are already able to generate the forward solution by means of the general purpose function 'ft_prepare_leadfield'.

    % check for uniqueness of triangles and remove the nearest ones...

    % initialize the elec structure
    elec = [];
    elec.chanpos = elecmat;
    elec.elecpos = elecmat;
    for i=1:size(elecmat,1)
    elec.label{i} = num2str(i);
    end

The real labels are then assigned using the routine ft_apply_montage (a manual operations to be done by the experimenter).
The next step is the calculation of the lead field

    % Option 1. Calculate the lead fields (example with only one point)
    cfg = [];
    cfg.elec = elec;
    cfg.headmodel = vol;
    cfg.sourcemodel.pos = point; % this can be done manually by clicking
    lf = ft_prepare_leadfield(cfg);

    % Option 2. Alternatively use a grid of equally spaced points
    res  =  1; % 1 mm spacing
    xlim = [-8 8];
    ylim = [-15 15];
    zlim = [0 12];

    cfg = [];
    cfg.xgrid  = xlim(1):res:xlim(2);
    cfg.ygrid  = ylim(1):res:ylim(2);
    cfg.zgrid  = zlim(2):res:zlim(1);
    gridd = ft_prepare_sourcemodel(cfg, vol, elec);

    cfg = [];
    cfg.elec = elec;
    cfg.headmodel = vol;
    cfg.grid = gridd;
    lf = ft_prepare_leadfield(cfg);

### Visualize the leadfields

Uses the function ft_plot_topo3d.m

### Solve the inverse problem, finally ...

See [beamformer](/tutorial/source/beamformer), look for 'Scanning the brain volume'
