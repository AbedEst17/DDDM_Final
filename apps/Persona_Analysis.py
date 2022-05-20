import streamlit as st
import pandas as pd
import plotly.express as px
import os

def app():
        
        st.markdown("<h1 style='text-align: center; color: #E1AD01;'>The Customers</h1><br>", unsafe_allow_html=True)#setting the title
        with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True)
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Meet our customers.</span></center>', unsafe_allow_html= True)
        df_agg = pd.read_csv(r'C:\Users\itm\Desktop\Multipage\apps\Cluster_data.csv') #reading the agg file that has the cluster names and their fields
        persona_list = [i for i in df_agg["Cluster_name"]] #turning the names of the clusters into a list to be used in the selectbox
        col1,col2,col3 = st.columns([0.33,0.33,0.33])
        with col1:
             persona = st.selectbox("Choose the Persona:", persona_list)
        if persona == "John":
            with col1:
                st.markdown('<center><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/John.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Meet John<br> He represents the majority of our customers. He doesn't buy from us often and when he does, his spending is meager.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Recommendations <br> Reach out to the Johns through mail marketing while targeting their interests based on their purchase history.</span></center>", unsafe_allow_html= True)
        elif persona == "Chantel":
            with col1:
                st.markdown('<center><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Chantel.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Meet Chantel<br> She's a heavy and frequent spender.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Recommendations<br> Upselling is an effective method to capatilize on her frequent visits.</span></center>", unsafe_allow_html= True)
        elif persona == "Joe":
            with col1:
                st.markdown('<center><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Joe.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Meet Joe<br> He's the all star big time spender. </span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Recommendations<br> There aren't many Joes, so it is best to set a unique loyalty program that caters to their interests with flashy perks and a flashier name.</span></center>", unsafe_allow_html= True)
        elif persona == "Zoey":
            with col1:
                st.markdown('<center><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Zoey.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Meet Zoey<br> She's a regular customer with the potential of spending more.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Recommendations<br> cross-sell items, offer a loyalty program and send gifts! If they cancel any of their orders, reach out to them directly and grow that one-on-one relationship. </span></center>", unsafe_allow_html= True)
        elif persona == "Sam":
            with col1:
                st.markdown('<center><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Sam.png"></center>', unsafe_allow_html = True)
            with col2:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Meet Sam<br> A recent shopper who is still to grow into a regular customer.</span></center>", unsafe_allow_html= True)
            with col3:
                st.markdown("<center><span style='text-align: center; font-size: 130%'> Recommendations<br> We should offer Sam loyalty programs and cross sell items to make him progressively buy more</span></center>", unsafe_allow_html= True)
        else:
            with col1:
                st.write("")
            with col2:
                st.write("")
            with col3:
                st.write("")