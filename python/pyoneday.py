#!/usr/bin/env python3

print("Hello World!!!!!!!!!")
newString = "Hello World".replace("World", "Universe")
print(newString)
'''
def times(a, b):
	return a * b
	
nam = times(2, 4)
print(nam)

def times(a, b):
	print (a * b)
	
times(2, 4)
'''

"""
 Without a return statement in function, 
 a function cannot communicate back to the caller of the function. 
 Hence, a variable cannot receive value from function.
 Also a return also replaces functions call with the returned value
"""

# This tzpe of argument is called Formal arg.

'''
def checkIfPrime (numberToCheck):
	for x in range(2, numberToCheck):
		if (numberToCheck%x == 0):
			return False
	return True
response = checkIfPrime (13)
print (response)
'''

# NB: All parameter with default values must be placed at the end of the parameter list 

'''
def fxn (a, b, c=1, d=2):
	print(a, b, c, d)

fxn(5, 10)
'''

# Variable Length Argument List
# (single) * before a parameter is telling the compiler that a function is taking more 
# than one arguments. Called Non-KeyWorded variable lenght argument list


def addNum (*num):
	sum = 0
	for i in num:
		sum += i
	print(sum)

addNum(12, 12, 10)
addNum(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#(double) **before a parameter denote KeyWorded variable lenght argument list i..e Dictionary

"""
def printage (**age):
	for i,j in age.items():
		# print("Name = %s, Age = %s" %(i, j))
		print(f"Name = {i}, Age = {j}")

printage(Yusuf =30, Sekinat = 31)
printage(Yusuf =30, Sekinat = 31, Zayd = 6, Nna = 3, Baby = 2)
"""

#If our function uses all the three args, it must follow the below order:
#		def someFunction2(farg, *args, **kwargs):



					# MODULES: 
# Pzthon comes with a large no of build-in functions saved in files called Modules.
# To use them we must import them into our program.
# three ways to import modules:

'''
#1
import random
random.randrange(2, 20)

#2
import random as r
r.randrange(1, 10)

#3--> importing specific fxn from modules
from random import randrange
from random import randrange, randint, randbytes
randrange(1, 18)
'''
				#WORKING WITH FILES

# Opening and Reading Text Files
#1. Using readline method

'''
f = open ('myfile.txt', 'r')

firstline = f.readline()
secondline = f.readline()
thirdline = f.readline()

print(firstline, end='')
print(secondline, end='')
print(thirdline, end='')

f.close()	# alwazs close file after reading to free up anz szstem resources
'''

#2. Using for loop to read text files

'''
f = open('myfile.txt', 'r')
for line in f:
	print(line, end='')
f.close()
'''

# Writing to a text file

'''
f = open('myfile.txt', 'a')
f.write("\n This sentence will be appended.")
f.write("\n Python is fun.")
f.write("\n It's getting easier.")
f.write("\n Alhamdulillah.............")
f.close()
'''

## Opening and Reading Text Files by Buffer Size

'''
inputfile = open ("myfile.txt", "r")
outputfile = open ("myoutputfile.txt", "w")

msg = inputfile.read(10)

while len(msg):
	outputfile.write(msg) #To print the character on a newline: outputfile.write(msg + "\n")
	msg = inputfile.read(10)

inputfile.close()
outputfile.close()
'''

## Opening, Reading and Writing Binary Files


inputfile = open ("files.png", "rb")
outputfile = open ("myoutputfile.png", "wb")

msg = inputfile.read()

while len(msg):
	outputfile.write(msg) 
	msg = inputfile.read()

inputfile.close()
outputfile.close()


# Deleting and Renaming Files
# remove() and rename() ~~> os modules; imported

'''
from os import remove, rename
remove("myoutputfile.png")

#rename("old-name" "new-name")
rename("files.png", "renamedbypython.png")
'''
