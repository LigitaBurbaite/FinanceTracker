expenses = []


def add_expense(expenses):
    name = input("Expense name: ")
    amount = float(input("Amount (£): "))
    category = input("Category: ")

    expenses.append({"name": name, "amount": amount, "category": category})
    print("Expense added successfully!")
    save_expenses(expenses)


def view_expenses(expenses):
    total = 0

    if len(expenses) == 0:
        print("No expenses yet.")
    else:
        print("\nYour expenses:")

        for expense in expenses:
            print(
                f"{expense['name']} - £{expense['amount']:.2f} - {expense['category']}"
            )
            total += expense["amount"]

        print(f"\nTotal spent: £{total:.2f}")


def remove_expense(expenses):
    remove_name = input("Which expense do you want to remove?")
    found = False

    for expense in expenses:
        if expense["name"].lower() == remove_name.lower():
            found = True
            expenses.remove(expense)
            print(f"{remove_name} Has been removed.")
            save_expenses(expenses)

            break

    if not found:
        print(f"`{remove_name}` was not found.")


def main():
    expenses = load_expenses()

    while True:
        print("\n===== Personal Finance Tracker =====")
        print("1. Add expense")
        print("2. View Expenses")
        print("3. Exit")
        print("4. Remove expense")

        choice = input("Choose an option: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            print("Goodbye!")
            break

        elif choice == "4":
            remove_expense(expenses)

        else:
            print("Invalid option.")


def save_expenses(expenses):
    with open("expenses.txt", "w") as f:
        for expense in expenses:
            f.write(f"{expense['name']},{expense['amount']},{expense['category']}\n")
    print("Expenses saved to expenses.txt")


def load_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                name, amount, category = line.strip().split(",")

                expenses.append(
                    {"name": name, "amount": float(amount), "category": category}
                )

    except FileNotFoundError:
        print("No saved expenses found.")

    return expenses


main()
