
import BankAccount

def main():

    # Get the starting balance.
    start_balance = float(input('Enter your start balance: '))

    # Create a BankAccount object.
    saving = BankAccount.BankAccount(start_balance)

    # Deposit the user's paycheck.
    pay = float(input('How much were you paid this week? '))
    print('I will deposit that into your account.')
    saving.deposit(pay)

    # Display the balance.
    print(f'Your account balance is ${saving.get_balance():,.2f}.')

    # Get the amount to withdraw.
    cash = float(input('How much would you like to withdraw? '))
    print('I will withdraw that from your account.')
    saving.withdraw(cash)

    # Display the balance.
    # print(f'Your account balance is ${saving.get_balance():,.2f}.')
    print(saving)

# Call the main function.
if __name__ == '__main__':
    main()




    