import streamlit as st
from data_fetch import fetch_stock_data
from preprocess import preprocess_data
import pandas as pd
import model as train_model



# Streamlit app
st.title("Stock Price Analysis AI")

# User inputs
ticker = st.text_input("Enter Stock Ticker (e.g., AAPL):", value="AAPL")
start_date = st.date_input("Start Date", value=pd.to_datetime("2020-01-01"))
end_date = st.date_input("End Date", value=pd.to_datetime("2023-01-01"))

if st.button("Analyze"):
    # Fetch and preprocess data
    raw_data = fetch_stock_data(ticker, str(start_date), str(end_date))
    processed_data = preprocess_data(raw_data)

    # Display raw and processed data
    st.subheader("Raw Data")
    st.write(raw_data.tail())

    st.subheader("Processed Data")
    st.write(processed_data.tail())

    # Train model and show results
    model, mse = train_model(processed_data)
    st.subheader("Model Performance")
    st.write(f"Mean Squared Error: {mse}")
    
