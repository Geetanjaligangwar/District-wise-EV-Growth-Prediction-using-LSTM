# District-wise EV Registration Forecasting and Analytics Dashboard using LSTM

## Problem Statement
Develop an Artificial Intelligence-based forecasting system to predict future monthly Electric Vehicle (EV) registrations across districts using historical registration data. The objective is to assist policymakers and stakeholders in understanding future EV adoption trends through accurate forecasting and interactive visualizations.

## Methodology
- Collected and preprocessed district-wise monthly EV registration data.
- Performed feature engineering by creating lag features, rolling statistics, and growth rate to capture temporal patterns.
- Applied Min-Max Scaling and generated sequential data for time-series forecasting.
- Trained a Long Short-Term Memory (LSTM) deep learning model to learn historical registration trends.
- Performed recursive multi-step forecasting to predict EV registrations for the next 12 months for every district.
- Developed an interactive Streamlit dashboard for visualization, district comparison, forecasting, and district ranking.

## Deliverables
- Developed an end-to-end Deep Learning-based EV registration forecasting system.
- Forecasted district-wise EV registrations for the next 12 months using an LSTM model.
- Generated district rankings based on predicted EV registrations.
- Built a multi-page interactive Streamlit dashboard featuring:
  - Historical EV Registration Analysis
  - Future EV Registration Forecast
  - District-wise Comparison
  - Top Predicted Districts
  - Downloadable Forecast Results
- Integrated data preprocessing, deep learning forecasting, and interactive visualization into a deployable web application.

## Technologies Used
- Python
- TensorFlow (LSTM)
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Streamlit

