try:
    with open("config.txt", "r") as file:
        name = file.read()
except FileNotFoundError:
    with open("config.txt", "w") as file:
        file.write("Guest")
    with open("config.txt", "r") as file:
        name = file.read()     
print("Welcome", name)
