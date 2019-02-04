#!/usr/bin/env python

import clientdata_pb2
import sys


# This function fills in a Person message based on file read
def SearchForPerson(person):
	# Read file and recover desired data
	with open('some.txt', 'r') as f:
		lines = f.readlines()
		idline = lines[1].split(':')[1].replace(',', '')
		nameline = lines[2].split(':')[1].replace('"', '').replace(' ', '')

	# Enter data
	person.id = idline
	person.name = nameline

# Check for file to be written to
if len(sys.argv) != 2:
	print("Usage:", sys.argv[0], "CLIENT_FILE")
	sys.exit(-1)

client_data = clientdata_pb2.ClientData()

# Read from existing file
try:
	with open(sys.argv[1], "rb") as cfile:
		client_data.ParseFromString(cfile.read())
		cfile.close()
except IOError:
	print(sys.argv[1] + ": Could not open file. Creating a new one.")

# Add client data
SearchForPerson(client_data.people.add())

# Write the new data
with open(sys.argv[1], "wb") as cfile:
	cfile.write(client_data.SerializeToString())
	print("Writing now...")
	cfile.close()
