#!/bin/bash
#
# Use as:
#   rename_figures.sh <page.md>
#
# This script does not do the conversion itself, but prints the commands to screen.
# The user of the script should check the commands prior to execution

[ -e "$1" ]  || exit 1

figures=$(grep "include image" $1  | cut -d \" -f 2)

n=1
for figure in $figures ; do
  oldname=$(basename $figure)
  ext=$(echo $oldname | cut -f 2 -d '.')
  newname=$(dirname $figure)/figure"$n"."$ext"
  echo git mv ."$figure" ."$newname"
  echo sed -i .bak s~$figure~$newname~g $1
  n=$(expr $n + 1)
done
