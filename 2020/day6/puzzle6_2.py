#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 6 - Part1 & Part 2
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
 
   def count_any_answers(self, group_answers):
      counter = 0
      for answers in group_answers:
         combined_answer = ''.join(answers)
         for i in letters :
            if i in combined_answer :
               counter += 1
      return counter

   def count_common_answers(self, group_answers):
      counter = 0
      for answers in group_answers:
         for i in letters :
            letter_counter = 0
            for entry in answers:
               if i in entry :
                  letter_counter += 1
            if letter_counter == len(answers):
               counter +=1
      return counter
      
#-------------------------------------------------------------------+
#	startup
#-------------------------------------------------------------------+
if __name__ == "__main__":
   separator = "\r\n+----------------------------+\r\n"
   print(separator)
   
   reader = Reader()
   Lines = reader.load_data("input6.txt")
   answers = reader.split_answers(Lines)

   unique_count = reader.count_any_answers(answers)
   print 'Sum of "Anyone answered yes" = ' + str(unique_count)
   
   count = reader.count_common_answers(answers)
   print 'Sum of "All of group answered yes" = ' + str(count)
   
   print(separator)

