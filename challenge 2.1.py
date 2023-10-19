class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
    self.__account_number = account_number
    self.__account_holder_name = account_holder_name
    self.__account_balance = initial_balance

  def deposit(self, amount):
    if amount > 0:
      self.__account_balance += amount
      print("Deposited â‚¹{}. New balance: â‚¹{}".format(amount,self.__account_balance))
    else:
      print("Invalid deposit amount. please deposit a positive amount.")

  def withdraw(self ,amount):
    if amount > 0 and amount <= self.__account_balance:
      self.__account_balance -= amount
      print("Withdraw â‚¹{}. New balance: â‚¹{}".format(amount,self.__account_balance))

    else:
      print("Invaid withdrawal amount or insufficient balance.")

  def display_balance(self):
    print("Account balance for {} (Account #{}): â‚¹{}".format(
      self.__account_holder_name, self.__account_number, self.__account_balance))

account = BankAccount(account_number="123456789",
                     account_holder_name="S GOKUL",
                     initial_balance=10000.0)

account.display_balance()
account.deposit(5000.0)
account.withdraw(2000.0)
account.display_balance()