# DataTypes

a = 10
a = "10"
# These are different!
# First one's type is int, second one's is string.

# integer
a = 10
d = 20

print(a)
print(type(a))

# string
b = 'hello'
c = '10'

print(type(b))

# print(b + c)
# concatenation

# print(a + d)
# arithmetic addition

# print(a + c)
# Type Error

# float
a = 10.5

# print(a + 3)


# boolean
p = True      # 1
q = False     # 0

# print(p + q)

# type()
# print(type(a + 3))


# Type Casting
# Python is Dynamically Typed, meaning you can change the data type a variable however you like.
# Using these methods below (these are actually class initializers but more on that later!)
'''
int()
str()
float()
bool()
'''

b = '30'
c = int(b)
# print(type(c))

d = 25
# print(int(b) + d)
# print(b + str(d))
# print(b)

# userAge = int(input())
# ValueError
# print(userAge / 5)


# Truthiness / Falseness, the idea of casting other types to booleans
q = 0
p = bool(q)
# print(p)
# print(q)

age = -10
# 0    -> False
# ..., -3, -2, -1, 1, 2, 3, ...    -> True
# print(bool(age))

name = 'Erfan'
# print(bool(name))

number = '0'
# print(type(number)) # returns string
# print(bool(number)) # return True
# print(bool(int(number)))
