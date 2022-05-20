import streamlit as st
from multiapp import MultiApp
from apps import Home, Data, EDA, Upload_Data, Clustering, Persona_Analysis, HeatMap, Meet_Dev # import your app modules here
import os
import base64
st.set_page_config(
     page_title="The Consultant",
     page_icon="🧠",
     layout="wide",
     initial_sidebar_state="expanded")

main_bg_ext = r"apps\Images\BG.png"
       
st.markdown(
         f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg_ext, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

app = MultiApp()

st.markdown('')

# Add all your application here
app.add_app("Home", Home.app)
app.add_app("Upload", Upload_Data.app)
app.add_app("Data", Data.app)
app.add_app("Clustering", Clustering.app)
app.add_app("EDA", EDA.app)
app.add_app("HeatMap", HeatMap.app)
app.add_app("Personas", Persona_Analysis.app)
app.add_app("Meet the Dev", Meet_Dev.app)



# The main app
app.run() 
