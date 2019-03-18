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

# git pull repo then rsync EXCLUDING SITES/DEFAULT/FILES to PROD

args = parser.parse_args()

build = {}
build['name'] = args.sitename
build['destination'] = 'd7-1.prod.www.umass.edu'

# Debug
pprint(build, depth=3)

# Local git directory
try:
	git_dir = '/mnt/builds/'+build['name']
	pprint(git_dir)

	# Initialize repo object and pull
	g = git.cmd.Git(git_dir)
	print g.pull()

	rsync = subprocess.Popen(['rsync', '-a', '-h', '-v', '--exclude=sites/default/settings.php', '--exclude-from=/mnt/builds/exclude.txt', git_dir, 'jenk@'+build['destination']+':/var/www/'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	pprint(rsync)

	# Rsync to the dev server

	print rsync.communicate()
	print 0
except:
	"Something went wrong"
	print 1

