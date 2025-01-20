import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd

# Streamlit app configuration
st.set_page_config(page_title="Stock Price Analysis", layout="wide")

# Title of the app
st.title("📈 Real-Time Stock Price Analysis")

# Input for stock ticker symbol
ticker = st.text_input("Enter Stock Ticker Symbol (e.g., AAPL, TSLA, MSFT):", "AAPL")

# Date range selection
st.sidebar.header("Select Date Range")
start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2020-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("today"))

# Fetch stock data function
@st.cache_data
def fetch_stock_data(ticker, start_date, end_date):
    try:
        stock_data = yf.download(ticker, start=start_date, end=end_date)
        return stock_data
    except Exception as e:
        st.error(f"Error fetching data: {e}")
        return None

# Display stock data and charts
if st.button("Analyze Stock"):
    with st.spinner("Fetching data..."):
        data = fetch_stock_data(ticker, start_date, end_date)
        if data is not None and not data.empty:
            st.success("Data fetched successfully!")
            
            # Display raw data
            st.subheader(f"Raw Data for {ticker}")
            st.dataframe(data.tail(10))

            # Plot stock data
            st.subheader(f"Price Trends for {ticker}")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(data['Close'], label='Closing Price', color='blue')
            ax.set_title(f"{ticker} Closing Price Over Time")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price (USD)")
            ax.legend()
            st.pyplot(fig)

            # Moving averages
            st.subheader(f"Moving Averages for {ticker}")
            data['SMA_50'] = data['Close'].rolling(window=50).mean()
            data['SMA_200'] = data['Close'].rolling(window=200).mean()
            fig2, ax2 = plt.subplots(figsize=(10, 5))
            ax2.plot(data['Close'], label='Closing Price', color='blue')
            ax2.plot(data['SMA_50'], label='50-Day SMA', color='green')
            ax2.plot(data['SMA_200'], label='200-Day SMA', color='red')
            ax2.set_title(f"{ticker} Moving Averages")
            ax2.set_xlabel("Date")
            ax2.set_ylabel("Price (USD)")
            ax2.legend()
            st.pyplot(fig2)
        else:
            st.warning("No data found for the given ticker or date range. Please try again.")

# Footer
st.sidebar.write("Powered by Streamlit & Yahoo Finance")
