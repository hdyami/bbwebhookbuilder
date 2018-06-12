#!/usr/bin/python
import os
import sys
import subprocess
import argparse
import json
from pprint import pprint

# setup our arguments
parser = argparse.ArgumentParser(description="Pipe in stdin or optionally invoke with a sitename and destination")
parser.add_argument('dbname', nargs='?', default=sys.stdin, help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Destination cluster for the db - dev, prod, stag")
parser.add_argument('-p', nargs='?', help="Password")

args = parser.parse_args()

# http://python-for-system-administrators.readthedocs.io/en/latest/ssh.html
COMMAND="mysql -uqsdbadmin --port=3307 -hdev.umwebdb.umass.edu -e 'show databases;'"

ssh = subprocess.Popen(["ssh", "%s" % args.d, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)

result = ssh.stdout.readlines()

print result
