# Boston House Price Prediction

import streamlit as st
import numpy as np
import pickle
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="Boston House Price Prediction",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load Model
@st.cache_resource
def load_model():
    with open("boston_linear_reg.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()


# Safe Image Loader
def load_image(path):
    try:
        return Image.open(path)
    except:
        return None

# Sidebar
sidebar_img = load_image("boston side bar.jpg")
if sidebar_img:
    st.sidebar.image(sidebar_img, width=300)  

st.sidebar.title("Boston House Features")
st.sidebar.caption("Adjust the inputs to estimate house price")

def get_user_input():
    return {
        "crim": st.sidebar.slider("Crime Rate (%)", 0.0, 100.0, 0.006, 0.001),
        "zn": st.sidebar.slider("Residential Land Zone (%)", 0.0, 100.0, 18.0, 1.0),
        "indus": st.sidebar.slider("Non-Retail Business Area (%)", 0.0, 30.0, 2.31, 0.1),
        "chas": st.sidebar.radio("Bound to Charles River?", options=[0, 1], index=0,
                                 format_func=lambda x: "Yes" if x == 1 else "No"),
        "rm": st.sidebar.slider("Average Number of Rooms", 3, 10, 7, 1),  # integer step
        "age": st.sidebar.slider("Owner-Occupied Units Built Before 1940 (%)", 0, 100, 65, 1),  # integer step
        "ptratio": st.sidebar.slider("Pupil–Teacher Ratio", 10.0, 30.0, 15.3, 0.1),
        "black": st.sidebar.slider("Black Population Index", 0.0, 500.0, 396.9, 0.1),
        "lstat": st.sidebar.slider("Lower Status Population (%)", 0.0, 40.0, 4.98, 0.01),
    }

user_data = get_user_input()


# Main Page Banner
banner_img = load_image("boston top.jpg")
if banner_img:
    st.image(banner_img, width=800)  

st.markdown(
    "<h1 style='text-align: center;'>🏠 Boston House Price Prediction</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Predict median house value based on neighborhood characteristics</p>",
    unsafe_allow_html=True
)

st.divider()

# Prediction Section
st.subheader("📊 Price Prediction")

FEATURE_ORDER = ["crim", "zn", "indus", "chas", "rm", "age", "ptratio", "black", "lstat"]

def prepare_input(data):
    return np.array([[data[feature] for feature in FEATURE_ORDER]])

if st.button("🔮 Predict House Price", use_container_width=True):
    input_array = prepare_input(user_data)
    prediction = model.predict(input_array)[0]

    st.success("Prediction Successful")
    st.metric(label="Estimated House Price", value=f"${prediction:,.2f}")

# Footer
st.caption("Model: Ridge Regression | Dataset: Boston Housing")

#to run the code
#python -m streamlit run house_pred_3.py
