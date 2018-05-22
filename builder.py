#!/usr/bin/python
import os
import subprocess
import sys
import argparse
import json
from pprint import pprint

# Ingest Bitbucket webhook json payload
for line in sys.stdin:
	bbdata = json.loads(line)
	# pprint(bbdata["repository"]["name"])

	repo = bbdata['repository']

cd_p = subprocess.Popen('cd', '/mnt/builds/'+str(repo['name']), stdout=PIPE, stderr=PIPE)
print cd_p.communicate()

gitpull_p = subprocess.Popen('git', 'pull', stdout=PIPE, stderr=PIPE)
print gitpull_p.communicate()

# pprint(repo['name'], depth=3)

print 0
