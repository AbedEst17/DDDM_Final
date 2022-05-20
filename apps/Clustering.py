import streamlit as st
import pandas as pd
from datetime import timedelta #calculating differences in dates
import plotly.express as px



def app():
     st.markdown("<h1 style='text-align: center; color: #E1AD01;'>The Clusters</h1><br>", unsafe_allow_html=True) #setting the title
     with st.sidebar:
          st.markdown('<center><a href="https://www.linkedin.com/in/abed-el-rahman-al-estwani/"><img style="max-width:75%" src="https://raw.githubusercontent.com/NythBusters/pics/main/Bustem.png"></center>', unsafe_allow_html= True) #setting the avatar
          st.markdown('<center><span style="font-size: 130%; color: #E1AD01;"><br> Our customers can be grouped into clusters that share common behavioral patterns.</span></center>', unsafe_allow_html= True) #setting a comment under the avatar
     df = pd.read_csv(r'data/main_data.csv') #reading the data carried over

     df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"]) #changing the date from string to datetime
     # --Group data by customerID--
     # Create snapshot date
     snapshot_date = df['InvoiceDate'].max() + timedelta(days=1) #taking the snapshot 1 day after our last date
     print(snapshot_date)
     # Grouping by CustomerID
     data_process = df.groupby(['CustomerID']).agg({
          'InvoiceDate': lambda x: (snapshot_date - x.max()).days, # this allows us to get recency 
          'InvoiceNo': 'count', #this allows us to get frequency
          'Sales': 'sum'}) #this allows us to get the monetary
     # Rename the columns 
     data_process.rename(columns={'InvoiceDate': 'Recency',
                              'InvoiceNo': 'Frequency',
                              'Sales': 'MonetaryValue'}, inplace=True) #changing the names into the RFM elements
     
     from sklearn.cluster import KMeans
     sse ={}
     for k in range(1,20):
         kmeans = KMeans(n_clusters =k, random_state = 42) 
         kmeans.fit(data_process)
         sse[k] = kmeans.inertia_
     #plt.title("The Elbow Method")
     #plt.xlabel('k')
     #plt.ylabel('SSE') 
     #sns.pointplot(x=list(sse.keys()), y = list(sse.values()))
     #plt.show()
     #didn't visualize the result of the elbow since it is of no importance to the audience. it is important to me so that I set the right hyperparameter.

     k = 5 #hyperparameter for the number of clusters based on the elbow point
     model = KMeans(n_clusters=k, random_state = 42) #the parameter of the model
     model.fit(data_process) #fitting the model
     data_process["Cluster"] = model.labels_ # the labels

     data_process["Cluster_name"] = 'Cluster' + data_process["Cluster"].astype('str') #setting the name of the clusters
     df_agg = data_process.groupby("Cluster_name").agg({
    "Recency": 'mean', 'Frequency': 'mean', 'MonetaryValue':['mean', 'count']
     }).round(0) 

     df_agg.columns = df_agg.columns.droplevel() #return DataFrame with requested index / column level(s) removed
     df_agg.columns = ["RecencyMean", "FrequencyMean", "MonetaryMean","Count"] #the fields 
     df_agg["Percent"] = round((df_agg['Count']/df_agg.Count.sum())*100,2) #getting the percentage out of our observations for each class

     df_agg = df_agg.reset_index() #reseting the index

     labels_dict = {'Cluster0': "John", "Cluster1": 'Chantel', "Cluster2": "Joe", "Cluster3": "Zoey", "Cluster4": "Sam"} #renaming the clusters into the personas

     df_agg["Cluster_name"] = df_agg['Cluster_name'].map(labels_dict) #mapping the names

     data_process['Cluster_name'] = data_process['Cluster_name'].map(labels_dict) #mapping the names on the previous data frame

     df_agg.to_csv(r'C:\Users\itm\Desktop\Multipage\apps\Cluster_data.csv', index=False) #saving the dataframe df_agg into csv file to carry it to other pages

     fig = px.scatter(df_agg, x="RecencyMean", y="MonetaryMean", size = "FrequencyMean", color = "Cluster_name", hover_name ="Cluster_name", size_max = 100, title= "Customer Clusters by RFM") #visualizing the clusters
     fig.update_xaxes(title_text="Recency Mean")#adding title
     fig.update_xaxes(showgrid=False)#removing the grid
     fig.update_yaxes(showgrid=False)#removing the grid
     fig.update_xaxes(showgrid=False, zeroline=False) #removing the zeroline
     fig.update_yaxes(showgrid=False, zeroline=False) #removing the zeroline

     fig5 = px.bar(df_agg, x="Cluster_name", y="Percent", title = "Cluster % of toal Customers")
     fig5.update_xaxes(title_text="Cluster name")
     fig5.update_xaxes(showgrid=False)
     fig5.update_yaxes(showgrid=False)
     fig5.update_xaxes(showgrid=False, zeroline=False)
     fig5.update_yaxes(showgrid=False, zeroline=False)
     fig5.update_layout(xaxis={'categoryorder':'total descending'})
     
     clusters = len(data_process["Cluster_name"].unique()) #getting the length of the list having the unique clusters to get the total numbers
     x = df_agg[df_agg["Percent"] == df_agg["Percent"].max()]['Cluster_name'] # returning the clustername that has the highest count
     x = [i for i in x] #list comprehension to to get the name of the cluster

     col1,col2 = st.columns([0.65,0.35]) #splitting the display screen into 2 un-equal parts.
     with col1:
        st.plotly_chart(fig, use_container_width=True) #showing the scatter plot
        st.write("Based on the RFM analysis, the clusters we have are:", clusters) # writing down the number of clusters we have 
        
     with col2:
        st.plotly_chart(fig5, use_container_width=True) #showing the bar graph
        st.write("The highest percentage of our customers at", df_agg["Percent"].max(), "is", x[0]) #writing down the name of the cluster that has the highest percentage of the total observations
