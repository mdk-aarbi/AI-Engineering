# Task_8: Write a while loop that implements a simple menu-driven CLI (add/remove/list/quit)
# until the user quits.

ids = list()
names = list()
ages = list()
citys = list()

repeat = True
while(repeat):

    print("Enter 1 to add.")
    print("Enter 2 to remove.")
    print("Enter 3 to list down.")
    print("Enter 0 to quit.")
    choice = int(input())

    if choice == 1:
        id = int(input("Enter a unique id: "))
        if id in ids:
            print("You did not enter a unique id. Try again.")
        else:
            ids.append(id)
            names.append(input("Enter the name: "))
            ages.append(input("Enter the age: "))
            citys.append(input("Enter the city: "))
    elif choice == 2:
        remove_id = int(input("Enter the id: "))
        if remove_id in ids:
            found = ids.index(remove_id)

            print("Confirm the details to be removed...")
            print(f"ID = {remove_id}")
            print(f"Name = {names[found]}")
            print(f"Age = {ages[found]}")
            print(f"City = {citys[found]}")
            print("To confirm enter 1.")
            print("To stop enter 0.")

            confirmation = int(input())
            if confirmation == 1:
                ids.pop(found)
                names.pop(found)
                ages.pop(found)
                citys.pop(found)
            elif confirmation == 0:
                print("Stopping...")
            else:
                print("You entered wrong input. Try again.")
        else:
            print("The id does not exist.")
    elif choice == 3:
        for ind in range(len(names)):
            print(f"Name = {names[ind]}")
            print(f"Age = {ages[ind]}")
            print(f"City = {citys[ind]}")
            print("")
    elif choice == 0:
        print("Quitting...")
        repeat = False
    else:
        print("You entered wrong input. Try again.")