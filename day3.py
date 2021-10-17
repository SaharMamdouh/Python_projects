##question 1########################
# read file
words=[]
words_dict={}
filee = open('test.text', 'r')
for line in filee:
    #split each line in the file into words
    line1=line.split()
    for word in line1:
       ##count number of repetition in each word 
        counter=line1.count(word)
        #create a dictionary has a word as a key and count as a corresponding value 
        words_dict[word] = counter
#sort the dictionary descending w.r.t the value        
a1_sorted_keys = sorted(words_dict, key=words_dict.get, reverse=True)
#select the first 20 words (keys) from the dictinary
for i in range (0,20):
    words.append(a1_sorted_keys[i])
#print(words)
#convert word from alist into string to can be written in the new file     
string_words=', '.join(words)    
#creating a new file to write the most 20 repeated words
f = open("popular_words.txt", "w")
f.write(string_words)
f = open("popular_words.txt", "r")
print(f.read())
filee.close()
f.close()
#############################################################################
#question 2 ####################
import math
def calc_distance(x1,x2,y1,y2):
    d1 = math.pow((x2-x1),2)
    d2 = math.pow((y2-y1),2)
    d=math.sqrt(d1+d2)
    print("distance is ",d)

X1=float(input("enter the value of x1"))  
X2=float(input("enter the value of x2"))   
X3=float(input("enter the value of x3"))   
X4=float(input("enter the value of x4"))    

calc_distance(X1,X2,X3,X4)
############################################################################
#question 3 ######################
class vechile:
     def __init__(self):
         print(self)
   
##########################################################################    
#question 4 ######################
class Vechile:
     def __init__(self,max_speed,mileage):
         self.max_speed=max_speed
         self.mileage=mileage
         
obj= Vechile(120,5000)  
print("the max speed is ", obj.max_speed)       
print("the mileage is " ,obj.mileage) 
#########################################################################
##question 5 ####################
string="welcome to iti python track"
li_string=string.split()
li_string.reverse()
reversed_string= ' '.join(li_string)
print(reversed_string)
#######################################################################
##question 6 #####################
class get_print :
    def __init__(self):
        self.string1=""

    def get_string(self):
        self.string1=input("enter the string")
        
    def print_string(self):
        print(self.string1.upper())

objct=get_print()
objct.get_string()
objct.print_string()
####################################################################
#question 7 #####################
import math
class circle:
    def __init__(self,radius):
        self.radius=radius

    def calc_area(self):
        self.area=math.pi*math.pow(self.radius,2)  
        print("the area of the circle is ",self.area)  

    def calc_perimeter(self):
        self.perimeter=2*math.pi*self.radius 
        print("the perimeter of the circle is ",self.perimeter)    

obj_circle=circle(5)  
obj_circle.calc_area()
obj_circle.calc_perimeter()      