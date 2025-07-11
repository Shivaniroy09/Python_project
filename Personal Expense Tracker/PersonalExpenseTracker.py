import os
from datetime import datetime
from collections import defaultdict

EXPENSES_FILE = 'expenses.txt'

# Predefined list of categories
CATEGORIES = ['Food', 'Travel']

def add_expense(category, amount, date):
    """Add an expense to the expenses file."""
    with open(EXPENSES_FILE, 'a') as file:
        file.write(f"{category},{amount},{date}\n")
    print("Expense added successfully!")

def view_expenses():
    """View all expenses categorized by type."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded.")
        return

    expenses = defaultdict(list)
    
    with open(EXPENSES_FILE, 'r') as file:
        for line in file:
            category, amount, date = line.strip().split(',')
            expenses[category].append((amount, date))

    print("Expenses:")
    for category in CATEGORIES:
        print(f"{category}:")
        if category in expenses and expenses[category]:
            for i, (amount, date) in enumerate(expenses[category], start=1):
                print(f"  {i}. Amount: {amount} - Date: {date}")
        else:
            print("  No expenses recorded.")

def monthly_summary(year, month):
    """Generate a monthly summary of expenses."""
    if not os.path.exists(EXPENSES_FILE):
        print("No expenses recorded.")
        return

    total_expenses = 0
    category_summary = defaultdict(int)

    with open(EXPENSES_FILE, 'r') as file:
        for line in file:
            category, amount, date = line.strip().split(',')
            expense_date = datetime.strptime(date, '%Y-%m-%d')
            if expense_date.year == year and expense_date.month == month:
                total_expenses += int(amount)
                category_summary[category] += int(amount)

    print(f"Monthly Summary ({datetime(year, month, 1).strftime('%B %Y')}):")
    print(f"Total Expenses: {total_expenses}")
    print("By Category:")
    for category in CATEGORIES:
        print(f"{category}: {category_summary[category]}")

def main():
    """Main function to run the expense tracker."""
    while True:
        print("\nWelcome to Personal Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            category = input("Enter category (Food or Travel): ")
            if category not in CATEGORIES:
                print("Invalid category. Please choose from 'Food' or 'Travel'.")
                continue
            amount = input("Enter amount: ")
            date = input("Enter date (YYYY-MM-DD): ")
            add_expense(category, amount, date)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            year = int(input("Enter year (YYYY): "))
            month = int(input("Enter month (1-12): "))
            monthly_summary(year, month)
        elif choice == '4':
            print("Exiting the Personal Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()