#!/usr/bin/env python
from collections import defaultdict
import csv
import json
import numpy
import os

# Keys for the database. Update as needed.
# Format is { "number" : {"name" : "name_of_section", index
# Note that signal names should not repeat themselves.
keys = {"1" : { "name" : "PANIC", 0 : "PANIC"}, \
        "B" : {"name" : "Throttle/Brake",   0 : "Torque Range 1", \
              1 : "Torque Range 2", 2 : "Brake", 3: "BSPD", \
              4 : "Startup Sequence", 5 : "Shutdown 0x05", \
              6 : "Shutdown 0x06", 7 : "Shutdown 0x07"}, \
        "C0" : {"name" : "BMS Master", 0 : "AMS Light", 1 : "IMD Status", \
               2 : "Average Temperature", 3 : "Average Voltage", \
               4 : "Average Current", 5 : "Fan Status", 6 : "Shutdown 0x0B", \
               7 : "Shutdown 0x0c"} ,\
        "D" : {"name" : "Air Control", 0 : "Precharge", \
              1 : "High Side AIR", 2 : "Shutdown 0x0D", \
              3 : "Shutdown 0x0E", 4 : "Shutdown 0x12" }, \
        "E" : { "name" : "Transom", 0 : "Transom Life"}, \
        "F" : {"name" : "Liquid Cooling", 0 : "Liquid Cooling Life"}, \
        "10" : {"name" : "Dashboard", 0 : "Start Button", \
               1 : "Dashboard Config 1", 2 : "Dashboard Config 2", 
               3 : "Dashboard Config 3", 4 : "Dashboard Config 4",
               5 : "Shutdown 0x08", 6 : "Shutdown 0x09", \
               7 : "Shutdown 0x0A" }, \
        "11" : {"name" : "Charging", 0 : "Charging Sequence", \
               1 : "Shutdown Charging"}, \
        "12" : {"name" : "Master Switch Panel", 0 : "Shutdown 0x02", \
               1 : "Shutdown 0x03", 2 : "Shutdown 0x04", \
               3 : "Shutdown 0x10", 4 : "Shutdown 0x11"} \
        }  


# TODO : This is less than ideal in general, but it's especially so from
#        a data structures point of view. It's probably worth cleaning up a 
#        lot of this processing somehow to make that not the case.

def txt_to_csv(text_file, msg_keys = keys, csv_name = 'data.csv'):
    """                                                                         
    Converts raw text file from vehicle can bus to CSV file with the first
    column containing timestamps and the following columns containing 
    headers based on the specific signal types specified in the JSON file.


    text_file : Text file of logged car data
    json_keys : JSON file with message headers and types. 
    """
                                                                             
    data_set = defaultdict(list)                                                                               
    raw_data = open(text_file, 'r')                                             
    
    # Put the data set into a usable dictionary
    for line in raw_data:                                                       
        field = line.split(":") 
        field[0] = field[0].strip(' ')                                                
        field[1]=field[1].strip(",time")
        field[2] = int(field[2].strip("\n")) 
        data_set[field[2]].append([field[0]] + field[1].split(","))             
    raw_data.close()

    # Create a csv
    with open(csv_name, 'wb') as csv_file:
        writer = csv.writer(csv_file, delimiter = ',', quotechar='"', \
                            quoting=csv.QUOTE_NONE, escapechar=' ')
        
        # Write header for the columns
        header = ['time']
        val_list = sorted(list(keys.values()))

        for entry in val_list:
            if 'name' in entry.keys():
                entry.pop('name')
                for label in sorted(list(entry.keys())):
                    header.append(entry[label])
        writer.writerow(header)
 
        # Now decode the rest of the message
        for key in sorted(list(data_set.keys())):
            for message in data_set.get(key):
                if message[0] in keys.keys():
                    index = header.index(keys[message[0]][0])
                    writer.writerow([key] + [''] * (index- 1) + message[1:])


# txt_to_csv('test_data.txt')
txt_to_csv('9_10_test_data.txt')
