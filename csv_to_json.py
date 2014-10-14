#! /usr/bin/python2
__author__ = 'bsanders'

import os
import sys
import csv
import json

def csv_to_json(filename):
    '''
    :param filename: a string representing the filename of the csv file
    Given a csv file 'foo.csv', will generate a json formatted 'foo.json'
    '''
    # "context manager"  Filehandle will automatically close at the end of the scope.
    with open(filename) as inputfile:
        csv_dict = csv.DictReader(inputfile)
        # dumps() converts an object to a JSON formatted string
        json_data = json.dumps([row for row in csv_dict], indent = 4)
    # splitext() returns a tuple with the filename without suffix, and the suffix
    basename = os.path.splitext(filename)[0]
    with open(basename + ".json", 'w') as outputfile:
        outputfile.write(json_data)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if os.path.exists(sys.argv[1]):
            csv_to_json(sys.argv[1])
            sys.exit(0)
        else:
            print "File does not exist: {0}".format(sys.argv[1])

    print "usage: {0} inputfile.csv".format(sys.argv[0])
    sys.exit(1)


