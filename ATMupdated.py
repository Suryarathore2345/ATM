import time
from datetime import datetime

# Initialize balance, PIN, transaction history, and daily withdrawal limit
balance = 1000.0
correct_pin = "1234"
transaction_history = []
daily_withdrawal_limit = 500.0
daily_withdrawn = 0.0

# Simulate entering the card and PIN
print("Please insert your card...")
time.sleep(5)  # Simulating card insertion delay
input("Press Enter to continue...")

# Prompt for PIN
pin_attempts = 0
max_attempts = 3

while pin_attempts < max_attempts:
    entered_pin = input("Please enter your PIN: ")
    if entered_pin == correct_pin:
        print("PIN accepted. Welcome to the ATM.")
        break
    else:
        pin_attempts += 1
        if pin_attempts < max_attempts:
            print("Incorrect PIN. You have " + str(max_attempts - pin_attempts) + " attempts left.")
        else:
            print("Incorrect PIN. You have reached the maximum number of attempts. Card blocked.")
            exit()

continue_banking = True

while continue_banking:
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Change PIN")
    print("5. Check Transaction History")
    print("6. Exit")
    
    try:
        choice = int(input("Please choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        # Check Balance
        print("\n-------------------")
        print(f"Your current balance is: Rs{balance:,.2f}")
        print("-------------------")
    elif choice == 2:
        # Deposit Money
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                balance += amount
                transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Deposited Rs{amount:,.2f}")
                print("\n------------------------")
                print(f"You have deposited Rs{amount:,.2f}.")
                print(f"Your new balance is: Rs{balance:,.2f}")
                print("------------------------")
        except ValueError:
            print("Invalid input. Please enter a valid amount.")
    elif choice == 3:
        # Withdraw Money
        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("\n------------------------")
                print("Insufficient funds.")
                print("\n------------------------")
            elif daily_withdrawn + amount > daily_withdrawal_limit:
                print("\n------------------------")
                print(f"Daily withdrawal limit exceeded. You can withdraw up to Rs{daily_withdrawal_limit - daily_withdrawn:,.2f} more today.")
                print("\n------------------------")
            else:
                balance -= amount
                daily_withdrawn += amount
                transaction_history.append(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - Withdrew Rs{amount:,.2f}")
                print("\n------------------------")
                print(f"You have withdrawn Rs{amount:,.2f}.")
                print(f"Your new balance is: Rs{balance:,.2f}")
                print("------------------------")
        except ValueError:
            print("\nInvalid input. Please enter a valid amount.")
    elif choice == 4:
        # Change PIN
        new_pin = input("Enter new PIN: ")
        confirm_pin = input("Confirm new PIN: ")
        if new_pin == confirm_pin and len(new_pin) == 4 and new_pin.isdigit():
            correct_pin = new_pin
            print("\n-------------------")
            print("PIN successfully changed.")
            print("-------------------")
        else:
            print("\n-------------------")
            print("PIN change failed. Make sure the PINs match and are exactly 4 digits.")
            print("-------------------")
    elif choice == 5:
        # Check Transaction History
        print("\n-------------------")
        if transaction_history:
            print("Transaction History:")
            for transaction in transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")
        print("-------------------")
    elif choice == 6:
        print("\n-----------------------------")
        print("Thank you for using the ATM. Goodbye!")
        print("-----------------------------")
        continue_banking = False
    else:
        print("\n-----------------------")
        print("Invalid choice. Please choose a number between 1 and 6.")
        print("-----------------------")
