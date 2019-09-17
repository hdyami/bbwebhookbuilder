#! /usr/bin/python
import sys
import argparse
import subprocess
import git
import json

# setup our arguments
parser = argparse.ArgumentParser(description="creates a repository")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='site name')
parser.add_argument('--host', nargs='?', default=sys.stdin, help='target host')

args = parser.parse_args()

if args.host == 'staging':
    DIR="/mnt/qs_ssd/www/stag/"
elif args.host =='dev':
    DIR="/mnt/qs_ssd/www/dev/"

# clone the given site repo on the given target host directory
def clone_repo():
    print( "Cloning git@bitbucket.org:nsssystems/%s to /var/www" % (args.sitename))
    try:
        git.Git(DIR).clone("git@bitbucket.org:nsssystems/"+ args.sitename + ".git")
    except:
        print "no bueno"

if __name__ == '__main__':
    clone_repo()