#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 1 - Part 1
#
#-------------------------------------------------------------------+

#	dependencies
import os
import re

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
   separator = "\r\n+----------------------------+\r\n"
   print(separator)
   reader = Reader()
   Lines = reader.load_data('testC.txt')

   cumulative_sum = 0
   for line in Lines:
      first_digit = 0
      first_found = False
      last_digit = 0
      for char in line:
         if char.isdigit():
            if not first_found:
               first_digit = char
               first_found = True
            last_digit = char
      two_digit = int(first_digit + last_digit)

      cumulative_sum += two_digit

   print("Answer part 1: " + str(cumulative_sum))