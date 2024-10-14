# for loop: just like while, but with a subtle difference
# for loop is used for iterating over iterables.

fruits = ['moz', 'angoor', 'khiar']

# print(fruits)

# for f in fruits:
#     print(type(f))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
numbers = list(range(14))

# for num in numbers:
#     print(num)

matrix = [
    [1, 4, 0], 
    [2, 5, 6], 
    [3, 6, 6]
]
i, j, k = matrix[0]

# print(matrix)
# for i, j, k in matrix:
#     print(i, j, k)
# Nerdy talk here later

# print(list(range(50, 100, 2)))

# for _ in range(5):
for i in range(5):
    # print(i)
    # print("Hi")
    pass


number = 123456
number = str(number)
# for digit in number:
#     print(digit)

# for i in range(10):
#     for j in range(10):
#         print(f'{i} * {j} = {i*j}')
#     print("-----------------")
    
# for row in matrix:
#     for num in row:
#         print(num, end=' ')
#     print()

a = 10
b = 20
c = 30

a, b = b, a

a, b, c = 10, 20, 30
# a, b, c = 10
values = [10, 20, 30]
a, b, c = values
print(a, b, c)


