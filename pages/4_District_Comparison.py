import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="District Comparison",
    page_icon="📊",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    historical = pd.read_csv("Data/final_model_dataset.csv")
    forecast = pd.read_csv("Data/forecast_results.csv")

    historical["date"] = pd.to_datetime(historical["date"])
    forecast["date"] = pd.to_datetime(forecast["date"])

    return historical, forecast

historical_df, forecast_df = load_data()

# ==========================================================
# TITLE
# ==========================================================

st.title("📊 District Comparison")

districts = sorted(historical_df["office_name"].unique())

col1, col2 = st.columns(2)

with col1:
    district1 = st.selectbox("Select District 1", districts)

with col2:
    district2 = st.selectbox("Select District 2", districts, index=1)

hist1 = historical_df[historical_df["office_name"] == district1]
hist2 = historical_df[historical_df["office_name"] == district2]

future1 = forecast_df[forecast_df["office_name"] == district1]
future2 = forecast_df[forecast_df["office_name"] == district2]

# ==========================================================
# HISTORICAL COMPARISON
# ==========================================================

st.subheader("Historical Comparison")

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=hist1["date"],
    y=hist1["monthly_registrations"],
    mode="lines",
    name=district1
))

fig.add_trace(go.Scatter(
    x=hist2["date"],
    y=hist2["monthly_registrations"],
    mode="lines",
    name=district2
))

fig.update_layout(
    title="Historical EV Registrations",
    xaxis_title="Date",
    yaxis_title="Registrations"
)

st.plotly_chart(fig, use_container_width=True)

# ==========================================================
# FORECAST COMPARISON
# ==========================================================

st.subheader("Forecast Comparison")

fig2 = go.Figure()

fig2.add_trace(go.Scatter(
    x=future1["date"],
    y=future1["monthly_registrations"],
    mode="lines+markers",
    name=district1
))

fig2.add_trace(go.Scatter(
    x=future2["date"],
    y=future2["monthly_registrations"],
    mode="lines+markers",
    name=district2
))

fig2.update_layout(
    title="Forecast Comparison",
    xaxis_title="Date",
    yaxis_title="Predicted Registrations"
)

st.plotly_chart(fig2, use_container_width=True)

# ==========================================================
# SUMMARY TABLE
# ==========================================================

summary = pd.DataFrame({
    "District": [district1, district2],
    "Historical Total": [
        hist1["monthly_registrations"].sum(),
        hist2["monthly_registrations"].sum()
    ],
    "Forecast Total": [
        future1["monthly_registrations"].sum(),
        future2["monthly_registrations"].sum()
    ]
})

st.subheader("Comparison Summary")

st.dataframe(summary, use_container_width=True)