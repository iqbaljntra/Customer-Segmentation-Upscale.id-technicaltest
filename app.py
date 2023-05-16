import streamlit as st
import joblib
import pandas as pd

# Load the saved pipeline object
all_process = joblib.load("all_process.joblib")

Gender = st.radio(('Male','Female'))
Profession = st.radio(('Healthcare', 'Engineer', 'Lawyer', 'Entertainment', 'Artist',
       'Executive', 'Doctor', 'Homemaker', 'Marketing'))
Age = st.slider('Points In Wallet',0, 99)
Annual Income ($) = st.slider()