## The configuration below is necessary for Python 2
# coding=utf-8

# How to print a message
print('Hello world')

# How to print the result of add operation
print(7+4)

# How to print the result of a concatenation of two numbers as a string
print('7' + '4')

# The print below will throw a TypeError
# TypeError: cannot concatenate 'str' and 'int' objects
#print('Olá' + 5)

# How to print a string and a number
print('Hello', 5)

# Defining variables

name   = 'Elton Douglas de Oliveira'
age    = 39
height = 1.16 #Meters 

print(name, age, height)

# Reading data from standard input
name   = input('What is your name?: ')
age    = input('How old are you?: ')
height = input('What is your height?: ')

print(name, age, height)
