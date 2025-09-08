---
title: I am getting strange artifacts in figures that use opacity
tags: [plotting, artifact]
category: faq
redirect_from:
    - /faq/i_am_getting_strange_artifacts_in_figures_that_use_opacity/
    - /faq/opacityrendering/
---

The MATLAB OpenGL renderer is very buggy when using opacity. Sometimes parts of your axes system disappear or colors are not drawn correctly, etc. , and some of these issues are especially prevalent when saving your figures as vectorized images using postscript (e.g.: .eps).

One option is to manually specify the renderer for your figure, e.g.,  

    set(gcf, 'renderer', 'zbuffer'); % valid options are painters, zbuffer, opengl, none

To specify the renderer for all figures (e.g., at startup of MATLAB), do

    set(0, 'defaultrenderer', 'zbuffer');

Alternatively, in the functions **[ft_singleplotER](/reference/ft_singleplotER)**/**[TFR](/reference/ft_singleplotTFR)** and **[ft_multiplotER](/reference/ft_multiplotER)**/**[TFR](/reference/ft_multiplotTFR)** there is a way to bypass these errors by using cfg.maskstyle = 'saturation' (default = 'opacity'). This uses saturation values to produce 'transparent' colors, which avoid the use of opacity in the OpenGL renderer. Colors are not actually transparent in the figure, which is why we are unable to implement a similar option in **[ft_topoplotER](/reference/ft_topoplotER)**/**[TFR](/reference/ft_topoplotTFR)**, **[ft_sourceplot](/reference/ft_sourceplot)** and others (as they specifically require the use of transparent parts of figures).

The advantage of using saturation is that you can also save it correctly to an .eps file.
