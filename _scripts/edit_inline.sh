#!/bin/bash

FILE="$1"
export FIND="$2"
export REPLACE="$3"

if [[   -z "$1" ]] ; then echo ERROR argument 1 missing   ; exit 1 ; fi
if [[   -z "$2" ]] ; then echo ERROR argument 2 missing   ; exit 1 ; fi
if [[   -z "$3" ]] ; then echo ERROR argument 3 missing   ; exit 1 ; fi
if [[ ! -z "$4" ]] ; then echo ERROR superfluous argument ; exit 1 ; fi

ruby -p -i -e "gsub(ENV['FIND'], ENV['REPLACE'])" "$FILE"
