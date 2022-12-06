# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")
# '#' comments out a line 
'''its called a multilined comment'''
'''Data types in python 
Integers Floatings Strings Booleans none 

...Operators in python ...
arithmetic : +.-,*,/
assignement : =,+=,-=,
comparison operators : ==,>,>=,<,!=
logical operators : and,or,not
...type() gives data type of input variable 
'''
a = 31
b = "Vighnesh"
print(type(a))
print(type(b))

#a number can be converted into string with help of ""
print(int(a))  #int converts the given string into int
#input()Function 
#allows user to take input from keyboard as a string


#write a program to add 3 input digits 
'''a = int(input("Enter the value of a "))
b = int(input("Enter the value of b "))
c = int(input("Enter the value of c "))
print(a+b+c)'''

'''num = int(input("Enter the value of num"))
print(num%2)'''

#to find the type of input 

#Var = (input("Enter your Var "))
#print(type(Var))

#to square a given number 
#TSq = int(input("Enter the number :"))
#print("the square of Tsq is ",TSq*TSq)

#Chapter 3 Strings
#String Slicing Vighnesh ,0 = v,1 = i ...7 = h

MyStr = "Vighnesh"
MyStr2 = "Vighnesh is a good boy"
print(MyStr[0:3])
print(MyStr[-3])
#len 
print(len(MyStr))
#Ends with
print(MyStr.endswith("esh"))
#String.count(i) - counts total numbers of i 
print(MyStr.count("h"))
#Strin. Capitalize - capitalizes first 
#String.find(word)
print(MyStr2.find("good"))
#String.replace(oldword,newword)
#print(MyStr2.replace("a good","best"))
#Escape sequence Characters 
#\n = new line
#\t = tab 
#\' = single quote 
#\\ = backslash 


#'''Chapter 3 practice set'''
#
#nam = input("Enter the name : ")
#print("Good Evening ",nam)

#
#letter = '''Dear <!name!> 
            #you are selected!
           # <!Date!>'''
          # '''
#print(letter.replace("<!name!>","Vighnesh").replace("<!Date!>","6 dec 2022"))

#finding double spaces in a string
'''
Nstr = "today is a  really great day"

print(Nstr.find("  "))'''
#replacing a double space with single space 
#Nstr = "today is a  really great day"

#print(Nstr.replace("  "," "))


#letter = "Dear harry\n this cource \nis nice\t "
#print(letter)

#List and Tuples
#Lists = ["",""]  a set which can store any number of datatype 
#List indexing 
#Mylis = ["Vighnesh",7,37,]
#print(Mylis[1])
#list methods 
l1 = [1,8,7,2,21,15]
'''print(l1.sort())#sorts the list in assending order 
print(l1.reverse())
print(l1.append(8))#adds 8 at the end of the list 
print(l1.insert(3,8))#adds 8 at 3 index 
print(l1.pop(2))#will remove the element at index 2 and return its value 
print(l1.remove(8))'''


#tupels in pyhton = immutabke data type in python 

