#!/usr/bin/env python
from collections import defaultdict
from flask import Flask
import numpy
import matplotlib
import os

app = Flask(__name__)

@app.route('/')
def show_data(time_span = [], message_span = []):
    """
    Displays the data in a Meaningful Way.
    
    time_span = List with start and end time as integers.
    message_span = List of strings with CAN bit message type names.
    """
    filename = "9_10_test_data.txt"
    # Change this to whatever file. I just made a big output file of the 
    # data from September 10, 2017.
    data_set = defaultdict(list)
    # This is pretty awful in terms of efficiency, but starting somewhere is
    # probably better than not doing that.
    printout = ""
    with open(filename, "r") as raw_data:
        # Toss everything into a dictionary with the unecessary text
        # stripped from the strings.
        for line in raw_data:
            field = line.split(":")
            field[1]=field[1].strip(",time")
            field[2] = int(field[2].strip("\n"))
            data_set[field[2]].append([field[0]] + field[1].split(","))
        for time in time_range:
            if data_set[time]:
                printout += (str(time) + " " + str(data_set[time]) + "\n")
            return printout

# Some quick test scripts...
time_range = numpy.linspace(1, 1000, 1000)
message_range = ['B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14']
show_data(time_range, message_range)
