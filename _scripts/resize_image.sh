#!/bin/bash
#
# This uses http://www.imagemagick.org/Usage/resize/

if [[   -z "$1" ]] ; then echo ERROR argument 1 missing   ; exit 1 ; fi
if [[   -z "$2" ]] ; then echo ERROR argument 2 missing   ; exit 1 ; fi
if [[ ! -z "$3" ]] ; then echo ERROR superfluous argument ; exit 1 ; fi

FILE=$1
WIDTH=$2

# split the path, filename and extension
P="$(dirname -- "$FILE")"
F="$(basename -- "$FILE")"
X="${F##*.}"
F="${F%.*}"

OUTFILE=${P}/${F}.${X}@${WIDTH}

convert -resize ${WIDTH}x ${FILE} ${OUTFILE}
