text = "hello world!"
textLen = len(text)
yellow = (255,255, 0)
r, g, b = yellow

# Dictionary
person = {
  "name": "Alice",
  "email": "alice@example.com"
}

# Set
x = {1,2,3,2,1}

# Boolean
yes = True
no  = False

print(text)
print(textLen)
print(r, g, b)
print('Person Name: ' + person["name"])
print('Person Email: ' + person["email"])
print(x)
print(yes)
print(no)

# print function
print('hello', 1, 2, 3)

# print length of array
print(len(['a', 'b', 'c']))

# print with int convertion
print(5 + int("2"))

# print with str convertion
print(str(5)+ "2")

# writing custom functions
def square(x):
  return x * x

def sum_of_squares(x,y):
  return square(x) + square(y);

clone_square = square
print(square(5))
print(square(2*5))
print(sum_of_squares(2, 1))
print(clone_square(9))

pi = 3.14
def area(r):
  return pi * square(r)

print(area(10))

a = 2
def f(v):
    a = square(v)
    return a
b = f(3)
print a, b

# Using built-in function
print min(2,3)
print max(2,3)

# Write a function count_digits to find number of difits in the given number
def count_digits(test):
  return len(str(test))

print count_digits(5)
print count_digits(12345)

# Use upper function
str_1 = "hello"
print(str_1.upper())

# Write a function istrcmp to compare two strings, ignoring the case
def istrcmp(str1, str2):
  return str(str1).lower() == str(str2).lower()

print istrcmp('python', 'Python')
print istrcmp('LaTex', 'Latex')
print istrcmp('a', 'b')

# What will be output of the following program
print 2 < 3 and 3 > 1 #true
print 2 < 3 or 3 >1   #true
print 2 < 3 or not 3 > 1 #true
print 2 < 3 and not 3 > 1 #false

# What will be output of the following program
x1 = 4
y1 = 5
p1 = x1 < y1 or x1 < z1
print(p1) #

# What happens when the following code is executed? Will it give any error ? Explain the reasons
x2 = 2
if x2 == 2:
  print(x2)
else: 
  print(y2)

# Lists
x3 = [1,2,3]
print len(x3)

# Modules
import time
import sys
print time.asctime()








