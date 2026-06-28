import streamlit as st

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="About Project",
    page_icon="ℹ️",
    layout="wide"
)

# ==========================================================
# TITLE
# ==========================================================

st.title("ℹ️ About This Project")

st.markdown("---")

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

st.header("📌 Project Overview")

st.write("""
The **District-wise EV Growth Prediction System** is a machine learning and deep learning
project developed to forecast future monthly Electric Vehicle (EV) registrations for
districts using historical registration data.

The forecasting model uses an **LSTM (Long Short-Term Memory)** neural network,
which is highly effective for time-series forecasting because it can learn long-term
patterns from sequential data.
""")

st.markdown("---")

# ==========================================================
# OBJECTIVES
# ==========================================================

st.header("🎯 Project Objectives")

st.markdown("""
- Forecast future EV registrations for every district.
- Analyze historical EV registration trends.
- Compare EV growth across districts.
- Identify districts with the highest expected EV growth.
- Provide an interactive dashboard for visualization and analysis.
""")

st.markdown("---")

# ==========================================================
# DATASET INFORMATION
# ==========================================================

st.header("📂 Dataset Information")

st.markdown("""
The dataset contains historical monthly EV registration records.

### Features

- Date
- Office Name (District)
- Monthly Registrations
- Year
- Month
- Quarter
- Month Name
- Lag-1
- Lag-2
- Lag-3
- Rolling Mean (3 Months)
- Rolling Standard Deviation
- Growth Rate

These engineered features improve the forecasting capability of the LSTM model.
""")

st.markdown("---")

# ==========================================================
# MODEL INFORMATION
# ==========================================================

st.header("🧠 Deep Learning Model")

st.markdown("""
### Model Used

- Long Short-Term Memory (LSTM)

### Why LSTM?

LSTM networks are designed for sequential and time-series data.
They can learn temporal dependencies and retain information from previous
time steps, making them suitable for forecasting monthly EV registrations.

### Forecast Horizon

- 12 Months Ahead Forecast

### Forecast Method

Recursive Multi-step Forecasting
""")

st.markdown("---")

# ==========================================================
# TECHNOLOGIES
# ==========================================================

st.header("🛠 Technologies Used")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### Programming

- Python

### Libraries

- Pandas
- NumPy
- Scikit-learn
- TensorFlow
- Joblib
""")

with col2:

    st.markdown("""
### Visualization

- Plotly
- Streamlit

### Development

- Google Colab
- VS Code
""")

st.markdown("---")

# ==========================================================
# WORKFLOW
# ==========================================================

st.header("⚙️ Project Workflow")

st.markdown("""
1. Data Collection
2. Data Cleaning
3. Feature Engineering
4. Data Scaling
5. Sequence Generation
6. LSTM Model Training
7. Future Forecasting
8. District Ranking
9. Dashboard Development using Streamlit
""")

st.markdown("---")

# ==========================================================
# DASHBOARD FEATURES
# ==========================================================

st.header("📊 Dashboard Features")

st.markdown("""
✅ Dataset Explorer

✅ Historical Trend Analysis

✅ Future EV Forecast

✅ District Comparison

✅ Top Predicted Districts

✅ Download Forecast Results
""")

st.markdown("---")

# ==========================================================
# FUTURE SCOPE
# ==========================================================

st.header("🚀 Future Scope")

st.markdown("""
- Real-time EV registration updates
- Integration with government databases
- Forecasting for multiple vehicle categories
- Interactive GIS-based district mapping
- Hybrid Deep Learning forecasting models
- Deployment on cloud platforms
""")

st.markdown("---")

# ==========================================================
# DEVELOPER
# ==========================================================

st.header("👩‍💻 Developer")

st.info("""
Project: District-wise EV Growth Prediction System

Developed using:

• Python

• TensorFlow (LSTM)

• Streamlit

• Plotly

• Pandas

• Scikit-learn
""")

st.markdown("---")

st.success("Thank you for exploring the District-wise EV Growth Prediction Dashboard!")