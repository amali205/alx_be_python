class BankAccount:
    def __init__(self , intial_balance=0):
        self.account_balance = intial_balance
    def deposit(self ,amount):
         self.account_balance += amount 
    def withdraw(self, amount):
         if amount <= self.account_balance:
          self.account_balance -= amount
          return True
         return False
    def display_balance(self):
      print (f"Current Balance: ${float(self.account_balance)}")
      
        
            