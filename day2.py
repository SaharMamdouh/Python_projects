## question 1
def reduction_func (li) :
    for k in li :
        if li.count(k) > 1 :
            li.remove(k)

    print(li)    
x=[1,2,3,4,4,4] 
reduction_func (x)  
######################################################################
## question 2
string1=input("enter the string ")
total_length1=len(string1)
if (total_length1 %2 == 0):
   length1=int(0.5*total_length1)
   part1=string1[0:length1]
   part2=string1[length1:total_length1]
   print(part1)
   print(part2)

elif (total_length1 %2 != 0):
   length1=int(0.5*total_length1)+1
   part1=string1[0:length1]
   part2=string1[length1:total_length1]  
   print(part1)
   print(part2)


string2=input("enter the string ")
total_length2=len(string2)
if (total_length2 %2 == 0):
   length2=int(0.5*total_length2)
   part12=string2[0:length2]
   part22=string2[length1:total_length2]
   print(part12)
   print(part22)

elif (total_length2 %2 != 0):
   length2=int(0.5*total_length2)+1
   part12=string2[0:length2]
   part22=string2[length2:total_length2]
   print(part12)
   print(part22) 

a="a-"
b="b-"  
print(a,part1, b,part12 ,  a,part2 , b,part22)     

#######################################################################
## question 3
def check_func (lis):
    lis_length=len(lis)
    lis_set_length=len(set(lis))
    if (lis_length==lis_set_length) :
        print("TRUE")
    else : 
        print("FALSE")    
     
y=[1,2,3,4,4,4] 
check_func (y)
#######################################################################
#question 4
arry=[1,5,7,2,4,3]

def bubble_sort(array):
    x=len(array)
    for i in range (x):
        for j in range (0,x-i-1):
            if (array[j] > array[j+1]):
                 array[j], array[j+1]=array[j+1] , array[j]

    print ("sorted array is ",array)

bubble_sort (arry)
########################################################################
#question 5
import random
## generating random number from the game 
game_num=random.randint(0,100)
print(game_num)
counter=0
numbers=[]
while counter < 10 :
    input_num=int(input("enter the number"))

    if (input_num != game_num and input_num < 100 and input_num not in numbers): 
        print ("In correct number ")
        counter+=1

    elif (input_num >= 100 ): 
        print ("It's not allowed ")
        
    elif (input_num in numbers):
          print ("you entered this number before ! ")

    elif (input_num == game_num): 
        print (" * Congratulations * ")
        game_num=random.randint(0,100)
        counter+=1      

    numbers.append(input_num)     

print ("You finished all your trials ..Do you want to play again ?")
##################################################################################
###Bonus######
## creating a square matrix
## i counter of rows
## j counter of columns
import random
mtx=[]
for i in range(3):
    row=[]
    for j in range (3):
        co=random.randint(-100,100)
        row.append(co)
    mtx.append(row)    
print(mtx)   

sum1=0
for k in range (3):
   # print(mtx[k][k])
    sum1+=mtx[k][k]
print(sum1)

sum2=0
for l in range (3):
   # print(mtx[l][2-l])
    sum2+=mtx[l][2-l]
print(sum2)

absolute_difference=abs(abs(sum1)-abs(sum2))
print("the absolute difference between the diagonal sum of the matrix is ",absolute_difference)
