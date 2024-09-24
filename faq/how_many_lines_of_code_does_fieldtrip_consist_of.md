---
title: How many lines of code does FieldTrip consist of?
category: faq
tags: [matlab]
---

# How many lines of code does FieldTrip consist of?

You can count that using the following commands

    roboos@mac001> cat `find fieldtrip-20221223 -name \*.m` | grep -v ' *%' | grep -v '^ *$' | wc -l
    493168

or excluding the external toolboxes with

    roboos@mac001> cat `find fieldtrip-20221223 -name \*.m | grep -v external` | grep -v ' *%' | grep -v '^ *$' | wc -l
    237209

So the answer is approximately 237209 lines of code, excluding comments and empty lines.

To provide some historical perspective here is the number of lines in older FieldTrip releases (also only counting lines of code).

| when     | lines of code |
| -------- | ------------- |
| 2003 nov | 3441          |
| 2004 jun | 11735         |
| 2005 dec | 19235         |
| 2006 dec | 27507         |
| 2007 dec | 32057         |
| 2008 dec | 66581         |
| 2009 dec | 89983         |
| 2010 dec | 92192         |
| 2011 dec | 114642        |
| 2012 dec | 125116        |
| 2013 dec | 128477        |
| 2014 dec | ?             |
| 2015 dec | ?             |
| 2016 dec | 184322        |
| 2017 dec | 198553        |
| 2018 dec | 205290        |
| 2019 dec | 215759        |
| 2010 dec | 226194        |
| 2021 dec | 234054        |
| 2022 dec | 237209        |
