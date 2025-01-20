def preprocess_data(data):
    data['Date'] = data.index
    data['SMA_50'] = data['Close'].rolling(window=50).mean()  # 50-day Simple Moving Average
    data['SMA_200'] = data['Close'].rolling(window=200).mean()  # 200-day Simple Moving Average
    data.dropna(inplace=True)
    return data

if __name__ == "__main__":
    from data_fetch import fetch_stock_data

    ticker = "AAPL"
    start_date = "2020-01-01"
    end_date = "2023-01-01"
    raw_data = fetch_stock_data(ticker, start_date, end_date)
    processed_data = preprocess_data(raw_data)
    print(processed_data.head())
