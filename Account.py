class Account:  #Parent account 

    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfInterest = rateOfInterest
        self.currentBalance = currentBalance

    def getAccountNumber(self):  
        self.accountNumber

    def getAccountHolderName(self):
        self.accountHolderName

    def getRateOfInterest(self):
        self.rateOfInterest

    def getCurrentBalance(self):
        self.currentBalance = self.currentBalance * self.rateOfInterest + self.currentBalance

    def setAccountHolderName(self):
        self.accountHolderName 

    def setRateOfInterest(self):
        self.rateOfInterest

    def deposit(self, amount):    #deposit method
        if amount > 0:
            self.currentBalance += amount
            return True
        else:
            return False

    def withdraw(self, amount):    #withdraw method
        if 0 < amount <= self.currentBalance:
            self.currentBalance -= amount
            return True
        else:
            return False
