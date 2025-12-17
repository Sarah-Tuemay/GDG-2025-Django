try:
    number_of_items = int(input("How many items do you want to buy? "))
    if number_of_items >= 3:
        print("Discount applied")
    else:
        print("No discount")
except ValueError:
    print("You entered invalid number")
