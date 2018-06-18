#!/usr/bin/python
import os
import sys
import subprocess
import argparse
import json
from pprint import pprint

# setup our arguments
parser = argparse.ArgumentParser(description="Provide a database name, target and password")
parser.add_argument('dbname', nargs='?', default=sys.stdin, help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Destination cluster for the db - dev, prod, stag")
# parser.add_argument('-p', nargs='?', help="Password")

args = parser.parse_args()

# http://python-for-system-administrators.readthedocs.io/en/latest/ssh.html
# querywrapper = "mysql -uqsdbadmin --port=3307 -hdev.umwebdb.umass.edu -e 'create database "+args.dbname+";'"
query = "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, LOCK TABLES, CREATE TEMPORARY TABLES ON \"cryptozoo_drpl\".* TO "cryptozoo_drpl"@"d7-%.dev.www.umass.edu" IDENTIFIED BY "zYVfEkTgYawVKMum" WITH MAX_USER_CONNECTIONS 30"

querywrapper = "mysql -uqsdbadmin --port=3307 -hdev.umwebdb.umass.edu -e '"+ query +"';"
pprint(querywrapper)

ssh = subprocess.Popen(["ssh", "%s" % args.d, querywrapper],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

result = ssh.stderr.readlines()

print result
