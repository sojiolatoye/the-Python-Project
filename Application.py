class Application:

    def showMainMenu(self, accountnumbers, newaccount, exit):
        self.accountnumbers = accountnumbers
        self.newaccount = newaccount 
        self.exit = exit

    def showAccountMenu(self, checkbalance, deposit, withdraw, exitaccount):
        self.checkbalance = checkbalance
        self.deposit = deposit
        self.withdraw = withdraw
        self.exitaccount = exitaccount

    def run(self):
        return f"{self.showMainMenu()}"