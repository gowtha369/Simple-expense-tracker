from decimal import Decimal, InvalidOperation

expenses = []

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

        expenses.append((name, amount))
        print("Expense added!")

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
