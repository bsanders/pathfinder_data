#! /usr/bin/python2
__author__ = 'bsanders'

import os
import sys
import csv
import json

# Given a csv file 'foo.csv', will generate a json formatted 'foo.json'

def csv_to_json(filename):
    '''
    :param filename: a string representing the filename of the csv file
    '''
    # "context manager"  Filehandle will automatically close at the end of the scope.
    with open(filename) as inputfile:
        csv_dict = csv.DictReader(inputfile)
        # dumps() converts an object to a JSON formatted string
        return json.dumps([row for row in csv_dict], indent = 4)

def json_to_file(json_string, filename):
    '''
    :param json_string: a string represention of JSON data
    :param filename: a string representing the filename of the json file
    '''
    with open(filename, 'w') as outputfile:
        outputfile.write(json_string)

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        print "usage: {0} <inputfile.csv> <...>".format(sys.argv[0])
        sys.exit(1)

    exit_status = 0
    for filename in sys.argv[1:]:
        if os.path.exists(filename):
            # splitext() returns a tuple with the filename without suffix, and the suffix
            json_string = csv_to_json(filename)
            json_filename = os.path.splitext(filename)[0] + ".json"
            json_to_file(json_string, json_filename)
        else:
            print "File does not exist: {0}".format(filename)
            exit_status += 1
    sys.exit(exit_status)
