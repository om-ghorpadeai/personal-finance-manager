# Personal Finance Manager

def add_income():
    try:
        amount = float(input("Enter income amount: ₹"))
        with open("finance.txt", "a") as file:
            file.write(f"Income,{amount}\n")
        print("✅ Income added successfully")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def add_expense():
    try:
        amount = float(input("Enter expense amount: ₹"))
        with open("finance.txt", "a") as file:
            file.write(f"Expense,{amount}\n")
        print("✅ Expense added successfully")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

def view_records():
    balance = 0
    try:
        with open("finance.txt", "r") as file:
            print("\n📊 --- Financial Records ---")

            for line in file:
                type_, amount = line.strip().split(",")
                amount = float(amount)

                if type_ == "Income":
                    balance += amount
                    print(f"💰 Income: ₹{amount}")
                else:
                    balance -= amount
                    print(f"💸 Expense: ₹{amount}")

        print("\n💼 Current Balance: ₹", balance)

    except FileNotFoundError:
        print("⚠️ No records found. Start by adding income or expenses.")

def menu():
    while True:
        print("\n" + "="*40)
        print("   💼 PERSONAL FINANCE MANAGER")
        print("="*40)
        print("1. Add Income")
        print("2. Add Expense")
        print("3. View Records")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_income()
        elif choice == "2":
            add_expense()
        elif choice == "3":
            view_records()
        elif choice == "4":
            print("\n👋 Exiting... Goodbye Om!")
            break
        else:
            print("❌ Invalid choice. Try again.")

# Run program
menu()
