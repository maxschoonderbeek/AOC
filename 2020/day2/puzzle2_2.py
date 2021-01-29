correct = 0
incorrect = 0 

file1 = open('input.txt', 'r') 
Lines = file1.readlines() 
  
for line in Lines:
   line = line.replace(":","")
   line = line.replace("\n","")
   string=line.split(' ')
   numbers = string[0].split('-')
   
   first = int(numbers[0])-1
   second = int(numbers[1])-1
   
   char = string[1]
   password = string[2];
   
   if ((password[first] == char) ^ (password[second] == char)):
      correct += 1
      print(string + ["correct"])
   else:
      incorrect += 1
      print(string + ["NOT correct"])

print(correct)