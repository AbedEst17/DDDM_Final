import streamlit as st

def app():
     st.markdown("<h1 style='text-align: center; color: #E1AD01;'>The Consultant</h1><br>", unsafe_allow_html=True) #title

     st.markdown("<center><h3>The Consultant will help you uncover your customer segments so that you can market to each group effectively and appropriately </center></h3>", unsafe_allow_html=True) #first words on the landing page

     st.markdown("<center><h4 style= 'color:#E1AD01;'>Marketing without data is like driving with your eyes closed. <br> -Dan Zarrella-</center></h3>", unsafe_allow_html=True) #quote about the importance of data in marketing. 

     with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True) #adding a clickable avatar that leads to my linkedin
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br>I am literally one click away</span></center>', unsafe_allow_html= True)#adding a comment under the avatar