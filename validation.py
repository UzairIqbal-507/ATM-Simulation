from datetime import datetime
from statement import save_transactions


def login_info():
    maximum=3
    print("attempts remaining: ",maximum)
    correct_pin="1234"
    while True:

        login_pin=input("Enter your login pin: ").lower()

        if login_pin == correct_pin:
            print("Login successful")
            print("Welcome to your Account")
            return True
        elif login_pin != correct_pin:
            print("Login failed")
            maximum-=1
            print("attempts remaining: ",maximum)


        if maximum==0:
            print("your account is temporarily closed")
            return False

def check_balance(balance):
    print(f'Your current balance is: Rs.{balance}')

def deposit_money(balance,transactions):

    try:
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print("deposit successful")
            print(f"your new balance is: Rs.{balance}")
            current_time = datetime.now()
            date = current_time.strftime("%Y-%m-%d")
            time = current_time.strftime("%H:%M:%S")
            transaction = {
                "type": "deposit",
                "amount": amount,
                "balance": balance,
                "date": date,
                "time": time,
            }

            transactions.append(transaction)
            save_transactions(transactions)
        else:
            print("enter a valid amount to deposit")
    except ValueError:
        print("invalid input! please enter a numeric input ")
    return balance


def withdraw_money(balance,transactions):
    try:
            amount = int(input("Enter the amount to withdraw: "))
            if (amount > 0) and (amount <= balance):
                balance -= amount
                print("withdraw successful")
                print(f"your new balance is: Rs.{balance}")
                current_time = datetime.now()
                date = (current_time.strftime("%Y-%m-%d "))
                time = (current_time.strftime("%H:%M:%S"))
                transaction = {
                    "type": "withdraw",
                    "amount": amount,
                    "balance": balance,
                    "date": date,
                    "time": time,
                }
                transactions.append(transaction)
                save_transactions(transactions)
            elif amount > balance:
                print("Insufficient balance!")

            else:
                print("enter a valid amount to withdraw")
    except ValueError:
        print("invalid input! please enter a numeric input ")
    return balance

def bank_statement(transactions):
    print("=========MINI STATEMENT===========")
    if not transactions:
        print("no transactions found ")

    else:
        for transaction in transactions:
            print (
                (f"Type:{transaction['type']}\n"
                f"Amount:Rs.{transaction['amount']}\n"
                f"Balance:{transaction['balance']}\n"
                f"Date:{transaction['date']}\n"
                f"Time:{transaction['time']}\n"
                ))
        print("=============================")
