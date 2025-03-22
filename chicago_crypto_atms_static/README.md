# Chicago Crypto ATMs

A static website directory for cryptocurrency ATMs in Chicago neighborhoods.

## Website Structure

- `index.html` - Main homepage with featured ATMs and search functionality
- `neighborhood/` - Directory of neighborhood pages with ATM listings
- `cryptocurrency/` - Directory of pages for each cryptocurrency type
- `static/` - Static assets (CSS, JavaScript, images)
  - `static/js/` - JavaScript files including search functionality
  - `static/images/` - Images for ATMs and cryptocurrencies
  - `static/css/` - CSS stylesheets (if separated from inline styles)

## How to Update ATM Locations

### 1. Update Neighborhood HTML Files

To add new ATM locations, edit the appropriate neighborhood HTML file in the `neighborhood/` directory. Each ATM listing follows this structure:

```html
<article class="atm-card">
    <img src="/static/images/locations/default.jpg" alt="ATM Name" class="atm-image">
    <div class="atm-details">
        <h2 class="atm-name">ATM Name</h2>
        <p class="atm-type">ATM Type (Buy-only or Two-way)</p>
        <div class="rating">
            ⭐⭐⭐⭐
            <span>(123)</span>
        </div>
        <p class="atm-address">123 Street Name, Chicago, IL 60600</p>
        <p class="atm-phone">(123) 456-7890</p>
        <div class="crypto-types">
            <span>Bitcoin</span>
            <span>Ethereum</span>
            <span>XRP</span>
            <!-- Add more cryptocurrencies as needed -->
        </div>
        <a href="https://atm-website.com" class="visit-button">Visit Website</a>
    </div>
</article>
```

### 2. Update Data JSON

For client-side search functionality to work correctly, also update the ATM data in `static/js/data.json`. Add a new entry following this structure:

```json
{
  "id": "unique-atm-id",
  "name": "ATM Name",
  "type": "Two-way Crypto ATM",
  "rating": 4.5,
  "reviews": 123,
  "address": "123 Street Name, Chicago, IL 60600",
  "phone": "(123) 456-7890",
  "neighborhood": "neighborhood-slug",
  "cryptocurrencies": ["bitcoin", "ethereum", "xrp"],
  "image": "/static/images/locations/default.jpg"
}
```

### 3. Adding New Images

If you have custom images for ATMs:

1. Place the image in the `static/images/locations/` directory
2. Reference the image in both the HTML and JSON data
3. Use optimized images (JPG/PNG) around 800x600px in size

## Search Functionality

The website includes client-side search functionality that:

1. Searches for cryptocurrencies by name (Bitcoin, Ethereum, etc.)
2. Searches for neighborhoods (Lincoln Park, West Loop, etc.)
3. Searches for specific ATMs by name or address
4. Redirects users to the appropriate page based on search results

The search functionality is implemented in `static/js/search.js` and uses data from `static/js/data.json`.

## Deployment

This is a static website that can be deployed to any static hosting provider:

- GitHub Pages
- Netlify
- Vercel
- Any web hosting service that supports static HTML/CSS/JS

## License

This project is for demonstration purposes. All rights reserved. 