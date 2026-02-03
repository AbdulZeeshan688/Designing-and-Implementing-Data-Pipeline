# coin_acceptor.py se CoinAcceptor class import kar rahe hain
from coin_acceptor import CoinAcceptor

print("Program starting.")

# CoinAcceptor ka object bana rahe hain
coin_acceptor = CoinAcceptor()

# loop taake menu bar bar aaye
while True:
    print("\n1 - Insert coin")
    print("2 - Show coins")
    print("3 - Return coins")
    print("0 - Exit program")

    # user se choice le rahe hain
    choice = input("Your choice: ")

    if choice == "1":
        # coin insert kar rahe hain
        coin_acceptor.insertCoin()

    elif choice == "2":
        # current coins show kar rahe hain
        print(f"Currently '{coin_acceptor.getAmount()}' coins in coin acceptor")

    elif choice == "3":
        # coins return kar rahe hain
        returned = coin_acceptor.returnCoins()
        print(f"Coin acceptor returned '{returned}' coins.")

    elif choice == "0":
        # program band kar rahe hain
        print("Program ending.")
        break

    else:
        # agar ghalat option ho
        print("Invalid choice, try again.")
