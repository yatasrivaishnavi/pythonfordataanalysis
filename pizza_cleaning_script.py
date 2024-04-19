# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 18:49:27 2024

@author: 91984
"""
import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

# read the excel files
pizza_sales_df=pd.read_excel('pizza_sales.xlsx')
pizza_size_df=pd.read_csv('pizza_size.csv')
pizza_category_df=pd.read_csv('pizza_category.csv')

#viewing top and bottom rows in dataframe
pizza_sales_df.head()
pizza_sales_df.head(10)

pizza_sales_df.tail()
pizza_sales_df.tail(10)

#describing data
pizza_sales_df.describe()
pizza_description=pizza_sales_df.describe()
# Having look at non values in each column
pizza_sales_df.info()
#counting the number null values in each column
null_count=pizza_sales_df.isnull().sum()

#check for duplicated rows
duplicated_rows=pizza_sales_df.duplicated().sum()
print(duplicated_rows)

# To select a column
quantity_column=pizza_sales_df['quantity']
selected_columns=pizza_sales_df[['order_id','quantity','unit_price']]

#Get row with index label 3
row=pizza_sales_df.loc[3]

#Get two rows index label 3 and 5
rows=pizza_sales_df.loc[[3,5]]

#Get rows between 3 and 5
subset=pizza_sales_df.loc[3:5]

#Get rows between index label 3 and 5 and specific columns
subset=pizza_sales_df.loc[3:5,['quantity','unit_price']]

#Truncate dataframe before index 3
truncated_before=pizza_sales_df.truncate(before=3)
 
#Truncate dataframe after index 5
truncated_after=pizza_sales_df.truncate(after=5)

#Truncating columns
quantity_series=pizza_sales_df['quantity']

#Truncate quantity series before index 3
truncated_series_before=quantity_series.truncate(before=3)

#Truncate quantity series after index 5
truncated_series_after=quantity_series.truncate(after=5)

# Filtering on Data
pizza_sales_df['order_date']=pizza_sales_df['order_date'].dt.date
date_target= datetime.strptime('2015-12-15','%Y-%m-%d').date()
filtered_rows_by_date=pizza_sales_df[pizza_sales_df['order_date']>date_target]

# Filtering on Multiple conditions 
# Using and condition
bbq_chicken_rows= pizza_sales_df[(pizza_sales_df['unit_price']>15)&(pizza_sales_df['pizza_name']== 'The Barbecue Chicken Pizza')]

# Using or condition
bbq_chicken_rows_or=pizza_sales_df[
    (pizza_sales_df['unit_price']>20)|(pizza_sales_df['pizza_name']==' The Barbecue Chicken Pizza')]

# Filtering on specific range
high_sales=pizza_sales_df[(pizza_sales_df['unit_price']>15)&(pizza_sales_df['unit_price']<=20)]

# dropping null values
pizza_sales_null_values_dropped=pizza_sales_df.dropna()
null_count=pizza_sales_null_values_dropped.isnull().sum()

# Replace nulls with a value
date_na_fill=datetime.strptime('2000-01-01','%Y-%m-%d').date()
pizza_sales_null_values_replaced=pizza_sales_df.fillna(date_na_fill)

#Deleting specific rows and columns in a dataframe
filtered_rows_2=pizza_sales_df.drop(2,axis=0)

#Deleting multiple rows 5 , 7, 9
filtered_rows_5_7_9=pizza_sales_df.drop([5,7,9],axis=0)

#Deleting a column by column name
filtered_unit_price=pizza_sales_df.drop('unit_price',axis=1)

#Deleting multiple columns
filtered_unit_price_and_order_id=pizza_sales_df.drop(['unit_price','order_id'],axis=1)

# Sorting Dataframe
#sorting in ascending order
sorted_df=pizza_sales_df.sort_values('total_price')

#sorting in descending order
sorted_df_desc=pizza_sales_df.sort_values('total_price',ascending=False)

#sort by multiple columns
sorted_df_multiple=pizza_sales_df.sort_values(['pizza_category_id','total_price'],ascending=[True,False])

#Group by pizza size id and get the count of sales(row count)
grouped_df_pizza_size=pizza_sales_df.groupby(['pizza_size_id']).count()

#Group by pizza size id and get the sum
grouped_df_pizza_size_by_sum=pizza_sales_df.groupby(['pizza_size_id'])['total_price'].sum()

#Group by pizza size id and sum total price and quantity
grouped_df_pizza_size_sales_quantity=pizza_sales_df.groupby(['pizza_size_id'])[['total_price','quantity']].sum()

#Aggregation functions
grouped_df_agg=pizza_sales_df.groupby(['pizza_size_id'])[['total_price','quantity']].min()

#using aggregation to perform different aggregations on different columns
aggregated_data=pizza_sales_df.groupby(['pizza_size_id']).agg({'quantity':sum,'total_price':'mean'})

# Merging pizza sales df and pizza size df
merged_df=pd.merge(pizza_sales_df,pizza_size_df,on='pizza_size_id')

#Add category information
merged_df=pd.merge(merged_df ,pizza_category_df, on='pizza_category_id')

# Concatenate two dataframes - appending rows to a dataframe vertically
another_pizza_sales_df=pd.read_excel('another_pizza_sales.xlsx')
concatenate_vertically=pd.concat([pizza_sales_df,another_pizza_sales_df])
concatenate_vertically=concatenate_vertically.reset_index()

# Concatenate 2 dataframes - appending columns to a dataframe horizontally
pizza_sales_voucher_df=pd.read_excel('C:/Users/91984/python Course/Source (Input) Data for the course/Pizza Sales Project/pizza_sales_voucher.xlsx')
concatenate_horizontally=pd.concat([pizza_sales_df,pizza_sales_voucher_df],axis=1)

#Changing cases in python
#converting to lower case
lower_text=pizza_sales_df['pizza_ingredients'].str.lower()
pizza_sales_df['pizza_ingredients']=pizza_sales_df['pizza_ingredients'].str.lower()

# convert to upper case
pizza_sales_df['pizza_ingredients']=pizza_sales_df['pizza_ingredients'].str.upper()

# converting to title case 
pizza_sales_df['pizza_ingredients']=pizza_sales_df['pizza_ingredients'].str.title()

# Replacing text values
replaced_text=pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese','Mozzarella Cheese')
pizza_sales_df['pizza_ingredients']=pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese','Mozzrella')

#Removing extra whitespaces from columns
pizza_sales_df['pizza_name']=pizza_sales_df['pizza_name'].str.strip()

#Generating a Boxplot
sns.boxplot(x='category',y='total_price',data=merged_df)
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.title('Boxplot showing distribution of Sales by Category')
plt.show()





