from validation import (login_info, check_balance, deposit_money, withdraw_money, bank_statement)
from statement import load_transactions, load_balance,save_balance


def show_menu():
    print("=======================")
    print("    Welcome to ATM     ")
    print("========================")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw Money")
    print("4.Transaction History")
    print("5.Exit")

balance=load_balance()
transactions = load_transactions()

login_status = login_info()
if login_status:
    while True:
        show_menu()
        try:
            choice=int(input("Enter your choice: "))
            if choice==1:
                check_balance(balance)
            elif choice==2:
                balance=deposit_money(balance,transactions)
                save_balance(balance)
            elif choice==3:
                balance=withdraw_money(balance,transactions)
                save_balance(balance)
            elif choice==4:
                bank_statement(transactions)
            elif choice==5:
                print("Exit")
                break
            else:
                print("invalid choice! please select 1-5")
        except ValueError:
            print("invalid choice! please select a numeric input")

else:
    print("Access denied")
