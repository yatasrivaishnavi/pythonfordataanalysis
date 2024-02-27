# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:30:38 2024

@author: 91984
"""
import pandas as pd

#load sales data from excel into a pandas DataFrame
sales_data=pd.read_excel('sales_data.xlsx')
# =============================================================================
# Exploring the data 
# =============================================================================

#get summary of data
sales_data.info()
sales_data.describe()
#look the columns
print(sales_data.columns)
#look at the first few rows of the data
print(sales_data.head())
#check the datatype of the columns
print(sales_data.dtypes)

# =============================================================================
# cleaning the data
# =============================================================================
#missing values in sales data
print(sales_data.isnull().sum())

#drop any rows that has any missing/nan values
sales_data_dropped=sales_data.dropna()

#drop rows with missing amounts based on Amount column
sales_data_cleaned=sales_data.dropna(subset=['Amount'])

#check for missing values in our sales data which is cleaned
print(sales_data_cleaned.isnull().sum())

# =============================================================================
# Slicing and Filtering Data
# =============================================================================

#selecting subset based on the category column
category_data=sales_data[sales_data['Category']=='Top']
print(category_data)

#select subset of data where the amount>1000
high_amount_data=sales_data[sales_data['Amount']>1000]
print(high_amount_data)

#subset of data based on multiple columns
filtered_data=sales_data[(sales_data['Category']=='Top')&(sales_data['Qty']==3)]

# =============================================================================
# Aggregating
# =============================================================================
#total sales by category
category_totals=sales_data.groupby('Category')['Amount'].sum()
category_totals=sales_data.groupby('Category',as_index=False)['Amount'].sum()
category_totals=category_totals.sort_values('Amount',ascending=False)


#calculate average amount by Category ans Fulfilment
fulfilment_averages=sales_data.groupby(['Category','Fulfilment'],as_index=False)['Amount'].sum()
fulfilment_averages=fulfilment_averages.sort_values('Amount',ascending=False)

#Calculate average amount by Category and Status
status_averages=sales_data.groupby(['Category','Status'],as_index=False)['Amount'].sum()
status_averages=status_averages.sort_values('Amount',ascending=False)

#calculate total sales by shipment and fulfilment
total_sales_shipandfulfil=sales_data.groupby(['Courier Status','Fulfilment'],as_index=False)['Amount'].sum()
total_sales_shipandfulfil=total_sales_shipandfulfil.sort_values('Amount',ascending=False)

# =============================================================================
# renaming columns
# =============================================================================

total_sales_shipandfulfil.rename(columns={'Courier Status':'Shipment'},inplace=True)

# =============================================================================
# Exporting Data
# =============================================================================

status_averages.to_excel('average_sales_by_category_and_sales.xlsx', index=False)
total_sales_shipandfulfil.to_excel('total_sales_by_ship_and_fulfil.xlsx',index=False)










