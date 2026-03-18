with open("residents.txt", "r") as file:
    print(file.read())
    lines = file.readlines()
    for line in lines:
        number, name, fee = line.strip().split(",")
        with open(f"resident_{number}.txt", "w") as file:
            file.write(f"number: {number}")
            file.write(f"name: {name}")
            file.write(f"fee: {fee}")

    
            
