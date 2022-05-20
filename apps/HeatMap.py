import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def app():
        st.markdown("<h1 style='text-align: center; color: #E1AD01;'>The Heatmap</h1><br>", unsafe_allow_html=True)#setting the title
        with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True)
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Understanding the correlation between Recency, Frequency, and Monetary.</span></center>', unsafe_allow_html= True)
        df_agg = pd.read_csv(r'data\Cluster_data.csv') #reading the agg file that has the cluster names and their fields
        df_agg = df_agg[["RecencyMean", "FrequencyMean", "MonetaryMean"]]
        col1,col2,col3 = st.columns([0.33,0.33,0.33])
        # Visualizing correlation coefficients between features and cancellation:
        fig = plt.figure(figsize=(5,7))
        plt.style.use(['dark_background', 'bmh']) #setting dark background to match the other visuals
        ax = sns.heatmap(df_agg.corr()[['MonetaryMean']].abs().sort_values('MonetaryMean', ascending=False), annot = True, annot_kws = {"size":12}, cmap='Reds')
        ax.set_title('Correlation MonetaryMean with Frequency and Recency means', fontsize=16)
        ax.set_xlabel('Features', fontsize = 16)
        ax.set_ylabel('Features', fontsize = 16)
        ax.tick_params(axis = "both", labelsize = 12)
        y_min, y_max = ax.get_ylim()
        ax.set_ylim(top=y_max+1)
        

        fig2 = plt.figure(figsize=(5,7))
        ax2 = sns.heatmap(df_agg.corr()[['FrequencyMean']].abs().sort_values('FrequencyMean', ascending=False), annot = True, annot_kws = {"size":12}, cmap='Reds')
        ax2.set_title('Correlation FrequenyMean with Recency and Monetary means', fontsize=16)
        ax2.set_xlabel('Features', fontsize = 16)
        ax2.set_ylabel('Features', fontsize = 16)
        ax2.tick_params(axis = "both", labelsize = 12)
        y_min, y_max = ax2.get_ylim()
        ax2.set_ylim(top=y_max+1)

        fig3 = plt.figure(figsize=(5,7))
        ax3 = sns.heatmap(df_agg.corr()[['RecencyMean']].abs().sort_values('RecencyMean', ascending=False), annot = True, annot_kws = {"size":12}, cmap='Reds')
        ax3.set_title('Correlation RecencyMean with Frequency and Monetary means', fontsize=16)
        ax3.set_xlabel('Features', fontsize = 16)
        ax3.set_ylabel('Features', fontsize = 16)
        ax3.tick_params(axis = "both", labelsize = 12)
        y_min, y_max = ax3.get_ylim()
        ax3.set_ylim(top=y_max+1)

        with col1:
            st.pyplot(fig)
        with col2:
            st.pyplot(fig2)
            st.markdown("<center> The closer the number is to 1, the stronger the relationship is.</center>", unsafe_allow_html= True)
        with col3:
            st.pyplot(fig3)
