#!/usr/bin/env python
# coding: utf-8

# # Project Stanley Exploratory Data Analysis

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns #visualisation
import matplotlib.pyplot as plt #visualisation
get_ipython().run_line_magic('matplotlib', 'inline')
sns.set(color_codes=True)


# In[3]:


sophos_computers = pd.read_csv('computers.csv')


# In[4]:


sophos_computers.head()


# In[6]:


sophos_computers.shape


# In[7]:


sophos_computers.info()


# In[9]:


sophos_computers.dtypes


# In[10]:


#drop irelevent collumns
sophos_computers.drop([])


# In[11]:


#renaming columns to get a better understanding of data
#sophos_computers.rename(columns = {'': ' '})
#sophos_computer.head()


# In[12]:


#total numbers of rows and columns 
#sophos_computers.shape


# In[15]:


## Rows containing duplicate data
duplicate_rows_sophos_computers = sophos_computers[sophos_computers.duplicated()]
print("number of duplicate rows: ",duplicate_rows_sophos_computers.shape)


# In[ ]:


# Dropping the duplicates 
#sophos_computers = sophos_computers.drop_duplicates()
#sophos_computers.head(5)


# In[16]:


# Counting the number of rows after removing duplicates.
#df.count()


# In[17]:


# Finding the null values.
#print(df.isnull().sum())


# In[18]:


# Dropping the missing values.
#df = df.dropna() 
#df.count()


# In[19]:


# After dropping the values
#print(df.isnull().sum()) 


# In[20]:


#if we want to detect outliers a box plot is the best option
#sns.boxplot(x=df[‘Price’])


# In[21]:


#Q1 = df.quantile(0.25)
#Q3 = df.quantile(0.75)
#IQR = Q3 — Q1
#print(IQR)


# In[22]:


#df = df[~((df < (Q1–1.5 * IQR)) |(df > (Q3 + 1.5 * IQR))).any(axis=1)]
#df.shape


# 9. Plot different features against one another (scatter), against frequency (histogram)
# 

# Histogram

# In[23]:


## Plotting a Histogram
#df.Make.value_counts().nlargest(40).plot(kind=’bar’, figsize=(10,5))
#plt.title(“Number of cars by make”)
#plt.ylabel(‘Number of cars’)
#plt.xlabel(‘Make’);


# Heat Maps

# In[24]:


# Finding the relations between the variables.
#plt.figure(figsize=(20,10))
#c= df.corr()
#sns.heatmap(c,cmap=”BrBG”,annot=True)
#c


# Scatterplot

# In[ ]:


## Plotting a scatter plot
#fig, ax = plt.subplots(figsize=(10,6))
#ax.scatter(df[‘HP’], df[‘Price’])
#ax.set_xlabel(‘HP’)
#ax.set_ylabel(‘Price’)
#plt.show()

