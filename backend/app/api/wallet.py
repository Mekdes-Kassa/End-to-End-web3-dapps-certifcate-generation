from fastapi import APIRouter
from algosdk import algod, account 

router = APIRouter()

@router.post("/gwallet")
class Wallet:
    def __init__(self):
        self.accounts = []

    def create_account(self):
        private_key, address = account.generate_account()
        self.accounts.append({"private_key": private_key, "address": address})
        return address

    def get_balance(self, address):
        # Connect to the Algorand node
        algod_client = algod.AlgodClient(self.algod_token, self.algod_address)

        # Get the account information
        account_info = algod_client.account_info(address)

        # Retrieve the balance from the account information
        balance = account_info.get("amount", 0)

        return balance




