# The BankAccount class simulates a bank account.
class BankAccount:
    # The __init__ method accepts an argument for
    # the account's balance. It is assigned to
    # the __balance attribute.
    def __init__(self, bal):
        self.__ballance = bal

    # The deposit method makes a deposit into the
    # account
    def deposit(self, amount):
        self.__ballance += amount

    # The withdraw method withdraws an amount
    # from the account.
    def withdraw(self, amount):
        if self.__ballance >= amount:
            self.__ballance -= amount
        else:
            print('Error: Influenced funds')

    # The get_balance method returns the
    # account balance.
    def get_balance(self):
        return self.__ballance

    def __str__(self):
        return f'The balance is ${self.__ballance:,.2f}'