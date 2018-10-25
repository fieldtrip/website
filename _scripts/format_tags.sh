#!/bin/bash

awk '!/^tags/; /^tags/ {printf "tags: ["; for (i=2; i<NF; i++) printf "%s, ", $i ; print $NF "]"}' $1
