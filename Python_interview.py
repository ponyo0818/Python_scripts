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
    print('{0:2d} {1:3d} {2:4d}').format(x, x*x, x*x*x))
