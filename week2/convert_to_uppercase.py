try:
    with open("messages.txt", "r") as file:
        for line in file:
            print(line.upper())
except FileNotFoundError:
    print("file not found")