try:
    with open("log.txt", "a") as file:
        file.write("\nUser Logged in")
except Exception as e:
    print(f"Error: {e}")

try:
    with open("log.txt", "r") as file:
        content = file.read()
        print("\n Full log history \n")
    if content:
        print(content)
    else:
        print("No log")
except FileNotFoundError:
    print("\n Log file not found")
