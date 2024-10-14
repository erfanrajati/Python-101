# Project: Grocery manager app (with UI)
# add items to the grocery list
# remove items from grocery list
# get the count of items in the list
# see the items in the grocery list

groceries = []

menu = '''
Choose from options below:
1 - Show List
2 - Add Item
3 - Delete Item
4 - Count Items
0 - Exit
'''
program_running = True
while program_running:
    print(menu)
    userIn = input("Type Here: ")

    if userIn == '1':
        print(groceries)
    elif userIn == '2':
        item = input("What do you want to add? ")
        groceries.append(item)
        print("Item added successfully.")
    elif userIn == '3':
        item = input()
        groceries.remove(item)
    elif userIn == '4':
        print(len(groceries))
    elif userIn == '0':
        program_running = False
