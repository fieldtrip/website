---
title: What is a good way to save images for later processing in other software?
tags: [plotting]
category: faq
redirect_from:
    - /faq/what_is_a_good_way_to_save_images_for_later_processing_in_other_software/
    - /faq/figure_export/
---

Here are some tips from various users/developers:

- Save in `.eps` format, these can be easily edited in Adobe Illustrator etc.

- Use the function [saveSameSize](http://www.mathworks.com/matlabcentral/fileexchange/17868-savesamesize) from the MathWorks File Exchange. This function saves the the figure like it looks on-screen.

- Use the function [export_fig](http://www.mathworks.com/matlabcentral/fileexchange/23629-exportfig) from the MathWorks File Exchange for advanced saving options.

When processing an exported `.eps` file in Adobe Illustrator, remember the following things/quirks about MATLAB's figure export:

- MATLAB usually creates invisible 'boxes/objects' around plot-elements like axes, text, etcetera. To make it easier to work with the objects that are actually important, delete all these superfluous and invisible objects by selecting everything (ctrl+a), or selecting 'empty space' and deleting the ones that contain none of the elements that you want, or look unimportant (there are ALWAYS many of these annoying objects). A 'clean' figure is always easier for a Journal copy-editor to work with.

- MATLAB usually creates white squares as background of axes, deleting these makes handling the plots a lot easier.

- In a regular `plot(x,y)` figure, many additional x,y-axes are often placed on top of each other and are 'invisible' which makes foreground/background transfers problematic, delete these x,y-axes.

- When plotting several lines in as `plot(x,y,etc)`, the output is usually read as a 'grouped' object by Illustrator. Ungrouping these objects (i.e. right click --> ungroup) makes handling/editing these lines much easier.

- Whenever you notice that elements of plots were not exported as objects, but as horizontal bars of a bitmap image, or anything else that is weird, it is usually a MATLAB openGL bug. Doing `set(gcf,'renderer','painters')` usually fixes this.
