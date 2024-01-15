from algosdk import account
import json 
import config 
def generate_nft_certificate(metadata):
    # Generate NFT certificate using metadata
    certificate = {
        "metadata": metadata,
        "signature": generate_signature(metadata)
    }
    return certificate

def generate_signature(metadata):
    # Convert the metadata to bytes
    metadata_bytes = json.dumps(metadata).encode()

    # Generate the signature using the private key
    private_key = config.ALGORAND_ACCOUNT_PRIVATE_KEY
    signature = account.sign_bytes(metadata_bytes, private_key)

    return signature


