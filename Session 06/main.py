# loop -> get students' info (name, lname, major, gpa, student_number)

# store all in list[dict]

# print all cleanly!

import os

def get_data(stu_count):
    data_list = []
    for i in range(1, stu_count+1):
        os.system('cls')
        print(f"Getting info for student {i}")
        stu_dict = {
            'name': input("Type Student Name: ").strip().title(),
            'lname': input("Type Student Last Name: ").strip().title(),
            'major': input("Type Student Major: ").strip().title(),
            'gpa': float(input("Type Student gpa: ").strip()),
            'stu_num': input("Type Student Number: ").strip()
        }

        data_list.append(stu_dict)
    
    return data_list


def print_data(data_list: list[dict]):
    os.system('cls')
    for stu in data_list:
        for k, v in stu.items():
            print(f"{k:<15} {v:}")
        print('-=-=-=-=-=-=-=-=-=-')


def main():
    student_count = int(input("How many students do you want to add? "))
    data_list = get_data(student_count)

    print_data(data_list)


if __name__ == "__main__":
    main()