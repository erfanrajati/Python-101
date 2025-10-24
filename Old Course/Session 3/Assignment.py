# Code a simple calculator

'''
input:
3
+
6

output:
9
'''

while True:
    num1 = int(input())
    opr = input() # exit
    num2 = int(input())

    if opr == '+':
        print(num1 + num2)
    elif opr == '-':
        print(num1 - num2)
    elif opr == '*':
        print(num1 * num2)
    elif opr == '/':
        print(num1 / num2)
    elif opr == 'exit':
        break
    else:
        print('wrong input.')

