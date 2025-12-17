sales_list = []
try:
    with open("week2/sales.txt", "r") as file:
        for line in file:
            try:
                sales_list.append(int(line))
            except ValueError:
                continue

    print(sum(sales_list))

except FileNotFoundError:
    print("File doesn't exist")
