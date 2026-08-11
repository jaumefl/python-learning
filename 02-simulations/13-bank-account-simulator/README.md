# Bank Account Simulator

My first class. A `BankAccount` bundles the data (an owner, a balance, a
transaction history) together with the only rules allowed to change it —
deposit and withdraw. The point of the project isn't the banking; it's that an
account is the obvious case of "some data plus the rules that guard it," so the
object owns its balance and nothing outside can touch it except through methods
I control.

## What's actually going on

Two accounts made from the same class are completely independent. `acc1.deposit`
only ever changes `acc1`, because inside that call `self` *is* `acc1` — Python
passes the object in for me. That independence is the whole reason objects
exist, and it comes for free from setting `self.balance` and `self.history = []`
in `__init__`: each new account runs its own `__init__`, so each gets its own
balance and its own list.

The guards `raise ValueError` instead of printing and limping on. A withdrawal
bigger than the balance, or any non-positive amount, is refused. Rejecting is
more honest than clamping to a legal value — clamping would hand back a
confident wrong balance. The order matters too: a negative amount is malformed
no matter what the balance is, so I check `amount <= 0` before I check funds.

`__str__` is what lets `print(acc)` show something readable instead of the
default object address, and every successful deposit or withdrawal appends a
timestamped line to the account's own history.

## Sample output

```
Owner: Jaume, Balance: $5000
Owner: Pol, Balance: $50000
Successfully deposited $1000 in Jaume's account
Owner: Jaume, Balance: $6000
Successfully withdrew $1000 from Pol's account
Owner: Pol, Balance: $49000
Successfully deposited $5000 in Jaume's account
Successfully withdrew $1350 in Jaume's account

History of Jaume's account:
Deposited $1000 at 2026-08-11 14:30.
Deposited $5000 at 2026-08-11 14:30.
Withdrew $1350 at 2026-08-11 14:30.
```