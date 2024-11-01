import streamlit as st
import matplotlib.pyplot as plt 
import seaborn as sns
import pandas as pd
import plotly.express as px
st.title("Credit Card Custemors")
st.write("""This journey is defined as the sequential process steps and touch points that a credit card customer of a bank, credit card company, or fintech, experiences throughout their life-cycle as a prospect, or customer.
         
End-to-end credit card customer journeys are typically broken out into the following sub-processes:
         
Marketing
Pre-activation
Activation
Customer service - website
Customer service - call center
Collections
Payments
Quality/Operations
Retention""")
df = pd.read_csv("bank dataset.csv")
st.sidebar.header("Navigation")
ekhtiar = st.sidebar.selectbox("Show you the table or continue to next?..",["Yes","Continue"])
if ekhtiar == "Yes":
    st.write(df)
ekhtiar2 = st.sidebar.radio("Which type of charts do you want?",["Bar chart","Scatter chart","Pie chart","Line chart"])
if ekhtiar2 == "Pie chart":
    st.subheader("Pie charts")
    stt = px.pie(data_frame=df,names="Education_Level",title="Levels")
    st.write(stt)
    stt = px.pie(data_frame=df,names="Gender",title="Gender")
    st.write(stt)
    stt = px.pie(data_frame=df,names="Card_Category",title="Card Category")
    st.write(stt)
    stt = px.pie(data_frame=df,names="Marital_Status",title="Status")
    st.write(stt)
elif ekhtiar2 == "Bar chart":
    st.subheader("Bar charts")
    st1 = px.bar(df,x= "Customer_Age",y= "Dependent_count",color="Gender")
    st.plotly_chart(st1)
    st2 = px.bar(df,x= "Customer_Age",y= "Months_on_book",color="Customer_Age")
    st.plotly_chart(st2)
elif ekhtiar2 == "Scatter chart":
    st.subheader("Scatter charts")
    st3 = px.scatter(data_frame=df,y="Dependent_count" , x= "Customer_Age", color= "Dependent_count", title="Dependent count")
    st.plotly_chart(st3)
    st4 = px.scatter(data_frame=df,y="Credit_Limit" , x= "Customer_Age", color= "Dependent_count",title="Credit limit")
    st.plotly_chart(st4)
elif ekhtiar2 == "Line chart":
    st.subheader("Line charts")
    st5 = px.line(data_frame=df,y="Dependent_count",x="Customer_Age",color="Customer_Age")
    st.plotly_chart(st5)







