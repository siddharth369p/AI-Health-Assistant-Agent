#to create virtual environment first =python -m venv env
# and then activate it through = .\env\Scripts\activate

import streamlit as st 
import os 

st.set_page_config(page_title="Health Assistant",
              page_icon="🤸",
              layout="wide")
st.title("AI Health Assistant 🤸")
st.header("Health Information")