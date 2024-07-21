#Khundrakpam Veeshel Singh
import csv #For saving csv files
from datetime import datetime #To get current times
from typing import List, Dict, Union # For type annotation

'''This mini Project is to teach my students 
how to apply python programming to day to day problem solving. 
It is simple enough to follow and learn the basics of python programming.
The project is call Income and Expenditure Management system
Features:
    1. Add Income
    2. Record Expenditure
    3. View Balance
    4. View Transaction History
    5. Generate Summary Report
All the features are basic implementation for beginers to understand.
Records are stored as csv file for convenient not to scare away the beginners with SQL and databases.
Feel free to use it, modify it and improve it.
Thank You'''
# Define types for better annotation
Transaction = Dict[str, Union[str, float]]  # Type for a single transaction
Transactions = List[Transaction]            # Type for list of transactions

def load_transactions() -> Transactions:
    """Load transactions from CSV file."""
    transactions = []
    try:
        with open('transactions.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print("No transactions found.")
    return transactions

def save_transactions(transactions: Transactions) -> None:
    """Save transactions to CSV file."""
    fieldnames = ['Type', 'Amount', 'Date', 'Category','Date of Expenditure']
    with open('transactions.csv', 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(transactions)

def add_income(amount: float) -> None:
    """Add income to transactions with current date."""
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = {'Type': 'Income', 'Amount': amount, 'Date': current_date, 'Category': ''}
    transactions = load_transactions()
    transactions.append(transaction)
    save_transactions(transactions)

def record_expenditure(amount: float, category: str, expense_date: str) -> None:
    """Record expenditure to transactions with current date."""
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = {'Type': 'Expenditure', 'Amount': amount, 'Date': current_date, 'Category': category, "Date of Expenditure": expense_date}
    transactions = load_transactions()
    transactions.append(transaction)
    save_transactions(transactions)

def calculate_balance(transactions: Transactions) -> float:
    """Calculate current balance."""
    total_income = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Income')
    total_expenditure = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Expenditure')
    return total_income - total_expenditure

def generate_summary_report(transactions: Transactions) -> str:
    """Generate a summary report of income, expenditures, and balance."""
    total_income = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Income')
    total_expenditure = sum(float(transaction['Amount']) for transaction in transactions if transaction['Type'] == 'Expenditure')
    
    summary = f"Summary Report:\n"
    summary += f"Total Income: Rs. {total_income:.2f}\n"
    summary += f"Total Expenditure: Rs. {total_expenditure:.2f}\n"
    
    categories = {}
    for transaction in transactions:
        if transaction['Type'] == 'Expenditure':
            category = transaction['Category']
            amount = float(transaction['Amount'])
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    
    if categories:
        summary += "Expenditure by Category:\n"
        for category, amount in categories.items():
            summary += f"{category}: Rs. {amount:.2f}\n"
    
    balance = calculate_balance(transactions)
    summary += f"Current Balance: Rs. {balance:.2f}\n"
    
    
    return summary

def main():
    """Main function to run the command-line interface."""
    while True:
        print("\n===== Income and Expenditure Management System =====")
        print("1. Add Income")
        print("2. Record Expenditure")
        print("3. View Balance")
        print("4. View Transaction History")
        print("5. Generate Summary Report")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            amount = float(input("Enter income amount: "))
            add_income(amount)
            print("Income added successfully.")
        
        elif choice == '2':
            amount = float(input("Enter expenditure amount: "))
            category = input("Enter category: ")
            expense_date = input("Enter date of expenditure: ")
            record_expenditure(amount, category, expense_date)
            print("Expenditure recorded successfully.")
        
        elif choice == '3':
            transactions = load_transactions()
            balance = calculate_balance(transactions)
            print(f"Current Balance: Rs. {balance:.2f}")
        
        elif choice == '4':
            transactions = load_transactions()
            count=0
            print("Transaction History:")
            print(f"{'SL.':<6}{'Type':<13}{'Amount':^13}  {'Category':^12}{'Date of Expenditure':^24}{'Entry date':^12}")
            for transaction in transactions:
                count+=1
                print(f"{count:<6}{transaction['Type']:<13}{transaction['Amount']:>13}  {transaction['Category']:<12}{transaction['Date of Expenditure']:^24}{transaction['Date']:^12}")
                # print(transaction)
        
        elif choice == '5':
            transactions = load_transactions()
            summary = generate_summary_report(transactions)
            print(summary)
        
        elif choice == '6':
            print("Exiting program. Thank you!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
