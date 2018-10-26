#!/bin/bash

if [[ ! -e _config.yml ]] ; then echo ERROR this should be executed in the toplevel directory ;  exit 1 ; fi

rsync -arpv --delete _site/* fieldtrip:/var/www/fieldtrip.fcdonders.nl_07
