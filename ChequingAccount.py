from Account import Account
class ChequingAccount(Account):  #Child class of Account class

    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance, overdraftLimit):
        super().__init__(accountNumber,accountHolderName, rateOfInterest, currentBalance)
        self.overdraftLimit = overdraftLimit

    def withdraw(self, amount):    #withdraw method 
        if amount > 0 and (self.currentBalance - amount) >= -self.overdraftLimit:
            self.currentBalance -= amount
            return True
        else:
            return False
