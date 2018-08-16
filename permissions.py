#!/usr/bin/python
import os
import subprocess
import sys
import argparse
import json
from pprint import pprint

# setup our arguments
parser = argparse.ArgumentParser(description="Give a sitename and destination for some permissions change")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='Name of the site to change')
parser.add_argument('-d', nargs='?', help="Destination host for the permission change")
# parser.add_argument('-S', nargs='?', help="Destination host for the build")

args = parser.parse_args()

build = {}
build['name'] = args.sitename
build['destination'] = args.d

# Debug
pprint(build, depth=3)

# Local git directory
try:


	# Rsync to the dev server
	ssh = subprocess.Popen(['ssh', 'jenk@'+build['destination']], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	ls = subprocess.Popen(['ls', '/var/www'] stdin=ssh.stdout, stderr=subprocess.PIPE)

	print ls.communicate()

	# debug
	# pprint(repo, depth=3)
	print 0

except NameError:
	print "Please provide a sitename and destination with the -d flag - or pipe in some json."
