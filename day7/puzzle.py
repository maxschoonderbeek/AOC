#!/usr/bin/env python

#-------------------------------------------------------------------+
#
# Advent of Code - Day 7
#
#-------------------------------------------------------------------+

#-------------------------------------------------------------------+
#	dependencies
#-------------------------------------------------------------------+

#-------------------------------------------------------------------+
#	main algorithm
#-------------------------------------------------------------------+

class reader:
	def __init__(self):
		pass
    
	# load input
	def _load_data(self, filename) :
		# if a filename is given, try to load it
		try:
			# entries = [data.rstrip() for data in open(filename)]
			with open(filename) as f:
				entries = f.read().split("\n\n")
		except Exception as e:
			print("Exception: {}".format(e))
			return [""]
		else:
			return entries
		

class processor

#-------------------------------------------------------------------+
#	startup
#-------------------------------------------------------------------+
if __name__ == "__main__":
	separator = "\r\n+----------------------------+\r\n"
	print(separator)
    reader = reader()
    reader.load_data("test.txt")
    
	print(separator)