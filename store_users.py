while True:
    choice = int(input("\n1. Show user\n2. Add user\n3. Update user\n4. Delete user\n5. Exit\n\nChoose: "))

    if choice == 1:
        with open("store_data.txt", "r") as file:
            print(file.read())

    elif choice == 2:
        with open("store_data.txt", "a") as file:
            added = input("Enter user to add: ")
            file.write(f"{added}\n")

    elif choice == 3:
        with open("store_data.txt", "r") as file:
            data = file.readlines()

        update_user_number = input("Enter user number to update: ")
        new_data = []
        for line in data:
            number, first_name, last_name, email = line.split(",")
            if update_user_number == number.strip(","):
                new_first = input("Enter new first name: ")
                new_last = input("Enter new last name: ")
                new_email = input("Enter new email: ")
                new_data.append(f"{number.strip()}, {new_first}, {new_last}, {new_email}\n")
                break
            else:
                new_data.append(line)
        else:
            print("User not found.")

        if new_data:
            with open("store_data.txt", "w") as file:
                file.writelines(new_data)

    elif choice == 4:
        with open("store_data.txt", "r") as file:
            data = file.readlines()

        user_number_delete = input("Enter user number to delete: ")
        new_data = []
        with open("store_data.txt", "w") as file:

            for line in data:
                number, first_name, last_name, email = line.split(",")
                if not line.startswith(f"{user_number_delete.split(',')[0]}"):
                    file.write(line)
                    print(f"Deleted: {line.strip()}") 
                    break
                else:
                    new_data.append(line) 
            else:
                print("User not found.")

        if new_data:
            with open("store_data.txt", "w") as file:
                file.writelines(new_data) 

    elif choice == 5: 
        print("Bye!")
        break