#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[39]:


data=pd.read_csv("dementia_dataset.csv")


# In[40]:


data.isnull().sum()


# In[41]:


data.dropna(inplace=True)


# In[42]:


import matplotlib.pyplot as lib


# In[43]:


import sklearn as sk


# In[44]:


data.head(10)


# In[45]:


data['Group'].unique()


# In[46]:


df2 = data.loc[data['Group'] == 'Converted']


# In[47]:


data=data.drop(df2.index)

df2.head(10)


# In[48]:


df2['Last_Visit'] = df2.groupby('Subject ID')['Visit'].transform('max')
df2.loc[df2['Visit'] < df2['Last_Visit'], 'Group'] = 'Nondemented'
df2.loc[df2['Visit'] == df2['Last_Visit'], 'Group'] = 'Demented'
df2.drop('Last_Visit', axis=1, inplace=True)
df2.head(5)


# In[49]:


frames= [data, df2]
df = pd.concat(frames)

df['Group'].unique()


# In[50]:


df.rename(columns={'M/F': 'Gender'}, inplace=True)

print(df.columns)

# Drop unnecessary columns from the DataFrame if they exist
columns_to_drop = ['Subject ID', 'MRI ID', 'Hand', 'Visit', 'MR Delay']
existing_columns_to_drop = [col for col in columns_to_drop if col in df.columns]
df.drop(columns=existing_columns_to_drop, inplace=True)


# In[51]:


import seaborn as sns

sns.countplot(data=df, x='Group', palette='Set2').set(title = 'Dementia Group');


# In[58]:


sns.countplot(data=df, x='Group', palette='Set2', hue='Gender').set(title = 'Dementia Group by Gender');


# In[59]:


sns.displot(data=df, x='EDUC', col='Gender', palette='Set2', hue='Group', kind='kde')


# In[60]:


sns.displot(data=df, x='Age', hue='Group', kind="kde", palette='Set2');


# In[61]:


sns.heatmap(df.corr(numeric_only=True), vmin=-1, cmap='coolwarm');


# In[62]:


sns.scatterplot(data=df, x='MMSE', y='CDR', palette='Set2', hue='Group');


# In[ ]:





# In[ ]:




