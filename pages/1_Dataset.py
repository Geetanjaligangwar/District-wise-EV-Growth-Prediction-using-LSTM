import streamlit as st
import pandas as pd

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📂",
    layout="wide"
)

# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():
    df = pd.read_csv("Data/final_model_dataset.csv")

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"])

    return df

df = load_data()

# ==========================================================
# PAGE TITLE
# ==========================================================

st.title("📂 Dataset Explorer")

st.markdown("""
Explore the historical EV registration dataset used for training the LSTM forecasting model.
""")

st.divider()

# ==========================================================
# DATASET INFORMATION
# ==========================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Records", len(df))

with col2:
    st.metric("Total Districts", df["office_name"].nunique())

with col3:
    if "date" in df.columns:
        st.metric(
            "Time Period",
            f"{df['date'].dt.year.min()} - {df['date'].dt.year.max()}"
        )

st.divider()

# ==========================================================
# FILTERS
# ==========================================================

st.subheader("🔍 Filter Dataset")

districts = sorted(df["office_name"].unique())

selected_district = st.selectbox(
    "Select District",
    ["All Districts"] + districts
)

filtered_df = df.copy()

if selected_district != "All Districts":
    filtered_df = filtered_df[
        filtered_df["office_name"] == selected_district
    ]

# Year filter (only if date column exists)
if "date" in filtered_df.columns:
    years = sorted(filtered_df["date"].dt.year.unique())

    selected_year = st.selectbox(
        "Select Year",
        ["All Years"] + list(years)
    )

    if selected_year != "All Years":
        filtered_df = filtered_df[
            filtered_df["date"].dt.year == selected_year
        ]

st.divider()

# ==========================================================
# DATA TABLE
# ==========================================================

st.subheader("📋 Historical Dataset")

st.dataframe(
    filtered_df,
    use_container_width=True,
    height=500
)

st.write(f"Showing **{len(filtered_df)}** records.")

st.divider()

# ==========================================================
# DOWNLOAD BUTTON
# ==========================================================

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📥 Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

st.divider()

# ==========================================================
# DATA SUMMARY
# ==========================================================

st.subheader("📊 Dataset Summary")

left, right = st.columns(2)

with left:
    st.write("### Dataset Shape")
    st.write(filtered_df.shape)

    st.write("### Columns")
    st.write(list(filtered_df.columns))

with right:
    st.write("### Missing Values")
    st.dataframe(filtered_df.isnull().sum())

st.divider()

st.success("Dataset loaded successfully.")