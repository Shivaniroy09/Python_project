import hashlib
import os
from datetime import datetime

# File paths
ACCOUNTS_FILE = "accounts.txt"
TRANSACTIONS_FILE = "transactions.txt"

# Utility Functions
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def read_accounts():
    if not os.path.exists(ACCOUNTS_FILE):
        return {}
    with open(ACCOUNTS_FILE, "r") as file:
        accounts = {}
        for line in file:
            acc_no, name, password, balance = line.strip().split(",")
            accounts[acc_no] = {
                "name": name,
                "password": password,
                "balance": float(balance)
            }
        return accounts

def write_accounts(accounts):
    with open(ACCOUNTS_FILE, "w") as file:
        for acc_no, details in accounts.items():
            file.write(f"{acc_no},{details['name']},{details['password']},{details['balance']}\n")

def log_transaction(account_no, transaction_type, amount):
    with open(TRANSACTIONS_FILE, "a") as file:
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"{account_no},{transaction_type},{amount},{date}\n")

# Banking Operations
def create_account():
    name = input("Enter your name: ")
    initial_deposit = float(input("Enter your initial deposit: "))
    password = input("Enter a password: ")

    accounts = read_accounts()
    account_no = str(len(accounts) + 1).zfill(6)  # Generate account number
    hashed_password = hash_password(password)

    accounts[account_no] = {"name": name, "password": hashed_password, "balance": initial_deposit}
    write_accounts(accounts)

    print(f"Account created successfully! Your account number is {account_no}")

def login():
    accounts = read_accounts()
    account_no = input("Enter your account number: ")
    password = input("Enter your password: ")
    hashed_password = hash_password(password)

    if account_no in accounts and accounts[account_no]["password"] == hashed_password:
        print("Login successful!")
        return account_no
    else:
        print("Invalid account number or password.")
        return None

def deposit(account_no):
    amount = float(input("Enter amount to deposit: "))
    accounts = read_accounts()
    accounts[account_no]["balance"] += amount
    write_accounts(accounts)
    log_transaction(account_no, "Deposit", amount)
    print(f"Deposit successful! Current balance: {accounts[account_no]['balance']}")

def withdraw(account_no):
    amount = float(input("Enter amount to withdraw: "))
    accounts = read_accounts()
    if accounts[account_no]["balance"] >= amount:
        accounts[account_no]["balance"] -= amount
        write_accounts(accounts)
        log_transaction(account_no, "Withdrawal", amount)
        print(f"Withdrawal successful! Current balance: {accounts[account_no]['balance']}")
    else:
        print("Insufficient balance.")

def banking_menu(account_no):
    while True:
        print("\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Logout")
        choice = input("Enter your choice: ")
        if choice == "1":
            deposit(account_no)
        elif choice == "2":
            withdraw(account_no)
        elif choice == "3":
            accounts = read_accounts()
            print(f"Current balance: {accounts[account_no]['balance']}")
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("Invalid choice!")

# Main Menu
def main():
    while True:
        print("\nWelcome to the Banking System!")
        print("1. Create Account\n2. Login\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            account_no = login()
            if account_no:
                banking_menu(account_no)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
