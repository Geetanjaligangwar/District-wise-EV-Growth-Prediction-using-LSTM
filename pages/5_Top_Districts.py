import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Top Districts",
    page_icon="🏆",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    return pd.read_csv("Data/district_ranking.csv")

ranking_df = load_data()

# ==========================================================
# SORT DATA
# ==========================================================

ranking_df = ranking_df.sort_values(
    by="Forecasted EV Registrations",
    ascending=False
).reset_index(drop=True)

ranking_df.index = ranking_df.index + 1

# ==========================================================
# TITLE
# ==========================================================

st.title("🏆 Top Predicted EV Districts")

st.markdown(
"""
Ranking of districts based on the **total forecasted EV registrations**
predicted by the LSTM model.
"""
)

st.divider()

# ==========================================================
# KPI CARDS
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Total Districts",
        len(ranking_df)
    )

with col2:
    st.metric(
        "Top District",
        ranking_df.iloc[0]["District"]
    )

with col3:
    st.metric(
        "Highest Prediction",
        int(ranking_df.iloc[0]["Forecasted EV Registrations"])
    )

st.divider()

# ==========================================================
# TOP 10 CHART
# ==========================================================

st.subheader("Top 10 Districts")

top10 = ranking_df.head(10)

fig = px.bar(
    top10,
    x="District",
    y="Forecasted EV Registrations",
    color="Forecasted EV Registrations",
    text="Forecasted EV Registrations",
    title="Top 10 Forecasted Districts"
)

fig.update_traces(textposition="outside")

fig.update_layout(
    xaxis_title="District",
    yaxis_title="Forecasted EV Registrations"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# COMPLETE TABLE
# ==========================================================

st.subheader("Complete District Ranking")

display_df = ranking_df.copy()

display_df.insert(
    0,
    "Rank",
    range(1, len(display_df)+1)
)

st.dataframe(
    display_df,
    use_container_width=True,
    height=600
)

st.divider()

# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

csv = display_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Ranking",
    csv,
    file_name="district_ranking.csv",
    mime="text/csv"
)

st.success("District ranking loaded successfully.")