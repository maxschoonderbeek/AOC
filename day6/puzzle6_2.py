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
      group_answers = []
      entry = []
      string = ''
      for idx in range(0,len(Lines)):
         if Lines[idx][0] != '\n':
            string = Lines[idx]
            string = string.replace('\n','')
            entry.append(string )
         else:
            group_answers.append(entry)
            entry = []
      group_answers.append(entry) # also append last one
      return group_answers
 
#broken 
   def count_unique_answers(self, group_answers):
      count = []
      for answers in group_answers:
         counter = 0
         for i in letters :
            for entry in answers:
               if i in entry :
                  counter += 1
            count.append(counter)
      return sum(count)

   def count_common_answers(self, group_answers):
      count = []
      for answers in group_answers:
         counter = 0
         for i in letters :
            letter_counter = 0
            for entry in answers:
               if i in entry :
                  letter_counter += 1
            if letter_counter == len(answers):
               counter +=1
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
   
   count = reader.count_common_answers(answers)
   
   print 'sum of common counts = ' + str(count)
   
   print(separator)

