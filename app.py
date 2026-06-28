import streamlit as st
import pandas as pd

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="District-wise EV Growth Prediction Dashboard",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    historical_df = pd.read_csv("Data/final_model_dataset.csv")

    forecast_df = pd.read_csv("Data/forecast_results.csv")

    ranking_df = pd.read_csv("Data/district_ranking.csv")

    return historical_df, forecast_df, ranking_df


historical_df, forecast_df, ranking_df = load_data()

# ==========================================================
# DATE CONVERSION
# ==========================================================

if "date" in historical_df.columns:
    historical_df["date"] = pd.to_datetime(historical_df["date"])

if "date" in forecast_df.columns:
    forecast_df["date"] = pd.to_datetime(forecast_df["date"])

# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🚗 EV Dashboard")

st.sidebar.markdown("---")

st.sidebar.header("Navigation")

st.sidebar.info(
"""
Use the pages in the sidebar to explore the dashboard.

📂 Dataset

📈 Historical Analysis

🔮 Forecast

📊 District Comparison

🏆 Top Districts

ℹ️ About Project
"""
)

st.sidebar.markdown("---")

st.sidebar.subheader("Technologies Used")

st.sidebar.write("✔ Python")

st.sidebar.write("✔ TensorFlow (LSTM)")

st.sidebar.write("✔ Streamlit")

st.sidebar.write("✔ Plotly")

st.sidebar.write("✔ Pandas")

st.sidebar.write("✔ Scikit-Learn")

# ==========================================================
# HOME PAGE
# ==========================================================

st.title("🚗 District-wise EV Growth Prediction Dashboard")

st.markdown("---")

st.write("""
Welcome to the **District-wise EV Growth Prediction Dashboard**.

This project predicts future Electric Vehicle (EV) registrations
for each district using a Long Short-Term Memory (LSTM)
Deep Learning model.

Using this dashboard you can:

- Explore historical registrations
- Visualize trends
- Forecast future registrations
- Compare districts
- Identify top-performing districts
- Download forecast results
""")

st.markdown("---")

# ==========================================================
# KPI CARDS
# ==========================================================

districts = historical_df["office_name"].nunique()

historical_records = len(historical_df)

forecast_records = len(forecast_df)

forecast_months = forecast_df["date"].nunique()

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Districts", districts)

with col2:
    st.metric("Historical Records", historical_records)

with col3:
    st.metric("Forecast Records", forecast_records)

with col4:
    st.metric("Forecast Months", forecast_months)

st.markdown("---")

# ==========================================================
# DATASET PREVIEW
# ==========================================================

st.subheader("📂 Dataset Preview")

tab1, tab2 = st.tabs(["Historical Dataset", "Forecast Dataset"])

with tab1:

    st.dataframe(
        historical_df.head(10),
        use_container_width=True
    )

with tab2:

    st.dataframe(
        forecast_df.head(10),
        use_container_width=True
    )

st.markdown("---")

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

st.subheader("📌 Project Objective")

st.write("""
The aim of this project is to forecast district-wise monthly
Electric Vehicle registrations using historical registration data.

The forecasting model has been developed using an
LSTM (Long Short-Term Memory) neural network, which is
well suited for time-series forecasting.

The dashboard helps users to:

- Analyze historical EV registrations
- Forecast future registrations
- Compare districts
- Identify top-performing districts
- Export prediction results
""")

st.markdown("---")

# ==========================================================
# QUICK STATISTICS
# ==========================================================

st.subheader("📊 Dataset Statistics")

left, right = st.columns(2)

with left:

    st.write("### Historical Dataset")

    st.write(f"Rows : {historical_df.shape[0]}")

    st.write(f"Columns : {historical_df.shape[1]}")

    st.write(f"Districts : {districts}")

with right:

    st.write("### Forecast Dataset")

    st.write(f"Rows : {forecast_df.shape[0]}")

    st.write(f"Columns : {forecast_df.shape[1]}")

    st.write(f"Forecast Months : {forecast_months}")

st.markdown("---")

# ==========================================================
# FEATURE LIST
# ==========================================================

st.subheader("📑 Available Features")

st.write(list(historical_df.columns))

st.markdown("---")

# ==========================================================
# FOOTER
# ==========================================================

st.caption(
    "District-wise EV Growth Prediction Dashboard | Developed using Streamlit, TensorFlow, Plotly and Pandas"
)