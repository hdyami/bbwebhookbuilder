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
	# pprint(bbdata["repository"]["name"])

	repo = bbdata['repository']

# Local git directory
git_dir = '/mnt/builds/'+repo['name']

# Initialize repo object and pull
g = git.cmd.Git(git_dir)
g.pull()

pprint(repo, depth=3)

print 0
