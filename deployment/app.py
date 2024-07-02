import streamlit as st
import PIL.Image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Cấu hình cho app
st.set_page_config(
    page_title="Real Estate Price Forecasting",
    page_icon=PIL.Image.open("./assets/img/icon.png"),
)

df = pd.DataFrame(np.random.randn(10, 2), columns=["x", "y"])
st.text(df)
st.line_chart(df)

st.sidebar.title("Sidebar")
