#!/usr/bin/python
import os
import subprocess
import git
import sys
import argparse
import json
from pprint import pprint

# Ingest Bitbucket webhook json payload
for line in sys.stdin:
	bbdata = json.loads(line)
	repo = bbdata['repository']

# Local git directory
git_dir = '/mnt/builds/'+repo['name']

# Initialize repo object and pull
g = git.cmd.Git(git_dir)
g.pull()

# Rsync to the dev server
rsync = subprocess.Popen(['rsync', '-a','-v','-h', git_dir, 'jenk@d7-1.dev.www.umass.edu:/home/jenk/builds/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

pprint(rsync.communicate())

# debug
pprint(repo, depth=3)

print 0
