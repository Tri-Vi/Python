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

