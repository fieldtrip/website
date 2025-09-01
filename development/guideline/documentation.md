---
title: Documentation guidelines
tags: [guidelines, development]
---

When you add documentation, please consider the following documentation guidelines to keep it consistent with other documentation and to facilitate cross-linking.

- FieldTrip should be written with capital "F" and capital "T"
- All FieldTrip functions should be written in the text made **bold**, without .m, and with a link to the reference documentation: i.e. **[ft_preprocessing](/reference/ft_preprocessing)**
- When you add a new page, please give it relevant [tags](#how_to_add_tags).
- If you see something that needs to be fixed in the documentation, report it as issue on [GitHub](https://github.com/fieldtrip/website/issues)
- Please structure new tutorials [in the following way](#how_to_structure_a_tutorial).
- Please give clear [names for example data](</#How to name example data>).
- If you refer to file formats using the extension, please do it like .txt, .dat or .ext in general.

## Where to add documentation on the website?

There are several places where you are especially encouraged to add your own input to the FieldTrip website. On the [frequently asked questions](/faq) page you can add answers to a variety of FieldTrip-related questions. On the [example scripts](/example) page you can put parts of your own scripts of specific analysis done in FieldTrip or in conjunction with FieldTrip. If these scripts get very elaborate and use example data, you can alternatively add a tutorial on the [tutorials](/tutorial) page and [contact](/support) us to [send](/faq/organization/datasharing) the example data so it can be put on the [download server](https://download.fieldtriptoolbox.org).

To submit changes to the FieldTrip website, make a Pull Request on the corresponding [website repository](https://github.com/fieldtrip/website) on GitHub.

## How to structure a tutorial?

The tutorials should be written with a clear purpose in mind: the reader of the tutorial expects to learn something. The tutorial should contain examples that can be reproduced. Furthermore, the examples should be explained in such a manner that the reader can generalize these hands-on examples to his/her own experimental data analysis.

For consistency the tutorials should preferably be structured in the following way:

- **Introduction:** introduction to the tutorial and dataset. This should include
  - What will you learn from this tutorial?
  - What does this tutorial expect as background understanding or skills?
  - Which topics are not covered in this tutorial?
- **Background:** some background on the methods used
- **Procedure:** summarize which analysis steps are performed in the tutorial. This should include a picture of the analysis protocol.
- All steps in the procedure are **subsequent headings**.
- **Summary and conclusion:**
  - What has been covered?
  - What has not been covered but is relevant in the context of the tutorial?
  - Provide links to suggested further reading, related FAQs and example scripts.

To check that the tutorial meets the expected didactical qualities, the introduction should spell out what the reader will learn, what is expected from him/her (e.g., that he/she already has done another tutorial) and what will not be covered. The summary should link to follow up documentation and to the more advanced topics that relate to the tutorial.

For an example of a well-structured tutorial see the [tutorial on event-related fields](/tutorial/sensor/eventrelatedaveraging).

## How to update the tutorial data on the download server?

Some computations in the tutorials may take a long time (or too long), or take more memory than available in the computers of the people that want to walk through the tutorial. To allow people in these cases to follow through the whole tutorial, we provide the intermediate data and final results at important stages in the tutorial. This data is stored in .mat files. See below for the recommended file and variable naming scheme.

The tutorial mat-files are made available on <https://download.fieldtriptoolbox.org/> and are distributed to all computers whenever we have a toolkit course or workshop. To get new files on the [download server](https://download.fieldtriptoolbox.org), or update existing files, you should copy them on the DCCN central storage system to the directory `/home/common/matlab/fieldtrip/data/ftp`. That directory is automatically synchronized with the download server.

## How to name example data?

When using example data in tutorials, please use consistent naming.

- Add a prefix to the data-name that shows what kind of data it is. Prefixes are: data (for raw/preprocessed data), timelock, freq, stat and source. For example, if you have timelocked data (ERP/ERF) of condition FIC, you can call it timelockFIC. So do not use 'data' for everything.
- Save the data as a .mat file with the same name, e.g., save the variable freqFIC to the file freqFIC.mat.
- Store only one variable in every .mat file.

## How to link to the function reference documentation?

We link to the documentation on GitHub to allow people to look up the help of a function similar to what they would see with `help functionname` in MATLAB. This also encourages people to browse the code to look up implementation details. Rather than linking directly to GitHub, we use a http redirect from the reference section on the website. In the MarkDown code you should specify  this as follows.

- `**[ft_preprocessing](/reference/ft_preprocessing)**` to link to **[ft_preprocessing](/reference/ft_preprocessing)**
- `**[ft_selectdata](/reference/utilities/ft_selectdata)**` to link to **[ft_selectdata](/reference/utilities/ft_selectdata)**

Note that by convention this includes the `**` to make the link appear in a bold font. The `.m` at the end of the filename should not be specified, and functions in subdirectories like `utilities` or `fileio` should include that subdirectory in the link.

## How to add tags?

At the top of each markdown page there is a [Jekyll front-matter](https://jekyllrb.com/docs/front-matter/) section like this:

```text
---
title: this is the title, it should also be the first top-level heading
tags: [tag1, tag2]
---
```

You can add tags to that list; these will be automatically shown at the top of each page on the actual website. The corresponding page with the overview of all pages that share the same tag (like [this](/tag/guidelines)) will be automatically constructed upon the next build of the website. To increase the value of the tags, you should choose tags that are also used on other pages, and you should not add too many tags to a single page. Please use only lower-case letters in the tags, and use a minus sign to separate multiple words that are combined in a single tag (like [meg-language](/tag/meg-language)).

## How to add figures?

The preferred format for figures on the website is the PNG format. Also figures from MATLAB and screenshots should preferably be exported in the PNG format. If you want to edit the MATLAB figure, you should first export the figure to EPS or AI, open the figure in Adobe Illustrator and make the changes, and save it to PNG.

Figures should be added to the `assets/img` directory of the website repository. Please do not upload very large binary files, such as PDFs, but send them to Robert for static inclusion on the website. Figures should not be included in the standard markdown style, since that does not allow the specification of the size and does not allow zooming in. Instead, figures should be included using a piece of custom [Liquid code](https://shopify.github.io/liquid/) which gets translated into html at the moment the website is rebuilt.

We also considered SVG, which is a standardized scalable vector graphics format. This would allow other people to download the figure, modify it, and upload the changed figure without loss of quality. However, SVG had too many problems rendering correctly in different browsers.

Making schematic figures in SVG is easy in Microsoft Word or Microsoft Powerpoint using their default shapes under the _insert_ tab. When you are done making the figure just select all text and images and copy-paste them it in Adobe Illustrator to save as SVG.

{% include image src="/assets/img/development/guideline/documentation/excel-drawing-tools-2007-2010.jpg" width="200" %}

## What colors to use

If you make schematic figures yourself we suggest the default Office 2007 color scheme. The lighter (pastel) colors are made by making the images 50% transparent (_right-button_ click on figure, then change transparency under _format shape_), or by using the RGB values in the boxes below. Also, we suggest using the Calibri or Arial font in figures. Here you can find an example of the colors.

{% include image src="/assets/img/development/guideline/documentation/fieldtrip_palette.png" %}

## Suggested further reading

Please also consider the [code guidelines](/development/guideline/code) when making contributions to FieldTrip.
