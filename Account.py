class Account:

    def __init__(self, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.accountnumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfInterest = rateOfInterest
        self.currentBalance = currentBalance

    def getAccountNumber(self):
        self.accountnumber

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

    def deposit(self):
        pass

    def withdraw(self):
        pass 