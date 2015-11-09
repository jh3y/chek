#!/usr/bin/python

import subprocess
import os

def check_repos(dir):
    for repo in os.listdir(dir):
        if os.path.isdir(dir + repo) and os.path.isdir(dir + repo + '/.git'):
            print repo
            print subprocess.check_output(['git', '-C', dir + repo, 'status'])

# Inform of the current location
print 'You are currently located @ ' + subprocess.check_output(['pwd'])
# Get location
location = raw_input('Enter the directory glob you wish to check repo statuses for: ')
check_repos(location)
