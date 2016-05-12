#!/usr/bin/python

# This is a helper script for adding students' gravatar icons to their
# blogs on the Python Summer of Code blog aggregator.

# Gravatar uses an md5 hash of email to identify each user, so we
# take a spreadsheet that includes student names and emails and output
# something that can be cut/pasted into the aggregator config file.

import sys
import hashlib
import csv

csvfilename = sys.argv[1]
print csvfilename

with open(csvfilename, 'r') as csvfile:
	studentreader = csv.reader(csvfile, delimiter=',')
	for student in studentreader:
		#print ', '.join(student)
		name = student[4]
		email = student[5]
 		print "[http://example.com]"
		print "name = " + name
		#print "# md5 -s " + email.replace('@',  ' ')
		print "face = " + hashlib.md5(str.lower(email)).hexdigest()
		print ""
