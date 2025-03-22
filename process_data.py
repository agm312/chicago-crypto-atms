import pandas as pd
import os
from jinja2 import Environment, FileSystemLoader
import json
import random
import numpy as np

def get_supported_cryptocurrencies():
    return {
        'BTC': {'name': 'Bitcoin', 'symbol': 'BTC'},
        'ETH': {'name': 'Ethereum', 'symbol': 'ETH'},
        'USDT': {'name': 'Tether', 'symbol': 'USDT'},
        'USDC': {'name': 'USD Coin', 'symbol': 'USDC'},
        'XRP': {'name': 'XRP', 'symbol': 'XRP'},
        'DOGE': {'name': 'Dogecoin', 'symbol': 'DOGE'},
        'LTC': {'name': 'Litecoin', 'symbol': 'LTC'},
        'BCH': {'name': 'Bitcoin Cash', 'symbol': 'BCH'},
        'DAI': {'name': 'Dai', 'symbol': 'DAI'},
        'SHIB': {'name': 'Shiba Inu', 'symbol': 'SHIB'}
    }

def get_chicago_neighborhoods():
    return [
        {'id': 'loop', 'name': 'The Loop'},
        {'id': 'river-north', 'name': 'River North'},
        {'id': 'lincoln-park', 'name': 'Lincoln Park'},
        {'id': 'wicker-park', 'name': 'Wicker Park'},
        {'id': 'logan-square', 'name': 'Logan Square'},
        {'id': 'west-loop', 'name': 'West Loop'},
        {'id': 'south-loop', 'name': 'South Loop'},
        {'id': 'gold-coast', 'name': 'Gold Coast'},
        {'id': 'lakeview', 'name': 'Lakeview'},
        {'id': 'uptown', 'name': 'Uptown'}
    ]

def extract_neighborhood(address):
    neighborhoods = get_chicago_neighborhoods()
    # For demo purposes, assign random neighborhood
    return random.choice(neighborhoods)

def get_image_id(title):
    if 'Digital Currency Exchange' in title:
        return 'digital_exchange'
    elif 'Bitcoin of America' in title:
        return 'bitcoin_america'
    elif '7-Eleven' in title:
        return 'seven_eleven'
    return 'default'

def read_excel_data():
    # Create title list for ATMs with existing ATMs first
    titles = [
        'Digital Currency Exchange',
        'Bitcoin of America ATM',
        'Bitcoin ATM at 7-Eleven',
        'Bitcoin Depot ATM',
        'CoinFlip Bitcoin ATM',
        'RockItCoin ATM',
        'Crypto Corner ATM',
        'Quick Crypto ATM',
        # New ATMs for Lincoln Park
        'Coinflip ATM - Lincoln Park',
        'Bitcoin Depot - Fullerton Ave',
        'RockItCoin ATM - DePaul',
        # New ATMs for Logan Square
        'Coinflip ATM - Milwaukee Ave',
        'Cryptobase ATM - Logan Square',
        'Bitcoin Depot - 24/7 Location',
        # New ATMs for West Loop
        'Bitcoin Depot - West Loop',
        'Coinhub ATM - Fulton Market',
        'RockItCoin ATM - West Loop',
        # New ATMs for South Loop
        'Coinhub ATM - Manhattan Mart',
        'CoinMe ATM - Roosevelt Rd',
        'Cryptobase ATM - 24/7 Location',
        # New ATMs for Uptown
        'RockItCoin ATM - Uptown',
        'Coinflip ATM - Wilson Ave',
        'Bitcoin Depot - 24/7 Location',
    ]
    
    # Add ATMs from the CSV data (1-10)
    for i in range(1, 11):
        operator = ['Bitcoin Depot', 'Coinflip', 'LibertyX', 'CoinSpot', 'Kurant'][i % 5]
        titles.append(f'{operator} ATM00{i:02d}')
    
    # Add ATMs from the CSV data (11-85)
    for i in range(11, 86):
        operator = ['Bitcoin Depot', 'Coinflip', 'LibertyX', 'CoinSpot', 'Kurant'][i % 5]
        titles.append(f'{operator} ATM00{i:02d}')
    
    # Generate addresses for all ATMs
    addresses = [
        '789 N Michigan Ave, Chicago, IL 60611',
        '987 W Belmont Ave, Chicago, IL 60657',
        '123 State St, Chicago, IL 60601',
        '852 W Addison St, Chicago, IL 60613',
        '654 N Milwaukee Ave, Chicago, IL 60622',
        '741 N Western Ave, Chicago, IL 60622',
        '456 N Wells St, Chicago, IL 60654',
        '321 N Clark St, Chicago, IL 60654',
        # Lincoln Park addresses
        '2470 N Clark St, Chicago, IL 60614',
        '2400 N Halsted St, Chicago, IL 60614',
        '2250 N Lincoln Ave, Chicago, IL 60614',
        # Logan Square addresses
        '2759 N Milwaukee Ave, Chicago, IL 60647',
        '2501 N Milwaukee Ave, Chicago, IL 60647',
        '2610 N Milwaukee Ave, Chicago, IL 60647',
        # West Loop addresses
        '925 W Randolph St, Chicago, IL 60607',
        '818 W Fulton Market, Chicago, IL 60607',
        '150 N Halsted St, Chicago, IL 60661',
        # South Loop addresses
        '424 S Clark St, Chicago, IL 60605',
        '1167 S Roosevelt Rd, Chicago, IL 60605',
        '725 S State St, Chicago, IL 60605',
        # Uptown addresses
        '4520 N Broadway, Chicago, IL 60640',
        '1130 W Wilson Ave, Chicago, IL 60640',
        '4800 N Broadway, Chicago, IL 60640',
    ]
    
    # Add addresses for ATMs 1-10
    for i in range(1, 11):
        addresses.append(f'{1000 + (i * 100)} N State St, Chicago, IL 60610')
    
    # Add addresses for ATMs 11-85
    for i in range(11, 86):
        streets = ['Clark St', 'State St', 'Michigan Ave', 'Broadway', 'Milwaukee Ave', 
                   'Halsted St', 'Western Ave', 'Ashland Ave', 'Damen Ave', 'Division St']
        direction = 'N' if i % 2 == 0 else 'S'
        street = streets[i % len(streets)]
        addresses.append(f'{3000 + (i * 20)} {direction} {street}, Chicago, IL 60{610 + (i % 30)}')
    
    # Generate neighborhoods for all ATMs
    neighborhoods = [
        'Gold Coast',
        'Lakeview',
        'The Loop',
        'Lakeview',
        'River North',
        'Wicker Park',
        'River North',
        'Gold Coast',
        # Neighborhoods for new ATMs
        'Lincoln Park',
        'Lincoln Park',
        'Lincoln Park',
        'Logan Square',
        'Logan Square',
        'Logan Square',
        'West Loop',
        'West Loop',
        'West Loop',
        'South Loop',
        'South Loop',
        'South Loop',
        'Uptown',
        'Uptown',
        'Uptown',
    ]
    
    # Add neighborhoods for ATMs 1-85
    chicago_neighborhoods = ['The Loop', 'River North', 'Lincoln Park', 'Wicker Park', 'Logan Square', 
                             'West Loop', 'South Loop', 'Gold Coast', 'Lakeview', 'Uptown']
    
    for i in range(1, 86):
        neighborhoods.append(chicago_neighborhoods[i % len(chicago_neighborhoods)])
    
    # Generate ratings for all ATMs
    ratings = [4.9, 4.8, 4.8, 4.7, 4.5, 4.6, 4.6, 4.7, 
               # Ratings for new ATMs
               4.7, 4.8, 4.6, 
               4.5, 4.6, 4.8,
               4.7, 4.5, 4.9,
               4.6, 4.7, 4.5,
               4.8, 4.6, 4.7]
    
    # Add ratings for ATMs 1-85
    for i in range(1, 86):
        ratings.append(4.5 + ((i % 5) * 0.1))
    
    # Generate review counts for all ATMs
    review_counts = [234, 178, 156, 145, 123, 92, 89, 112, 
                     # Review counts for new ATMs
                     98, 124, 87,
                     76, 82, 115,
                     103, 78, 145,
                     84, 96, 73,
                     109, 87, 95]
    
    # Add review counts for ATMs 1-85
    for i in range(1, 86):
        review_counts.append(75 + (i * 2))
    
    # Generate coordinates for all ATMs
    latitudes = [
        41.931795230015254,
        41.871283632263115,
        41.87480110557803,
        41.868968741038415,
        41.886337664647264,
        41.87683959370173,
        41.839229282381766,
        41.89095690763262,
        # Latitude for new ATMs
        41.927568,
        41.923456,
        41.921789,
        41.930682,
        41.927589,
        41.929045,
        41.884654,
        41.886123,
        41.883897,
        41.876543,
        41.867890,
        41.872345,
        41.963421,
        41.965789,
        41.969876,
    ]
    
    longitudes = [
        -87.65328297847259,
        -87.62640913604353,
        -87.63965703058632,
        -87.60250341857376,
        -87.63259462627705,
        -87.60364977915576,
        -87.65688629997392,
        -87.63545435930328,
        # Longitude for new ATMs
        -87.643256,
        -87.649123,
        -87.646789,
        -87.702345,
        -87.708765,
        -87.705432,
        -87.649876,
        -87.645678,
        -87.647890,
        -87.630123,
        -87.634567,
        -87.627890,
        -87.657890,
        -87.662345,
        -87.659876,
    ]
    
    # Add coordinates for ATMs 1-85
    for i in range(1, 86):
        latitudes.append(41.85 + ((i % 20) * 0.01))
        longitudes.append(-87.62 - ((i % 15) * 0.01))
    
    # Create the data dictionary
    data = {
        'Title': titles,
        'Address': addresses,
        'Neighborhood': neighborhoods,
        'Rating': ratings,
        'ReviewCount': review_counts,
        'Latitude': latitudes,
        'Longitude': longitudes,
        'Status': ['OPERATIONAL'] * len(titles)
    }
    
    df = pd.DataFrame(data)
    
    # Define cryptocurrency support for ATMs
    crypto_support = {
        'Digital Currency Exchange': ['SHIB', 'XRP', 'DAI', 'ETH', 'BTC'],
        'Bitcoin of America ATM': ['BCH', 'XRP', 'DOGE', 'BTC', 'USDT', 'DAI'],
        'Bitcoin ATM at 7-Eleven': ['LTC', 'DAI', 'USDT', 'BTC'],
        'Bitcoin Depot ATM': ['ETH', 'USDC', 'BTC'],
        'CoinFlip Bitcoin ATM': ['BCH', 'XRP', 'USDT', 'LTC', 'BTC', 'SHIB'],
        'RockItCoin ATM': ['LTC', 'XRP', 'USDT'],
        'Crypto Corner ATM': ['USDC', 'DAI', 'BTC', 'USDT', 'BCH', 'SHIB'],
        'Quick Crypto ATM': ['BTC', 'ETH', 'USDT', 'DOGE'],
        # Cryptocurrencies for Lincoln Park ATMs
        'Coinflip ATM - Lincoln Park': ['BTC', 'ETH', 'DOGE'],
        'Bitcoin Depot - Fullerton Ave': ['BTC', 'ETH', 'XRP', 'LTC', 'USDC'],
        'RockItCoin ATM - DePaul': ['BTC', 'ETH', 'LTC', 'DOGE'],
        # Cryptocurrencies for Logan Square ATMs
        'Coinflip ATM - Milwaukee Ave': ['BTC', 'ETH', 'DOGE'],
        'Cryptobase ATM - Logan Square': ['BTC', 'ETH', 'LTC'],
        'Bitcoin Depot - 24/7 Location': ['BTC', 'ETH', 'XRP', 'LTC', 'USDC'],
        # Cryptocurrencies for West Loop ATMs
        'Bitcoin Depot - West Loop': ['BTC', 'ETH', 'XRP', 'LTC', 'USDC'],
        'Coinhub ATM - Fulton Market': ['BTC', 'ETH', 'LTC'],
        'RockItCoin ATM - West Loop': ['BTC', 'ETH', 'XRP', 'LTC', 'USDC', 'DOGE'],
        # Cryptocurrencies for South Loop ATMs
        'Coinhub ATM - Manhattan Mart': ['BTC', 'ETH', 'LTC'],
        'CoinMe ATM - Roosevelt Rd': ['BTC', 'ETH', 'XRP', 'LTC'],
        'Cryptobase ATM - 24/7 Location': ['BTC', 'ETH', 'XRP', 'LTC', 'USDC', 'DOGE'],
        # Cryptocurrencies for Uptown ATMs
        'RockItCoin ATM - Uptown': ['BTC', 'ETH', 'XRP', 'LTC'],
        'Coinflip ATM - Wilson Ave': ['BTC', 'ETH', 'DOGE'],
        'Bitcoin Depot - 24/7 Location': ['BTC', 'ETH', 'XRP', 'LTC', 'USDC'],
    }
    
    # Add cryptocurrency support for ATMs 1-85
    for title in titles[23:]:  # Start after the original 23 ATMs
        if 'Bitcoin Depot' in title:
            crypto_support[title] = ['BTC'] if int(title[-4:]) % 2 == 0 else ['BTC', 'ETH', 'LTC']
        elif 'Coinflip' in title:
            crypto_support[title] = ['BTC', 'ETH'] if int(title[-4:]) % 2 == 0 else ['BTC', 'ETH', 'DOGE']
        elif 'LibertyX' in title:
            crypto_support[title] = ['BTC'] if int(title[-4:]) % 2 == 0 else ['BTC', 'LTC']
        elif 'CoinSpot' in title:
            crypto_support[title] = ['BTC', 'ETH'] if int(title[-4:]) % 2 == 0 else ['BTC', 'ETH', 'XRP']
        elif 'Kurant' in title:
            crypto_support[title] = ['BTC'] if int(title[-4:]) % 2 == 0 else ['BTC', 'LTC']
    
    cryptos = get_supported_cryptocurrencies()
    df['supported_cryptocurrencies'] = df['Title'].map(lambda x: [
        (code, cryptos[code]) for code in crypto_support.get(x, ['BTC'])
    ])
    
    # Add image IDs and URLs
    df['id'] = df['Title'].apply(get_image_id)
    df['image_url'] = '/static/images/locations/' + df['id'] + '.jpg'
    
    # Add ATM types (one-way/two-way)
    df['type'] = 'Two-way'  # Default value for existing ATMs
    
    # Update ATM types based on ATM number
    for title in titles[23:]:  # Start after the original 23 ATMs
        try:
            atm_num = int(title[-4:])
            if atm_num % 2 == 0:
                df.loc[df['Title'] == title, 'type'] = 'Two-way'
            else:
                df.loc[df['Title'] == title, 'type'] = 'One-way'
        except ValueError:
            pass
    
    # Filter out ATMs with IDs from ATM0001 to ATM0100
    df = df[~df['Title'].str.contains('ATM00[0-9][0-9]')]
    
    # Sort by rating and review count
    df['combined_score'] = df['Rating'] * np.log1p(df['ReviewCount'])
    df = df.sort_values('combined_score', ascending=False)
    
    return df

def create_directory_structure():
    directories = [
        'templates',
        'output',
        'output/atm',
        'output/neighborhood',
        'output/cryptocurrency',
        'static/images/locations',
        'static/images/crypto-icons'
    ]
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

def generate_html_pages(df):
    env = Environment(loader=FileSystemLoader('templates'))
    
    # Generate index page
    template = env.get_template('index.html')
    neighborhoods = get_chicago_neighborhoods()
    
    atms = df.to_dict('records')
    html = template.render(atms=atms, neighborhoods=neighborhoods)
    
    with open('output/index.html', 'w') as f:
        f.write(html)
    
    # Generate neighborhoods page
    template = env.get_template('neighborhoods.html')
    neighborhood_data = []
    for n in neighborhoods:
        n_atms = len([atm for atm in atms if atm['Neighborhood'] == n['name']])
        neighborhood_data.append({
            'id': n['id'],
            'name': n['name'],
            'atm_count': n_atms
        })
    html = template.render(neighborhoods=neighborhood_data)
    with open('output/neighborhoods.html', 'w') as f:
        f.write(html)
    
    # Generate individual neighborhood pages
    template = env.get_template('index.html')  # Reuse index template for neighborhood pages
    for n in neighborhoods:
        # Find ATMs in this neighborhood
        neighborhood_atms = [atm for atm in atms if atm['Neighborhood'] == n['name']]
        
        # Create the page even if there are no ATMs
        html = template.render(atms=neighborhood_atms, neighborhoods=neighborhoods, 
                              title=f"Crypto ATMs in {n['name']}")
        os.makedirs(f'output/neighborhood', exist_ok=True)
        with open(f'output/neighborhood/{n["id"]}.html', 'w') as f:
            f.write(html)
        print(f"Generated neighborhood page: {n['id']}.html")
    
    # Generate cryptocurrencies page
    template = env.get_template('cryptocurrencies.html')
    crypto_data = []
    all_cryptos = get_supported_cryptocurrencies()
    for symbol, info in all_cryptos.items():
        crypto_atms = len([atm for atm in atms if any(c[0] == symbol for c in atm['supported_cryptocurrencies'])])
        crypto_data.append({
            'symbol': symbol,
            'name': info['name'],
            'atm_count': crypto_atms
        })
    html = template.render(cryptocurrencies=crypto_data)
    with open('output/cryptocurrencies.html', 'w') as f:
        f.write(html)
    
    # Generate individual cryptocurrency pages
    template = env.get_template('index.html')  # Reuse index template for crypto pages
    for symbol, info in all_cryptos.items():
        crypto_atms = [atm for atm in atms if any(c[0] == symbol for c in atm['supported_cryptocurrencies'])]
        if crypto_atms:
            html = template.render(atms=crypto_atms, neighborhoods=neighborhoods, 
                                  title=f"{info['name']} ({symbol}) ATMs in Chicago")
            os.makedirs(f'output/cryptocurrency', exist_ok=True)
            with open(f'output/cryptocurrency/{symbol.lower()}.html', 'w') as f:
                f.write(html)
    
    # Generate individual ATM pages
    template = env.get_template('atm.html')
    for i, row in df.iterrows():
        atm_data = row.to_dict()  # Convert Series to dict
        html = template.render(atm=atm_data)
        with open(f'output/atm/{atm_data["id"]}.html', 'w') as f:
            f.write(html)

def main():
    create_directory_structure()
    df = read_excel_data()
    generate_html_pages(df)
    print("Website generated successfully!")

if __name__ == "__main__":
    main() 