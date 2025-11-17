# Control Flow

# age = int(input("Type your age: "))

# if age < 18:
#     print("You don't have access to this website.")

# else:
#     print("Welcome to our website!!")


num = int(input("Type your number: "))


# if not (num % 5 or num % 3):

if ((num % 5) == 0) and ((num % 3) == 0):
    print("FizzBuzz")
elif (num % 3) == 0: # 0, 1, 2
    print("Fizz")
elif (num % 5) == 0:
    print("Buzz")
else:
    print(num)



gpa = float(input("Type your GPA: "))

# A: 17 <= gpa <= 20
# Normal: 12 <= gpa < 17
# Fail: 0 <= gpa < 12
# else: Error ---

if gpa > 20 or gpa < 0:
    print("Wrong GPA score. Must be between 0 and 20!")
elif 17 <= gpa:
    print("You passed with A grade!")
elif 12 <= gpa:
    print("You passed!")
else:
    print("Sorry, you failed!")


