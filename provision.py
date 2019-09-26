#! /usr/bin/python
# import os
import sys
import argparse
import subprocess
import requests
import git
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session
from pprint import pprint
from repo import get_token
from repo import create_repo

# setup our arguments
parser = argparse.ArgumentParser(description="creates a repository")
parser.add_argument('sitename', nargs='?', default=sys.stdin, help='site name')
parser.add_argument('--structure', nargs='?', default=sys.stdin, help='structure')
parser.add_argument('--sponsor', nargs='?', default=sys.stdin, help='sponsor')
parser.add_argument('--developer', nargs='?', default=sys.stdin, help='developer')

parser.add_argument('--version', nargs='?', help="which version of drupal do we desire?")

d8source = 'git@bitbucket.org:nsssystems/qs-site-d8-standard-framework.git'
devdir = '/mnt/qs_ssd/www/dev/'

args = parser.parse_args()

def inlet(message, payload):
    print( message)
    try:
        s = subprocess.Popen(payload, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = s.communicate()
        if output:
            print(s.returncode)
            print(output)
        if error:
            print(s.returncode)
            print(error.strip())
    except OSError as e:
        print "OSError > ",e.errno
        print "OSError > ",e.strerror
        print "OSError > ",e.filename
    except:
        print "Error > ",sys.exc_info()[0]


if __name__ == '__main__':
    token = get_token()
    create_repo(token, args.sitename)

    inlet("Cloning git@bitbucket.org:nsssystems/qs-site-d8-standard-framework.git to /var/www", ['git', 'clone', d8source, devdir+args.sitename])
    inlet("Blank the slate", ['rm', '-rf', devdir+args.sitename+'/.git'])
    inlet("Composer install", ["composer", "install", "-d="+devdir+args.sitename])
    inlet("Initialize a blank repository", ['git', 'init', devdir+args.sitename])
    inlet("Add new site to blank repo", ['git', '--work-tree='+devdir+args.sitename, "--git-dir="+devdir+args.sitename+"/.git", "add", devdir+args.sitename])
    inlet("Commit new stuff", ['git', '--work-tree='+devdir+args.sitename, "--git-dir="+devdir+args.sitename+"/.git", "commit", "-am", "\"inital commit\""])
    inlet("Link up this repository with it's remote", ['git', '--work-tree='+devdir+args.sitename, "--git-dir="+devdir+args.sitename+"/.git", "remote", "add", "origin", "git@bitbucket.org:nsssystems/"+args.sitename+".git"])
    inlet("Push to repo and also create master branch", ['git', '--work-tree='+devdir+args.sitename, "--git-dir="+devdir+args.sitename+"/.git", "push", "origin", "master"])