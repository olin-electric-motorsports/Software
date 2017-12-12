#!/usr/bin/env python
from collections import defaultdict
from flask import *
import numpy
import matplotlib
import os

app = Flask(__name__)

@app.route('/')
def run_on_startup():
    """
    Runs when you start the flask server. Run functions from here.
    """
    data_set = create_data_set()
    time_range = numpy.linspace(1, 1000, 1000)
    message_range = ['B', 'C', 'D', 'E', 'F', '10', '11', '12', '13', '14']
    return print_data_set(data_set, time_range)


def print_data_set(data_set= {}, time_span = []):
    """
    Literally just blindly prints the data set dictionary. Useful for
    debugging, and possibly only for debugging.
    time_span = List with start and end time as integers.
    message_span = List of strings with CAN bit message type names.
    """
    printout = ""
    # TODO There's probably some defaultdict magic that can make this really
    # quick and not wasteful like this. At the same time, this whole function
    # is somewhat trivial, so there's that...
    res = []
    for time in time_span:
        if data_set[time]:
            printout = str(time) + " " + str(data_set[time])
            res.append(printout)
    # return printout
    random_stuffsss = print_random_stuff()
    return render_template('home.html', data=random_stuffsss)


def create_data_set(text_file = 'data/9_10_test_data.txt'):
    """
    text_file = The text file of the CAN bus artifacts.

    Returns a defaultdict of all of the values based on the text file.
    It should look like {time: [[MESSAGE_TYPE, bit 1, bit 2],
    [MESSAGE_TYPE, bit 1, bit 2]]}
    """
    # TODO this is a lazy choice. I could use a real dictionary. I should
    # choose whether I need to actually use one.
    data_set = defaultdict(list)

    # with app.open_resource(text_file) as raw_data:
    raw_data = open(text_file, 'r')
    # Get rid of uncessary characters and toss it into a dictionary.
    for line in raw_data:
        field = line.split(":")
        field[1]=field[1].strip(",time")
        field[2] = int(field[2].strip("\n"))
        data_set[field[2]].append([field[0]] + field[1].split(","))
    return data_set


def print_random_stuff(text_file = 'data/9_10_test_data.txt'):
    data = open(text_file, 'r')
    ans = []
    for line in data:
        stuff = line.split('\n')
        ans.append(stuff[0])
    return ans[0:100]


if __name__ == '__main__':
    HOST = '0.0.0.0' if 'PORT' in os.environ else '127.0.0.1'
    PORT = int(os.environ.get('PORT', 5000))

    app.run(host=HOST, port=PORT)
    app.run(threaded=True)
