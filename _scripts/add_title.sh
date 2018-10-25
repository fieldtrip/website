#!bin/bash

if [[   -z "$1" ]] ; then echo ERROR argument 1 missing   ; exit 1 ; fi

FILE=$1
TEMP=`mktemp`

# this is for pages with a table of content
# TITLE=`grep '^#' $FILE | head -2 | tail -n 1 | tr -d '#' `

# this is for pages without a table of content
TITLE=`grep '^#' $FILE | head -1 | tail -n 1 | tr -d '#' `

head -1 $FILE        >> $TEMP
echo title: ${TITLE} >> $TEMP
tail +2 $FILE        >> $TEMP

mv $TEMP $FILE
