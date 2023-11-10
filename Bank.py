class Bank:

    def accountList(self, bankName, accountNumber, accountHolderName, rateOfInterest, currentBalance):
        self.bankName = bankName
        self.accountNumber = accountNumber
        self.accountHolderName = accountHolderName
        self.rateOfInterest = rateOfInterest
        self.currentBalance = currentBalance

    def chequingAccountOne(self):
        self.accountNumber = 1234
        self.accountHolderName = "Soji Olatoye"
        self.rateOfInterest = 6
        self.currentBalance = 1000

    def chequingAccountTwo(self):
        self.accountNumber = 2345
        self.accountHolderName = "Olumide Olatoye"
        self.rateOfInterest = 5
        self.currentBalance = 2000

    def chequingAccountThree(self):
        self.accountNumber = 3456
        self.accountHolderName = "Odunola Olatoye"
        self.rateOfInterest = 4
        self.currentBalance = 3000

    def savingsAccountOne(self):
        self.accountNumber = 4567
        self.accountHolderName = "Kemi Olatoye"
        self.rateOfInterest = 3
        self.currentBalance = 4000

    def savingsAccountTwo(self):
        self.accountNumber = 5678
        self.accountHolderName = "Ola Olatoye"
        self.rateOfInterest = 2
        self.currentBalance = 5000

    def savingsAccountThree(self):
        self.accountNumber = 6789
        self.accountHolderName = "Ayo Olatoye"
        self.rateOfInterest = 1
        self.currentBalance = 6000
        

    def searchAccount(self, accountNumber):
        self.accountNumber = accountNumber
        accountNumber = 1234
       
       
            
        
        

    def openAccount(self):
        pass
        
    def __str__(self):
        return f"""Balance is {self.currentBalance} """