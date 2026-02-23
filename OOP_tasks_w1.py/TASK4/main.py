# ==============================================================================
# Coder Name: Abdul Zeeshan Mirza
# Course: Designing and Implementing Data Pipelines
# Date: 2026-02-23
# Time: 23:23 EET
# Description: Main menu script for Cryptocurrency Wallet system.
# ==============================================================================

from wallet import CryptoWallet # importing class

# Multiple wallets store karne ke liye dictionary use kar rahe hain
wallets = {}

while True:
    print("\n--- Crypto Wallet Menu ---")
    print("1 - Create Wallet")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("4 - Check Balance")
    print("5 - Transaction History")
    print("0 - Exit")

    choice = input("Select an option: ")

    try:
        if choice == '1':
            # Naya wallet create karna
            w_id = input("Enter a unique Wallet ID: ")
            if w_id in wallets:
                print("Error: Wallet ID already existsPlease choose another one.")
            else:
                new_wallet = CryptoWallet(wallet_id=w_id)
                wallets[w_id] = new_wallet
                print(f"Wallet '{w_id}' has been created successfully.")

        elif choice == '2':
            # Wallet mein paise dalne ka logic
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                amount = float(input("Enter amount to deposit: "))
                wallets[w_id].deposit(amount)
            else:
                print("Error: Wallet not found.")

        elif choice == '3':
            # Wallet se paise nikalne ka logic
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                amount = float(input("Enter amount to withdraw: "))
                wallets[w_id].withdraw(amount)
            else:
                print("Error: Wallet not found.")

        elif choice == '4':
            # Balance check karne ke liye method call
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                wallets[w_id].check_balance()
            else:
                print("Error: Wallet not found.")

        elif choice == '5':
            # History print karne ke liye method call
            w_id = input("Enter Wallet ID: ")
            if w_id in wallets:
                wallets[w_id].generate_history()
            else:
                print("Error: Wallet not found.")

        elif choice == '0':
            # Program khatam karne ke liye
            print("Exiting Crypto Wallet System. Goodbye!")
            break

        else:
            # Agar user 0-5 ke ilawa kuch aur enter kare
            print("Invalid selection. Please try again.")

    except ValueError:
        # Agar text input dede kahan numbers zaroori the (like deposit amount)
        print("Error: Invalid input format. Please enter numeric values where required.")
    except Exception as e:
        # Koi aur unexpected error handle karne ke liye
        print(f"An unexpected error occurred: {e}")