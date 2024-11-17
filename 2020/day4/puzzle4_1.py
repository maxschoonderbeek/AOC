#!/usr/bin/env python3

#-------------------------------------------------------------------+
#
# Advent of Code - Day 4 - Part 1
#
#-------------------------------------------------------------------+

#-------------------------------------------------------------------+
#	dependencies
#-------------------------------------------------------------------+

import os
import re

keys = [
   'byr',
   'iyr',
   'eyr',
   'hgt',
   'hcl',
   'ecl',
   'pid']

   # cid is not important
#-------------------------------------------------------------------+
#	main algorithm
#-------------------------------------------------------------------+

class Reader:
   def __init__(self):
      pass

   def load_data(self, filename):
      try:
         file =  open(filename)
         entries = file.readlines()
      except Exception as e:
         print("Exception: {}".format(e))
         return [""]
      else:
         return entries  
		
   def split_passports(self, Lines):
      passports = []
      passport_entry = ''
      for idx in range(0,len(Lines)):
         if Lines[idx][0] != '\n':
            passport_entry = passport_entry + Lines[idx]
         else:
            passport_entry = passport_entry.replace('\n',' ')
            passports.append(passport_entry)
            passport_entry = ''
      passport_entry = passport_entry.replace('\n',' ')
      passports.append(passport_entry) # also append last one
      return passports
   
   def count_valid_passport(self, passports):
      regex = '^'
      for key in keys:
         regex = regex + '(?=.*' + key + ')'
      print regex
      p = re.compile(regex)
      count = 0
      for passport in passports:
         if p.match(passport):
            count = count + 1
      return count
 
#-------------------------------------------------------------------+
#	startup
#-------------------------------------------------------------------+
if __name__ == "__main__":
   separator = "\r\n+----------------------------+\r\n"
   print(separator)
   
   reader = Reader()
   Lines = reader.load_data("input4_1.txt")
   passports = reader.split_passports(Lines)
   count = reader.count_valid_passport(passports)
   
   print 'total passports = ' + str(len(passports))
   print 'correct passports = ' + str(count)
   
   print(separator)

