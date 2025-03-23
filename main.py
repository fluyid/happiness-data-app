import streamlit as st
import plotly.express as px
import pandas as pd

st.title("In Search for Happiness")

options = ("GDP", "Happiness", "Generosity")
x_axis = st.selectbox("Select the data for the X-axis", options=options)
y_axis = st.selectbox("Select the data for the Y-axis", options=options)

st.subheader(f"{x_axis} and {y_axis}")

happiness_score_df = pd.read_csv("happy.csv")

x_value = happiness_score_df[f"{x_axis.lower()}"]
y_value = happiness_score_df[f"{y_axis.lower()}"]

labels = {
    "x": x_axis,
    "y": y_axis
}

figure = px.scatter(x=x_value, y=y_value, labels=labels)
st.plotly_chart(figure)