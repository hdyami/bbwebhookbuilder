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
# parser.add_argument('-S', nargs='?', help="Destination host for the build")


args = parser.parse_args()

# If the stdin was piped
if type(args.sitename) is file:
	# Ingest Bitbucket webhook json payload
	for line in args.sitename:
		bbdata = json.loads(line)

		build = {}
		build['name'] = bbdata['repository']['name']
		build['destination'] = 'd7-1.dev.www.umass.edu'
else: # If arguments were given by a human/external invocation
	build = {}
	build['name'] = args.sitename
	build['destination'] = args.d

# Debug
pprint(build, depth=3)

# Local git directory
try:
	git_dir = '/mnt/builds/'+build['name']

	# Initialize repo object and pull
	g = git.cmd.Git(git_dir)
	print g.pull()

	# Rsync to the dev server
	rsync = subprocess.Popen(['rsync', '-r','-l', '-v','-h', git_dir, 'jenk@'+build['destination']+':/var/www/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

	print rsync.communicate()

	# debug
	# pprint(repo, depth=3)
	print 0

except NameError:
	print "Please provide a sitename and destination with the -d flag - or pipe in some json."






