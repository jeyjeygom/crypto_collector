import requests
import pandas as pd

# Function to get cryptocurrency data
def get_crypto_data(pages):
    coins = []
    for page in range(1, pages+1):
        url = "https://api.coingecko.com/api/v3/coins/markets"
        params = {
            "vs_currency": "usd",  # Currency to get data in
            "order": "market_cap_desc",  # Order by market cap descending
            "per_page": 150,  # Get 150 coins per page
            "page": page,  # Page number
            "sparkline": False  # Exclude sparkline data
        }
        response = requests.get(url, params=params)  # Make the API request
        data = response.json()  # Parse the JSON response
        for coin in data:
            coins.append({
                "ID": coin["id"],
                "Name": coin["name"],
                "Symbol": coin["symbol"],
                "Current Price": coin["current_price"],
                "Market Cap": coin["market_cap"],
                "Total Volume": coin["total_volume"],
                "High 24h": coin["high_24h"],
                "Low 24h": coin["low_24h"],
                "Price Change 24h": coin["price_change_24h"],
                "Price Change Percentage 24h": coin["price_change_percentage_24h"],
            })
    return coins

# Get data for the top 300 cryptocurrencies
coins = get_crypto_data(pages=2)

# Create a Pandas DataFrame with the cryptocurrency data
df = pd.DataFrame(coins)

# Save the data to an Excel file
file_path = "cryptocurrencies.xlsx"
df.to_excel(file_path, index=False)

print(f"Data saved to {file_path}")
