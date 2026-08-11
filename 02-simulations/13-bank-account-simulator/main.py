from datetime import datetime
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        self.history = []

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Must deposit money")
        self.balance += amount
        print(f"Successfully deposited ${amount} in {self.owner}'s account")
        self.history.append(f"Deposited ${amount} into the account at {datetime.now().strftime('%Y-%m-%d %H:%M')}.")

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Must withdraw money from the account")
        if amount > self.balance:
            raise ValueError("Not enough funds")
        self.balance -= amount
        print(f"Successfully withdrew ${amount} from {self.owner}'s account")
        self.history.append(f"Withdrew ${amount} from the account at {datetime.now().strftime('%Y-%m-%d %H:%M')}.")

    def print_history(self):
        print()
        print(f"History of {self.owner}'s account:")
        for action in self.history:
            print(action)
        print()


    def __str__(self):
        return f"Owner: {self.owner}, Balance: ${self.balance}"

if __name__ == "__main__":
    acc1 = BankAccount("Jaume", 5000)
    acc2 = BankAccount("Pol", 50000)

    print(acc1)
    print(acc2)

    acc1.deposit(1000)
    print(acc1)

    acc2.withdraw(1000)
    print(acc2)

    acc1.deposit(5000)
    acc1.withdraw(1350)
    acc1.print_history()


