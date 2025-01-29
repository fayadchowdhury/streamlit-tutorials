import streamlit as st
import numpy as np
import pandas as pd

# st.set_page_config(page_title="Page 1", page_icon=":material/phone:")
st.title("Dashboard")

stock_names = ["ABC", "DEF", "GHI", "JKL"]
data = pd.DataFrame(
    {
        "Stock Names": stock_names,
        "Prices": np.random.randint(low=0, high=20, size=len(stock_names))
    }
)

st.header("Line chart for stock prices")
st.bar_chart(data, x="Stock Names", y="Prices")