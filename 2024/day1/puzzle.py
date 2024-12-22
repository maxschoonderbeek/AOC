#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 1 - Part 2
#
#-------------------------------------------------------------------+

#	dependencies
import os
import re
import numpy as np

#-------------------------------------------------------------------+
#	main algorithm
#-------------------------------------------------------------------+



class Reader:
    def __init__(self):
        pass

    def load_data(self, filename):
        try:
            script_dir = os.path.dirname(__file__)
            abs_file_path = os.path.join(script_dir, filename) 
            file =  open(abs_file_path)
            entries = file.readlines()
        except Exception as e:
            print("Exception: {}".format(e))
            return [""]
        else:
            return entries

#-------------------------------------------------------------------+
#	startup
#-------------------------------------------------------------------+
if __name__ == "__main__":
    SEPRATOR = "\r\n+----------------------------+\r\n"
    print(SEPRATOR)
    reader = Reader()
    Lines = reader.load_data('input.txt')
    r = re.compile(r"[0-9]+", flags=re.I)

    first = []
    second = []

    for line in Lines:
        out = r.findall(line)
        first.append(int(out[0]))
        second.append(int(out[-1]))

    first.sort()
    second.sort()
    cumulative_distance = 0
    for f,s in zip(first,second):
        distance = abs(f-s)
        cumulative_distance += distance

    print("Answer part 1: " + str(cumulative_distance))

    similarity_score = 0
    for f in first:
        count = second.count(f)
        similarity_score += f*count
    print("Answer part 2: " + str(similarity_score))
