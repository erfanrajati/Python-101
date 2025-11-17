def get_int():
    user_in = input("Type an integer: ").strip()
    user_in = int(user_in)
    return user_in

def is_odd(khar):
    return khar % 2

    # return "Even" if khar % 2 == 0 else "Odd"

    # if khar % 2 == 0:
    #     return "Even"
    # else:
    #     return "Odd"

def main():
    # get the number from user
    # cast number to int
    user_in = get_int()

    # check if number is even or odd
    status = is_odd(user_in)

    # print result!
    print(
        "The given number is:", 
        "Odd" if status else "Even"
    )


main()