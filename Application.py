from Account import Account
from Bank import Bank

class Application:
    def __init__(self, bank):
        self.bank = bank

    def show_main_menu(self):
        print("Welcome to the Bank Application")
        print("1. Open a New Account")
        print("2. Show Existing Accounts")
        print("3. Exit")
        return input("Choose an option: ")

    def open_account(self):
        account_type = input("Enter account type (savings/chequing): ")
        account_holder_name = input("Enter account holder name: ")
        rate_of_interest = float(input("Enter the rate of interest: "))
        current_balance = float(input("Enter the current balance: "))

        new_account_number = self.bank.generate_account_number(account_type)

        # Additional parameters for specific account types
        if account_type == "savings":
            minimum_balance = float(input("Enter the minimum balance: "))
            account = self.bank.create_account(account_type,new_account_number, account_holder_name, rate_of_interest, current_balance, minimumBalance=minimum_balance)
        elif account_type == "chequing":
            overdraft_limit = float(input("Enter the overdraft limit: "))
            account = self.bank.create_account(account_type, new_account_number, account_holder_name, rate_of_interest, current_balance, overdraftLimit=overdraft_limit)
        else:
            print("Invalid account type.")
            return

        print(f"Account created successfully. Account Number: {account.accountNumber}")

    def show_account(self):
        account_number = input("Enter the account number: ")
        account = self.bank.get_account(account_number)

        if account is None:
            print("Account not found.")
        else:
            print(f"Account Number: {account.accountNumber}, Account Holder: {account.accountHolderName}, Balance: {account.currentBalance}")



    def run(self):
        while True:
            choice = self.show_main_menu()
            if choice == '1':
                self.open_account()
            elif choice == '2':
                self.show_account()
            elif choice == '3':
                print("Exiting the application.")
                break
            else:
                print("Invalid option, please try again.")

if __name__ == "__main__":
    bank = Bank()
    app = Application(bank)
    app.run()


    