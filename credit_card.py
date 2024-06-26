class CreditCard:
    # Constructor
    def __init__(self, client, bank, account, limit):
        self._client = client
        self._bank = bank
        self._account = account
        self._limit = limit
        self._balance = 0

    # Encapsulation
    def get_client(self):
        return self._client

    def get_bank(self):
        return self._bank
    
    def get_account(self):
        return self._account

    def get_limit(self):
        return self._limit

    def get_balance(self):
        return self._balance

    # Additional Methods
    def charge(self, price):
        if (price+self._balance) > self._limit:
            return False
        else:
            self._balance+=price
            return True

    def make_payment(self, amount):
        self._balance-=amount

# Testing the class
if __name__=="__main__":
    wallet = CreditCard("MD Saim Islam", "Brac Bank PLC", "1063476100001", 50000)
    wallet.charge(1400)
    print(f"{wallet.get_client()} has {wallet.get_balance()} BDT")
    wallet.make_payment(1400)
    print(f"After Payment {wallet.get_client()} has {wallet.get_balance()} BDT")



    
