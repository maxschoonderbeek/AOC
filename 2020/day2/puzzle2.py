

import string

correct = 0
incorrect = 0 

file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
count = 0
# Strips the newline character 
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