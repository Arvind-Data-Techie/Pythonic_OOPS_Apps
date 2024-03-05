class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited \${amount}  \nCurrent balance: \${self.balance}"
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return f"Withdrew \${amount}.  \nCurrent balance: \${self.balance}"
        else:
            return "Insufficient funds or invalid amount for withdrawal."

    def display_balance(self):
        return f"Account Number: {self.account_number}  \nCurrent Balance: \${self.balance}"


class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
        self.accounts = {}

    def create_account(self, account_number, initial_balance=0):
        if account_number not in self.accounts:
            self.accounts[account_number] = Account(account_number, initial_balance)
            return "Account created successfully."
        else:
            return "Account already exists."

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            return "Account not found"

    def display_all_accounts(self):
        result = f"All accounts in {self.bank_name}:\n"
        for account_number, account in self.accounts.items():
            result += f"  \n\nAccount Number: {account_number},  \nBalance: ${account.balance}\n"
        return result
