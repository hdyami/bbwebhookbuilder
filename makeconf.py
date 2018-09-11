# generate an apache config file and push it to sites-available on the target host

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
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='Name of the sites configuration to build')
parser.add_argument('-d', nargs='?', default=sys.stdin, help='Destination for the configuration')

args = parser.parse_args()

file_loader = FileSystemLoader(TEMP_DIR)

env = Environment(loader=file_loader)

template = env.get_template('web_config.j2')

output = template.render(name=args.sitename)

# write file to disk
with open(CONF_DIR+args.sitename+'.conf', 'w') as filehandle:
    filehandle.write(output)

# Rsync to the dev server
rsync = subprocess.Popen(['rsync', '-rv','-l', '-h', CONF_DIR+args.sitename+'.conf', 'jenk@'+args.d+':/etc/httpd/conf.d/sites-available'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

print rsync.communicate()

os.remove(CONF_DIR+args.sitename+'.conf')
