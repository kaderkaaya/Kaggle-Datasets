import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('e_commerce_data/olist_geolocation_dataset.csv')
print('Head:\n',df.head())
print('Describe:\n',df.describe())
print('Info:\n',df.info())
print('Columns:\n',df.columns)
print('DataType of geolocation zip code:\n',df['geolocation_zip_code_prefix'].dtype)
print('Count of the sao paulo:\n',(df['geolocation_city'] =='são paulo').sum())
the_total_number_of_Sao_Paulo = (df['geolocation_city']== 'sao paulo').sum()
the_total_number_of_São_Paulo = (df['geolocation_city']== 'são paulo').sum()
print(50* '*')
print('the_total_number_of_Sao_Paulo',the_total_number_of_Sao_Paulo)
print('the_total_number_of_São_Paulo',the_total_number_of_São_Paulo)

top_counts = df['geolocation_city'].value_counts().head()
print('cities',top_counts)
df2 = pd.DataFrame({
    'cities':['sao paulo','são paulo'],
    'totals':[the_total_number_of_Sao_Paulo,the_total_number_of_São_Paulo]
})
print('df2:\n',df2)# 
## #Geolocation Dataset of SaoPaulo and SãoPaulo
cities = df2['cities']
totals =df2['totals']
plt.figure(figsize=(9,5))
plt.bar(cities,
        totals,
        color = 'skyblue',
        width= 0.7,
        edgecolor = 'black',
        linewidth =1.0
        )
plt.title('Geolocation Dataset of SaoPaulo and SãoPaulo',fontsize = 16)
plt.xlabel('Cities',fontsize =12)
plt.ylabel('Totals',fontsize =12)
plt.show()
####Geolocation Dataset of Cities
plt.bar(top_counts.index,
        top_counts.values,
        color = 'skyblue',
        width= 0.7,
        edgecolor = 'black',
        linewidth =1.0
)
plt.title('Geolocation Dataset of Cities',fontsize = 16)
plt.xlabel('Cities',fontsize =12)
plt.ylabel('Totals',fontsize =12)
plt.show()
###Correlocation Data
numerical_cols = ['geolocation_lat','geolocation_lng']
print('numerical_cols:\n',numerical_cols)
numerical_df = df[numerical_cols]
print('numerical_df:\n',numerical_df)
correlation_matrix = numerical_df.corr()
print('Correlation Matrix:\n',correlation_matrix)
sns.heatmap(correlation_matrix,
            annot=True,
            fmt='.2f',
            cmap='YlGn',
            linewidths=.5,
            linecolor='gray',
            cbar_kws={'label':'Correlation Coefficient'}
            )
plt.title('Correlation Matrix',fontsize =12)
plt.xticks(rotation= 45, ha= 'right')
plt.yticks(rotation= 0)
plt.tight_layout()
plt.show()