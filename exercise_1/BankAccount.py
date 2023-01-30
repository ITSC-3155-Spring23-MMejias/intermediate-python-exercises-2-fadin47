class BankAccount:
  def __init__(self, name:str, balance:float):
    self.name = name
    self.balance = balance

  def deposit(self, amount):
    self.balance += amount

  def withdraw(self, amount):
    self.balance -= amount

  def get_balance(self):
    return f'{self.name} has a balance of {self.balance}'