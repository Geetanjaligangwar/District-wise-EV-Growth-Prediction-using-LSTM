import streamlit as st
import pandas as pd
import plotly.express as px

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Historical Analysis",
    page_icon="📈",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    df = pd.read_csv("Data/final_model_dataset.csv")
    df["date"] = pd.to_datetime(df["date"])
    return df

df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📈 Historical EV Registration Analysis")

st.markdown("""
Analyze historical monthly EV registrations for each district.
""")

st.divider()

# ==========================================================
# DISTRICT SELECTION
# ==========================================================

districts = sorted(df["office_name"].unique())

selected_district = st.selectbox(
    "Select District",
    districts
)

district_df = df[df["office_name"] == selected_district].sort_values("date")

# ==========================================================
# KPI CARDS
# ==========================================================

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Total Registrations",
        int(district_df["monthly_registrations"].sum())
    )

with col2:
    st.metric(
        "Average Monthly",
        round(district_df["monthly_registrations"].mean(), 2)
    )

with col3:
    st.metric(
        "Maximum",
        int(district_df["monthly_registrations"].max())
    )

with col4:
    st.metric(
        "Minimum",
        int(district_df["monthly_registrations"].min())
    )

st.divider()

# ==========================================================
# LINE CHART
# ==========================================================

st.subheader("📈 Monthly EV Registration Trend")

fig = px.line(
    district_df,
    x="date",
    y="monthly_registrations",
    markers=True,
    title=f"Historical EV Registrations - {selected_district}"
)

fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Monthly Registrations"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# ==========================================================
# MONTHLY BAR CHART
# ==========================================================

st.subheader("📊 Registrations by Month")

monthly = district_df.groupby("month_name")["monthly_registrations"].mean().reset_index()

month_order = [
    "January","February","March","April","May","June",
    "July","August","September","October","November","December"
]

monthly["month_name"] = pd.Categorical(
    monthly["month_name"],
    categories=month_order,
    ordered=True
)

monthly = monthly.sort_values("month_name")

fig2 = px.bar(
    monthly,
    x="month_name",
    y="monthly_registrations",
    title="Average Monthly Registrations"
)

st.plotly_chart(fig2, use_container_width=True)

st.divider()

# ==========================================================
# HISTORICAL DATA TABLE
# ==========================================================

st.subheader("📋 Historical Records")

st.dataframe(
    district_df,
    use_container_width=True
)

st.divider()

# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

csv = district_df.to_csv(index=False).encode("utf-8")

st.download_button(
    "📥 Download Historical Data",
    csv,
    file_name=f"{selected_district}_historical.csv",
    mime="text/csv"
)

st.success("Historical analysis loaded successfully.")