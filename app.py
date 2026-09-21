#to create virtual environment first =python -m venv env
# and then activate it through = .\env\Scripts\activate

import streamlit as st 
import os 
from diet import bmi_calculator,bmr_calculator,tdee_calculator,calorie_target

st.set_page_config(page_title="Health Assistant",
              page_icon="🤸",
              layout="wide")
st.title("AI Health Assistant 🤸")
st.write("Personal Health and Diet Recommendation Agent")
st.header("Health Information🤏🏼")

#create a sidebar
#--------------------------------controrls---------------------------#
st.sidebar.header("💁🏼‍♂️Your Information ")
gender=st.sidebar.selectbox("Gender",["Male","Female"])
age=st.sidebar.number_input("Age",1,100)
weight =st.sidebar.number_input("weight(kg)",1,120)
height=st.sidebar.number_input("height(cm)",100,200)

activity = st.sidebar.selectbox(
    "Activity",
    [
        "Sedentary",
        "Lightly_Active",
        "Moderately_Active",
        "Very_Active",
        "Extra_Active"
    ]
)
aim=st.sidebar.selectbox("Aim",["Weight maintain","Weight loss","Weight gain"])
#------------------------------------------------------------------------------#
#calculations
bmi=bmi_calculator(weight,height)
bmr=bmr_calculator(gender,age,weight,height)
tdee=tdee_calculator(bmr,activity)
calories=calorie_target(tdee,aim)

#--------------------
col1,col2,col3,col4=st.columns(4)
col1.metric("BMI",bmi)
col2=col2.metric("BMR",f"{bmr}kcal🔥")
col3=col3.metric("TDEE",f"{tdee}kcal🔥")
col4=col4.metric("Calorie Target",f"{calories}kcal🔥")








