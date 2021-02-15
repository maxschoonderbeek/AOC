#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 6 - Part 1
#
#-------------------------------------------------------------------+

#-------------------------------------------------------------------+
#	dependencies
#-------------------------------------------------------------------+

import os
import re

letters = "abcdefghijklmnopqrstuvwxyz"

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
		
   def split_answers(self, Lines):
      answers = []
      passport_entry = ''
      for idx in range(0,len(Lines)):
         if Lines[idx][0] != '\n':
            passport_entry = passport_entry + Lines[idx]
         else:
            passport_entry = passport_entry.replace('\n','')
            answers.append(passport_entry)
            passport_entry = ''
      passport_entry = passport_entry.replace('\n','')
      answers.append(passport_entry) # also append last one
      return answers
   
   def count_unique_answers(self, answers):
      count = []
      for answer in answers:
         counter = 0
         for i in letters :
            if i in answer :
               counter += 1
         count.append(counter)
      return sum(count)
 
#-------------------------------------------------------------------+
#	startup
#-------------------------------------------------------------------+
if __name__ == "__main__":
   separator = "\r\n+----------------------------+\r\n"
   print(separator)
   
   reader = Reader()
   Lines = reader.load_data("input6.txt")
   answers = reader.split_answers(Lines)
   print answers
   
   count = reader.count_unique_answers(answers)
   
   print 'sum of counts = ' + str(count)
   
   print(separator)

