

# print(20)
# print(20)
# print(20)
# print(20)
# print(20)
# print(20)
# print(20)
# print(20)


n = 100
while n > 0:
    # print(n)
    n -= 1

if n > 0:
    # print(n)
    n -= 1
    # repeat
else:
    pass


name = "Erfan"
# print(name[2])
n = 0
while n < len(name):
    # print(name[n])
    n += 1


number = 123456
while number > 0:
    ones = number % 10
    # print(ones)
    number = number // 10


n = 0
while n < 100:
    if n % 3 == 0:
        print(n)
    elif n == 21:
        break
    else:
        pass
    n += 7
