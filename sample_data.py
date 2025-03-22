import pandas as pd
import numpy as np

# Create sample data
data = {
    'title': [
        'Bitcoin ATM at 7-Eleven',
        'Crypto Corner ATM',
        'Digital Currency Exchange',
        'Quick Crypto ATM',
        'CoinFlip Bitcoin ATM',
        'Bitcoin of America ATM',
        'RockItCoin ATM',
        'Bitcoin Depot ATM'
    ],
    'address': [
        '123 State St, Chicago, IL 60601 (The Loop)',
        '456 N Wells St, Chicago, IL 60654 (River North)',
        '789 N Michigan Ave, Chicago, IL 60611 (Gold Coast)',
        '321 W North Ave, Chicago, IL 60610 (Old Town)',
        '654 N Milwaukee Ave, Chicago, IL 60622 (River West)',
        '987 W Belmont Ave, Chicago, IL 60657 (Lakeview)',
        '741 N Western Ave, Chicago, IL 60622 (Ukrainian Village)',
        '852 W Addison St, Chicago, IL 60613 (Lakeview)'
    ],
    'rating': [4.8, 4.6, 4.9, 4.7, 4.5, 4.8, 4.6, 4.7],
    'reviews_count': [156, 89, 234, 67, 123, 178, 92, 145],
    'business_status': ['OPERATIONAL'] * 8
}

# Create DataFrame
df = pd.DataFrame(data)

# Save to Excel
df.to_excel('Outscraper-1-crpto-atm.xlsx', index=False)
print("Sample data file created successfully!") 