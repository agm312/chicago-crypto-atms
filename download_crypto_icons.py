import os
import requests

def download_icon(symbol, filename):
    url = f"https://raw.githubusercontent.com/spothq/cryptocurrency-icons/master/svg/color/{symbol}.svg"
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {filename}")
    else:
        print(f"Failed to download: {filename}")

# Create directory if it doesn't exist
os.makedirs("static/images/crypto-icons", exist_ok=True)

# List of cryptocurrencies with their symbols and filenames
cryptos = [
    ("btc", "bitcoin.svg"),
    ("eth", "ethereum.svg"),
    ("usdt", "tether.svg"),
    ("usdc", "usdc.svg"),
    ("xrp", "xrp.svg"),
    ("doge", "dogecoin.svg"),
    ("ltc", "litecoin.svg"),
    ("bch", "bitcoin-cash.svg"),
    ("dai", "dai.svg"),
    ("shib", "shiba-inu.svg")
]

# Download each icon
for symbol, filename in cryptos:
    download_icon(symbol, f"static/images/crypto-icons/{filename}") 