sum = 0
with open("numbers.txt", "r") as file:
    for line in file:
        try:
            sum += int(line)
        except ValueError:
            continue

print(sum)