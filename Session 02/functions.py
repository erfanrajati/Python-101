def say_hi():
    print("HI")
    print("HI")
    print("HI")


def say_hi_to(name, lname):
    msg = "Hello" + ' ' + name + ' ' + lname
    print(msg)


def generate_msg(name, lname):
    msg = f"Hello, {name} {lname}"
    return msg

print(generate_msg("Erfan", "Rajati"))