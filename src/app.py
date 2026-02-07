import streamlit as st
from main import run_pipeline

st.title("Expense Analyzer")

data = run_pipeline()

# ---- Monthly Trend ----
st.subheader("Monthly Spending Trend")

monthly = data["monthly"]

monthly_plot = monthly.sort_index().copy()
st.line_chart(monthly_plot)

# ---- Forecast Predict ----
st.subheader("Forecast")
st.metric("Next Month Prediction", f"${data['forecast']:.2f}")