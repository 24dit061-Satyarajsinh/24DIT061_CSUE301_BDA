import yfinance as yf
import pandas as pd
import os

folder = r"C:\SEM5\BDA\Prac8"

stocks = {
    "RELIANCE.NS": "RELIANCE",
    "TCS.NS": "TCS",
    "INFY.NS": "INFY",
    "HDFCBANK.NS": "HDFCBANK"
}

frames = []

for ticker, symbol in stocks.items():

    print("Downloading:", symbol)

    data = yf.download(
        ticker,
        period="1y",
        interval="1d",
        auto_adjust=False,
        progress=False
    )

    data = data.reset_index()

    # Handle MultiIndex columns
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    data = data[["Date", "Close"]].copy()

    data["Stock"] = symbol

    data.rename(columns={"Close": "Price"}, inplace=True)

    frames.append(data[["Date", "Stock", "Price"]])

# Combine all stocks
combined = pd.concat(frames, ignore_index=True)

# Remove missing values
combined.dropna(inplace=True)

# Save CSV
output_file = os.path.join(folder, "stock_data.csv")

combined.to_csv(output_file, index=False)

print("\nStock data downloaded successfully!")
print("File:", output_file)
print("Total records:", len(combined))
print("\nFirst 10 records:")
print(combined.head(10))