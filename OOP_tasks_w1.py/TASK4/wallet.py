import datetime

class CryptoWallet:
    def __init__(self, wallet_id: str) -> None:
        # Private attributes set kar rahe hain taake bahar se direct access na ho
        self._walletId = wallet_id
        self._balance = 0.0
        
        # Transactions ka record rakhne ke liye list
        self._transactions = [] 
        self._record_transaction("Wallet created")

    def _record_transaction(self, details: str) -> None:
        # Private method jo sirf class ke andar use hoga history update karne ke liye
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") # --- USED AI HERE ---
        self._transactions.append(f"[{timestamp}] {details}")

    def deposit(self, amount: float) -> None:
        # Amount deposit karne ka logic
        if amount > 0:
            self._balance += amount
            self._record_transaction(f"Deposited: {amount}")
            print(f"Successfully deposited {amount} to wallet {self._walletId}.")
        else:
            print("Deposit amount must be greater than zero.")

    def withdraw(self, amount: float) -> None:
        # Amount withdraw karne ka logic aur validation
        if amount > 0:
            if self._balance >= amount:
                self._balance -= amount
                self._record_transaction(f"Withdrew: {amount}")
                print(f"Successfully withdrew {amount} from wallet {self._walletId}.")
            else:
                print("Insufficient balance! Transaction failed.")
        else:
            print("Withdraw amount must be greater than zero.")

    def check_balance(self) -> None:
        # Balance check karne ke liye method, direct variable access kiye baghair
        print(f"Current balance for wallet {self._walletId}: {self._balance}")

    def generate_history(self) -> None:
        # Transaction history screen par print karne ke liye
        print(f" Transaction History ({self._walletId})")
        if not self._transactions:
            print("No transactions found.")
        else:
            for txn in self._transactions:
                print(txn)
        print("-----------------------------------")