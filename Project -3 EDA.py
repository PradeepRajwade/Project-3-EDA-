#!/usr/bin/env python
# coding: utf-8

# # Project 3-Exploratory Data Analysis

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 


# Data uploding

# In[3]:


data=pd.read_csv("housing_data.csv")


# To Check top 5 columns of data

# In[4]:


data.head()


# To check bottom 5 columns of given data

# In[5]:


data.tail()


# To check number of rows and columns in given dataset

# In[6]:


data.shape


# Given data set have 1460 rows and 81 columns 

# In[7]:


data.info()


# In[8]:


data.describe()


# Null value verification

# In[9]:


data.isnull().sum()


# Columns prsent in Data set

# In[10]:


data.columns


# In[11]:


data.head(10).T


# #Duplicate rows 

# In[12]:


data.duplicated().sum()


# In[13]:


data.columns


# In[14]:


rename_column ={'LotShape':'Shape_of_property',}


# In[15]:


data1=data.rename(columns=rename_column)


# In[16]:


data1


# In[17]:


data['Alley'].nunique()


# In[18]:


data.count()


# In[19]:


data.sum()


# In[20]:


data.duplicated().sum()


# In[21]:


data["MSZoning"].unique()


# In[22]:


import seaborn as sns 


# In[23]:


sns.boxplot(x=data["LotArea"])
plt.show()


# In[24]:


# Distribution of the prices
plt.figure(figsize=(12,5))
sns.set_theme(style="darkgrid")
sns.distplot(data['SalePrice'], color=('r'))
plt.ylabel('SalePrice', fontsize=14)
plt.xlabel('LotArea', fontsize=14)
plt.title("Price variation ", fontsize = 15)
plt.show()


# In[25]:


data.columns


# In[26]:


data.rename({'BldgType':'Building Type'})


# In[27]:


pd.set_option("display.max_columns",None)


# In[28]:


data


# In[29]:


data.rename({'BldgType':'Building Type'})
data


# In[30]:


data["MSSubClass"].replace({'SC60':"exc"},inplace=True)


# In[31]:


data


# Year Built vs Price of Property 

# In[32]:


plt.figure(figsize=(12,8))
sns.set_theme(style="darkgrid")
sns.histplot(data["YearBuilt"],color="b")
plt.show()


# In[33]:


data["Alley"].unique()


# In[ ]:





# In[34]:


plt.scatter(data["SalePrice"],data["OverallCond"],color="red")
plt.ylabel("Overall_condition",fontsize=12)
plt.xlabel("Sales price",fontsize=12)
sns.set_theme(style="darkgrid")
plt.title("Overall_condition vs Sales price")
plt.show()


# In[35]:


sns.lineplot(y="LotArea",x="SalePrice",data=data)
plt.title("Variation of price with lot area")
plt.ylabel("Lot Area")
plt.xlabel("Sales price")
plt.show()


# In[36]:


sns.boxplot(x=data["SalePrice"])
plt.show()


# In[37]:


from statistics import mean
sns.pointplot(y= 'GrLivArea', x = 'SalePrice', data=data, estimator=np.mean,color="green")

# Add axis and labels
plt.ylabel("LIVING AREA")
plt.xlabel('Average Price')
plt.title('Average Price by GRliving area')
plt.show()


# In[42]:


plt.figure(figsize=(12,8))
sns.set_theme(style="ticks")
sns.histplot(data["LotFrontage"],color="orange",)
plt.show()


# In[ ]:





# In[ ]:




