---
layout: default
---

{{tag>guidelines development}}

# Documentation guidelines

When you add documentation, please consider the following documentation guidelines to keep it consistent with other documentation and to facilitate cross-linking.

*  FieldTrip should be written with capital "F" and capital "T"

*  All FieldTrip functions should be written in the text made **bold**, without .m, and with a link to reference documentation: i.e. **[ft_preprocessing](/reference/ft_preprocessing)**

*  When you add a new page, please give it relevant [tags](/#how_to_add_tags).

*  If you see something that needs to be fixed in the documentation, add a FIXME comment (write fixme in capital letters), and also [add the tag](/#how_to_add_tags) 'fixme' at the top of the page.

*  Please structure new tutorials [in the following way](/#how_to_structure_a_tutorial).

*  Please give clear [names for example data](/#How to name example data).

*  If you refer to file formats using the extension, please do it like *.txt, *.dat or *.ext in general.

## Where to add documentation on the website?

There are several places where you are especially encouraged to add your own input to the FieldTrip wiki. On the [frequently asked questions](/faq) page you can add answers to a variety of FieldTrip-related questions. On the [example scripts](/example) page you can put parts of your own scripts of specific analysis done in FieldTrip or in conjunction with FieldTrip. If these scripts get very elaborate and use example data, you can alternatively add a tutorial on the [tutorials](/tutorial) page and [contact](/contact) us to [send](/faq/how_should_i_send_example_data_to_the_developers) the example data so it can be put on the ftp-server (ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip/tutorial).

## How to add a page to the wiki?

Go to the [frequently asked questions](/faq), [example scripts](/example), or [tutorials](/tutorial) page, and hit the 'Edit this page' button. Add the title of your contribution to the list and hit 'save'.
    You add e.g.: * [example:This is the name of your example script](/example/This is the name of your example script)
You now see the title of your contribution as a red link. If you click on this link you can create the page and add your content (under Page tools on the upper left). See [syntax](/wiki/syntax) for further Wiki syntax. You can also practice on the [playground:playground](/playground/playground).

## How to add tags?

By adding [tags](http://www.dokuwiki.org/plugin:tag) your contribution will be easier to find. Add as a first line (for example
    {{tag>example eeg source statistics}}
if you add an example script that describes performing source statistics in eeg. The tags 'example','eeg', 'source', and 'statistics' will be given to your page. [Here](/tagcloud) you can find  a list of possible tags. Please always add 'faq', 'example' or 'tutorial', depending on your type of contribution.

## How to structure a tutorial?

The tutorials should be written with a clear audience in mind: the reader of the tutorial expects to learn something. The tutorial should contain examples that can be reproduced. Furthermore, the examples should be explained in such a manner that the reader can generalize these hands-on examples to his/her own experimental data analysis.

For consistency the tutorials should preferably be structured in the following wa


*  **Introduction:** introduction to the tutorial and dataset. This should include
    * What will you learn from this tutorial?
    * What does this tutorial expect as background understanding or skills?
    * Which topics are not covered in this tutorial?

*  **Background:** some background on the methods used

*  **Procedure:** summarize which analysis steps are performed in the tutorial, this should include a picture of the analysis protocol (please use SVG).

*  All steps in the procedure are subsequent headings.

*  **Summary and conclusion:**
    * What has been covered?
    * What has not been covered but is relevant in the context of the tutorial?
    * Provide links to suggested further reading, related FAQ's and example scripts.

To check that the tutorial meets the expected didactical qualities, the introduction should spell out what the reader will learn, what is expected from him (e.g. that he already has done another tutorial) and what will not be covered. The summary should link to follow up documentation and to the more advanced topics that relate to the tutorial.

For an example of a well-structured tutorial see the [tutorial on event related fields](/tutorial/eventrelatedaveraging).

## How to update the tutorial data on the FTP?

Some computations in the tutorials may take a (too) long time, or take more memory than available in the  computers of the people that want to walk through the tutorial. To allow people in these cases to follow through the whole tutorial, we provide the intermediate data and final results at important stages in the tutorial. This data is stored in *.mat files. See below for the recommended file and variable naming scheme.

The tutorial mat files are made available on ftp:/ftp.fieldtriptoolbox.org/pub/fieldtrip and are distributed to all computers whenever we have a toolkit course or workshop. To get new files on the FTP server, or update existing files, you should copy them on the DCCN central storage system to the directory /home/common/matlab/fieldtrip/dataftp. That directory is automatically synchronized with the FTP server.

## How to name example data?

When using example data in tutorials, please use consistent naming. That i

*  add a prefix to the data-name that shows what kind of data it is. Prefixes are: data (for raw/preprocessed data), timelock, freq, stat and source. Example: if you have timelocked data (ERP/ERF) of condition FIC, you can call it timelockFIC. So do not use 'data' for everything.

*  save the data as a mat-file with the same name (e.g. save the variable freqFIC to the file freqFIC.mat)

## How to add figures?

The preferred format for figures on this wiki is the SVG graphics format. SVG is a standardized scalable vector graphics format and can be edited with several software packages (e.g. Inkscape on Linux, and Adobe Illustrator for Windows and OS X). The advantage of SVG is that it allows other people to download the figure, modify it, and upload the changed figure without loss of quality.

Figures from MATLAB should preferably be exported in the PNG format. If you think it might be beneficial that the MATLAB figure is editable in the future, you should export the figure to EPS or AI, open the figure in Adobe Illustrator, and save it to SVG.

Making schematic figures in SVG is easy in Office Word or Office Powerpoint using their default shapes under the *insert* ta

{{:excel-drawing-tools-2007-2010.jpg?200px}}

When you are done making the figure just select all text and images and copy-paste them it in Adobe Illustrator to save as SVG.


## What colors to use

If you make schematic figures yourself we suggest the default Office 2007 color scheme. The lighter (pastel) colors are made by making the images 50% transparent (//right-button// click on figure, then change transparency under *format shape*), or by using the RGB values in the boxes below. Also, we suggest using the Calibri or Arial font in figures. Here you can download Adobe Illustrator swatch (palette) and an example.

{{:fieltrip_palette.png|}}

## How to make the banners for this Wiki?

Explaining how to make the images to include in the photo rotator at the top of the FieldTrip wiki is done in [a separate page](/development/wiki_banners), since it is only relevant for people at the DCCN.

## Suggested further reading

Please also consider the [code guidelines](/development/guidelines/code) when making contributions to the FieldTrip project.
