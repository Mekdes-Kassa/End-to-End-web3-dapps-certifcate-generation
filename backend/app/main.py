from fastapi import FastAPI
from app.api import nft, wallet, contract

app = FastAPI()

app.include_router(nft.router, prefix="/nft", tags=["NFT"])
app.include_router(wallet.router, prefix="/wallet", tags=["Wallet"])
app.include_router(contract.router, prefix="/contract", tags=["Contract"])
