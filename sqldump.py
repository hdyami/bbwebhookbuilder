#!/usr/bin/python
import os
import sys
import re
import subprocess
import argparse
import mysql.connector
from mysql.connector import errorcode
import json
from pprint import pprint
from umwebpass import password

# setup our arguments
parser = argparse.ArgumentParser(description="Provide a database name, target and password")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Source of the dump")

args = parser.parse_args()

NAME = args.sitename
HOST = args.d

drush = subprocess.Popen(["ssh", "jenk@"+HOST, "drush", "@"+NAME+"-dev", "sql-dump > /var/www/"+NAME+"/NAME_drpl.sql", shell=False, stdout=subprocess.PIPE)
drushresponse = drush.communicate()

params = drushresponse[0]
#fields = params.strip().split()

#user = fields[1]
#password = fields[2]
#database = re.sub('--database=', '', fields[3])
#host = fields[4]
#port = fields[5]

#print user
#print password
#print database
#print host
#print port

 mysqldump = subprocess.Popen(["mysqldump", database, host, user, password, ">", "/home/jenk/"+NAME+"_drpl.sql"], shell=False, stdout=subprocess.PIPE)
#mysqldump = subprocess.list2cmdline(["mysqldump", database, host, user, password, ">", "/home/jenk/"+NAME+"_drpl.sql"])

# mysqldumpresponse = mysqldump.communicate()

print mysqldump
