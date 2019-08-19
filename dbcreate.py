#!/usr/bin/python
import os
import sys
import subprocess
import argparse
import mysql.connector
from mysql.connector import errorcode
import json
from pprint import pprint
from umwebpass import password
# from passwordgen import randomPassword

# todo - optionally create password with strong password, as opposed to entering a password to use with a flag
#print randomPassword(16)

# setup our arguments
parser = argparse.ArgumentParser(description="Provide a database name, target and password")
parser.add_argument('dbname', nargs='?', default=sys.stdin, help='Name of the site to build e.g. cryptozoo_drpl')
parser.add_argument('-d', nargs='?', help="Destination cluster for the db - e.g. d7-%.dev.www.umass.edu")
parser.add_argument('-p', nargs='?', help="Password")

args = parser.parse_args()

NAME = args.dbname
PASS = args.p

if args.d == 'd7dev':
	HOST = 'd7-%.dev.www.umass.edu'
	CONFHOST = 'dev.umwebdb.umass.edu'
	PORT = '3307'
elif args.d == 'd7stag':
	HOST = 'd7-%.stag.www.umass.edu'
	CONFHOST = 'stag.umwebdb.umass.edu'
	PORT = '3307'
elif args.d == 'd7prod':
	HOST = 'd7-%.prod.www.umass.edu'
	CONFHOST = 'umwebdb.umass.edu'
	PORT = '3308'
elif args.d == 'd8dev':
	HOST = 'd8-%.dev.www.umass.edu'
	CONFHOST = 'dev.umwebdb.umass.edu'
	PORT = '3307'
elif args.d == 'd8stag':
	HOST = 'd8-%.stag.www.umass.edu'
	CONFHOST = 'stag.umwebdb.umass.edu'
	PORT = '3307'
elif args.d == 'd8prod':
	HOST = 'd8-%.prod.www.umass.edu'
	CONFHOST = 'umwebdb.umass.edu'
	PORT = '3308'

config = {
	'user': 'qsdbadmin',
	'host': CONFHOST,
	'port': PORT,
	'password': password('qsdbadmin')
	# 'option_files': '/home/jenk/.my.cnf',
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor(buffered=False)

def create_database(cursor):
	try:
		cursor.execute("CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(NAME))
		print("Success creating database {}".format(NAME))
	except mysql.connector.Error as err:
		print("Failed creating database: {}".format(err))
		exit(1)

def enable_database_access(cursor):
	query = ("GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, INDEX, ALTER, LOCK TABLES, CREATE TEMPORARY TABLES ON {}.* TO %s@%s IDENTIFIED BY %s WITH MAX_USER_CONNECTIONS 30".format('`'+ NAME +'`'))
	try:
		cursor.execute(query, (NAME, HOST, PASS))
		print("Success granting permissions for {}".format(NAME))
	except mysql.connector.Error as err:
		print("Failed querying: {}".format(err))
		exit(1)

def flush_privileges(cursor):
	try:
		cursor.execute("flush privileges")
		print("Success Flushing Privileges")
	except mysql.connector.Error as err:
		print("Failed flushing privileges")
		exit(1)

create_database(cursor)
enable_database_access(cursor)
flush_privileges(cursor)

cnx.close()

