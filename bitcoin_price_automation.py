# Bitcoin Price Automation - Automated Reporting
# This code retrieves the current Bitcoin price via CoinGecko API, logs it to a CSV, calculates statistics, and generates visualizations.

import pandas as pd
import requests
import datetime
import os
import logging
import matplotlib.pyplot as plt
from scipy.stats import skew, kurtosis
import plotly.express as px

# Configure logging for debugging
# Replace 'C:\\Users\\YourUsername\\YourDirectory' with the actual path on your system (e.g., 'C:\\Users\\YourName\\Documents\\Projects')
logging.basicConfig(filename='C:\\Users\\YourUsername\\YourDirectory\\bitcoin_price_log.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

# Function to get the current Bitcoin price via CoinGecko API
def get_bitcoin_price():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    try:
        response = requests.get(url, timeout=10)  # Add 10-second timeout to prevent hangs
        response.raise_for_status()  # Check for HTTP request errors
        data = response.json()
        price = data['bitcoin']['usd']
        logging.info(f"Bitcoin price obtained: ${price:.2f}")
        return price
    except requests.RequestException as e:
        logging.error(f"Error accessing API: {e}")
        return None

# Function to log the price, calculate statistics, and generate visualizations
def update_bitcoin_prices():
    current_time = datetime.datetime.now()
    price = get_bitcoin_price()
    if price is None:
        logging.error("Failed to obtain price, record not created.")
        return

    # Replace 'C:\\Users\\YourUsername\\YourDirectory' with the actual path on your system (e.g., 'C:\\Users\\YourName\\Documents\\Projects')
    csv_path = 'C:\\Users\\YourUsername\\YourDirectory\\bitcoin_prices.csv'

    # Create or update a DataFrame with the data
    if os.path.exists(csv_path):
        df = pd.read_csv(csv_path)
        df['DateTime'] = pd.to_datetime(df['DateTime'])  # Ensure DateTime is datetime
    else:
        df = pd.DataFrame(columns=['DateTime', 'BTC_Price_USD'])

    # Add the new entry
    new_entry = pd.DataFrame({'DateTime': [current_time], 'BTC_Price_USD': [price]})
    df = pd.concat([df, new_entry], ignore_index=True)
    df.to_csv(csv_path, index=False)  # Use absolute path to save

    # Calculate descriptive statistics
    if len(df) > 1:  # Only calculate statistics if there are more than one record
        mean_price = df['BTC_Price_USD'].mean()
        median_price = df['BTC_Price_USD'].median()
        std_dev_price = df['BTC_Price_USD'].std()
        skewness_price = skew(df['BTC_Price_USD'])
        kurtosis_price = kurtosis(df['BTC_Price_USD'])

        # Replace 'C:\\Users\\YourUsername\\YourDirectory' with the actual path on your system (e.g., 'C:\\Users\\YourName\\Documents\\Projects')
        stats_df = pd.DataFrame({
            'Statistic': ['Mean', 'Median', 'Standard Deviation', 'Skewness', 'Kurtosis'],
            'Value': [f"${mean_price:.2f}", f"${median_price:.2f}", f"${std_dev_price:.2f}", f"{skewness_price:.2f}", f"{kurtosis_price:.2f}"]
        })
        stats_df.to_csv('C:\\Users\\YourUsername\\YourDirectory\\bitcoin_price_stats.csv', index=False)

        # Replace 'C:\\Users\\YourUsername\\YourDirectory' with the actual path on your system (e.g., 'C:\\Users\\YourName\\Documents\\Projects')
        # Generate line chart with Matplotlib (save as PNG)
        plt.figure(figsize=(12, 6))
        plt.plot(df['DateTime'], df['BTC_Price_USD'], marker='o', linestyle='-', color='blue')
        plt.title("Bitcoin Price Over Time")
        plt.xlabel("Date and Time")
        plt.ylabel("Price (USD)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.savefig('C:\\Users\\YourUsername\\YourDirectory\\bitcoin_price_chart.png')
        plt.close()

        # Replace 'C:\\Users\\YourUsername\\YourDirectory' with the actual path on your system (e.g., 'C:\\Users\\YourName\\Documents\\Projects')
        # Generate interactive chart with Plotly (save as HTML)
        fig = px.line(df, x='DateTime', y='BTC_Price_USD', title='Bitcoin Price Over Time (Interactive)')
        fig.write_html('C:\\Users\\YourUsername\\YourDirectory\\bitcoin_price_chart.html')

    # Display the most recent record (optional, for testing)
    print(f"Recorded at {current_time}: Bitcoin Price = ${price:.2f}")
    logging.info(f"Recorded at {current_time}: Bitcoin Price = ${price:.2f}")
    print("Current price table (last row):")
    print(df.tail(1))

# Execute the function (for manual testing; will be automated later)
if __name__ == "__main__":
    update_bitcoin_prices()
