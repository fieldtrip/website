---
title: nmt_tbxdti_quiver3
---
```
QUIVER3 3-D quiver plot.
   QUIVER3(X,Y,Z,U,V,W) plots velocity vectors as arrows with components
   (u,v,w) at the points (x,y,z).  The matrices X,Y,Z,U,V,W must all be
   the same size and contain the corresponding position and velocity
   components.  QUIVER3 automatically scales the arrows to fit.

   QUIVER3(Z,U,V,W) plots velocity vectors at the equally spaced
   surface points specified by the matrix Z.

   QUIVER3(Z,U,V,W,S) or QUIVER3(X,Y,Z,U,V,W,S) automatically
   scales the arrows to fit and then stretches them by S.
   Use S=0 to plot the arrows without the automatic scaling.

   QUIVER3(...,LINESPEC) uses the plot linestyle specified for
   the velocity vectors.  Any marker in LINESPEC is drawn at the base
   instead of an arrow on the tip.  Use a marker of '.' to specify
   no marker at all.  See PLOT for other possibilities.

   QUIVER3(...,'filled') fills any markers specified.

   H = QUIVER3(...) returns a vector of line handles.

   Example:
       [x,y] = meshgrid(-2:.2:2,-1:.15:1);
       z = x .* exp(-x.^2 - y.^2);
       [u,v,w] = surfnorm(x,y,z);
       quiver3(x,y,z,u,v,w); hold on, surf(x,y,z), hold off

   See also QUIVER, PLOT, PLOT3, SCATTER.

 Courtesy of SPM Tools / tbxDiffusion:
 https://sourceforge.net/projects/spmtools/
```
