import os

print("Welcome to the Expense Tracker!")

Expense_options = {
    1: "Track Expenses",
    2: "View Expense History",
    3: "Set_Budget",
    4: "Logout"
}

choose_Month = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}

def choose_option(username):
    print(Expense_options)
    option = int(input("Enter the number corresponding to your choice: "))
    if option in Expense_options:
        print(choose_Month)
        if Expense_options[option] == "Track Expenses":
            print("\n")
            month = input("Enter the month for which you want to set the budget (e.g., 1,2,3...12): ")
            
            TrackExpenses(username, choose_Month[int(month)])

        elif Expense_options[option] == "View Expense History":
            print("\n")
            month = input("Enter the month for which you want to set the budget (e.g., 1,2,3...12): ")
            
            Expense_History(username, choose_Month[int(month)])

        elif Expense_options[option] == "Set_Budget":
            print("\n")
            month = input("Enter the month for which you want to set the budget (e.g., 1,2,3...12): ")
            
            Set_Budget(username, choose_Month[int(month)])

        elif Expense_options[option] == "Logout":
            print("Logging out...")
            return "Thank you for using the Expense Tracker. Goodbye!"
    else:
        print("Invalid option. Please choose a valid option.")
        print("\n")
        choose_option(username)

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    # validate the username and password
    with open("./expense_users/user.txt", 'r') as f:
        users = f.readlines()
        if f"{username}:{password}\n" in users:
            print(f"Welcome back, {username},let's get started with tracking your expenses.")
            choose_option(username)
        else:
            print("Invalid username or password. Please try again.")
            login()
    
    return None

def register():
    username = input("Choose a username: ")
    password = input("Choose a password: ")

    # In a real application, you would validate the username and password
    data = {
        "username": username,
        "password": password
    }

    # Check if the username already exists
    if os.path.exists(f"./expense_users/{username}"):
        print("Username already exists. Please choose a different username.")
        return register()
    # If the username does not exist, create a new user directory and save the credentials
    else:
        os.makedirs(f"./expense_users/{username}")
        with open(f"./expense_users/user.txt", 'a') as f:
            f.write(f"{data['username']}:{data['password']}\n")
    
    # In a real application, you would save the username and password securely
    print(f"User {username} registered successfully!")
    return login()

def TrackExpenses(username,month):
    print("\n\n")
    print("Tracking expenses for user:", username)

    expense = []

    while True:
        
        expense_category = input("Enter the name of the expense category ex. travel, grocery, party, events, etc... (or type 'done' to finish): ").lower()
        if expense_category == 'done':
            break
        date = input("Enter the date of the expense (YYYY-MM-DD): ")
        expense_description = input("Enter a description for this expense: ").lower()
        expense_amount = float(input("Enter the amount for this expense: "))

        expense.append( {"date": date, "category": expense_category, "amount": expense_amount, "description": expense_description} )
    
    for exp in expense:
        if os.path.exists(f"./expense_users/{username}/{month}"):
            with open (f"./expense_users/{username}/{month}/expenses.txt", 'a') as f:
                f.write(f"{exp}\n")
        else:
            os.makedirs(f"./expense_users/{username}/{month}", exist_ok=True)
            with open (f"./expense_users/{username}/{month}/expenses.txt", 'a') as f:
                f.write(f"{exp}\n")
    return choose_option(username)

def Set_Budget(username,month):

    print("\n\n")

    print("Budget Allocation:")

    Monthly_income = float(input("Enter your monthly income: "))
    Long_term_saving_percentage = float(input("Enter the percentage of your income you want to save for long-term goals: "))
    Short_term_saving_percentage = float(input("Enter the percentage of your income you want to save for short-term goals: "))
    Mid_term_saving_percentage = float(input("Enter the percentage of your income you want to save for mid-term goals: "))
    Essential_expenses_percentage = float(input("Enter the percentage of your income you want to allocate for essential expenses: "))

    Long_term_saving = (Long_term_saving_percentage/100) * Monthly_income
    Short_term_saving = (Short_term_saving_percentage/100) * Monthly_income
    Mid_term_saving = (Mid_term_saving_percentage/100) * Monthly_income
    Essential_expenses = (Essential_expenses_percentage/100) * Monthly_income  

    if not os.path.exists(f"./expense_users/{username}/{month}"):
        os.makedirs(f"./expense_users/{username}/{month}", exist_ok=True)
    
    with open(f"./expense_users/{username}/{month}/budget.txt", 'a') as f:
        f.write(f"Monthly_Income: {Monthly_income}\n")
        f.write(f"Longterm_savings: {Long_term_saving}\n")
        f.write(f"Shortterm_savings: {Short_term_saving}\n")
        f.write(f"Midterm_savings: {Mid_term_saving}\n")
        f.write(f"Essential_expenses: {Essential_expenses}\n")
        f.write(f"Total_allocated: {Long_term_saving + Short_term_saving + Mid_term_saving + Essential_expenses}\n")
        f.write(f"Remaining_income: {Monthly_income - (Long_term_saving + Short_term_saving + Mid_term_saving + Essential_expenses)}\n")
    
    return choose_option(username)

def Expense_History(username,month):
    print("\n")
    if os.path.exists(f"./expense_users/{username}/{month}/expenses.txt"):
        with open(f"./expense_users/{username}/{month}/expenses.txt", 'r') as f:
            expenses = f.readlines()
            for expense in expenses:
                print(expense)
    else:
        print("No expenses found for this month.")
    return choose_option(username)


choose = {1: "login", 2: "register"}

ask_user = int(input("Do you want to (1) Login or (2) Register? "))

    # # Handle the user's choice and call the appropriate function
if ask_user in choose:
    user = choose[ask_user]
    if user == "login":
        login()
    elif user == "register":
        register()
else:
    print("Invalid choice. Please choose either 1 or 2.")


