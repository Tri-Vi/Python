# 2.1 Lists

a = [1,2]
b = [1.5, 2, a]
x = range(1,5)
c = [1,2,3]
d = [4,5]
e = range(10)
d.append(6)

#print statements
print b
print x
print len(x)
print(c+d)
print(x[0:2])
print(x[1:4])
print(e[0:6:2])
print(e[::-1])
print(2 in e)
print(10 in e)
print(d)

# Problem 1: What will be the output of the following program?
x1 = [0,1, [2]]
x1[2][0] = 3
print(x1)
x1[2].append(4)
print(x1) 
x1[2] = 2
print(x1)

# 2.1.1 The for Statement
for x2 in [1,2,3,4]:
  print(x2)
for i in range(10):
  print(i, i*i, i*i*i)

print(zip(["a", "b", "c"], [1,2,3]))

names = ["a", "b", "c"]
values =[1,2,3]
for name, value in zip(names, values):
  print(name, value)

#Problem 2: Python has a built-in function sum to find sum of all elements of  a list. Provide an impmementation for sum
print(sum([1,2,3]))

#Problem 3: What happesn when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.
def my_sum(arr):
  text = ""
  for x in arr:
    text += x
  return text
print(my_sum(["hello", "world"]))
print(my_sum(["aa", "bb", "cc"]))

#problem 4: Implement a function product to compute a product of a list of numbers
def product(aList):
  result = 1
  for x in aList:
    result *= x
  return result

print(product([1,2,3]))

#problem 5: Write a function **factorial** to compute a factorial of a number. Can you use the product function defined in the previous example to compute factorial?
def factorial(num):
  result = 1
  while num > 0:
    result *= num
    num = num - 1
  return result

print(factorial(4))

# Problem 6: Write a function **reverse** to reverse a list. Can you do this withou using list slicing?
def reverse(aList):
  listLen = len(aList)
  reverseList = []
  while listLen > 0:
    reverseList.append(aList[listLen-1])
    listLen -= 1
  return reverseList

print(reverse([1, 2, 3, 4]))
print(reverse(reverse([1, 2, 3, 4])))

# Problem 7: Python has built in functions **min** and **max** to compute minimum 