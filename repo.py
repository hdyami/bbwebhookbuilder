#! /usr/bin/python3
# import os
import sys
import argparse
import requests
import json
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from pprint import pprint

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

def create_repo(token, r_name):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token['access_token']
    }

    data = '{"scm": "git", "project": {"key": "QS"}, "is_private": "true", "fork_policy": "no_public_forks" }'

    # create our repo
    try:
        r = requests.post(url+'repositories/nsssystems/' + r_name, headers=headers, data=data)
    except requests.ConnectionError:
        print("failed to connect")
    else:
        if r.status_code == 200:
            return pretty_json(r.text)

            print 0
            sys.exit(0)
        else:
            error_msg = json.loads(r.text)
            print error_msg['error']['message']

            print 1

    return r

def get_repo_info(token):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+token['access_token']
        }

        r = requests.get(url+'repositories/nsssystems/' + args.repo_name, headers=headers)

    except requests.ConnectionError:
        print("failed to connect")
    else:
        if r.status_code == 200:
            return pretty_json(r.text)

            print 0
            sys.exit(0)
        else:
            error_msg = json.loads(r.text)
            print error_msg['error']['message']

            print 1

    return r

def delete_repo(token):
    try:
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+token['access_token']
        }

        r = requests.delete(url+'repositories/nsssystems/' + args.repo_name, headers=headers)

    except requests.ConnectionError:
        print("failed to connect")
    else:
        if r.status_code == 204:
            return "Succes deleting"

            print 0
            sys.exit(0)
        else:
            error_msg = json.loads(r.text)
            print error_msg['error']['message']

            print 1
            sys.exit(0)

    return r

def rename_repo(token):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer '+token['access_token']
    }

    data = '{"name": "'+ args.rename +'"}'
    pprint(data)
    # create our repo
    try:
        r = requests.put(url+'repositories/nsssystems/' + args.repo_name, headers=headers, data=data)
    except requests.ConnectionError:
        print("failed to connect")
    else:
        pprint(r)
        if r.status_code == 200:
            return pretty_json(r.text)

            print 0
            sys.exit(0)
        else:
            error_msg = json.loads(r.text)
            print error_msg['error']['message']

            print 1
            sys.exit(0)
    return r

def pretty_json(j):
    parsed = json.loads(j)

    return json.dumps(parsed, indent=4, sort_keys=True)

if __name__ == '__main__':
    # setup our arguments
    parser = argparse.ArgumentParser(description="creates a repository")
    parser.add_argument('repo_name', nargs='?', default=sys.stdin, help='repository name')
    parser.add_argument('--delete', nargs='?', help="delete")
    parser.add_argument('--create', nargs='?', help="create")
    parser.add_argument('--info', nargs='?', help="get info")
    parser.add_argument('--rename', nargs='?', help="rename")

    args = parser.parse_args()
    
    if args.info:
        token = get_token()
        r = get_repo_info(token)
        print r
    elif args.create:
        token = get_token()
        r = create_repo(token, args.repo_name)
        print r
    elif args.delete:
        token = get_token()
        r = delete_repo(token)
        print r
    elif args.rename:
        token = get_token()
        r = rename_repo(token)
        print r
    else:
        print("Invalid option")