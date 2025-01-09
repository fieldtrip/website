---
title: How can I read EGI mff data without the JVM?
parent: Specific data formats
category: faq
tags: [egi]
redirect_from:
    - /faq/how_can_i_read_egi_mff_data_without_the_jvm/
---

# How can I read EGI mff data without the JVM?

FieldTrip implements two methods for reading data from EGI .mff datasets. The first was implemented to get started with the existing data that was being recorded in some labs. Subsequently EGI offered support to make a new MATLAB implementation based on their reference toolbox (which is implemented in Java).

You can specify egi_mff_v1 or egi_mff_v2 as the headerformat, dataformat and eventformat options to **[ft_preprocessing](/reference/ft_preprocessing)** or the lower-level ft_read_XXX functions to determine which implementation will be used.

Both the egi_mff_v1 and the egi_mff_v2 implementations make use of the JVM (Java virtual machine), which might in certain situations be problematic.

With the first implementation it is possible to get it to work without JVM using an alternative implementation of the XML parser that does not rely on Java. This requires that you download the alternative from http://www.mathworks.com/matlabcentral/fileexchange/6268-xml4mat-v2-0. If you add the xml4mat toolbox to your path and remove the file "fieldtrip/fileio/private/xml2struct.m", the XML parser from xml4mat will be used instead.
