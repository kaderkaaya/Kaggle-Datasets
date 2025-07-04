import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv('/Users/kaderkaya/Desktop/E-Commerce-Dataset/e_commerce_data/olist_customers_dataset.csv')
five_Row =  df.head()
print('Head Rows:\n',five_Row)
print('Table Info:\n',df.info())
print('Describe to table:\n',df.describe)
print('The count of null rows:\n',df.isnull().sum())
print('Data Type:\n',df['customer_zip_code_prefix'].dtype)
special_code = df['customer_zip_code_prefix'] =df['customer_zip_code_prefix'].astype(str)
print('Data Type:\n',special_code.dtype)
special_code_count = (special_code == '30320').sum()
print('special_code:\n',special_code_count)
print('Columns:\n',df.columns)
zip_code_counts = df['customer_zip_code_prefix'].value_counts()
print('zip_code_counts:\n',zip_code_counts)
zip_codes = df['customer_zip_code_prefix']
top_n = 16
zip_code_counts_to_plot = zip_code_counts.head(top_n)
print('zip_code_counts_to_plot:\n',zip_code_counts_to_plot)
print('zip_codes',zip_codes)
plt.figure(figsize=(10,6))
plt.bar(zip_code_counts_to_plot.index,
        zip_code_counts_to_plot.values,
        color ='skyblue',
        width=0.7,
        edgecolor='gray',
        linewidth =1.0
        )
plt.title('number of people by zip code',fontsize = 16)
plt.xlabel('Zip Codes',fontsize = 12)
plt.ylabel('Number of Persons',fontsize=12)

for i,v in enumerate(zip_code_counts):
    plt.text(
        i,v + 1, str(v),
        ha='center',
        va = 'bottom',
        fontsize =1,
        color ='dimgray'       
                )
plt.ylim(0,max(zip_code_counts)+14)
plt.grid(axis='y',linestyle= '--',alpha = 0.7) 
plt.show()
df['lives_in_cachoeiro']= df['customer_city'] = 'cachoeiro'
print(df)