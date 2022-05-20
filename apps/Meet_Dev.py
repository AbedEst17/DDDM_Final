import streamlit as st

def app():
        st.markdown("<h1 style='text-align: center; color: #E1AD01;'>Meet the Dev</h1><br>", unsafe_allow_html=True)#setting the title
        with st.sidebar:
          st.markdown('<center><a href="https://www.aub.edu.lb/osb/MSBA/Pages/default.aspx"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Logo%20MSBA.png"></center>', unsafe_allow_html= True)#MSBA logo
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Powered by MSBA</span></center>', unsafe_allow_html= True)#facts

        col1,col2, col3=st.columns([0.3,0.3, 0.3]) #splitting the page into 3 parts
        
        with col1:
           st.markdown("<center><span style= 'color: #E1AD01;'>For a deeper analysis into customer behavior, check my ARM dashboard.</span></center>", unsafe_allow_html=True)
           st.markdown('<center><a href="https://abedest17.shinyapps.io/abedest_arm/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Rshiny.png"></center>', unsafe_allow_html=True) #Rshiny logo holding link to the Rshiny dashboard 
        with col2:
            st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True) #avatar with a link to linkedIn
            st.markdown("<h1 style='text-align: center; color: #E1AD01;'>Abed Estwani</h1><br>", unsafe_allow_html=True)
        with col3:
            st.markdown("<center><span style= 'color: #E1AD01;'>A previous project Using Streamlit</span></center>", unsafe_allow_html=True)
            st.markdown('<center><a href="https://share.streamlit.io/nythbusters/netflix/main/Streamlit_Netflix.py"><img style="max-width:75%" src="https://streamlit.io/images/brand/streamlit-mark-color.png"></center>', unsafe_allow_html=True)#streamlit logo carrying link to another streamlit dashboard 
            
        
            
