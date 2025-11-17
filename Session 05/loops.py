
# i = 0
# while i < 10:
#     print(i)
#     i += 1


# i = 0
# while i < 10:
#     print(i)
#     i += 2


# user_in = int(input("Type count: "))
# step = int(input("Type step: "))

# i = 0
# while i < user_in:
#     print(i)
#     i += step


def get_int():
    while True:
        user_in = int(input("Type bound: "))
        if user_in <= 0:
            print("Wrong input, try again!")
        else:
            break
    return user_in

def main():
    bound = get_int()

    i = 0
    while i < bound:
        if ((i % 5) == 0) and ((i % 3) == 0):
            print("FizzBuzz")
        elif (i % 3) == 0:
            print("Fizz")
        elif (i % 5) == 0:
            print("Buzz")
        else:
            print(i)
        i += 1

# main()




'''
7
5
#######
#######
#######
#######
#######
'''

# height = int(input("Type height: "))  # 10
# width = int(input("Type width: "))  # 5

# # counter
# i = 0
# while i < height:
#     # print('#' * width)
#     j = 0
#     while j < width:
#         print('#', end='')
#         j += 1
#     print()
#     i += 1


'''
5
#
##
###
####
#####
'''

count = int(input("Type count: "))

# i = 0
# while i < count:
#     j = 0
#     while j <= i: 
#         print('#', end='')
#         j += 1
#     print()
#     i += 1