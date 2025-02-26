# Bitcoin Price Automation

## Overview
This project automates the tracking of Bitcoin prices using the CoinGecko API, logging data to a CSV file, calculating descriptive statistics, and generating visualizations (PNG and HTML). It is designed to run periodically on Windows using Task Scheduler, providing continuous updates without manual intervention.

## Features
- Retrieves real-time Bitcoin prices in USD via the CoinGecko API.
- Logs prices with timestamps to `bitcoin_prices.csv`.
- Calculates descriptive statistics (mean, median, standard deviation, skewness, kurtosis) and saves them to `bitcoin_price_stats.csv`.
- Generates a static line chart (PNG) and an interactive line chart (HTML) to visualize price trends over time.
- Automates execution with Windows Task Scheduler for daily or hourly updates.

## Data
The project records Bitcoin prices over time, stored in:
- `bitcoin_prices.csv`: Contains columns `DateTime` (timestamp) and `BTC_Price_USD` (price in USD).
- `bitcoin_price_stats.csv`: Contains descriptive statistics of the recorded prices.

## Requirements
- Python 3.x
- Libraries: `pandas`, `requests`, `datetime`, `os`, `logging`, `matplotlib`, `plotly`, `scipy`
  - Install with: `pip install pandas requests matplotlib plotly scipy`

## How to Run
1. Clone this repository to your local machine.
2. Ensure Python 3.x is installed and the required libraries are installed.
3. Update the file paths in `bitcoin_price_automation.py` to match your system. Replace `C:\\Users\\YourUsername\\YourDirectory` with your actual directory path (e.g., `C:\\Users\\YourName\\Documents\\Projects`).
4. Save the script as `bitcoin_price_automation.py` in the specified directory.
5. Configure Windows Task Scheduler to run the script:
   - Open Task Scheduler (press `Win + S`, type "Task Scheduler", and open).
   - Create or update a task named "Bitcoin Price Automation":
     - **General**: Name "Bitcoin Price Automation", check "Run whether user is logged on or not" and optionally "Run with highest privileges".
     - **Triggers**: Set to "Daily" at "8:00 AM" (or "Repeat task every 1 hour for 24 hours" for hourly updates).
     - **Actions**: 
       - Program/Script: `C:\Python39\python.exe` (or your Python path, found with `where python` in Command Prompt).
       - Add arguments: `C:\Users\YourUsername\YourDirectory\bitcoin_price_automation.py` (replace `C:\Users\YourUsername\YourDirectory` with your actual path).
       - Start in: `C:\Users\YourUsername\YourDirectory` (replace with your actual path).
     - **Settings**: Check "Allow task to be run on demand", "Run task as soon as possible after a scheduled start is missed", and "Restart if the task fails" (3 attempts, 1 minute interval).
   - Save the task and test manually by clicking "Run" in Task Scheduler.
6. Verify that `bitcoin_prices.csv`, `bitcoin_price_stats.csv`, `bitcoin_price_chart.png`, `bitcoin_price_chart.html`, and `bitcoin_price_log.txt` are generated in your specified directory.

## Visualizations
- **Static Line Chart (`bitcoin_price_chart.png`)**: A Matplotlib line chart showing Bitcoin prices over time, with date/time on the X-axis and price in USD on the Y-axis.
- **Interactive Line Chart (`bitcoin_price_chart.html`)**: A Plotly line chart for interactive exploration, saved as an HTML file.

## Descriptive Statistics
The script calculates:
- **Mean**: Average Bitcoin price (e.g., $50,000.50).
- **Median**: Median price, less affected by outliers.
- **Standard Deviation**: Measures price variability (e.g., $2,000.00).
- **Skewness**: Indicates if the price distribution is skewed (positive or negative tail).
- **Kurtosis**: Measures the "tailedness" of the price distribution, indicating outliers.

## Observations and Analyses
- The `bitcoin_prices.csv` records show Bitcoin price fluctuations over time, typically ranging around $50,000 USD as of March 2025 (subject to real-time changes).
- Periods with prices significantly above/below the mean can be identified using the calculated statistics, such as peaks or dips in volatile markets.
- The price distribution may appear positively skewed if there are rare high prices, inferred from skewness values in `bitcoin_price_stats.csv`.

## License
This code is protected by copyright and is not licensed for use, modification, or distribution without explicit permission from the author. All rights reserved. Please contact renatofraga.rr@gmail.com for inquiries.
