import csv
from decimal import Decimal, InvalidOperation
from pathlib import Path

file_path = Path(__file__).with_name("expenses.csv")
expenses = []

# Read expenses saved earlier.
if file_path.exists():
    with file_path.open(newline="", encoding="utf-8") as file:
        for name, amount in csv.reader(file):
            expenses.append((name, Decimal(amount)))

while True:
    print("\n--- My Expense Tracker ---")
    print("1. Add an expense")
    print("2. Show expenses and total")
    print("3. Exit")

    choice = input("Choose 1, 2, or 3: ").strip()

    if choice == "1":
        name = input("What did you spend money on? ").strip()

        if not name:
            print("Please enter a name.")
            continue

        try:
            amount = Decimal(input("Amount in SEK: ").strip())

            if not amount.is_finite() or amount <= 0:
                print("Please enter an amount greater than zero.")
                continue

        except InvalidOperation:
            print("Please enter a number, like 80 or 25.50.")
            continue

        # Save the new expense.
        with file_path.open("a", newline="", encoding="utf-8") as file:
            csv.writer(file).writerow([name, str(amount)])

        expenses.append((name, amount))
        print("Expense saved!")

    elif choice == "2":
        if not expenses:
            print("No expenses yet.")
        else:
            for name, amount in expenses:
                print(f"{name}: {amount:.2f} SEK")

            total = sum(amount for name, amount in expenses)
            print(f"Total: {total:.2f} SEK")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, or 3.")
