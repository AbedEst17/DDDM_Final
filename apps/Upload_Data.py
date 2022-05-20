import pandas as pd
import streamlit as st


def app():
        st.markdown("<h1 style='text-align: center; color: E1AD01;'>Data Upload</h1><br>", unsafe_allow_html=True) #setting the title at the center
        with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True)
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Please upload your Data.</span></center>', unsafe_allow_html= True)
        uploaded_file = st.file_uploader("Upload your input CSV file", type=["csv"]) #uploading the file
        global data #setting the data to be global
        if uploaded_file is not None: #if the data is not uploaded
            data = pd.read_csv(uploaded_file) #read the file
            data.to_csv('data/main_data.csv', index=False) #save the file into a csv into the folder to carry it to the other pages
 
        else:
            data = ""
        
        if uploaded_file is not None: #if we have the file
            st.dataframe(data.head(n=6)) #show the head of the dataframe for a quick inspection of the elemnts we have
        else:
            st.write("")
