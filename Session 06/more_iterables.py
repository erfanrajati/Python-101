# Data Structure

# a = 10 # -> 8 bit

# c = 'a'

# f = 10.5 # -> 8 bit

# b = True # -> 1 bit

# arr = []

i = 0
# print(id(i))

i += 1
# print(id(i))


nums = [1, 2, 3, 4]
# print(id(nums))

nums = nums + [1]
# print(id(nums))


nums = [1, 2, 3, 4]
# print(id(nums))

nums[2] = 10 # item assignment
# print(id(nums))

i = [1, 2, 3, 4]
j = [1, 2, 3, 4]
# print(id(i))
# print(id(j))
# if i is j:
#     print("matched")
# else:
#     print("not matched")


name = 'channel 1337'

# name[2] = '&'

# Mutable vs Immutable

# i = 10
# i += 1

nums = [1, 2, 3, 4]
# print(id(nums))

nums.append(5)
# print(id(nums))




nums_list = [1, 2, 3, 4] # mutable
nums_tuple = (1, 2, 3, 4) # immutable

# nums_tuple[1] = 10
# del nums_list[1] # deprecated

nums_list.remove(3) # remove by value
popped = nums_list.pop(0) # remove by index

# print(nums_list)

nums_list = [1, 2, 3, 4] # mutable
nums_tuple = (1, 2, 3, 4) # immutable

nums_set = {1, 2, 3, 4} # immutable, no indexing, no order, no item repetition

# print(nums_set[2])

# nums_set.add(10)
# print(nums_set)


stu1 = {
    'name':'Erfan',
    'lname':'Rajati',
    'stu_number': 4916982632
}

students = [
    {
        'name': 'Sheldon',
        'lname': 'Cooper',
        'Expertise': 'Theoretical Physics'
    },
    {
        'name': 'Leonard',
        'lname': 'Hofstater',
        'Expertise': 'Applied Physics'
    },
    {
        'name': 'Howard',
        'lname': 'Volowetz',
        'Expertise': 'Engineer!!'
    },
]


leonard = students[1]

# for k, v in leonard.items():
#     print(k, v)

# a, *b = 1, 2, 2, 4, 6
# print(a)
# print(b)

# for stu in students:
#     for k, v in stu.items():
#         print(f"{k:<10} {v:}")
#     print("-----------")


info = {
    'time': 10,
    'day': 20,
}

info.pop('time')

print(info)