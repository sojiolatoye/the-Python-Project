class Account:

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

    def deposit(self, depo):
        self.depo = depo
        self.depo = self.currentBalance + self.depo

    def withdraw(self, withdrawal):
        self.withdrawal = withdrawal
        self.withdrawal = self.currentBalance - self.withdrawal
