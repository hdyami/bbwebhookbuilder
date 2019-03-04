#!/usr/bin/python
import os
import datetime
import subprocess
import sys
import argparse
import json
from pprint import pprint

## right now only D7 sites ##
# setup our arguments
parser = argparse.ArgumentParser(description="Give a sitename and a host")
parser.add_argument('sitename', nargs='?', help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Destination host for the build")

args = parser.parse_args()

datestamp = datetime.datetime.today().strftime('%Y-%m-%d')
site = args.sitename
host = args.d

if host == 'd7-1.dev.www.umass.edu':
	suffix = 'dev'
	backupfix = 'd7'
elif host == 'd7-1.stag.www.umass.edu':
	suffix = 'stag'
	backupfix = 'd7'
elif host == 'd7-1.prod.www.umass.edu':
	suffix = 'prod'
	backupfix = 'd7'
elif host == 'd8-1.dev.www.umass.edu':
        suffix = 'dev'
	backupfix = 'd8'
elif host == 'd8-1.stag.www.umass.edu':
        suffix = 'stag'
	backupfix = 'd8'
elif host == 'd8-1.prod.www.umass.edu':
        suffix = 'prod'
	backupfix = 'd8'

backup_dir = '/mnt/qs_nlsas/'+backupfix+'/'+suffix+'/backup/'
# dump sql
try:
	# make the sqldump TODO use object orientation!!!!!!!!!
	subprocess.call(["python", "sqldump.py", site, "-d", host])
except NameError:
	print "Error from sqldump.py"

try:
	# create tarball
	subprocess.call(["ssh", host, "tar", "-czvf ", backup_dir+site+"-"+datestamp+".tar.gz", "/var/www/"+site])

	print 0
except NameError:
	print "Error creating tarball"
