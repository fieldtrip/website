#!/bin/bash
#
# This script parses all pages for tags and creates an overview page for each tag.
# It results in an update of _data/tag/*.yml and of tag/*.md
#
# Following execution of this script, you should commmit the tag pages that have
# been changed.

if [[ ! -e _config.yml ]] ; then echo ERROR this should be executed in the toplevel directory ;  exit 1 ; fi

# these will be recreated
rm       tag/*.md
rm _data/tag/*.yml

TAGFILE=`mktemp`

# this constructs a list of all tags
find . -name \*.md | xargs grep -h '^tags:' | cut -d : -f 2 | tr -d '[] ' | tr , '\n' | sort -u > $TAGFILE

# this constructs a list of pages that have a certain tag
for TAG in `cat ${TAGFILE}` ; do
  FILELIST=`find . -name \*.md | xargs grep -wl ^tags:.*${TAG} | sort | uniq `
  for FILE in ${FILELIST}; do
    NAME=`grep title: $FILE | cut -d : -f 2 | cut -b 2-`
    LINK=${FILE:1:$((${#FILE}-4))}
    echo '- name: ' $NAME  >> _data/tag/$TAG.yml
    echo '  link: ' $LINK  >> _data/tag/$TAG.yml
    echo ''                >> _data/tag/$TAG.yml
  done
done

# this constructs an overview page for each tag
for TAG in `cat ${TAGFILE}` ; do
  echo '---'        >  tag/$TAG.md
  echo layout: tag  >> tag/$TAG.md
  echo tag: $TAG    >> tag/$TAG.md
  echo '---'        >> tag/$TAG.md
done
