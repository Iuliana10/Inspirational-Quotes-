class BankAccount:
    def __init__(self, initial_balance=0):
        self._balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Depunere efectuată: {amount:.2f} unități. Sold actual: {self._balance:.2f} unități.")
        else:
            print("Suma depusă trebuie să fie pozitivă.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Retragere efectuată: {amount:.2f} unități. Sold actual: {self._balance:.2f} unități.")
            else:
                print("Fonduri insuficiente pentru retragere.")
        else:
            print("Suma retrasă trebuie să fie pozitivă.")

    def get_balance(self):
        return self._balance

cont = BankAccount(100)
cont.deposit(50)
cont.withdraw(30) 
print(f"Sold final: {cont.get_balance():.2f} unități")
