---
layout: default
---

- Extract the filled volume of the outer skull using morphological operators\\
- Dilate the outer skull to estimate the scalp compartment\\
- Erode the inner skull to estimate the inside of the CSF compartment\\
- Fill all the compartments with a flood fill algorithm\\
- Create a boundary for all the filled volumes with one of [these methods](/#Triangulation methods)\\
- **[only for BEMCP]** Create an additional 4th point for each triangle in each triangulated mesh ('solid angle' BEM method)\\
- Assign the conductivity to each compartment (from literature)\\
- Projection of the electrodes on the triangulated surface/s\\
- Check of the direction of the normals (outwards or inwards)\\
