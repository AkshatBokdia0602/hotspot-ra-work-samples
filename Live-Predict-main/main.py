import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
import plotly.express as px

def sidebar():
    with st.sidebar:
        st.subheader("About")
        st.markdown("""Welcome to LivePredict 📈, your go-to platform for real-time stock predictions! Select your
        favorite stocks and get instant forecasts with continuously updated AI models. Perfect for all investors,
        stay ahead of market trends and make informed decisions with LivePredict 📈!""")
        st.write("")
        st.write("")

        st.markdown("<h1 style='font-style: italic; color: #A9A9A9;'>Settings</h1>", unsafe_allow_html = True)
        st.write("")
        selected_stock = st.radio(
        "Pick a Stock",
        ["ADANIENT.NS", "HDFCBANK.NS", "RELIANCE.NS", "SBIN.NS", "TCS.NS"],
        captions = ["Adani Enterprises Limited", "HDFC Bank Limited", "Reliance Industries Limited",
                    "State Bank of India", "Tata Consultancy Services Limited"], index = None)

        return selected_stock


def main():
    st.set_page_config(page_title = "LivePredict・Streamlit", page_icon = "📈")
    stock = sidebar()
    st.markdown("<h1 style='margin-bottom:-3%;'> <span style='color:#0000FF;'>Live</span><span style='color:#FF0000;'> Predict</span></h1>", unsafe_allow_html=True)
    st.markdown("<p style = 'padding-bottom: 2%'>📈 Real-Time Stock Forecasting at Your Fingertips</p>", unsafe_allow_html = True)

    if stock == "ADANIENT.NS":
        regressor = tf.keras.models.load_model('AdaniENT_model.h5')
    elif stock == "HDFCBANK.NS":
        regressor = tf.keras.models.load_model('HDFC_model.h5')
    elif stock == "RELIANCE.NS":
        regressor = tf.keras.models.load_model('Reliance_model.h5')
    elif stock == "SBIN.NS":
        regressor = tf.keras.models.load_model('SBI_model.h5')
    elif stock == "TCS.NS":
        regressor = tf.keras.models.load_model('TCS_model.h5')

    if stock is not None:
        with st.spinner("Generating Content... This may take a while ⏳"):
            ticker = yf.Ticker(stock)
            dataset = ticker.history(period = "max").iloc[:, 0:1].values

            sc = MinMaxScaler(feature_range = (0, 1))
            dataset_scaled = sc.fit_transform(dataset[:len(dataset) - 60])

            inputs = dataset[len(dataset) - 60:]
            inputs = sc.transform(inputs)
            preds = []

            for i in range(60, 90):
                X_test = []
                X_test.append(inputs[i - 60 : i, 0])
                X_test = np.array(X_test)
                X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))

                predicted_stock_price_scaled = regressor.predict(X_test)
                predicted_stock_price = sc.inverse_transform(predicted_stock_price_scaled)[0][0]
                preds.append(predicted_stock_price)

                inputs = np.concatenate((inputs, predicted_stock_price_scaled), axis = 0)

            line = pd.DataFrame(np.concatenate((dataset[len(dataset) - 60:],
                                                np.expand_dims(np.array(preds), axis = 1)), axis = 0), columns = ["Value"])

            sep = []
            for i in range(len(line)):
                if i < 60:
                    sep.append("Current")
                else:
                    sep.append("Forecasted")
            line['Trend'] = sep

            fig = px.line(line, x = line.index, y = 'Value', color = 'Trend', markers = True,
                        title = f"{stock} Stock Price Prediction")
            fig.update_layout(xaxis_title = "Time Period", yaxis_title = "Open Value (Rs.)")
            st.plotly_chart(fig, use_container_width = True, theme = None)

            image = fig.to_image(format = 'png')
            st.download_button(label = 'Download', data = image, file_name = "image.png")

if __name__ == "__main__":
    main()