import re
import os

correct = 0
incorrect = 0 

script_dir = os.path.dirname(__file__)
rel_path = 'input.txt'
abs_file_path = os.path.join(script_dir, rel_path)
file1 = open(abs_file_path, 'r') 
Lines = file1.readlines() 
  
for line in Lines:
   line = line.replace(":","")
   line = line.replace("\n","")
   string=line.split(' ')
   numbers = string[0].split('-')
   lower_boundary = int(numbers[0])
   upper_boundary = int(numbers[1])
   
   char = string[1]
   password = string[2];
   count = password.count(char)
   
   if (lower_boundary <= count <= upper_boundary):
      correct += 1
      print(string + ["correct"])
   else:
      incorrect += 1
      print(string + ["NOT correct"])

print(correct)