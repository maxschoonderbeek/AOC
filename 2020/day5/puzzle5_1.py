#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent Of Code - Day 5 - Part 1
#
#-------------------------------------------------------------------+

#-------------------------------------------------------------------+
#	dependencies
#-------------------------------------------------------------------+

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
         file =  open(filename)
         entries = file.readlines()
      except Exception as e:
         print("Exception: {}".format(e))
         return [""]
      else:
         return entries  
	
   def convert_passes(self, passes):
      boarding_seats = []
      for bpass in passes:
         boarding_seats.append(self._calculate3(bpass))
      return boarding_seats
   
   def _calculate(self, bpass):
      max_row_idx = 7
      row = 0
      max_column_idx = 3
      column = 0
      # use bitwise shift i.s.o. power
      for idx in range(max_row_idx):
         if(bpass[idx] == 'B'):
            row = row + 2**(max_row_idx-idx-1)
      
      for idx in range(max_column_idx):
         if(bpass[max_row_idx + idx] == 'R'):
            column = column + 2**(max_column_idx-idx-1)   
      
      return row * 8 + column
 
   def _calculate2(self, bpass):
      max_idx = 10
      count = 0

      for idx in range(max_idx):
         count = count << 1
         if bpass[idx] == 'B' or bpass[idx] == 'R' :
            count = count | 1
         print bin(count)
      
      return count
 
   def _calculate3(self, bpass):
      bpass = bpass.replace('F','0')
      bpass = bpass.replace('B','1')
      bpass = bpass.replace('L','0')
      bpass = bpass.replace('R','1')
      bpass_nr = int(bpass, 2)
      
      return bpass_nr
 
 
#-------------------------------------------------------------------+
#	startup
#-------------------------------------------------------------------+
if __name__ == "__main__":
   separator = "\r\n+----------------------------+\r\n"
   print(separator)
   reader = Reader()
   Lines = reader.load_data("test.txt")
   boarding_passes = reader.convert_passes(Lines)
   boarding_passes.sort()
   
   for idx in range(len(boarding_passes)):
      if boarding_passes[idx] != min(boarding_passes)+idx:
         print 'missing pass = ' + str(boarding_passes[idx]-1)
         break
            
   print '  highest = ' + str(max(boarding_passes))
   
   print(separator)

