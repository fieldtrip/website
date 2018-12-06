#!/bin/bash

# Add RVM to PATH for scripting. Make sure this is the last PATH variable change.
export PATH="$PATH:$HOME/.rvm/bin"
export PATH="$PATH:$HOME/.rvm/rubies/ruby-2.5.3/bin"
export PATH="$PATH:$HOME/.rvm/gems/ruby-2.5.3/bin"
export GEM_PATH="/home/mrphys/roboos/.rvm/gems/ruby-2.5.3:/home/mrphys/roboos/.rvm/gems/ruby-2.5.3@global"
export GEM_HOME="/home/mrphys/roboos/.rvm/gems/ruby-2.5.3"
# Load RVM into a shell session *as a function*
[[ -s "$HOME/.rvm/scripts/rvm" ]] && source "$HOME/.rvm/scripts/rvm"

# this runs from a cron-job, so paths are not set as in an interactive terminal
LOGFILE=$HOME/log/website.log
GIT=/usr/bin/git
BUNDLE=$HOME/.rvm/rubies/ruby-2.5.3/bin/bundle
CP=/usr/bin/cp

[ -e $LOGFILE ] || touch $LOGFILE

cd $HOME/website

# ensure that we have the latest version of the repository
# let's hope there are no conflicts with th ereference documentation
$GIT pull > /dev/null 2>&1

# integrate updates to the reference documentation, these get copied from elsewhere to the web server
$GIT commit -m "updated reference documentation" reference > /dev/null 2>&1
$GIT push > /dev/null 2>&1

# compare the latest to the previous version
PREVIOUS=$(cat $LOGFILE)
LATEST=$(git log -1 --format=%H)
if [ "$LATEST" != "$PREVIOUS" ] ; then

echo BUILDING WEBSITE VERSION $LATEST
echo $LATEST > $LOGFILE

# add a link to the latest commit to the website
cat << EOF > commit.md
---
title: Latest documentation commit
layout: default
tags: development
---
[$LATEST](https://github.com/fieldtrip/website/commit/$LATEST)
EOF

$BUNDLE install           > /dev/null 2>&1
$BUNDLE exec jekyll build > /dev/null 2>&1

# copy some static assets over to the root directory
$CP assets/root/* _site/

else
# update the timestamp of the logfile, to check when the script was executed 
touch $LOGFILE
fi

