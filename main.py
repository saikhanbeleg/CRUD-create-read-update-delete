while True:
    choice = int(input("\n1. Show students\n2. Add student\n3. Update student\n4. Delete student\n5. Exit\n\nChoose: "))

    if choice == 1:
        with open("data.txt", "r") as file:
            print(file.read())

    elif choice == 2:
        with open("data.txt", "a") as file:
            name = input("Enter student name: ")
            age = input("Enter student age: ")
            file.write(f"\n{name}, {age}")

    elif choice == 3:
        with open("data.txt", "r") as file:
            lines = file.readlines()

        ubdate_name = input("search update name: ")
        ubdate_age = input("search update age: ")
        new_name = input("Enter new name: ")
        new_age = input("Enter new age: ")

        for i in range(len(lines)):
            if lines[i].strip():
                name, age = lines[i].strip().split(",")
                if ubdate_name == name.strip() and ubdate_age == age.strip():
                    lines[i] = f"{new_name}, {new_age}\n" 
                    break
        else:
            print("invalid name")

        with open("data.txt", "w") as file:
            file.writelines(lines)

    elif choice == 4:
        with open("data.txt", "r") as file:
            lines = file.readlines()

        student_name = input("enter student name to delete: ")
        student_age = input("enter student age to delete: ")
        for i in range(len(lines)):
            if lines[i].strip():
                name, age = lines[i].strip().split(",")
                if student_name == name.strip() and student_age == age.strip():
                    remove = lines.pop(i)
                    print(f"deleted: {remove.strip()}")
                    break
        else:
            print("invalid name")

        with open("data.txt", "w") as file:
            file.writelines(lines)

    elif choice == 5:
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Please enter 1-5.")