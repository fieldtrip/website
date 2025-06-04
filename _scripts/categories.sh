#!/bin/bash
#
# This script parses all pages for categories and creates an overview page for each category.
# It results in an update of _data/category/*.yml and of category/*.md
#
# Following execution of this script, you should commmit the category pages that have
# been changed.

if [[ ! -e _config.yml ]] ; then echo ERROR this should be executed in the toplevel directory ;  exit 1 ; fi

# these will be recreated
rm       category/*.md
rm _data/category/*.yml

CATEGORYFILE=`mktemp`

# this constructs a list of all categories
find . -name \*.md | xargs grep -h '^category:' | cut -d : -f 2 | tr -d '[] ' | tr , '\n' | sort -u > $CATEGORYFILE

# this constructs a list of pages that belong to a certain category
for CATEGORY in `cat ${CATEGORYFILE}` ; do
  FILELIST=`find . -name \*.md -not -path ./.bundle/\*| xargs grep -wl ^category:.*${CATEGORY} | sort -u `

  for FILE in ${FILELIST}; do
    TITLE=`grep title: $FILE | cut -d : -f 2 | cut -b 2-`
    LINK=${FILE:1:$((${#FILE}-4))}
    echo '- title: ' $TITLE >> _data/category/$CATEGORY.yml
    echo '  link: '  $LINK  >> _data/category/$CATEGORY.yml
    echo ''                 >> _data/category/$CATEGORY.yml
  done
done

# this constructs an overview page for each category
for CATEGORY in `cat ${CATEGORYFILE}` ; do
  echo '---'               >  category/$CATEGORY.md
  echo layout: category    >> category/$CATEGORY.md
  echo category: $CATEGORY >> category/$CATEGORY.md
  echo '---'               >> category/$CATEGORY.md
done
