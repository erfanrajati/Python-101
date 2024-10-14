# Write a password checker program


# we need to store a password: Done
# we need to get the password from user: Done
# we need an algorithm to compare passrwords: Done
# main loop: Done
# Debug

while True:
    password = input("Set initial password: ")
    if len(password) != 4:
        print("Password must be 4 digits!")
    else:
        print("Password was set.")
        break


while True:
    userIn = input("Type password: ")

    if userIn == password:
        print("Log in Successful.")
        break
    else:
        print("Wrong Password!")

