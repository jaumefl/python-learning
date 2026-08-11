class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        if amount <= 0:
            raise ValueError("Must deposit money")
        self.balance += amount
        print(f"Successfully deposited ${amount} in {self.owner}'s account")

    def withdraw(self,amount):
        if amount <= 0:
            raise ValueError("Must withdraw money from the account")
        if amount > self.balance:
            raise ValueError("Not enough funds")
        self.balance -= amount
        print(f"Successfully withdrew ${amount} from {self.owner}'s account")

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


