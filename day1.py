#!/usr/bin/env
## the 1st question
fname=input("enter the first name")
lname=input("enter the last name")
print (lname ,fname)
###############################################################################################
## the 2nd question
num=int(input("enter the number"))
n1 = int('%i%i' % (num,num))
n2 = int('%i%i%i' % (num,num,num))
print(num+n1+n2)
###############################################################################################
## the 3rd question
doc=('a string that you "don\'t" have to escape \n This \n is a ..... multi-line \n heredoc string')
print (doc)
###############################################################################################
## the 4th question
import math
radius=int(input("enter the sphere radius"))
volume=(4/3)*math.pi*math.pow(radius,3)
print ("the volume of sphere is ",volume)
###############################################################################################
## the 5th question
base = int(input("enter the triangle base"))
height = int(input("enter the triangle height"))
area = 0.5 * base * height
print ("the area of triangle is ",area)
###############################################################################################
## the 6th question
rows = int(input("Enter the number of rows: ")) 
  
# Outer loop will print the number of rows  
for i in range(0, rows):  
    # This inner loop will print the stars  
    for j in range(0, i + 1):  
        print("*", end=' ')  
    # Change line after each iteration  
    print(" ")  
# For second pattern  
for i in range(rows + 1, 0, -1):  
    for j in range(0, i - 1):  
        print("*", end=' ')  
    print(" ")    

###############################################################################################
## the 7th question
word = input("enter a word")
for char in range(len(word) - 1, -1, -1):
  print(word[char], end="")
###############################################################################################
## the 8th question
for x in range(0,7) :
   if (x==3 or x==6) :
       continue
   print(x)    

###############################################################################################
## the 9th question
x = 0
y = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
for count in range (0,50):
  print(sum, end = " ")
  count += 1
  x = y
  y = sum
  sum = x + y
  print("\n")
###############################################################################################
## the 10th question
input_string=input("enter the string")
sum_char=0
sum_digit=0
for i in input_string :
    if i.isdigit():
        sum_digit += 1
    elif  i.isalpha():
        sum_char += 1
print("number of digits is ", sum_digit)
print("number of chars is ", sum_char)