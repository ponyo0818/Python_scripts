# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 15:06:42 2019

@author: Yuan
"""
#1 for loop
for i in range(2,9):
    print (i)


#2 while loop
i = 1
while i<=10:
    print (i)
    i+=1

#3 if, elif, else
a = 10
b = 20
if a<b:
    print ("{} is less than {}".format(a,b))
elif a == 20:
    print ("{} is equal to {}".format(a,b))
else:
    print ("{} is greater than {}".format(a,b))


#4 past experience with python, e.g. move files to another folder

import os, glob
os.chdir("C:/Users/Yuan/Pictures/PICTURES/1-20")
for file in glob.glob("*.jpg"):
    print(file)


#Fizz Buzz
for num in range(1,101):
    if num % 5 ==0 and num % 3 == 0:
        print ("FizzBuzz")
    elif num % 5 == 0:
        print ("Fizz")
    elif num % 3 == 0:
        print ("Buzz")
    else:
        print (num)

# Fibonacci Sequence
a, b = 0, 1
for i in range(0,10):
    print (a)
    a, b = b, a+b

# google python interview question
#Basic data type

# lists are mutable whereas tuples are immutable
#Lists
my_list = [10,20,30]
for i in my_list:
    print (i)

#Tuples
my_tup = (1,2,3)
for i in my_tup:
    print(i)

#Dict
my_dict = {'name': 'Tom', 'age':'2', 'occupation':'teacher'}
for key,val in my_dict.iteritems():
    print ("My {} is {}".format(key,val))

#Set :values are unique in the set
my_set = {10,20,30}
for i in my_set:
    print (i)

#OOP in python: need to write this over and over
#1.self is used to make an instance of class
class Person(object):
    def __init__(self, name):
        self.name = name
    def reveal_identity(self):
        print (" My name is {}".format(self.name))

class SuperHero(Person): #SuperHero class is inherit from Person class
    def __init__(self, name, hero_name):
        super(SuperHero, self).__init__(name)
        self.hero_name = hero_name
    def reveal_identity(self):
        super(SuperHero, self).reveal_identity()
        print ("...And I am {}".format(self.hero_name))

corey = Person('Corey')
corey.reveal_identity()
#OR
wade = SuperHero('Wade Wilson', 'Deadpool')
wade.reveal_identity()


#format output
#replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
for x in range(1,11):
    print(('{0:2d} {1:3d} {2:4d}').format(x, x*x, x*x*x))
    
#Write to count the number of capital letters in a file
#take input in console
message = input("Type word:")
print("capital letters:", sum(1 for c in message if c.isupper()))
# read txt file
with open('C:/Users/Yuan/Desktop/cs/python/interview/file.txt','r')as f: 
#f= open('C:/Users/Yuan/Desktop/cs/python/interview/file.txt','r')
    count = 0;
    text = f.read(); #return the whole text, readline()return line
    for character in text:
        if character.isupper():
            count+=1
print(count)   
#f.close() no need when using "with"

#Write to count the number of lines in a txt file
def lineCounter(filename):
    count=0
    with open(filename) as file:
        for line in file:
            if line.strip(): #non_blank line counts, blankline returns empty string
                count+=1
    return count
print(lineCounter("C:/Users/Yuan/Desktop/cs/python/interview/file2.txt"))

#OR
def lineCounter(filename):
    with open(filename) as file:
        return  sum (1 for line in file if line.strip()) #use generator expression
        
print(lineCounter("C:/Users/Yuan/Desktop/cs/python/interview/file2.txt"))

    
#Sort a numerical list
list = [1, 2, 5, 4, 3, 6]
list.sort()
print(list)

#convert string list to num list
list = ['1', '3', '5']
print(type(list[1]))
list = [int(i) for i in list]
print(type(list[1]))

#reverse a list 
list.reverse()

#remove and return the last object from a list
list.pop(obj = list[-1])

#Explain split(), sub(), subn() methods of “re” module [regular expression operations]
# 1. split() method returns a list of strings after breaking the given string by the specified separator.
#str.split(separator, maxsplit)
text = 'ponyo is a fish'
print(text.split())
# Splitting at 3 
word = 'CatBatSatFatOr'
print([word[i:i+3] for i in range(0, len(word), 3)]) 

#2. sub(): This method is used to find a substring where a regex pattern matches and 
#then it replaces that matched substring with a different string.
import re
text = "she is very good"
text2 = re.sub("good","cool",text)
print(text2)

## re.sub(pat, replacement, str) -- returns new string with all replacements,
## 1 is group(1), 2 group(2) in the replacement
phone = "2004-959-559 # This is Phone Number"
# Delete Python-style comments
num = re.sub(r'#.*$', "", phone)
print ("Phone Num : ", num)

# Remove anything other than digits
num = re.sub(r'\D', "", phone)    
print ("Phone Num : ", num)

#More about python regular expression pattern
#https://www.tutorialspoint.com/python/python_reg_expressions

#range() used to iterate in for loops, it return a list, take more memory than xrange which is only used in python2
for i in range(7,17):
    print(i)

#Define pickling and unpickling 
# Pickling - is the process whereby a Python object hierarchy is converted into a byte stream, 
    #putting data into a form that can be stored in a file and retrieved later. 
# Unpickling - is the inverse operation, whereby a byte stream is converted back into an object hierarchy.  
import pickle

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
output = open('data.pkl', 'wb')
# Pickle dictionary using protocol 0.
pickle.dump(data1, output)
# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)
output.close()    


#map function
#The map() function in Python has two parameters, function and iterable. The map() function takes a function as an 
#argument and then applies that function to all the elements of an iterable, passed to it as another argument. It 
#returns an object list of results.
def calculatesq(n):
    return n*n
numbers = [2,3,4,6]
result = list(map(calculatesq,numbers))
print(result)

#get indice of N max values in a Numpy array
#numpy.argsort(a, axis=-1, kind=None, order=None)Returns the indices that would sort an array.
#[0 2 1 3 4 5]

#The[:] means "take everything in this dimension" and the [::-1] means "take everything in this dimension but backwards."
import numpy as np
ar = np.array([1, 3, 2, 4, 5, 6])
print(ar.argsort()[-3:][::-1])


"""with statement-open a file and close it asa the block of code
   with open ("filename","mode") as file_name"""
f = open ("C:/Users/Yuan/Desktop/cs/python/interview/file2.txt","w+") #open a file for writing
for i in range(10):
    f.write("This is line %d\r\n" %(i+1)) #%d interger,\n go next line,\r like enter
f.close()

#a+ append mode
f = open ("C:/Users/Yuan/Desktop/cs/python/interview/file2.txt","a+") 
for i in range(11,20):
    f.write("Appended line %d\r\n"% (i))
f.close()
# r in read mode

#display the contents of a file in reverse.
for line in reversed(list(open("C:/Users/Yuan/Desktop/cs/python/interview/file2.txt"))):
    print(line.rstrip()) #remove leading whitespaces
#str.rstrip() all chars have been stripped from the end of string, lstrip() is from the right of string
    
f = open("c:/hello.txt", "wt") #w-open for writing, t-text mode

#Lambda function: powerful when use it as anonymous fuctions inside another function
# add 10 to the number passed in as an argument
x = lambda a: a+10
print(x(5))

x= lambda a, b, c: a*b+c
print(x(2,3,4))
# use the same function to make both functions 
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))


#list() constructor creates a list
x = ['abc','cde']
print(list(map(list,x)))

#construct a set
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)

#functional programming-writing pure functions
list(map(lambda x : x*x, range(10)))

import functools
#reduce() do the deuction 1-2-3-4-5
functools.reduce(lambda x,y:x-y,[1,2,3,4,5])

#check palindrome
def checkPalindrome(string):
    if (string == string[::-1]):
        return True
    return False
print(checkPalindrome("madam"))
    

#calculate the sum of a list of number
def calSum(num):
    return sum(num[::])
print(sum([2]))
    
#read a random line in a file
import random
def readRandom(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(readRandom('C:/Users/Yuan/Desktop/cs/python/interview/file2.txt'))
    

