#!/bin/bash

SOURCE=$1
TARGET=$2

TARGETDIR=`dirname $TARGET`

if [ ! -d $TARGETDIR ]; then 
  mkdir -p $TARGETDIR
fi

cp $SOURCE $TARGET

