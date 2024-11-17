#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 1 - Part 2
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
   Lines = reader.load_data('input.txt')

   digit_strings = {
      "1" : 1,"one" : 1,
      "2" : 2,"two" : 2,
      "3" : 3,"three" : 3,
      "4" : 4,"four" : 4,
      "5" : 5,"five" : 5,
      "6" : 6,"six" : 6,
      "7" : 7,"seven" : 7,
      "8" : 8,"eight" : 8,
      "9" : 9,"nine" : 9
      }
   regex = '|'.join([r'%s' % d for d in digit_strings.keys()])
   r = re.compile(regex, flags=re.I)

   digit_list = []
   cumulative_sum = 0
   for line in Lines:
      line = line.replace("one", "o1e")
      line = line.replace("eight", "ei8ht")
      out = r.findall(line)
      first_digit = digit_strings.get(out[0])
      last_digit = digit_strings.get(out[-1])
      double_digit = 10*first_digit + last_digit
      digit_list.append(double_digit)
      cumulative_sum += double_digit
   print(digit_list)

   print("Answer part 2: " + str(cumulative_sum))