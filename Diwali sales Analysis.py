#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[4]:


df=pd.read_csv(r'D:\IIT MADRAS\PROJECT\Diwali sales\Diwali Sales Data.csv',encoding = 'unicode_escape')


# In[6]:


df.shape


# In[13]:


df.head()


# In[14]:


df.info()


# In[17]:


df.drop(['Status','unnamed1'],axis=1,inplace=True)


# In[18]:


df.info()


# In[20]:


pd.isnull(df).sum()


# In[21]:


df.dropna(inplace=True)


# In[23]:


df.shape


# In[25]:


pd.isnull(df).sum()


# In[26]:


df['Amount'] = df['Amount'].astype('int')


# In[27]:


df['Amount'].dtypes


# In[32]:


df.rename(columns= {'Marital_Status': 'Shaadi'})


# In[33]:


df.describe()


# In[34]:


df[['Age','Orders','Amount']].describe()


# # Exploratory Data Analysis

# In[ ]:


#Gender


# In[35]:


df.columns


# In[36]:


ax = sns.countplot(x = 'Gender',data=df)

for bars in ax.containers:
    ax.bar_label(bars)
    


# In[37]:


sns.countplot(x = 'Gender',data=df)


# In[41]:


df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[42]:


sales_gen = df.groupby(['Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x = 'Gender', y = 'Amount',data=sales_gen)


# In[ ]:


#From above graphs we can conclude that females are the most buyers and even they have more purchasing powers than men


# In[46]:


sns.countplot(data=df,x='Age Group',hue='Gender')


# In[48]:


ax=sns.countplot(data=df,x='Age Group',hue='Gender')

for bars in ax.containers:
    ax.bar_label(bars)


# In[49]:


df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)


# In[50]:


Sales_age = df.groupby(['Age Group'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.barplot(x='Age Group',y='Amount',data=Sales_age)


# In[ ]:


#From above graph we can see that most of the buyers are from age group 26-35 yrs female


# In[74]:


sales_state = df.groupby(['State'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Orders',data=sales_state)


# In[75]:


sales_state_amount = df.groupby(['State'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(x='State',y='Amount',data=sales_state_amount)


# In[ ]:


#Most of the orders and revenue is generated from Uttar Pradesh,Maharashtra and Karnataka respectively.


# In[85]:


ax= sns.countplot(data=df,x='Marital_Status')

sns.set(rc={'figure.figsize':(7,5)})
for bars in ax.containers:
    ax.bar_label(bars)


# In[91]:


sales_state = df.groupby(['Marital_Status','Gender'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(10,5)})
sns.barplot(data=sales_state,x='Marital_Status',y='Amount',hue='Gender')


# In[ ]:


#From the above graph we can see that married womans have more purchasing powers.


# In[94]:


sns.set(rc={'figure.figsize':(17,5)})
ax = sns.countplot(data=df,x='Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[96]:


sales_state=df.groupby(['Occupation'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='Occupation',y='Amount')


# In[ ]:


#From above graph we can see that most buyers work in IT sector,Healthcare and Aviation.


# In[ ]:


Product category


# In[103]:


ax=sns.countplot(data=df,x='Product_Category')
sns.set(rc={'figure.figsize':(23,5)})

for bars in ax.containers:
    ax.bar_label(bars)


# In[110]:


sales_state=df.groupby(['Product_Category'],as_index=False)['Amount'].sum().sort_values(by='Amount',ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data=sales_state,x='Product_Category',y='Amount')


# In[ ]:


#From the abocve graph we can see that people spend the most on Food followed by clothing and electronic gadgets.


# In[112]:


sales_state = df.groupby(['Product_ID'],as_index=False)['Orders'].sum().sort_values(by='Orders',ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=sales_state,x='Product_ID',y='Orders')


# # Married Women age group 26-35 yrs from UP, Maharsahtra and Karnataka working in IT, Healthcare and Aviation are more likely to buy products from Food, Clothing and Electronic category.
