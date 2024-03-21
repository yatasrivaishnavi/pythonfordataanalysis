# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:32:53 2024

@author: 91984
"""
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#set working directory

os.chdir('C:/Users/91984/python Course/Source (Input) Data for the course/Ecommerce Orders Project')

#check current working directory
print(os.getcwd())

# =============================================================================
# Loading the files
# =============================================================================
# Load orders data
orders_data=pd.read_excel('orders.xlsx')

# Load payments Data 
payments_data=pd.read_excel('order_payment.xlsx')

#Load customers data
customers_data=pd.read_excel('customers.xlsx')

# =============================================================================
# Describing Data
# =============================================================================
orders_data.info()
payments_data.info()
customers_data.info()

# Handling with missing data
# checking for missing data in the orders data
orders_data.isnull().sum()
payments_data.isnull().sum()
customers_data.isnull().sum()

# Filling missing values with a default value in orders data
orders_data2=orders_data.fillna('N/A')

#checking if there is null value in orders data 
orders_data2.isnull().sum()

#Dropping rows with missing values in payments data
payments_data=payments_data.dropna()

# check if there arre any missing values
payments_data.isnull().sum()

# =============================================================================
# removing Duplicate Data
# =============================================================================

# check for duplicates in orders data
orders_data.duplicated().sum()

#remove duplicated data in orders data
orders_data=orders_data.drop_duplicates()

#check duplicates in payments data
payments_data.duplicated().sum()

#remove duplicated in payments data
payments_data=payments_data.drop_duplicates()

# =============================================================================
# Filtering data
# =============================================================================

#select subset of orders based on order status
invoiced_orders_data=orders_data[orders_data['order_status']=='invoiced']

#reset index
invoiced_orders_data=invoiced_orders_data.reset_index(drop=True)

#select subset of payments data where payment type = credit card and payment value >1000
credit_card_payments_data=payments_data[
   ( payments_data['payment_type']=='credit_card' ) & (payments_data['payment_value']>1000)
    ]

#select a subset of customers based on customers status= SP
customers_data_state=customers_data[customers_data['customer_state']== 'SP']

# =============================================================================
# Merge and join dataframes
# =============================================================================

# Merge orders data with payments data on order_id column
merged_data=pd.merge(orders_data, payments_data,on='order_id')

#join the merged data with our customers data on customer_id column
joined_data=pd.merge(merged_data,customers_data,on='customer_id')

# =============================================================================
# Data Visualization
# =============================================================================

# creating field called month_year from order_purchase_timestamp
joined_data['month_year']=joined_data['order_purchase_timestamp'].dt.to_period('M')

# creating field called week_year from order_purchase_timestamp
joined_data['week_year']=joined_data['order_purchase_timestamp'].dt.to_period('W')

# creating field called year from order_purchase_timestamp
joined_data['year']=joined_data['order_purchase_timestamp'].dt.to_period('Y')



# grouping data month_year and payment_value
grouped_data=joined_data.groupby('month_year')['payment_value'].sum()
grouped_data=grouped_data.reset_index()
# converting month_year from period to string
grouped_data['month_year']=grouped_data['month_year'].astype(str)

#creating a plot
plt.plot(grouped_data['month_year'],grouped_data['payment_value'],color='red', marker='o')
plt.ticklabel_format(useOffset= False, axis='y', style='plain')
plt.xticks(rotation = 90,fontsize=8)
plt.yticks(fontsize=8)
plt.xlabel('Month and year')
plt.ylabel('Payment Value')
plt.title('payment Value by Month and Year')

# Scatter Plot
scatter_df=joined_data.groupby('customer_unique_id').agg({'payment_value':'sum','payment_installments':'sum'})
plt.scatter(scatter_df['payment_value'],scatter_df['payment_installments'])
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value Vs Installment by Customers')
plt.show()

# creating scatter plot using seaborn
sns.set_theme(style='darkgrid')
sns.scatterplot(data=scatter_df,x='payment_value',y='payment_installments')
plt.xlabel('Payment Value')
plt.ylabel('Payment Installments')
plt.title('Payment Value Vs Installments by Cutomers')
plt.show()

# Creating a bar chart
bar_chat_df=joined_data.groupby(['payment_type','month_year'])['payment_value'].sum()
bar_chat_df=bar_chat_df.reset_index()
pivot_data=bar_chat_df.pivot(index='month_year',columns='payment_type',values='payment_value')
pivot_data.plot(kind='bar',stacked='True')
plt.ticklabel_format(useOffset=False, style='plain',axis='y')
plt.xlabel('Month of payment')
plt.ylabel('Payment Value')
plt.title('Payment per Payment Type')

# Creating a box plot
payment_values=joined_data['payment_value']
payment_types=joined_data['payment_type']

# creating a seperate box plot payment types
plt.boxplot([payment_values[payment_types == 'credit_card'],
             payment_values[payment_types == 'boleto'],
             payment_values[payment_types == 'voucher'],
             payment_values[payment_types == 'debit_card']],
         labels= ['Credit card','Boleto','Voucher','Debit Card']
            )
# set labels and titles
plt.xlabel('Payment Type')
plt.ylabel('Payment Value')
plt.title('Box Plot showing Payment Value ranges by Payment Type')
plt.tight_layout()
plt.show()
 
#Creating a subplot(3 plots in one)
fig,(ax1,ax2,ax3)=plt.subplots(3,1,figsize=(10,10))

#ax1 which is box plot
ax1.boxplot([payment_values[payment_types == 'credit_card'],
             payment_values[payment_types == 'boleto'],
             payment_values[payment_types == 'voucher'],
             payment_values[payment_types == 'debit_card']],
         labels= ['Credit card','Boleto','Voucher','Debit Card']
            )
# set labels and titles
ax1.set_xlabel('Payment Type')
ax1.set_ylabel('Payment Value')
ax1.set_title('Box Plot showing Payment Value ranges by Payment Type')

#ax2 is the stacked bar chart
pivot_data.plot(kind='bar',stacked='True',ax=ax2)
ax2.ticklabel_format(useOffset=False, style='plain',axis='y')

# set labels and titles
ax2.set_xlabel('Month of payment')
ax2.set_ylabel('Payment Value')
ax2.set_title('Payment per Payment Type by month')

#ax3 is a scatter plot
ax3.scatter(scatter_df['payment_value'],scatter_df['payment_installments'])

# set labels and titles
ax3.set_xlabel('Payment Value')
ax3.set_ylabel('Payment Installments')
ax3.set_title('Payment Value Vs Installment by Customers')
fig.tight_layout()
plt.savefig('plots.png')

