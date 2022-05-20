import streamlit as st
import pandas as pd
import plotly.express as px

def app():
        st.markdown("<h1 style='text-align: center; color: #E1AD01;'>The EDA</h1><br>", unsafe_allow_html=True)#setting the title
        with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True)
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Understanding the behavioral patterns through the lense of Recency, Frequency, and Monetary.</span></center>', unsafe_allow_html= True)
        df_agg = pd.read_csv(r'data\Cluster_data.csv') #reading the agg file that has the cluster names and their fields
        fig2 = px.bar(df_agg, x="Cluster_name", y="MonetaryMean", title = "Monetary mean value of each cluster") #setting the bar graph for the clusters' monetary mean
        fig2.update_xaxes(title_text="Cluster name")
        fig2.update_xaxes(showgrid=False)
        fig2.update_yaxes(showgrid=False)
        fig2.update_xaxes(showgrid=False, zeroline=False)
        fig2.update_yaxes(showgrid=False, zeroline=False)
        fig2.update_layout(xaxis={'categoryorder':'total descending'})

        fig3 = px.bar(df_agg, x="Cluster_name", y="RecencyMean", title = "Recency mean value of each cluster") #setting the bar graph for the clusters' recency mean
        fig3.update_xaxes(title_text="Cluster name")
        fig3.update_xaxes(showgrid=False)
        fig3.update_yaxes(showgrid=False)
        fig3.update_xaxes(showgrid=False, zeroline=False)
        fig3.update_yaxes(showgrid=False, zeroline=False)
        fig3.update_layout(xaxis={'categoryorder':'total descending'})

        fig4 = px.bar(df_agg, x="Cluster_name", y="FrequencyMean", title = "Frequency mean value of each cluster") #setting the bar graph for the clusters' frequency mean
        fig4.update_xaxes(title_text="Cluster name")
        fig4.update_xaxes(showgrid=False)
        fig4.update_yaxes(showgrid=False)
        fig4.update_xaxes(showgrid=False, zeroline=False)
        fig4.update_yaxes(showgrid=False, zeroline=False)
        fig4.update_layout(xaxis={'categoryorder':'total descending'})

        x = df_agg[df_agg["FrequencyMean"] == df_agg["FrequencyMean"].max()]['Cluster_name'] #getting the name cluster with the max frequency mean
        y = df_agg[df_agg["MonetaryMean"] == df_agg["MonetaryMean"].max()]['Cluster_name'] #getting the name cluster with the max Monetary mean
        z = df_agg[df_agg["RecencyMean"] == df_agg["RecencyMean"].max()]['Cluster_name'] #getting the name cluster with the max Recencymean

        x= [i for i in x] #list comprehension to get the name
        y = [i for i in y] #list comprehension to get the name
        z = [i for i in z] #list comprehension to get the name

        col1,col2, col3=st.columns([0.3,0.3, 0.3]) #splitting the page into 3 parts
        with col3:
            st.plotly_chart(fig4, use_container_width=True) #plotting the 3rd bar graph
            st.write("The cluster that visits the most is:", x[0])
        with col2:
            st.plotly_chart(fig3, use_container_width=True) #plotting the 2nd bar graph
            st.write("The cluster that waits long between visits is:",z[0])
        with col1:
            st.plotly_chart(fig2, use_container_width=True) #plotting the first bar graph
            st.write("The cluster that spends the most is:", y[0])
