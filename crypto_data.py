import requests
import pandas as pd
import time
import schedule

API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 50,
    "page": 1,
    "sparkline": False
}

EXCEL_FILE = "crypto_data.xlsx"

def fetch_crypto_data():
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return []

def process_data(data):
    if not data:
        return None, None, None, None, None

    df = pd.DataFrame(data)[["name", "symbol", "current_price", "market_cap",
                             "total_volume", "price_change_percentage_24h"]]

    top_5 = df.nlargest(5, "market_cap")
    avg_price = df["current_price"].mean()
    highest_change = df.nlargest(1, "price_change_percentage_24h")
    lowest_change = df.nsmallest(1, "price_change_percentage_24h")

    return df, top_5, avg_price, highest_change, lowest_change

def update_excel():
    data = fetch_crypto_data()
    if not data:
        print("No data fetched. Skipping update.")
        return

    df, top_5, avg_price, highest_change, lowest_change = process_data(data)

    with pd.ExcelWriter(EXCEL_FILE, engine="openpyxl", mode="w") as writer:
        df.to_excel(writer, sheet_name="Top 50", index=False)
        top_5.to_excel(writer, sheet_name="Top 5", index=False)
        pd.DataFrame({"Average Price": [avg_price]}).to_excel(writer, sheet_name="Average Price", index=False)
        highest_change.to_excel(writer, sheet_name="Highest Change", index=False)
        lowest_change.to_excel(writer, sheet_name="Lowest Change", index=False)

    print("Excel file updated successfully!")

update_excel()

schedule.every(5).minutes.do(update_excel)

print("Updating Excel every 5 minutes... Press Ctrl+C to stop.")
while True:
    schedule.run_pending()
    time.sleep(1)
