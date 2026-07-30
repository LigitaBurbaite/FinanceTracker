expenses = []

while True:
    print("\n===== Personal Finance Tracker =====")
    print("1. Add expense")
    print("2. View Expenses")
    print("3. Exit")
    print("4. Remove expense")

    choice = input ("Choose an option: ")

    if choice == "1":
        name = input("Expense name: ")
        amount = float(input("Amount (£): "))
        category = input("category: ")
        expenses.append({
            "name": name,
            "amount": amount,
            "category": category
        })

        print("Expense added successfully!")

    elif choice =="2":
        total = 0

        if len(expenses) == 0:
            print("No expenses yet.")

        else:
            print("\nYour expenses:")

            for expense in expenses:
                print(f"{expense["name"]} - £{expense["amount"]:.2f} - {expense["category"]}")
                total += expense["amount"]

            print(f"\nTotal spent: £{total:.2f}")

    elif choice == "3":
        print("Goodbuy!")
        break

    elif choice == "4":
        remove_name = input("Which expense do you want to remove?")
        found = False

        for expense in expenses:
         print(expense["name"])
         if expense["name"]==remove_name:
           found = True
           expenses.remove(expense)
           print(f"{remove_name} Has been removed.")
           break

        if not found:
            print("expense not found.")
            
    else:
     print("Invalid option.")
