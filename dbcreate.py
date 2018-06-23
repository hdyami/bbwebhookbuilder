#!/usr/bin/python
import os
import sys
import subprocess
import argparse
import mysql.connector
from mysql.connector import errorcode
import json
from pprint import pprint

# setup our arguments
parser = argparse.ArgumentParser(description="Provide a database name, target and password")
parser.add_argument('dbname', nargs='?', default=sys.stdin, help='Name of the site to build')
parser.add_argument('-d', nargs='?', help="Destination cluster for the db - dev, prod, stag")
# parser.add_argument('-p', nargs='?', help="Password")

args = parser.parse_args()

config = {
	'user': 'qsdbadmin',
	'host': 'dev.umwebdb.umass.edu',
	#'database': args.dbname,
	'port': '3307',
	#'raise_on_warnings': True,
	'option_files': '/home/jenk/.my.cnf',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=False)

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(args.dbname))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)

create_database(cursor)

cnx.close()

# http://python-for-system-administrators.readthedocs.io/en/latest/ssh.html
# querywrapper = "mysql -uqsdbadmin --port=3307 -hdev.umwebdb.umass.edu -e 'create database "+args.dbname+";'"


#ssh -L 2222:umwebdb...:3307 <user>@<host>

#127.0.0.1 2222
