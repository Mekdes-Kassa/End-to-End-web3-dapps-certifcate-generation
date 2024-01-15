from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_nft_certificate():
    response = client.post("/nft/create_nft_certificate")
    assert response.status_code == 200
    assert response.json() == {"message": "NFT certificate created and minted successfully"}

def test_generate_wallet():
    response = client.post("/wallet/generate_wallet")
    assert response.status_code == 200
    assert response.json() == {"message": "Wallet generated successfully"}

def test_deploy_contract():
    response = client.post("/contract/deploy_contract")
    assert response.status_code == 200
    assert response.json() == {"message": "Smart contract deployed successfully"}
