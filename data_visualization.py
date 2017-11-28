#!/usr/bin/env python
from flask import Flask
import numpy
import matplotlib
import os

#app = Flask(__name__)

#@app.route('/')
def show_data(time_span = [], message_span = []):
    """
    Displays the data in a Meaningful Way.
    
    time_span = List with start and end time as integers.
    message_span = List of strings with CAN bit message type names.
    """
    # Change this to whatever file. I just made a big output file of the 
    # data from September 10, 2017.
    filename= os.getcwd() + "/output.txt"
    data_set = {}
    # This is pretty awful in terms of efficiency, but starting somewhere is
    # probably better than not doing that.
    with open(filename, "r") as raw_data:
        # Toss everything into a dictionary with the unecessary text
        # stripped from the strings.
        for line in raw_data:
            field = line.split(":")
            field[1]=field[1].strip(",time")
            field[2] = field[2].strip("\n")
            data_set[(field[2].strip(),  field[0].strip())] = field[1].split(",")
        # Blindly print stuff to start.
        for time in time_span:
            for bit_type in message_span:
                print("Time: " + str(time) + " Message type: " + bit_type +  \
                      "Message: " + data_set[(time, bit_type)])

time_range = [0, 1000000]
message_range = ['B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14']
show_data(time_range, message_range)
