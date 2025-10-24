import os
import sys

def reader(filename):
    caller_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    abs_file_path = os.path.join(caller_dir, filename)
    with open(abs_file_path) as f:
        lines = f.readlines()
    return lines
