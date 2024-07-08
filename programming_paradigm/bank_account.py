# bank_account.py

class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        self.account_balance += amount

    def withdraw(self, amount):
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f'Current Balance: ${self.account_balance}')

if __name__ == '__main__':
    # Optional test code can be added here if needed
    # Test display_balance method
    account = BankAccount(100)  # Initial balance of 100
    account.display_balance()  # Should print: Current Balance: $100

    # Additional test cases
    account.deposit(50)
    account.display_balance()  # Should print: Current Balance: $150

    if account.withdraw(70):
        account.display_balance()  # Should print: Current Balance: $80
    else:
        print("Withdrawal failed.")

    if account.withdraw(100):
        account.display_balance()  # Should print: Withdrawal failed.
    else:
        print("Withdrawal failed.")  # Should print: Withdrawal failed.
