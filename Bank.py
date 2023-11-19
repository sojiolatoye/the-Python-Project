from SavingsAccount import SavingsAccount
from ChequingAccount import ChequingAccount
class Bank:
    def __init__(self):
        self.accounts = {}
        self.last_account_number = 3

        self.accounts["S001"] = SavingsAccount("S001", "Alice", 0.02, 1000, 500)
        self.accounts["S002"] = SavingsAccount("S002", "Bob",  0.03, 2000, 500)
        self.accounts["S003"] = SavingsAccount("S003", "Charlie", 0.025, 3000, 500)

        self.accounts["C001"] = ChequingAccount("C001", "Dave", 0.01, 500, 100)
        self.accounts["C002"] = ChequingAccount("C002", "Eve", 0.01, 750, 200)
        self.accounts["C003"] = ChequingAccount("C003", "Frank", 0.01, 1000, 300)

    def generate_account_number(self, account_type):
        """
        Generates a unique sequential account number with a prefix based on account type.
        """
        self.last_account_number += 1
        account_prefix = "S" if account_type.lower() == "savings" else "C"
        return f"{account_prefix}{str(self.last_account_number).zfill(3)}" 

    def create_account(self, account_type, account_number, account_holder_name, rate_of_interest, current_balance, **kwargs):
        if account_number in self.accounts:
            raise ValueError("Account number already exists.")

        if account_type == "savings":
            self.accounts[account_number] = SavingsAccount(account_number, account_holder_name, rate_of_interest, current_balance, **kwargs)
        elif account_type == "chequing":
            self.accounts[account_number] = ChequingAccount(account_number, account_holder_name, rate_of_interest, current_balance, **kwargs)
        else:
            raise ValueError("Invalid account type.")

        return self.accounts[account_number]

    def get_account(self, account_number):
        # Retrieve an account by its account number
        return self.accounts.get(account_number, None)
