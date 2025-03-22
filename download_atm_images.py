import os
import requests
from PIL import Image
from io import BytesIO

def download_image(url, filename):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img = img.resize((800, 600), Image.LANCZOS)  # Resize to consistent dimensions
            img.save(filename)
            print(f"Downloaded: {filename}")
            return True
        else:
            print(f"Failed to download {url}: Status code {response.status_code}")
            return False
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return False

def main():
    # Create directory if it doesn't exist
    os.makedirs("static/images/locations", exist_ok=True)
    
    # Dictionary of ATM images to download
    atm_images = {
        "digital_exchange": "https://www.bitsonline.com/wp-content/uploads/2018/01/bitcoin-atm-1068x712.jpg",
        "bitcoin_america": "https://www.chicagotribune.com/resizer/Ck_ySJGBGLGYLXYfnALOqiVQLDQ=/1200x0/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/JTWX5OWLHFHVFPZAEDLGJ2OGME.jpg",
        "seven_eleven": "https://www.atmmarketplace.com/sites/atmmarketplace.com/files/styles/max_width_770/public/2018-01-11-bitcoin-atm-7-eleven.jpg?itok=_4hF9Zxe",
        "default": "https://www.atmia.com/files/ATM%20Security/Bitcoin%20ATM.jpg",
        "bitcoin_depot": "https://www.retaildive.com/user_media/cache/12/1a/121a5941-0d94-4034-a0a2-6b50fd3918d6/bitcoin-atm-bitcoin-depot-1000_tojfur.jpg",
        "coinflip": "https://www.chicagotribune.com/resizer/Ck_ySJGBGLGYLXYfnALOqiVQLDQ=/1200x0/top/arc-anglerfish-arc2-prod-tronc.s3.amazonaws.com/public/JTWX5OWLHFHVFPZAEDLGJ2OGME.jpg",
        "rockitcoin": "https://www.atmmarketplace.com/sites/atmmarketplace.com/files/styles/max_width_770/public/2018-01-11-bitcoin-atm-7-eleven.jpg?itok=_4hF9Zxe",
        "crypto_corner": "https://www.bitsonline.com/wp-content/uploads/2018/01/bitcoin-atm-1068x712.jpg",
        "quick_crypto": "https://www.atmia.com/files/ATM%20Security/Bitcoin%20ATM.jpg"
    }
    
    # Download each image
    for image_id, url in atm_images.items():
        filename = f"static/images/locations/{image_id}.jpg"
        download_image(url, filename)

if __name__ == "__main__":
    main() 