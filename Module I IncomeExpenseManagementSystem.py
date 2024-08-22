#Khundrakpam Veeshel Singh
import csv #For saving csv files
from datetime import datetime #To get current times
from typing import List, Dict, Union # For type annotation
import sys, os
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
Records are stored as csv file for convenient not to scare away the beginners
with SQL and databases.
Feel free to use it, modify it and improve it.
Thank You'''

# Define types for better annotation
Transaction = Dict[str, Union[str, float]]  # Type for a single transaction
Transactions = List[Transaction]            # Type for list of transactions
def clear_terminal()->None:
    """
    Function clear terminal
    """
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')
def load_transactions() -> Transactions:
    """
   Load transactions from a CSV file and return them as a list of dictionaries.

   Returns:
       List[Dict[str, Any]]: A list of transaction records, where each record is a dictionary containing
                             the transaction details. Each dictionary includes fields like 'Type',
                             'Amount', 'Date', 'Category', and 'Date of Expense/Income'.

   Description:
       - Opens and reads the CSV file named 'transactions.csv'.
       - Uses `csv.DictReader` to parse the CSV file into a list of dictionaries.
       - Each dictionary in the list represents a transaction record.
       - If the CSV file does not exist, a `FileNotFoundError` is caught, and a message is printed.
       - Returns an empty list if the file is not found.

   Example:
       transactions = load_transactions()
       print(transactions)
   """
    transactions = []
    try:
        with open('transactions.csv', 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                transactions.append(row)
    except FileNotFoundError:
        print("",end='')
    return transactions

def save_transactions(transactions: Transactions) -> bool:
    """
    Save a list of transactions to a CSV file.

    Args:
        transactions (List[Dict[str, Any]]): A list of transaction records where each record is a dictionary 
                                             containing transaction details. Each dictionary must include 
                                             the keys 'Type', 'Amount', 'Date', 'Category', and 'Date of Expense/Income'.

    Returns:
        bool: This function returns True if saving is successful otherwise False.
    
    Description:
        - Opens (or creates) a file named 'transactions.csv' in write mode.
        - Uses the `csv.DictWriter` to write the list of transactions to the file.
        - The CSV file will include a header row with the columns: 'Type', 'Amount', 'Date', 'Category', and 'Date of Expense/Income'.
        - Writes each transaction in the list as a row in the CSV file.

    Example:
        transactions = [
            {'Type': 'Income', 'Amount': '5000.00', 'Date': '2024-08-05 14:23:00', 'Category': '', 'Date of Expense/Income': '2024-08-05'},
            {'Type': 'Expenditure', 'Amount': '150.00', 'Date': '2024-08-06 09:15:00', 'Category': 'Food', 'Date of Expense/Income': '2024-08-06'}
        ]
        save_transactions(transactions)
    """
    fieldnames = ['Type', 'Amount', 'Date', 'Category','Date of Expense/Income']
    try:
        with open('transactions.csv', 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(transactions)
    except:
        return False
    return True
def add_income(amount: float, category: str, income_date:str) -> bool:
    """
    Add an income transaction with the current date and save it to the transactions list.

    Args:
        amount (float): The amount of the income.
        category (str): The category of the income (e.g., 'Salary', 'Investment').
        income_date (str): The date of the income in 'YYYY-MM-DD' format.

    Returns:
        bool: This function returns True if successfully added otherwise False.

    Description:
        - Creates a transaction dictionary with the following fields:
            - 'Type': Set to 'Income'.
            - 'Amount': The amount of the income.
            - 'Date': The current date and time when the income is recorded.
            - 'Category': The category of the income.
            - 'Date of Expense/Income': The date when the income occurred, provided by the user.
        - Loads existing transactions from a persistent store using `load_transactions()`.
        - Appends the new income transaction to the list of transactions.
        - Saves the updated list of transactions back to the persistent store using `save_transactions()`.

    Example:
        add_income(2000.00, 'Salary', '2024-08-05')
    """
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = {
                'Type': 'Income', 
                'Amount': amount, 
                'Date': current_date, 
                'Category': category,
                "Date of Expense/Income": income_date}
    transactions = load_transactions()
    transactions.append(transaction)
    save_transactions(transactions)
    return True

def record_expenditure(amount: float, category: str, expense_date: str) -> bool:
    """
    Record an expenditure transaction with the current date and save it to the transactions list.

    Args:
        amount (float): The amount of the expenditure.
        category (str): The category of the expenditure (e.g., 'Food', 'Transport').
        expense_date (str): The date of the expense in 'YYYY-MM-DD' format.

    Returns:
        bool: This function returns True if expenditure is succssfully recorded.

    Description:
        - Creates a transaction dictionary with the following fields:
            - 'Type': Set to 'Expenditure'.
            - 'Amount': The amount of the expenditure.
            - 'Date': The current date and time when the expenditure is recorded.
            - 'Category': The category of the expenditure.
            - 'Date of Expense/Income': The date of the expense provided by the user.
        - Loads existing transactions from a persistent store using `load_transactions()`.
        - Appends the new expenditure transaction to the list of transactions.
        - Saves the updated list of transactions back to the persistent store using `save_transactions()`.

    Example:
        record_expenditure(150.00, 'Food', '2024-08-05')
    """
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    transaction = {'Type': 'Expenditure', 
                   'Amount': amount, 
                   'Date': current_date, 
                   'Category': category, 
                   "Date of Expense/Income": expense_date}
    transactions = load_transactions()
    transactions.append(transaction)
    save_transactions(transactions)
    return True
def calculate_balance(transactions: Transactions) -> float:
    """
    Calculate the current balance based on a list of transactions.

    Args:
        transactions (List[Dict[str, Any]]): A list of transaction records where each record is a dictionary 
                                             containing details of the transaction. Each dictionary must 
                                             include at least the keys 'Type' and 'Amount'.

    Returns:
        float: The current balance, calculated as the total income minus the total expenditure.
    
    Description:
        - Computes the total income by summing the amounts of transactions labeled as 'Income'.
        - Computes the total expenditure by summing the amounts of transactions labeled as 'Expenditure'.
        - Returns the balance by subtracting the total expenditure from the total income.

    Example:
        transactions = [
            {'Type': 'Income', 'Amount': '5000.00'},
            {'Type': 'Expenditure', 'Amount': '1500.00'},
            {'Type': 'Expenditure', 'Amount': '200.00'}
        ]
        balance = calculate_balance(transactions)
        print(balance)  # Output: 3300.00
    """
    total_income = sum(float(transaction.get('Amount')) 
                       for transaction in transactions 
                       if transaction.get('Type') == 'Income')
    total_expenditure = sum(float(transaction.get('Amount')) 
                            for transaction in transactions 
                            if transaction.get('Type') == 'Expenditure')
    return total_income - total_expenditure

def generate_summary_report(transactions: Transactions) -> str:
    """
   Generate a summary report of income, expenditures, and balance from a list of transactions.

   Args:
       transactions (List[Dict[str, Any]]): A list of transaction records where each record is a dictionary 
                                            containing details of the transaction. Each dictionary must 
                                            include at least the keys 'Type', 'Amount', and optionally 'Category'.

   Returns:
       str: A summary report that includes total income, total expenditure, expenditure by category, and 
            the current balance.
   
   Description:
       - Calculates the total income and total expenditure from the given list of transactions.
       - Aggregates income and expenditure by category if categories are provided.
       - Includes a balance calculation which is assumed to be done by the `calculate_balance` function.
       - Formats the report as a string with details of total income, total expenditure, expenditure by category, 
         and the current balance.

   Example:
       transactions = [
           {'Type': 'Income', 'Amount': '5000.00', 'Category': 'Salary'},
           {'Type': 'Expenditure', 'Amount': '1500.00', 'Category': 'Food'},
           {'Type': 'Expenditure', 'Amount': '200.00', 'Category': 'Transport'},
           {'Type': 'Expenditure', 'Amount': '300.00', 'Category': 'Food'}
       ]
       print(generate_summary_report(transactions))
   """
    total_income = sum(float(transaction.get('Amount')) for 
                       transaction in transactions 
                       if transaction.get('Type') == 'Income')
    total_expenditure = sum(float(transaction.get('Amount')) 
                            for transaction in transactions 
                            if transaction.get('Type') == 'Expenditure')
    
    summary = f"\n  Total Income        : Rs. {total_income:>12.2f}\n"
    summary += f"  Total Expenditure   : Rs. {total_expenditure:>12.2f}\n\n"
    
    categories = {}
    for transaction in transactions:
        if transaction.get('Type') == 'Income':
            category = transaction.get('Category')
            amount = float(transaction.get('Amount'))
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    
    if categories:
        summary += "Income by Category:\n"
        for category, amount in categories.items():
            summary += f"  {category:<20}: Rs. {amount:>12.2f}\n"
    summary += '\n'
    categories = {}
    for transaction in transactions:
        if transaction.get('Type') == 'Expenditure':
            category = transaction.get('Category')
            amount = float(transaction.get('Amount'))
            if category in categories:
                categories[category] += amount
            else:
                categories[category] = amount
    
    if categories:
        summary += "Expenditure by Category:\n"
        for category, amount in categories.items():
            summary += f"  {category:<20}: Rs. {amount:>12.2f}\n"
    summary += '\n'
    balance = calculate_balance(transactions)
    summary += f"\nCurrent Balance: Rs. {balance:>.2f}\n"
    
    
    return summary


def validate_date(date_str:str)->bool:
    """
    Validate if the given date string is in the format YYYY-MM-DD and if it is on or before today's date.
    
    Args:
    date_str (str): The date string to be validated.
    
    Returns:
    bool: True if the date is valid and on or before today, False otherwise.
    """
    try:
        # Parse the input date string into a datetime object
        income_date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Get today's date
        today = datetime.now()
        
        # Compare the income date to today's date
        if income_date <= today:
            return True
        else:
            return False
    
    except ValueError:
        # Return False if the date format is incorrect
        return False

def main():
    """Main function to run the command-line interface."""
    while True:
        print(f'\n\n{"-"*52}')
        print("===== Income and Expenditure Management System =====")
        print(f'{"-"*52}')
        print("  1. Add Income")
        print("  2. Record Expenditure")
        print("  3. View Balance")
        print("  4. View Transaction History")
        print("  5. Generate Summary Report")
        print("  6. Exit")
        print(f'{"-"*52}\n')
        
        choice = input(" Enter your choice (1-6): ")
        
        if choice == '1':
            clear_terminal()
            print(f'\n\n{"-"*52}\n')
            print(f"{'Add Income':^52}")
            print(f'{"-"*52}')
            while True:
                try:
                    amount = float(input("  Enter income amount              : "))
                    break  # If conversion is successful, exit the loop
                except ValueError:
                    print("  Invalid input. Please enter a numeric value.")
            category = input("  Enter category                   : ").capitalize()
            income_date = input("  Enter date of Income (YYYY-MM-DD): ")
            while not validate_date(income_date):
                print("  Invalid date. Please enter a date in YYYY-MM-DD format on or before today.")
                income_date = input("  Enter date of Income (YYYY-MM-DD): ")
            if add_income(amount,category, income_date):
                print("  Income added successfully.")
            else:
                print("  Something went wrong. Try again")
            print(f'{"-"*52}\n')
        elif choice == '2':
            clear_terminal()
            print(f'\n\n{"-"*52}\n')
            print(f"{'Record Expenditure':52}")
            print(f'{"-"*52}')
            while True:
                try:
                    amount = float(input("  Enter expenditure amount              : "))
                    break  # If conversion is successful, exit the loop
                except ValueError:
                    print("  Invalid input. Please enter a numeric value.")
            category = input("  Enter category                        : ").capitalize()
            expense_date = input("  Enter date of expenditure (YYYY-MM-DD): ")
            while not validate_date(expense_date):
                print("  Invalid date. Please enter a date in YYYY-MM-DD format on or before today.")
                expense_date = input("Enter date of expenditure (YYYY-MM-DD): ")
            if record_expenditure(amount, category, expense_date):
                print("  Expenditure recorded successfully.")
            else:
                print("  Something went wrong. Try again")
            print(f'{"-"*52}\n')
        elif choice == '3':
            clear_terminal()
            print(f'\n\n{"-"*52}')
            print(f"{'View Balance':^52}")
            print(f'{"-"*52}')
            transactions = load_transactions()
            if transactions:
                balance = calculate_balance(transactions)
                print(f"  Current Balance: Rs. {balance:.2f}")
            else:
                print(' No transaction found.')
            print(f'{"-"*52}\n')
        elif choice == '4':
            clear_terminal()
            print(f'\n\n{"-"*87}')
            print(f"{'Transaction History':^87}")
            print(f'{"-"*87}')
            transactions = load_transactions()
            if transactions:
                count=0
                print(f"{'SL.':<6}{'Type':<13}{'Amount':>13}  {'Category':^12}{'Date of Expense/Income':^24}{'Entry date':^12}")
                
                for transaction in transactions:
                    count+=1
                    print(f"{count:<6}{transaction.get('Type'):<13}{float(transaction.get('Amount')):>13.2f}  {transaction.get('Category'):^12}{transaction.get('Date of Expense/Income'):^24} {transaction.get('Date'):^12}")
            else:
                print(' No transaction found.')
            print(f'{"-"*87}\n')
        elif choice == '5':
            clear_terminal()
            print(f'\n\n{"-"*52}')
            print(f"{'Summary Report':^52}")
            print(f'{"-"*52}')
            transactions = load_transactions()
            if transactions:
                summary = generate_summary_report(transactions)
                print(summary)
            else:
                print(' No transaction found.')
            print(f'{"-"*52}\n')
        elif choice == '6':
            clear_terminal()
            print(f'\n\n{"-"*52}\n')
            print("Exiting program. Thank you!")
            print(f'{"-"*52}\n\n')
            break
        
        else:
            clear_terminal()
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
