import streamlit as st
import pandas as pd
import json
import os

# Load failure log JSON
json_path = os.path.join("..", "reports", "failed_cases_log.json")
if not os.path.exists(json_path):
    st.error("Failure log not found. Please run log_failures.py first.")
    st.stop()

with open(json_path, 'r') as f:
    failed_cases = json.load(f)

# Convert to DataFrame
df = pd.DataFrame(failed_cases)

st.title("PharmaQA – Failed Drug Response Test Cases")
st.markdown("This dashboard shows failed test cases from scientific software QA logs.")

# Filters
drug_filter = st.multiselect("Select Drug(s):", df["drug_name"].unique(), default=df["drug_name"].unique())
dose_min, dose_max = st.slider("Dose Range (mg):", int(df["dose_mg"].min()), int(df["dose_mg"].max()), (int(df["dose_mg"].min()), int(df["dose_mg"].max())))
error_thresh = st.slider("Max Error Threshold", 0.01, 0.20, 0.05)

# Apply filters
filtered_df = df[
    (df["drug_name"].isin(drug_filter)) &
    (df["dose_mg"] >= dose_min) &
    (df["dose_mg"] <= dose_max) &
    (df["error"] > error_thresh)
]

# Show table
st.subheader("Filtered Failed Cases")
st.dataframe(filtered_df)

# Plot bar chart
if not filtered_df.empty:
    st.subheader("Response Deviation Chart")
    chart_data = filtered_df[["drug_name", "expected", "actual"]].set_index("drug_name")
    st.bar_chart(chart_data)
else:
    st.info("No data matching the selected filters.")

st.caption("Built with ❤️ for scientific QA testing.")
