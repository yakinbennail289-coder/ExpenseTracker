def show_average():

    if not expenses:
        print("No expenses recorded.")
        return

    total = 0

    for expense in expenses:
        total += expense["amount"]

    average = total / len(expenses)

    print("Average =", average)


expenses = []

while True:

    print("\n=== Expense Tracker ===")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expenses")
    print("4. Exit")
    print("5. Show Average")

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
        show_average()

    else:
        print("Invalid choice")
