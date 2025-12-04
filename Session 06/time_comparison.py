import random
import time

nums_list = list()
nums_set = set()

for i in range(1500000):
    nums_set.add(random.randrange(0, 15000000000))
    nums_list.append(random.randrange(0, 15000000000))


list_search_begin = time.time()
if 293746 in nums_list:
    print("found in nums list")
list_search_end = time.time()


set_search_begin = time.time()
if 324978 in nums_set:
    print("found in nums set")
set_search_end = time.time()


print("list search:", round(list_search_end - list_search_begin, 8))
print("set search:", round(set_search_end - set_search_begin, 8))