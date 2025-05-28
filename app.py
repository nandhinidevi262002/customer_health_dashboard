import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Customer Health Dashboard", layout="wide")
st.title("Customer Health Dashboard")

def normalize_column(col):
    min_val = col.min()
    max_val = col.max()
    return (col - min_val) / (max_val - min_val) if max_val != min_val else 0

@st.cache_data
def load_default_data():
    return pd.read_excel("Customer_Health_Score.xlsx", sheet_name=0, engine="openpyxl")

st.sidebar.header("Data Source Selection")
data_source = st.sidebar.radio("Select data source", ["Default", "Manual Upload"])

if data_source == "Manual Upload":
    uploaded_file = st.sidebar.file_uploader("Upload Excel File", type=["xlsx"])
    if uploaded_file:
        xls = pd.ExcelFile(uploaded_file, engine="openpyxl")
        sheet_names = xls.sheet_names
        selected_sheet = st.sidebar.selectbox("Select Sheet", sheet_names)
        df = pd.read_excel(xls, sheet_name=selected_sheet, engine="openpyxl")
    else:
        st.warning("Please upload an Excel file to proceed.")
        st.stop()
else:
    st.sidebar.info("Using default dataset.")
    df = load_default_data()

metrics = ["Usage Frequency (per week)", "Logins (last 30 days)",
           "Support Ticket Responses", "Feature Adoption Rate (%)", "CSM Engagement Score (1-10)"]

for col in metrics:
    norm_col = normalize_column(df[col])
    df[f"{col} (Norm)"] = norm_col

weights = {
    "Usage Frequency (per week) (Norm)": 0.25,
    "Logins (last 30 days) (Norm)": 0.2,
    "Support Ticket Responses (Norm)": 0.15,
    "Feature Adoption Rate (%) (Norm)": 0.25,
    "CSM Engagement Score (1-10) (Norm)": 0.15,
}

df["Health Score"] = sum(df[col] * weight for col, weight in weights.items()) * 100
df["Health Status"] = pd.cut(df["Health Score"], bins=[-1, 49, 74, 100],
                             labels=["Critical", "At-Risk", "Healthy"])

st.sidebar.header("Filter Options")
industries = st.sidebar.multiselect("Select Industry", df["Industry"].unique(), default=df["Industry"].unique())
plans = st.sidebar.multiselect("Select Plan", df["Plan"].unique(), default=df["Plan"].unique())
filtered_df = df[df["Industry"].isin(industries) & df["Plan"].isin(plans)]

st.subheader("Summary Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Customers", len(filtered_df))
col2.metric("Healthy", (filtered_df["Health Status"] == "Healthy").sum())
col3.metric("At-Risk", (filtered_df["Health Status"] == "At-Risk").sum())
col4.metric("Critical", (filtered_df["Health Status"] == "Critical").sum())

st.subheader("Health Status Distribution")
health_dist = filtered_df["Health Status"].value_counts().reset_index()
health_dist.columns = ["Health Status", "Count"]
fig1 = px.pie(health_dist, names="Health Status", values="Count", hole=0.4,
              color_discrete_map={"Healthy": "green", "At-Risk": "orange", "Critical": "red"})
st.plotly_chart(fig1, use_container_width=True)

st.subheader("Top 5 At-Risk Customers (Highest Health Scores)")
top_5_at_risk = filtered_df[filtered_df["Health Status"] == "At-Risk"]
top_5_at_risk = top_5_at_risk.sort_values("Health Score", ascending=False).head(5)
st.dataframe(top_5_at_risk[["Customer ID", "Industry", "Plan", "Health Score", "Health Status"]])

st.subheader("CSM Engagement vs Health Score")
fig2 = px.scatter(filtered_df, x="CSM Engagement Score (1-10)", y="Health Score",
                  color="Health Status", hover_data=["Customer ID", "Industry"],
                  color_discrete_map={"Healthy": "green", "At-Risk": "orange", "Critical": "red"})
st.plotly_chart(fig2, use_container_width=True)

st.subheader("Health Status by Industry")
industry_dist = filtered_df.groupby(["Industry", "Health Status"]).size().reset_index(name="Count")
fig3 = px.bar(industry_dist, x="Industry", y="Count", color="Health Status", barmode="stack",
              color_discrete_map={"Healthy": "green", "At-Risk": "orange", "Critical": "red"})
st.plotly_chart(fig3, use_container_width=True)

st.subheader("Health Status by Plan")
plan_dist = filtered_df.groupby(["Plan", "Health Status"]).size().reset_index(name="Count")
fig4 = px.bar(plan_dist, x="Plan", y="Count", color="Health Status", barmode="stack",
              color_discrete_map={"Healthy": "green", "At-Risk": "orange", "Critical": "red"})
st.plotly_chart(fig4, use_container_width=True)

st.subheader("Preview Filtered Customer Data")
st.dataframe(filtered_df, use_container_width=True)

st.subheader("Export Filtered Data")
csv_data = filtered_df.to_csv(index=False).encode("utf-8")
st.download_button("Download as CSV", data=csv_data, file_name="filtered_customers.csv", mime="text/csv")