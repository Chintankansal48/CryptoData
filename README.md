# Crypto Data Fetcher

This Python script fetches live cryptocurrency data for the top 50 cryptocurrencies using the **CoinGecko API**, analyzes it, and updates an **Excel sheet** every 5 minutes.

## 🚀 Features
- Fetches **live cryptocurrency data** including:
  - Cryptocurrency Name
  - Symbol
  - Current Price (USD)
  - Market Capitalization
  - 24-hour Trading Volume
  - Price Change (24-hour, percentage)
- Identifies the **top 5 cryptocurrencies** by market cap.
- Calculates the **average price** of the top 50 cryptocurrencies.
- Finds the **highest & lowest 24-hour price changes**.
- Updates an **Excel sheet every 5 minutes** automatically.

---

## 🛠 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Chintankansal48/CryptoData.git
   cd CryptoData
Install dependencies:
pip install requests pandas openpyxl schedule
Run the script:
python crypto_data.py

📊 Data Analysis
The script performs the following analysis:

Top 5 Cryptocurrencies by market cap.
Average price of the top 50 cryptocurrencies.
Highest and lowest 24-hour price change percentages.
The output is saved in an Excel file (crypto_data.xlsx) with multiple sheets:

Top 50 Cryptos
Top 5 Cryptos
Average Price
Highest Change
Lowest Change
⚡ Usage
The script will automatically update the Excel file every 5 minutes.
If you want to stop the script, press Ctrl + C.
📌 Requirements
Python 3.x
Pandas
Requests
OpenPyXL
Schedule
👤 Author
Chintankansal48