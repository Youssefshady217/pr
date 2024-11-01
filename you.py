# Importing Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:/path/to/your/file/company_sales_data.csv")


# Set up the Streamlit app layout
st.title("Company Sales Analysis")
st.sidebar.header("Navigation")
st.sidebar.markdown("Created by [Your Name](https://www.linkedin.com/in/yourprofile/)")

# Sidebar - Selection
sidebar_option = st.sidebar.radio("Choose an Option:", ["Data Overview", "EDA", "Visualizations"])

# Display the data overview
if sidebar_option == "Data Overview":
    st.header("Data Overview")
    st.write("This dataset provides information about sales, profit, and product categories across different regions and companies.")
    st.write(df.head())
    st.markdown("### Dataset Summary")
    st.write(df.describe())
    if st.sidebar.checkbox("Show Data Sample"):
        st.write(df.sample(10))

# Exploratory Data Analysis (EDA)
elif sidebar_option == "EDA":
    st.header("Exploratory Data Analysis")
    
    # Histogram of Sales
    st.subheader("Sales Distribution")
    fig1 = px.histogram(df, x='Sales', nbins=20, title="Distribution of Sales")
    st.plotly_chart(fig1)
    
    # Box Plot of Profit by Region
    st.subheader("Profit Distribution by Region")
    fig2 = px.box(df, x='Region', y='Profit', color='Region', title="Profit Distribution across Regions")
    st.plotly_chart(fig2)
    
    # Pie Chart for Product Category Distribution
    st.subheader("Product Category Distribution")
    fig3 = px.pie(df, names='Product Category', title="Product Category Breakdown")
    st.plotly_chart(fig3)

# Visualizations with Interactive Widgets
elif sidebar_option == "Visualizations":
    st.header("Interactive Visualizations")
    
    # Select Region and Product Category for Filtering
    selected_region = st.sidebar.selectbox("Select Region", df['Region'].unique())
    selected_category = st.sidebar.selectbox("Select Product Category", df['Product Category'].unique())
    
    # Filter data based on selections
    filtered_data = df[(df['Region'] == selected_region) & (df['Product Category'] == selected_category)]
    
    st.write(f"Showing data for Region: {selected_region} and Product Category: {selected_category}")
    st.write(filtered_data)
    
    # Bar Chart for Sales by Company
    st.subheader("Sales by Company")
    fig4 = px.bar(filtered_data, x='Company', y='Sales', color='Company', title="Sales Distribution among Companies")
    st.plotly_chart(fig4)

    # Line Chart for Sales Over Time
    st.subheader("Sales Over Time")
    fig5 = px.line(filtered_data, x='Order Date', y='Sales', title="Sales Trend Over Time")
    st.plotly_chart(fig5)
    
    # Scatter Plot for Sales vs Profit
    st.subheader("Sales vs Profit")
    fig6 = px.scatter(filtered_data, x='Sales', y='Profit', color='Company', size='Profit', title="Sales vs Profit by Company")
    st.plotly_chart(fig6)

# Footer
st.sidebar.markdown("***")
st.sidebar.write("End of App")

