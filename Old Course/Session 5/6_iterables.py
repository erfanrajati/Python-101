# [] Brackets - Braces
# {} Curly Braces
# () Parenthesis
# " Double Quotation
# ' Single Quotation
# / Forward Slash
# \ Backward Slash

# Lists

b = [1, 2, 3]
a = [1, '2', 3, '4', True, 12.4, b]


# print(a[6])

list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# print(list1[-1])

# List Slicing
# print(type(list1[0:1]))

# print(type(list1[0]))

# print(list1[3:10:2])
# print(list1[3:])
# print(list1[:9])
# print(list1[::-1])
# print(list1[::-2])


name = "Erfan Rajati Haghi"
# name = input()
# print(name[::-1])
mylist = list(name)
# print(mylist)

# a = list(190) # Raise Error

# Nested Lists
matrix = [
    [1, 4, 0], 
    [2, 5, 6], 
    [3, 6]
]

# print(matrix[::-1])


# Looping over the list
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
n = 0
while n > -(len(list1)+1):
    n -= 1
    # print(list1[n])

# print(a)

message = "Python"
n = 0
while n < len(message):
    # print(message[n], end='')
    n += 1



list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list2 = []
n = 0
while n < len(list1):
    if list1[n] % 3 == 0:
        list2.append(list1.pop(n))
    else:
        n += 1

print(list1)
print(list2)