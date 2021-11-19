#“Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment.
#  These objects should allow for depositing and withdrawing funds from each category, as well computing category balances and transferring balance amounts between categories”

class Budget:

    def __init__(self) -> None:
        self.balance =0.0
        
    
    def depoit(self, moneyin):
        self.balance += moneyin
    
    
    def withdraw(self, moneyout):
        self.balance -= moneyout

    def transferto(self,account,value):
    self.withdraw(value)
    account.deposit(value)


food = Budget()
food.withdraw()



clothes = Budget()

entertainment = Budget()

food.deposit(100)
food.withdraw(20)
print("food", food.balance)
print("clothes", clothes.balance)

    (self, food, clothing, entertainment)
self, food, clothing, entertainment):


