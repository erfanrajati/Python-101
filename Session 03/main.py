def get_int():
    user_in = input("Type an integer: ").strip()
    user_in = int(user_in)
    return user_in

def check_odd_even(khar):
    is_odd = bool(khar % 2)
    is_even = not is_odd
    return is_odd, is_even

def main():
    # get the number from user
    # cast number to int
    user_in = get_int()

    # check if number is even or odd
    is_odd, is_even = check_odd_even(user_in)

    # print result!
    print("is the number odd?", is_odd)
    print("is the number even?", is_even)


main()