---
title: ft_colormap
---
```plaintext
 FT_COLORMAP is a wrapper function with the same usage as the normal COLORMAP
 function, but it also knows about the colormaps from BREWERMAP and some colormaps
 from MATPLOTLIB.

 Use as
   ft_colormap(name)
   ft_colormap(name, n)
   ft_colormap(handle, name)
   ft_colormap(handle, name, n)

 The name is a string that specifies the colormap (see below). The optional handle
 can be used to specify the current figure (which is the default, see GCF) or the
 current axes (see GCA). The optional parameter n determines the number of steps or
 unique colors in the map (by default 64).

 The colormaps from MATLAB include 'parula', 'jet', 'hsv', 'hot', 'cool', 'spring',
 'summer', 'autumn', 'winter', 'gray', 'bone', 'copper', 'pink', 'lines',
 'colorcube', 'prism', and 'flag'.

 The colormaps from MATPLOTLIB include 'cividis', 'inferno', 'magma', 'plasma',
 'tab10', 'tab20', 'tab20b', 'tab20c', 'twilight', and 'viridis'.

 The colormaps from CMOCEAN include 'thermal', 'haline', 'solar', 'ice', 'oxy',
 'deep', 'dense' 'algae', 'matter', 'turbid', 'speed', 'amp', 'tempo', 'rain', 
 'delta', 'curl', 'diff', 'tarn', 'phase', and 'topo'. To reverse these
 colormaps, specify them with minus sign in front, e.g. '-topo'

 The colormaps from BREWERMAP can be specified as a string, e.g. 'RdBu' or with an
 asterisk (e.g. '*RdBu' to reverse the colormap, like '*RdBu'. See BREWERMAP for more 
 information, or execute the interactive BREWERMAP_VIEW function to see them in detail.

 See also COLORMAP, COLORMAPEDITOR, BREWERMAP, MATPLOTLIB, CMOCEAN
```
