# -*- coding: utf-8 -*-
"""failure_deployment.ipynb"""

#import libraries
import numpy as np
import joblib
import streamlit as st

# Load model
model = joblib.load('failure_prediction.pkl')

st.set_page_config(page_title='Failure Prediction', layout="centered")
st.title("Failure Classification App")
st.write("Predict whether the system is **operating** or **failing** under certain conditions")

# Inputs (value=None removed)
footfall = st.number_input("Value of footfall", value=0.0)
tempMode = st.number_input("Value of tempMode", value=0.0)
AQ = st.number_input("Value of AQ", value=0.0)
USS = st.number_input("Value of USS", value=0.0)
CS = st.number_input("Value of CS", value=0.0)
VOC = st.number_input("Value of VOC", value=0.0)
RP = st.number_input("Value of RP", value=0.0)
IP = st.number_input("Value of IP", value=0.0)
Temperature = st.number_input("Value of Temperature", value=0.0)

if st.button("Predict"):
    input_data = np.array([[
        footfall,
        tempMode,
        AQ,
        USS,
        CS,
        VOC,
        RP,
        IP,
        Temperature
    ]])

    prediction = model.predict(input_data)[0]

    if prediction == 0:
        st.error("**Failing**")
    else:
        st.success("**Working**")
