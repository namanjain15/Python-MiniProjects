# Smart ATM System

class InsufficientBalanceError(Exception):
    """Custom error for insufficient account balance."""
    pass


def show_balance(balance):
    print(f"\n💰 Current Balance: ₹{balance:.2f}")


def withdraw_money(balance):
    try:
        amount = float(input("Enter amount to withdraw: ₹"))

        # Raising custom error
        if amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if amount > balance:
            raise InsufficientBalanceError(
                "Insufficient balance for this withdrawal."
            )

        balance -= amount
        print(f"✅ ₹{amount:.2f} withdrawn successfully.")
        print(f"💰 Remaining Balance: ₹{balance:.2f}")

        return balance

    except ValueError as error:
        print(f"❌ Invalid input: {error}")

    except InsufficientBalanceError as error:
        print(f"❌ Transaction failed: {error}")

    finally:
        print("🔒 Withdrawal process completed.")

    return balance


def check_transaction_history(history):
    print("\n📜 Transaction History")

    # for loop with else
    for transaction in history:
        print(f"- {transaction}")
    else:
        print("✔ Transaction history checked successfully.")


def deposit_money(balance, history):
    try:
        amount = float(input("Enter amount to deposit: ₹"))

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        balance += amount

        history.append(f"Deposited ₹{amount:.2f}")

        print(f"✅ ₹{amount:.2f} deposited successfully.")
        print(f"💰 New Balance: ₹{balance:.2f}")

        return balance

    except ValueError as error:
        print(f"❌ Invalid amount: {error}")

    finally:
        print("🔒 Deposit process completed.")

    return balance


# -----------------------------
# Main Program
# -----------------------------

balance = 10000.00
history = []

print("================================")
print("       🏦 SMART ATM SYSTEM")
print("================================")

while True:

    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice (according to the serial number): "))

        if choice == 1:

            show_balance(balance)

        elif choice == 2:

            old_balance = balance
            balance = deposit_money(balance, history)

            if balance != old_balance:
                history.append(
                    f"Balance after deposit: ₹{balance:.2f}"
                )

        elif choice == 3:

            old_balance = balance
            balance = withdraw_money(balance)

            if balance != old_balance:
                history.append(
                    f"Withdrawn successfully. Balance: ₹{balance:.2f}"
                )

        elif choice == 4:

            if len(history) == 0:
                print("\n⚠ No transactions available.")
            else:
                check_transaction_history(history)

        elif choice == 5:

            print("\nThank you for using Smart ATM! 👋")
            break

        else:

            raise ValueError("Please choose a number between 1 and 5.")

    except ValueError as error:
        print(f"❌ Error: {error}")

    finally:
        print("\n-------------------------------")
        print("ATM session step completed.")
        print("-------------------------------")