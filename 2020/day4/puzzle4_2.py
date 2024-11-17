#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 4 - Part 1
#
#-------------------------------------------------------------------+

#-------------------------------------------------------------------+
#	dependencies
#-------------------------------------------------------------------+

import os
import re

keys = [
   ['byr','(19[2-9][0-9]|200[0-2])'],
   ['iyr','(201[0-9]|2020)'],
   ['eyr','(202[0-9]|2030)'],
   ['hgt','(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))'],
   ['hcl','#[0-9a-f]{6}'],
   ['ecl','(amb|blu|brn|gry|grn|hzl|oth)'],
   ['pid','\\b[0-9]{9}\\b']
]

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
         regex = regex + '(?=.*\\b' + key[0] + ':' + key[1] + '\\b)'
      print 'REGEX:\n' + regex
      p = re.compile(regex)
      count = 0
      for passport in passports:
         if p.match(passport):
            print passport
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
   
   print '  total passports = ' + str(len(passports))
   print 'correct passports = ' + str(count)
   
   print(separator)

