
class Account:

    def __init__(self, owner, balance):
        #creates an account w/ an owner and a balance
        self.owner = owner
        self.balance = balance


    def  deposit(depo):
        self.balance = self.balance + depo
        print("Deposit Accepted")


    def withdraw(with):
        new_balance = self.balance - with
        if new_balance < 0:
            print("Funds Unavailable")
        else:
            self.balance = new_balance
            print("Withdrawal Accepted")

acct1 = Account("Jose",100)
print(acct1)
acct1.deposit()
#acct1.withdraw()
