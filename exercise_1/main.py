import BankAccount

broke = BankAccount.BankAccount("Fadi", 10.00)

broke.deposit(20.00)
broke.withdraw(5.00)
print(broke.get_balance())