class BankAccount:
    __balance = 0
    def deposite(self, amount):
        if amount < 0:
            print("Invalid amount")
        else:
            self.__balance += amount

    def withdraw(self, amount):
        if amount < 0:
            print("you can't enter negative number")
        elif amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print("You have successfully withdrawn your money")
    def get_balance(self):
        print(f"Your balance is {self.__balance}")

account1 = BankAccount()
account1.deposite(300)
account1.withdraw(200)
account1.get_balance()

