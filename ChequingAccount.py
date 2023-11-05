from Account import Account
class ChequingAccount(Account):

    def __init__(self, overdraftLimit):
        self.overdraftLimit = overdraftLimit

    def withdraw(self):
        pass