#!/usr/bin/python
import os
import sys
import re
import subprocess
import argparse
import json
from pprint import pprint
from umwebpass import password

# setup our arguments
parser = argparse.ArgumentParser(description="Provide a database name, host and password. Creates a NAME_drpl.sql file at /var/www/NAME/")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Source of the dump")

args = parser.parse_args()

NAME = args.sitename
HOST = args.d

if HOST == 'd7-1.dev.www.umass.edu':
	SUFFIX = '-dev'
elif HOST == 'd7-1.stag.www.umass.edu':
	SUFFIX = '-staging'
elif HOST == 'd7-1.prod.www.umass.edu':
	SUFFIX = '-prod'

drush = subprocess.Popen(["ssh", "jenk@"+HOST, "drush", "@"+NAME+SUFFIX, "sql-dump > /var/www/"+NAME+"/"+NAME+"-drpl.sql"], shell=False, stdout=subprocess.PIPE)
drushresponse = drush.communicate()

params = drushresponse[0]
print params
