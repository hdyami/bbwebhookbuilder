#! /usr/bin/python3
# import os
import sys
import argparse
import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from pprint import pprint

# setup our arguments
parser = argparse.ArgumentParser(description="creates a repository")
parser.add_argument('repo_name', nargs='?', default=sys.stdin, help='repository name')
# parser.add_argument('-p', nargs='?', help="a parameter")
args = parser.parse_args()


client_id = 'SM3uvZPabGrthhTyNH'
client_secret = 'NXBtTfEWWdFm5BFJ5ju2Q6pUf6WNH7A9'

auth_url = 'https://bitbucket.org/site/oauth2/access_token'
url = 'https://api.bitbucket.org/2.0/'

def get_token():
    # grab our oauth2 token
    client = BackendApplicationClient(client_id=client_id)

    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url=auth_url, client_id=client_id, client_secret=client_secret)

    return token

def create_repo(token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token['access_token']
    }

    data = '{"scm": "git", "project": {"key": "QS"}, "is_private": "true", "fork_policy": "no_public_forks" }'

    # create our repo
    r = requests.post(url+'repositories/nsssystems/' + args.repo_name, headers=headers, data=data)
    return r


if __name__ == '__main__':
    token = get_token()
    r = create_repo(token)
    if r.status_code == '200':
        pprint(r.text)
        
        print 0
        sys.exit(0)
    else:
        error_msg = json.loads(r.text)
        print error_msg['error']['message']
        
        print 1
