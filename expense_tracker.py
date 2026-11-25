def delete_expense():

    if not expenses:
        print("No expenses to delete.")
        return

    for i, expense in enumerate(expenses, start=1):
        print(i, expense["description"])

    choice = input("Expense number to delete: ")

    if choice.isdigit():

        index = int(choice) - 1

        if 0 <= index < len(expenses):

            removed = expenses.pop(index)

            print("Deleted:",
                  removed["description"])


expenses = []

while True:

    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    print("5.delete Expense")
    choice = input("Enter your choice: ")

    if choice == "1":

        description = input("Description: ")
        amount = float(input("Amount: "))

        expense = {
            "description": description,
            "amount": amount
        }

        expenses.append(expense)

    elif choice == "2":

        for expense in expenses:
            print(
                expense["description"],
                "-",
                expense["amount"]
            )

    elif choice == "3":

        total = 0

        for expense in expenses:
            total += expense["amount"]

        print("Total =", total)

    elif choice == "4":
        break

    elif choice == "5":
        delete_expense()
    else:
        print("Invalid choice")
