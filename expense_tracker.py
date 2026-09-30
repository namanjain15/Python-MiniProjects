# ==========================================
# Personal Expense Tracker
# ==========================================

import datetime
import math
import os
import random


# Global Variables

APP_NAME = "Personal Expense Tracker"
expenses = []

total_expense = 0


# Add Expense

def add_expense():
    global total_expense

    try:
        title = input("Enter expense name: ")
        amount = float(input("Enter amount: ₹"))

        if amount <= 0:
            print("❌ Amount must be greater than 0.")
            return

        category = input("Enter category: ")

        expense = {
            "title": title,
            "amount": amount,
            "category": category
        }

        expenses.append(expense)

        total_expense += amount

        print("\n✅ Expense added successfully!")
        print(f"Expense: {title}")
        print(f"Amount: ₹{amount:.2f}")

    except ValueError:
        print("❌ Please enter a valid amount.")


# Display Expenses

def show_expenses():

    if not expenses:
        print("\n📭 No expenses recorded.")
        return

    print("\n========== EXPENSE LIST ==========")

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. "
            f"{expense['title']} | "
            f"₹{expense['amount']:.2f} | "
            f"{expense['category']}"
        )


# Calculate Statistics

def expense_statistics():

    # Local variable
    local_total = sum(
        expense["amount"] for expense in expenses
    )

    if len(expenses) > 0:

        average = local_total / len(expenses)

        highest = max(
            expenses,
            key=lambda x: x["amount"]
        )

        lowest = min(
            expenses,
            key=lambda x: x["amount"]
        )

        print("\n========== STATISTICS ==========")

        print(f"Total Expenses : ₹{local_total:.2f}")
        print(f"Average Expense: ₹{average:.2f}")

        print(
            f"Highest Expense: "
            f"{highest['title']} - ₹{highest['amount']:.2f}"
        )

        print(
            f"Lowest Expense : "
            f"{lowest['title']} - ₹{lowest['amount']:.2f}"
        )

    else:
        print("\n📭 No data available.")


# Category Summary

def category_summary():

    if not expenses:
        print("\n📭 No expenses available.")
        return

    categories = {}

    for expense in expenses:

        category = expense["category"]

        categories[category] = (
            categories.get(category, 0)
            + expense["amount"]
        )

    print("\n========== CATEGORY SUMMARY ==========")

    for category, amount in categories.items():

        print(
            f"{category}: ₹{amount:.2f}"
        )


# Random Expense Suggestion

def random_expense():

    if not expenses:
        print("\n📭 No expenses available.")
        return

    selected = random.choice(expenses)

    print("\n🎲 Random Expense")
    print(f"Name    : {selected['title']}")
    print(f"Amount  : ₹{selected['amount']:.2f}")
    print(f"Category: {selected['category']}")


# System Information

def system_information():

    current_time = datetime.datetime.now()

    print("\n========== SYSTEM INFORMATION ==========")

    print(f"Application : {APP_NAME}")
    print(f"Date & Time : {current_time}")
    print(f"Current Dir : {os.getcwd()}")

    print(
        f"Expense Count: {len(expenses)}"
    )


# Main Menu

def main():

    # Local variable
    running = True

    print("=" * 45)
    print(f"     {APP_NAME}")
    print("=" * 45)

    while running:

        print("\n1. Add Expense")
        print("2. Show Expenses")
        print("3. Expense Statistics")
        print("4. Category Summary")
        print("5. Random Expense")
        print("6. System Information")
        print("7. Exit")

        try:
            choice = int(
                input("\nEnter your choice: ")
            )

        except ValueError:
            print("❌ Please enter a number.")
            continue

        if choice == 1:

            add_expense()

        elif choice == 2:

            show_expenses()

        elif choice == 3:

            expense_statistics()

        elif choice == 4:

            category_summary()

        elif choice == 5:

            random_expense()

        elif choice == 6:

            system_information()

        elif choice == 7:

            running = False

            message = (
                "Thank you for using the Expense Tracker!"
                if total_expense > 0
                else "No expenses were recorded."
            )

            print(f"\n{message}")

        else:

            print("❌ Invalid choice.")


# Program Entry Point

if __name__ == "__main__":
    main()