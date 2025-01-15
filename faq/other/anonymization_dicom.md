---
title: How can I anonymize or deidentify DICOM files?
parent: Various other questions
grand_parent: Frequently asked questions
category: faq
tags: [mri, anonymize, sharing]
redirect_from:
    - /faq/how_can_i_anonymize_dicom_files/
    - /faq/anonymization_dicom/
---

# How can I anonymize or deidentify DICOM files?

DICOM files contain a lot of header details that might provide information about your subject, such as the name and date of birth, but also the date and time at which the scan was performed.

{% include markup/red %}
Besides the potentially identifying data in the header of the DICOM file, the facial information in an anatomical MRI can be reconstructed into picture that might be used for identification. Furthermore, the cortical folding or the specific anatomical connectivity in a DTi scan might be considered as a "fingerprint". In both cases an external database would be required to match the data against subject identifiers, e.g., a facial reconstructed picture could be matched against the database formed by Google images.

The remainder of this FAQ is only about the metadata in the header, not about [defacing](/faq/how_can_i_anonymize_an_anatomical_mri) the data or about imposing legal restrictions to prevent matching data against external databases.
{% include markup/end %}

Since it is not easy to determine if there is potentially identifying data in the DICOM headers, many researchers choose to share the data in NIfTI format rather than DICOM format. The NIfTI format is used by most neuroimaging software anyway, and the NIfTI header is very simple and does store any identifying information. However, there are also situations where it is desired to share the original DICOM files.

## Using MATLAB

The MATLAB image processing toolbox contains functions for reading and writing DICOM files. You can use

    dicominfo(FILE_IN)

to see all the header information, and

    dicomanon(FILE_IN, FILE_OUT)

to remove all confidential metadata from the DICOM header.

## Using Horos

[Horos](https://www.horosproject.org) is a free DICOM image file viewer for macOS. You can use it to view your image files and explore the metadata in the header. It works by importing all DICOM files and organizing it in its own internal database. It has an "anonymize" option which allows you to remove/replace the values in specific fields.

The default behavior of the anonymize option is that only the metadata in own internal database is anonymized; if you want the DICOM files to be anonymized on disk, you should use the export option to write the data back to disk. To be sure that the data on disk is anonymized, I recommend importing it a second time to check the metadata.

## Using GDCM

[GDMC](http://gdcm.sourceforge.net/wiki/index.php/Main_Page) is an open source implementation of the DICOM standard in C++. You can download the software from [SourceForge](http://gdcm.sourceforge.net), or on the compute cluster at the DCCN you can use

    module add gdcm

to add it to your path. Subsequently you can use the [gdcmanon](http://gdcm.sourceforge.net/html/gdcmanon.html) command to anonymize individual files

    gdcmanon <file-in> <file-out>

or a whole directory with many DICOM files at once

    gdcmanon <dir-in> <dir-out>

You can use the [gdcmdump](http://gdcm.sourceforge.net/html/gdcmdump.html) command line program to dump one of the output DICOM file to the console and to check that all metadata fields have been anonymized.

## Using DCMTK

[DCMTK](http://www.dcmtk.org) is a collection of libraries and applications implementing large parts the DICOM standard. It includes software for examining, constructing and converting DICOM image files. You can download the software from its [homepage](http://www.dcmtk.org), or on the compute cluster at the DCCN you can use

    module add dcmtk

to add it to your path. Subsequently you can use the [dcmdump](http://support.dcmtk.org/docs/dcmdump.html) command to show all DICOM header data

    dcmdump <file>

and the [dcmodify](http://support.dcmtk.org/docs/dcmodify.html) command

    dcmodify -ea "(0010,0010)" <file>

to erase the specific tags. In this case the "PatientName" tag (0010,0010) is erased from the file. Note that this overwrites the existing file, but keeps a backup of the original. You may have to erase other fields as well.

{% include markup/red %}
The help of dcmodify suggests that "-ep" or "--erase-private" can be used to erase private data, but this is **not** the personal data of the subject, but rather header information that is system/software specific and not shared between different DICOM systems.
{% include markup/end %}
