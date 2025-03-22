import os
from PIL import Image, ImageDraw, ImageFont

def generate_atm_image(filename, title, color=(200, 100, 100)):
    # Create a new image with a solid color background
    img = Image.new('RGB', (800, 600), color=color)
    draw = ImageDraw.Draw(img)
    
    # Try to use a system font, or fall back to default
    try:
        font = ImageFont.truetype("Arial", 40)
    except IOError:
        font = ImageFont.load_default()
    
    # Draw text in the center of the image
    text = f"Crypto ATM\n{title}"
    
    # Use textbbox instead of textsize (which is deprecated)
    try:
        # For newer Pillow versions
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
    except AttributeError:
        # Fallback for older Pillow versions
        text_width, text_height = draw.textsize(text, font=font)
    
    position = ((800 - text_width) // 2, (600 - text_height) // 2)
    
    # Add a white rectangle behind the text for better visibility
    padding = 20
    draw.rectangle(
        [
            position[0] - padding,
            position[1] - padding,
            position[0] + text_width + padding,
            position[1] + text_height + padding
        ],
        fill=(255, 255, 255)
    )
    
    # Draw the text
    draw.text(position, text, fill=(0, 0, 0), font=font)
    
    # Save the image
    img.save(filename)
    print(f"Generated: {filename}")

def main():
    # Create directory if it doesn't exist
    os.makedirs("static/images/locations", exist_ok=True)
    
    # Dictionary of ATM titles and colors
    atm_info = {
        "digital_exchange": ("Digital Currency Exchange", (100, 150, 200)),
        "bitcoin_america": ("Bitcoin of America ATM", (200, 100, 100)),
        "seven_eleven": ("Bitcoin ATM at 7-Eleven", (100, 200, 100)),
        "default": ("Crypto ATM", (150, 150, 150)),
        "bitcoin_depot": ("Bitcoin Depot ATM", (200, 150, 100)),
        "coinflip": ("CoinFlip Bitcoin ATM", (100, 200, 200)),
        "rockitcoin": ("RockItCoin ATM", (200, 100, 200)),
        "crypto_corner": ("Crypto Corner ATM", (150, 200, 150)),
        "quick_crypto": ("Quick Crypto ATM", (200, 200, 100))
    }
    
    # Generate each image
    for image_id, (title, color) in atm_info.items():
        filename = f"static/images/locations/{image_id}.jpg"
        generate_atm_image(filename, title, color)

if __name__ == "__main__":
    main() 