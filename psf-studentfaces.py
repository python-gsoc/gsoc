#!/usr/bin/python

# This is a helper script for adding students' gravatar icons to their
# blogs on the Python Summer of Code blog aggregator.

# Gravatar uses an md5 hash of email to identify each user, so we
# take a spreadsheet that includes student names and emails and output
# something that can be cut/pasted into the aggregator config file.

import sys
import hashlib

csvfilename = sys.argv[1]
print csvfilename

csvfile = open(csvfilename, 'r')
for line in csvfile:
	linearray = str.split(line, ',')
	name = linearray[2]
	email = linearray[3]
	print name
	print "# md5 -s " + email
	print "face = " + hashlib.md5(str.lower(email)).hexdigest()
	print ""
