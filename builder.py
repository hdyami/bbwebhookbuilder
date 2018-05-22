#!/usr/bin/python
import os
import sys
import argparse
import json
from pprint import pprint

# Ingest Bitbucket webhook json payload
for line in sys.stdin:
	bbdata = json.loads(line)
	pprint(bbdata["repository"]["name"])

print 0
