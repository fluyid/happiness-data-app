import streamlit as st
import plotly.express as px

st.title("In Search for Happiness")

options = ("GDP", "Happiness", "Generosity")
x_axis = st.selectbox("Select the data for the X-axis", options=options)
y_axis = st.selectbox("Select the data for the Y-axis", options=options)

st.subheader(f"{x_axis} and {y_axis}")