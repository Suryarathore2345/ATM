# ATM
#Simple ATM Stimulator
import time

# Initialize balance and PIN
balance = 1000.0
correct_pin = "1234"

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
    print("4. Exit")
    
    try:
        choice = int(input("Please choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue

    if choice == 1:
        # Check Balance
        print("\n-------------------")
        print("Your current balance is: Rs" + str(round(balance, 2)))
        print("-------------------")
    elif choice == 2:
        # Deposit Money
        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("Deposit amount must be positive.")
            else:
                balance += amount
                print("\n------------------------")
                print("You have deposited Rs" + str(round(amount, 2)) + ".")
                print("Your new balance is: Rs" + str(round(balance, 2)))
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
            else:
                balance -= amount
                print("\n------------------------")
                print("You have withdrawn Rs" + str(round(amount, 2)) + ".")
                print("Your new balance is: Rs" + str(round(balance, 2)))
                print("------------------------")
        except ValueError:
            print("\nInvalid input. Please enter a valid amount.")
    elif choice == 4:
        print("\n-----------------------------")
        print("Thank you for using the ATM. Goodbye!")
        print("-----------------------------")
        continue_banking = False
    else:
        print("\n-----------------------")
        print("Invalid choice. Please choose a number between 1 and 4.")
        print("-----------------------")
