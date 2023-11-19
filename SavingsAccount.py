from Account import Account
class SavingsAccount (Account):

    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance,minimumBalance):
        super().__init__(accountNumber, accountHolderName, rateOfInterest, currentBalance)
        self.minimumBalance = minimumBalance

    def withdraw(self, amount):
        if amount > 0 and (self.currentBalance - amount) >= self.minimumBalance:
            self.currentBalance -= amount
            return True
        else:
            return False 
