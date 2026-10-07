import streamlit as st
import pandas as pd
 
st.title("Telangana PDS Analytics Dashboard")
 
st.write("Multi-Dimensional Shop Performance Clustering Dashboard")
 
uploaded_file = st.file_uploader(
"Upload Clustered CSV",
type="csv"
)
 
if uploaded_file:
 
df = pd.read_csv(uploaded_file)
 
st.subheader("Dataset Preview")
 
st.dataframe(df.head())
 
if "Cluster" in df.columns:
st.subheader("Cluster Distribution")
 
st.bar_chart(
df["Cluster"].value_counts()
)
