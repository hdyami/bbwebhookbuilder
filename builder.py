#!/usr/bin/python
# DICK-BUNION
import os
import subprocess
import git
import sys
import argparse
import json
from pprint import pprint

# setup our arguments
parser = argparse.ArgumentParser(description="Pipe in stdin or optionally invoke with a sitename and destination")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Destination host for the build")

args = parser.parse_args()

# If the stdin was piped
if type(args.sitename) is file:
	# Ingest Bitbucket webhook json payload
	for line in args.sitename:
		bbdata = json.loads(line)
		repo = bbdata['repository']
else:
	repo = {}
	repo['name'] = args.sitename

pprint(repo, depth=3)

# Local git directory
try:
	git_dir = '/mnt/builds/'+repo['name']

	# Initialize repo object and pull
	g = git.cmd.Git(git_dir)
	print g.pull()

	# Rsync to the dev server
	rsync = subprocess.Popen(['rsync', '-a','-v','-h', git_dir, 'jenk@d7-1.dev.www.umass.edu:/home/jenk/builds/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	pprint(rsync.communicate())

	# debug
	# pprint(repo, depth=3)
	print 0

except NameError:
	print "Please provide a sitename and destination with the -d flag - or pipe in some json."

def destination():
	pass

