import streamlit as st
import pandas as pd
import os


#in this page we are manipulating the imported data and extracting some useful features.

def app():
         st.markdown("<h1 style='text-align: center; color: #E1AD01;'>The Data</h1><br>", unsafe_allow_html=True)
         with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True)
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Data in the right hands, is the greatest competitve edge.</span></center>', unsafe_allow_html= True)
         if 'main_data.csv' not in os.listdir('data'): #if data is not uploaded we have to set a warning message.
            st.warning("Please upload data through `Upload Data` page!") # the warning message.
         else: # if the data is uploaded, we will proceed forward.
          global df
          df = pd.read_csv(r'data/main_data.csv') # read the csv file
          df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]) #change the InvoiceDate into datetime data type
         
          df.dropna(subset=['CustomerID'], inplace=True) # Drop null values

          df = df.loc[df['Quantity'] > 0] # Keep records with positive quantities 

          df = df.loc[df['UnitPrice'] > 0]# Remove records with negative price
          
          df['Sales'] = df['Quantity'] * df['UnitPrice'] # Calculate total sales

          st.dataframe(df.head()) #show the dataframe

          observations = df.shape[0] #getting the number of rows

          fields = df.shape[1] #getting the number of columns

          res = [] #initializing an empty list
          desc = [i for i in df["Description"].unique()] #getting a list of unique items
          unique = len(desc) #getting the number of unique items in the list
          
          country = [ i for i in df["Country"].unique()] # getting the unique countries in a list
          u_country = len(country) # getting the number of unique countries

          x = df["InvoiceDate"].max() - df["InvoiceDate"].min() #getting the time span of the data

          y = df["CustomerID"].unique() #setting the unique customers
          u_cust = len(y) # getting the number of unique customers and putting it into a variable

          df.to_csv(r'data\main_data.csv', index=False)
          col1,col2,col3=st.columns([0.33,0.33,0.33]) #splitting the page into 3 columns
          with col1:
             st.write("Observations' Count:", observations)  #printing the number of observations
             st.write("Fields' Count:", fields) #printing the number of fields
             
          with col2:
             st.write("Unique items' Count:", unique) # printing the number of unique items
             st.write("Unique Countries Count:", u_country) #printing the number of unique countries
         
          with col3:
             st.write("Time Span:", x) #printing the timespan that we have
             st.write("Unique Customers' Count", u_cust) #printing the number of unique customers



