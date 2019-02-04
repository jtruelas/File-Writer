#!/usr/bin/bash

while true; do
	echo
	echo
	echo "To exit press Ctrl+C..."
	echo
	read -p "Enter name: " name;
	echo
	while [[ -z "$name" ]]; do
		read -p "Enter name: " name;
		echo
	done
	read -p "Enter id(format: xxxx): " id;
	echo
	while [[ -z "$id" ]]; do
		read -p "Enter id(format: xxxx): " id;
		echo
	done
	curl -s localhost:8000/api/$name/$id/ -o some.txt
	./filewriter.py client_data.txt
done