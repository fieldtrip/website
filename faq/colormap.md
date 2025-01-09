---
title: Which colormaps are supported?
parent: Plotting and visualization
category: faq
tags: [plotting]
---

# Which colormaps are supported?

FieldTrip includes a helper-function **[ft_colormap](/reference/plotting/ft_colormap)** with which you can select any of the standard [MATLAB](https://nl.mathworks.com/help/matlab/ref/colormap.html) colormaps, but also those of [Matplotlib](https://matplotlib.org), [Brewermap](https://nl.mathworks.com/matlabcentral/fileexchange/45208-colorbrewer-attractive-and-distinctive-colormaps), [CMOcean](https://www.chadagreene.com/CDT/cmocean_documentation.html) and [ColorCET](https://colorcet.com).

You can use **[ft_colormap](/reference/plotting/ft_colormap)** just like you would the standard MATLAB [colormap](https://nl.mathworks.com/help/matlab/ref/colormap.html) function. Furthermore, most plotting functions support the option `cfg.colormap` with which you can specify the desired colormap.

The following sections of code loop through a large number of the available colormaps.

## MATLAB

    cmap = {'parula', 'jet', 'hsv', 'hot', 'cool', 'spring', 'summer', 'autumn', 'winter', 'gray', 'bone', 'copper', 'pink', 'lines', 'colorcube', 'prism', 'flag'};
    figure
    set(gcf, 'Name', 'matlab')
    for i=1:length(cmap)
      subplot(length(cmap),1,i)
      rgb = ft_colormap(cmap{i});
      image(reshape(rgb, [1 64 3]))
      axis off
      text(65, 1, cmap{i})
    end

{% include image src="/assets/img/faq/colormap/matlab.png" width="600" %}

## Matplotlib

    cmap = {'cividis', 'inferno', 'magma', 'plasma', 'tab10', 'tab20', 'tab20b', 'tab20c', 'twilight', 'viridis'};
    figure
    set(gcf, 'Name', 'matplotlib')
    for i=1:length(cmap)
      subplot(length(cmap),1,i)
      rgb = ft_colormap(cmap{i});
      image(reshape(rgb, [1 64 3]))
      axis off
      text(65, 1, cmap{i})
    end

{% include image src="/assets/img/faq/colormap/matplotlib.png" width="600" %}

## Brewermap

    cmap = {'BrBG', 'PRGn', 'PiYG', 'PuOr', 'RdBu', 'RdGy', 'RdYlBu', 'RdYlGn', 'Spectral', 'Accent', 'Dark2', 'Paired', 'Pastel1', 'Pastel2', 'Set1', 'Set2', 'Set3', 'Blues', 'BuGn', 'BuPu', 'GnBu', 'Greens', 'Greys', 'OrRd', 'Oranges', 'PuBu', 'PuBuGn', 'PuRd', 'Purples', 'RdPu', 'Reds', 'YlGn', 'YlGnBu', 'YlOrBr', 'YlOrRd'};
    figure
    set(gcf, 'Name', 'brewermap')
    for i=1:length(cmap)
      subplot(length(cmap),1,i)
      rgb = ft_colormap(cmap{i});
      image(reshape(rgb, [1 64 3]))
      axis off
      text(65, 1, cmap{i})
    end

{% include image src="/assets/img/faq/colormap/brewermap.png" width="600" %}

## CMOcean

    cmap = {'thermal', 'haline', 'solar', 'ice', 'gray', 'oxy', 'deep', 'dense', 'algae', 'matter', 'turbid', 'speed', 'amp', 'tempo', 'rain', 'phase', 'topo', 'balance', 'delta', 'curl', 'diff', 'tarn'};
    figure
    set(gcf, 'Name', 'cmocean')
    for i=1:length(cmap)
      subplot(length(cmap),1,i)
      rgb = ft_colormap(cmap{i});
      image(reshape(rgb, [1 64 3]))
      axis off
      text(65, 1, cmap{i})
    end

{% include image src="/assets/img/faq/colormap/cmocean.png" width="600" %}

## ColorCET

    cmap = {'blueternary', 'coolwarm', 'cyclicgrey', 'depth', 'divbjy', 'fire', 'geographic', 'geographic2', 'gouldian', 'gray', 'greenternary', 'grey', 'heat', 'phase2', 'phase4', 'rainbow', 'rainbow2', 'rainbow3', 'rainbow4', 'redternary', 'reducedgrey', 'yellowheat'};
    figure
    set(gcf, 'Name', 'colorcet')
    for i=1:length(cmap)
      subplot(length(cmap),1,i)
      rgb = ft_colormap(cmap{i});
      image(reshape(rgb, [1 64 3]))
      axis off
      text(65, 1, cmap{i})
    end

{% include image src="/assets/img/faq/colormap/colorcet.png" width="600" %}

## Cyclic colormaps for phase plots

To plot phase color-coded, you need a colormap that starts and ends at the same color. Some of the colormaps that can be used are `hsv`, `phase`, `phase2`, `phase4`, and `cyclicgrey`. You can check these yourself using the following code.

    % construct linearly increasing angles that wrap twice
    a = [linspace(-pi, pi) linspace(-pi, pi) linspace(-pi, pi)]

    figure
    plot(a)

    figure
    imagesc(a)
    ft_colormap phase
