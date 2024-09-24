---
title: I am having problems printing figures that use opacity
category: faq
tags: [plotting]
---

# I am having problems printing figures that use opacity

In some FieldTrip figures opacity is used to indicate statistical significance, for example in **[ft_sourceplot](/reference/ft_sourceplot)** where you can use color=functional-value, opacity=significance, grey-level=anatomy, or for example in **[ft_topoplotER](/reference/ft_topoplotER)**.

You can use the MATLAB command "print" for printing figures to a printer or for saving them to a bitmap or PostScript file (see help print). If you encounter difficulties printing/saving the figure, you should try printing with the extra option "-opengl".
