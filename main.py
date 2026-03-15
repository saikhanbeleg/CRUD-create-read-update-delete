while True:
    choice = int(input("\n1. Show students\n2. Add student\n3. Update student\n4. Delete student\n5. Exit\n\nChoose: "))

    if choice == 1:
        with open("data.txt", "r") as file:
            print(file.read())

    elif choice == 2:
        with open("data.txt", "a") as file:
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            file.write(f"{name}, {age}\n")

    elif choice == 3:
        with open("data.txt", "r") as file:
            lines = file.readlines()

        update_name = input("Search update name: ")
        new_name = input("Enter new name: ")
        new_age = input("Enter new age: ")
        new_lines = []

        for line in lines:
            name, age = line.split(",")
            if update_name == name.strip():
                new_lines.append(f"{new_name}, {new_age}\n")
            else:
                new_lines.append(line)
        else:
            print("Student not found.")

        with open("data.txt", "w") as file:
            file.writelines(new_lines)

    elif choice == 4:
        with open("data.txt", "r") as file:
            lines = file.readlines()

        student_name = input("Enter student name to delete: ")
        new_lines = []
        with open("data.txt", "w") as file:

            for line in lines:
                name, age = line.split(",")
                if not line.startswith(f"{student_name}"):
                    file.write(line) 
                else:
                    new_lines.append(line)

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice")