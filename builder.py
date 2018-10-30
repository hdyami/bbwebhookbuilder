#!/usr/bin/python
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
parser.add_argument('-f', nargs='?', help='Use Exclude file (excludes sites/default/files) - y for yes n for no. Default to y')


args = parser.parse_args()

# If the stdin was piped
if type(args.sitename) is file:
	# Ingest Bitbucket webhook json payload
	for line in args.sitename:
		bbdata = json.loads(line)

		build = {}
		build['name'] = bbdata['repository']['name']
		build['destination'] = 'd7-1.dev.www.umass.edu'
		build['f'] = 'y'
else: # If arguments were given by a human/external invocation
	build = {}
	build['name'] = args.sitename
	build['destination'] = args.d
	build['f'] = args.f

# Debug
pprint(build, depth=3)

# Local git directory
try:
	git_dir = '/mnt/builds/'+build['name']
	pprint(git_dir)

	# Initialize repo object and pull
	g = git.cmd.Git(git_dir)
	print g.pull()


	if build['f'] == 'n':
		rsync = subprocess.Popen(['rsync', '-a', '-h', '-v', git_dir, 'jenk@'+build['destination']+':/var/www/', '--delete'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	else:
		rsync = subprocss.Popen(['rsync', '-a', '-h', '-v', '--exclude-from=/mnt/builds/exclude.txt', git_dir, 'jenk@'+build['destination']+':/var/www/', '--delete'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	pprint(rsync)

	# Rsync to the dev server

	print rsync.communicate()


	print 0

except NameError:
	print "Please provide a sitename and destination with the -d flag - or pipe in some json."

