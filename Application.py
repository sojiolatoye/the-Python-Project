from Account import Account
from Bank import Bank


def showMainMenu():
    bank = Bank()
    while True:
        a1 = input("Welcome to the banking menu. Choose one of the following : Select Account, Open Account, Exit")
        if a1 == "Select Account":
            a2 = int(input("enter the account number of the account you want to work with"))
            if a2 == bank.searchAccount():
                showAccountMenu()
            else:
                print("Input valid account number")
        elif a1 == "Open Account":
            a3 = int(input("input account number"))
            a4 = input("input account holder name")
            a5 = float(input("input rate of interest"))
            a6 = float(input("input current balance"))
            a = Account(a3, a4, a5, a6)
            print(a)
        elif a1 == "Exit":
            break
        else:
              print("Input valid option")
    

def showAccountMenu():
        bank = Bank()
        while True:
            a7 = input("Welcome to the Account menu. Choose one of the following : Check Balance, Deposit, Withdraw, Exit")
            if a7 == "Check Balance":
                print(bank)
            elif a7 == "Deposit":
                a8 = float(input("Input deposit amount"))
                print(a8)
            elif a7 == "withdraw":
                a9 = float(input("Input withdrawal amount"))
                print(a9)
            elif a7 == "Exit":
                break
            else:
                print("Input valid option")

def run():
    showMainMenu()    

run()









    





