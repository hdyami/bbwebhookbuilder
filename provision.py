#! /usr/bin/python3
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

import repo

# setup our arguments
parser = argparse.ArgumentParser(description="creates a repository")
parser.add_argument('site_name', nargs='?', default=sys.stdin, help='site name')
# parser.add_argument('--version', nargs='?', help="which version of drupal do we desire?")

args = parser.parse_args()

def clone_standard():
    # https://stackoverflow.com/a/28413657
    # https://gist.github.com/s4553711/9488399
    print( "Cloning git@bitbucket.org:nsssystems/qs-site-d8-standard-framework.git to /var/www")
    try:
        s = subprocess.Popen(['ssh', 'd8-1.dev.www.umass.edu', 'cd /var/www; git clone git@bitbucket.org:nsssystems/qs-site-d8-standard-framework.git' ], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = s.communicate()
        if output:
            print s.returncode
            print output
        if error:
            print s.returncode
            print error.strip()
    except OSError as e:
        print "OSError > ",e.errno
        print "OSError > ",e.strerror
        print "OSError > ",e.filename
    except:
        print "Error > ",sys.exc_info()[0]

def clone_newrepo():
    # https://stackoverflow.com/a/28413657
    # https://gist.github.com/s4553711/9488399
    print( "Cloning git@bitbucket.org:nsssystems/%s to /var/www" % (args.site_name))
    try:
        s = subprocess.Popen(['ssh', 'd8-1.dev.www.umass.edu', 'cd /var/www; git clone git@bitbucket.org:nsssystems/'+ args.site_name +'.git' ], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = s.communicate()
        if output:
            print s.returncode
            print output
        if error:
            print s.returncode
            print error.strip()
    except OSError as e:
        print "OSError > ",e.errno
        print "OSError > ",e.strerror
        print "OSError > ",e.filename
    except:
        print "Error > ",sys.exc_info()[0]

def copy_standard():
    # https://stackoverflow.com/a/28413657
    # https://gist.github.com/s4553711/9488399
    print( "Renaming qs-site-d8-standard-framework to %s" % (args.site_name))
    try:
        s = subprocess.Popen(['ssh', 'd8-1.dev.www.umass.edu', 'mv /var/www/qs-site-d8-standard-framework', '/var/www/%s' % args.site_name ], shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = s.communicate()
        if output:
            print s.returncode
            print output
        if error:
            print s.returncode
            print error.strip()
    except OSError as e:
        print "OSError > ",e.errno
        print "OSError > ",e.strerror
        print "OSError > ",e.filename
    except:
        print "Error > ",sys.exc_info()[0]

if __name__ == '__main__':
    token = repo.get_token()
    repo.create_repo(token, args.site_name)
    clone_standard()
    clone_newrepo()
    copy_standard()
    
