import os
import git
import sys
import argparse
import subprocess
import json
import csv
from pprint import pprint
from jinja2 import Environment, FileSystemLoader

#Globals
TEMP_DIR = '/home/jenk/scripts/templates'
CONF_DIR = '/var/tmp/'

# setup our arguments
parser = argparse.ArgumentParser(description="Invoke with a sitename")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='Name of the site to build')

args = parser.parse_args()

file_loader = FileSystemLoader(TEMP_DIR)

env = Environment(loader=file_loader)

template = env.get_template('web_config.j2')

output = template.render(name=args.sitename)

with open(CONF_DIR+args.sitename+'.conf', 'w') as filehandle:
    filehandle.write(output)


