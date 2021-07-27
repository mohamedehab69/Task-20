#!/usr/bin/env python
# coding: utf-8

# # Ecommerce Purchases Exercise - Solutions
# 
# In this Exercise you will be given some Fake Data about some purchases done through Amazon! Just go ahead and follow the directions and try your best to answer the questions and complete the tasks. Feel free to reference the solutions. Most of the tasks can be solved in different ways. For the most part, the questions get progressively harder.
# 
# Please excuse anything that doesn't make "Real-World" sense in the dataframe, all the data is fake and made-up.
# 
# Also note that all of these questions can be answered with one line of code.
# 
# **Import pandas and read in the 'data/Ecommerce Purchases.csv' file and set it to a DataFrame called ecom.**

# In[1]:


import pandas as pd


# In[2]:


df=pd.read_csv("Ecommerce Purchases.csv")


# **Check the head of the DataFrame.**

# In[4]:


df


# In[4]:


df.head()


# **How many rows and columns are there?**

# In[5]:


df.info()


# **What is the average Purchase Price?**

# In[5]:


df["Purchase Price"].mean()


# **What were the highest and lowest purchase prices?**

# In[6]:


df["Purchase Price"].max()


# In[7]:


df["Purchase Price"].min() 


# **How many people have English 'en' as their Language of choice on the website?**
# 

# In[8]:


len (df[df['Language']=='en'])


# **How many people have the job title of "Lawyer" ?**
# 

# In[9]:


len(df[df['Job']=="Lawyer"])


# **How many people made the purchase during the AM and how many people made the purchase during PM ?**
# 
# **(Hint: Check out [value_counts()](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.Series.value_counts.html) )**

# In[10]:


df[['AM or PM']].value_counts()


# **What are the 5 most common Job Titles?**

# In[40]:


df['Job'].sort_values(ascending=False).unique()[:5]


# In[ ]:





# **Someone made a purchase that came from Lot: "90 WT" , what was the Purchase Price for this transaction?**

# In[41]:


df[df["Lot"]=="90 WT"]["Purchase Price"]


# **What is the email of the person with the following Credit Card Number: 4926535242672853**

# In[42]:


df[df["Credit Card"]==4926535242672853]["Email"]


# **How many people have American Express as their Credit Card Provider *and* made a purchase above $95 ?**

# In[7]:


sety=df[df["CC Provider"]=="American Express"]
sety[sety["Purchase Price"]>95].count()


# **Hard: How many people have a credit card that expires in 2025?**

# In[10]:


df[df["CC Exp Date"].apply(lambda x: x[3:]=='25')].count()
sum(df["CC Exp Date"].apply(lambda x: x[3:])=='25')


# **Hard: What are the top 5 most popular email providers/hosts (e.g. gmail.com, yahoo.com, etc...)**

# In[11]:


df["Email"].str.split('@').str[1].value_counts().head(5)


# # Great Job!
