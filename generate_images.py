import os
from PIL import Image, ImageDraw, ImageFont
import random

def create_image(width, height, text, filename, is_hero=False):
    # Create a new image with a random background color
    if is_hero:
        background_color = (40, 40, 40)  # Dark gray for hero
    else:
        background_color = (random.randint(200, 255), random.randint(200, 255), random.randint(200, 255))
    
    image = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Add some shapes for visual interest
    for _ in range(5):
        shape_color = (
            random.randint(180, 220),
            random.randint(180, 220),
            random.randint(180, 220)
        )
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        draw.line([(x1, y1), (x2, y2)], fill=shape_color, width=3)

    # Add text
    try:
        font_size = 40 if is_hero else 30
        font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", font_size)
    except:
        font = ImageFont.load_default()

    # Calculate text size and position
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # Add a semi-transparent overlay for better text visibility
    if is_hero:
        overlay = Image.new('RGBA', (width, height), (0, 0, 0, 128))
        image.paste(overlay, (0, 0), overlay)

    # Draw the text
    draw.text((text_x, text_y), text, fill='white', font=font)

    # Save the image
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    image.save(filename)
    print(f"Created image: {filename}")

def main():
    # Create hero image
    create_image(1200, 400, "", "static/images/chicago-hero.jpg", is_hero=True)

    # Create location images
    locations = {
        'default': 'Default ATM Location',
        'digital_exchange': 'Digital Currency Exchange',
        'bitcoin_america': 'Bitcoin of America ATM',
        'seven_eleven': 'Bitcoin ATM at 7-Eleven',
        'bitcoin_depot': 'Bitcoin Depot ATM',
        'coinflip': 'CoinFlip Bitcoin ATM',
        'rockitcoin': 'RockItCoin ATM',
        'crypto_corner': 'Crypto Corner ATM',
        'quick_crypto': 'Quick Crypto ATM'
    }

    for image_id, text in locations.items():
        filename = f"static/images/locations/{image_id}.jpg"
        create_image(800, 600, text, filename)

if __name__ == "__main__":
    main() 