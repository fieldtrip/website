---
title: How many lines of code does FieldTrip consist of?
tags: [faq]
---

# How many lines of code does FieldTrip consist of?

You can count that using the following commands

    roboos@mac001> cat `find . -name \*.m` | grep -v ' *%' | grep -v '^ *$' | wc -l
    366391

or excluding the external toolboxes with

    roboos@mac001> cat `find . -name \*.m | grep -v external` | grep -v ' *%' | grep -v '^ *$' | wc -l
    187938

So the answer is approximately 187938 lines of code, excluding comments and empty lines.

To provide some historical perspective here is the number of lines in older FieldTrip releases (also only counting lines of code).

| when     | lines of code |
| -------- | ------------- |
| 2003 nov | 3441          |
| 2004 jun | 11735         |
| 2005 jun | 16969         |
| 2005 dec | 19235         |
| 2006 jun | 24410         |
| 2006 dec | 27507         |
| 2007 jun | 30306         |
| 2007 dec | 32057         |
| 2008 jun | 37963         |
| 2008 dec | 66581         |
| 2009 jun | 87756         |
| 2009 dec | 89983         |
| 2010 jun | 95049         |
| 2010 dec | 92192         |
| 2011 jun | 103813        |
| 2011 dec | 114642        |
| 2016 oct | 187938        |
