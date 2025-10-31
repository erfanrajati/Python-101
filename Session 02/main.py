def generate_msg(name, lname):
    return f"Hello, {name} {lname}"


def main():
    name = input("Type your first name: ")
    lname = input("Type your last name: ")

    print(generate_msg(name, lname))


main()