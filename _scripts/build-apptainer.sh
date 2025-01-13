#!/bin/bash
#
# This script builds the FieldTrip website

# this runs from a cron-job, so paths are not set as in an interactive terminal
GIT=/usr/bin/git
CP=/usr/bin/cp
BUNDLE=$HOME/fieldtrip/apptainer/bundle

# needed to prevent /tmp read-only error in the container
export TMPDIR=$HOME/tmp && mkdir -p $TMPDIR

cd $HOME/fieldtrip/website

LOCKFILE=$HOME/fieldtrip/website.lock
LOGFILE=$HOME/fieldtrip/website.log

# prevent concurrent builds
while [ -e $LOCKFILE ] ; do
  LOCKTIME=$(( $(date +"%s") - $(stat -c "%Y" $LOCKFILE) ))
  if [ "$LOCKTIME" -gt "300" ]; then
    echo removing stale lock
    rm $LOCKFILE
  else
    echo waiting for previous build to complete
    sleep 10
  fi
done

# make sure that these exist
[ -e $LOGFILE  ] || touch $LOGFILE
[ -e $LOCKFILE ] || touch $LOCKFILE

# ensure that we have the latest version of the repository
# let's hope there are no conflicts with the reference documentation
$GIT pull > /dev/null 2>&1

# compare the latest to the previous version
PREVIOUS=$(cat $LOGFILE)
LATEST=$(git log -1 --format=%H)

if [ "$LATEST" != "$PREVIOUS" ] ; then

# DISABLED FOR NOW TO AVOID A PUSH/PULL LOOP
#
# # update the tags, this uses a bash script
# _scripts/tags.sh
# $GIT add _data/tag/*.yml
# $GIT add tag/*.md
# $GIT commit -m "updated tags" _data/tag tag > /dev/null 2>&1
# 
##  update the categories, this uses a bash script
# _scripts/categories.sh
# $GIT add _data/category/*.yml
# $GIT add category/*.md
# $GIT commit -m "updated categories" _data/category category > /dev/null 2>&1

# push the updates back to the repository
$GIT push > /dev/null 2>&1

echo building website version $LATEST
echo $LATEST > $LOGFILE

JEKYLL_ENV=production
$BUNDLE install           # > /dev/null 2>&1
$BUNDLE exec jekyll build # > /dev/null 2>&1

# copy the large assets that are not in the repository to the released site
cd $HOME/fieldtrip/website
$CP assets/root/* _site/

fi

# remove the lock
rm $LOCKFILE
