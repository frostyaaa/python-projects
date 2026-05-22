# expense tracker CLI model

# function to add expenses
def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    amount = float(input("Enter Amount: "))
    category = input("Enter Expense Category: ")
    description = input("Enter Description: ")

    expense ={
        "date": date,
        "amount": amount,
        "category": category,
        "description": description
    }
    expenses.append(expense)
    print("\nExpenses added succesfully.")

# function to view expense
def view_expense():
    if len(expenses)==0:
            print("\n No expenses found.")
    else:
        print("\nExpenses:")
        for expense in expenses:
            print(f"Date: {expense['date']}")
            print(f"Amount: {expense['amount']}")
            print(f"Category: {expense['category']}")
            print(f"Description: {expense['description']}")
            print("\n")

#function to calculate expenses
def total_expense():
    total_expense = 0
    for expense in expenses:
        total_expense += expense["amount"]
    print(f"\nTotal Expenses: {total_expense}")




expenses = []

print("\n Welcome to Expense Tracker")

while True:
    print("\n******MENU******")
    print("1. Add Expense")
    print("2. view Expense")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
        
    elif choice == "2":
        view_expense()
        
    elif choice == "3":
        total_expense()
    
    elif choice == "4":
        print("\nThanks for using Expense Tracker")
        break
        
    else:
        print("\nInvalid choice. Please try again.")




    
