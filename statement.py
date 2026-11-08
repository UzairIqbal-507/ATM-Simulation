import json

def save_transactions(transactions):
    with open("transactions.json", "w") as file:
        json.dump(transactions, file,indent=4)

def load_transactions():
    try:
        with open("transactions.json", "r") as file:
            transactions = json.load(file)
            if isinstance(transactions, list):
                return transactions
            else:
                return []
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_balance(balance):
    with open("balance.json", "w") as file:
        json.dump({"balance":balance}, file, indent=4)

def load_balance():
    try:
        with open("balance.json","r") as file:
            data = json.load(file)
            if isinstance(data["balance"], (int, float)) and data["balance"] > 0:
                return data["balance"]
            else:
                return 0
    except (FileNotFoundError, json.JSONDecodeError,KeyError):
        return 0