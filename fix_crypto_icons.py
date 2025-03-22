import os
import shutil

def main():
    # Create directory if it doesn't exist
    os.makedirs("static/images/crypto-icons", exist_ok=True)
    
    # Map of existing icon filenames to lowercase symbol names
    icon_mapping = {
        "bitcoin.svg": "btc.svg",
        "ethereum.svg": "eth.svg",
        "tether.svg": "usdt.svg",
        "usdc.svg": "usdc.svg",
        "xrp.svg": "xrp.svg",
        "dogecoin.svg": "doge.svg",
        "litecoin.svg": "ltc.svg",
        "bitcoin-cash.svg": "bch.svg",
        "dai.svg": "dai.svg",
        "shiba-inu.svg": "shib.svg"
    }
    
    # Copy and rename each icon
    for original, new_name in icon_mapping.items():
        original_path = f"static/images/crypto-icons/{original}"
        new_path = f"static/images/crypto-icons/{new_name}"
        
        # Skip if source and destination are the same
        if original_path == new_path:
            print(f"Skipping {original} as it's the same as {new_name}")
            continue
            
        if os.path.exists(original_path):
            shutil.copy2(original_path, new_path)
            print(f"Copied {original} to {new_name}")
        else:
            print(f"Warning: {original_path} does not exist")

if __name__ == "__main__":
    main() 