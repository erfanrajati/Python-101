user_1 = input("choose from r, p, s: ")
user_2 = input("choose from r, p, s: ")

if user_1 == user_2:
    print("tie")
elif user_1 == 'p' and user_2 == 'r':
    print("user_1 wins")
elif user_1 == 'r':
    print("you win.")
elif user_1 == 'r' and user_2 == 'p':
    print("user_2 wins")
elif user_1 == 'r':
    print("you win.")
elif user_1 == 's' and user_2 == 'p':
    print("user_1 wins")
elif user_1 == 's' and user_2 == 'r':
    print("user_2 wins")
else:
    print("wrong input.")