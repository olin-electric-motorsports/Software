#!/usr/bin/env python
from collections import defaultdict
from flask import Flask, render_template
import numpy
import matplotlib
import os
import csv
import pandas

app = Flask(__name__)

@app.route('/')
def run_on_startup():
    """
    Runs when you start the flask server. Run functions from here.
    """
    data_set = create_data_set()
    time_range = numpy.linspace(1, 1000, 1000)
    message_range = ['B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14']
    return render_template("table.html", data_set=data_set)

"""
def print_data_set(data_set= {}, time_span = []):

    Literally just blindly prints the data set dictionary. Useful for
    debugging, and possibly only for debugging.
    time_span = List with start and end time as integers.
    message_span = List of strings with CAN bit message type names.


    return " ".join(["%s %s" % (str(time), str(data_set[time])) for time in time_span if data_set[time]])
"""

def create_data_set(text_file = 'static/9_10_test_data.txt'):
    """
    text_file = The text file of the CAN bus artifacts.

    Returns a defaultdict of all of the values based on the text file.
    It should look like {time: [[MESSAGE_TYPE, bit 1, bit 2],
    [MESSAGE_TYPE, bit 1, bit 2]]}
    """
    data_set = dict()

    # with app.open_resource(text_file) as raw_data:
    raw_data = open(text_file, 'r')
    # Get rid of uncessary characters and toss it into a dictionary.
    for line in raw_data:
        line = line.strip()
        data_lst = line.split(':')
        data_lst[1] = data_lst[1].replace(',time','')
        data_set[data_lst[2]] = data_lst[0:2]
    return data_set


if __name__ == '__main__':
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000))

    app.run(host=HOST, port=PORT)
    app.run(threaded=True)
