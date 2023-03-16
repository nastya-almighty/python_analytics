#!/usr/bin/env python
# coding: utf-8

# In[22]:


import pandas as pd


# # Задание 1

# ## 1

# In[23]:


houses = pd.read_csv("C:/Users/Acer/Desktop/geekbrains/питон аналитик/kc_house_data.csv")
houses.head()


# ## 2

# In[24]:


houses['delta_renovated'] = houses['yr_renovated'] - houses['yr_built']
houses.loc[houses['yr_renovated'] == 0, 'delta_renovated'] = 0
houses.head()


# ## 3

# In[25]:


houses['year_sold'] = houses['date'].str[:4]
houses['month_sold'] = houses['date'].str[5:7]
houses.head()


# In[26]:


houses['year_sold'] = pd.to_datetime(houses['date']).dt.year
houses['month_sold'] = pd.to_datetime(houses['date']).dt.month
houses.head()


# В первом случае месяц почему-то выходил 20 или 22, например, хотя, глядя на таблицу, кажется, что дата записывалась в формате ГГГГ-ММ-ДД.

# ## 4

# In[28]:


houses.drop(columns = ['date', 'zipcode', 'lat', 'long'], inplace = True)
houses.head()


# # Задание 2

# ## 1

# In[29]:


clients = pd.DataFrame({
    'client_id': [1459, 4684, 3498, 3942, 4535, 2308, 2866, 2765, 1472, 4236, 2295,
                  939, 3840, 280, 20, 4332, 3475, 4213, 3113, 4809, 2134, 2242,
                  2068, 4929, 1384, 1589, 3317, 2260, 1727, 1764, 1611, 1474],
    'house_id': [8965450190, 6823100225, 5104540330, 2131701075, 1522700060,
                 1189000207, 6821600300, 7137950720, 9510920050, 6131600255,
                 5428000070, 1788800910, 8100400160, 3123049142, 6306800010,
                 5083000375, 7920100025, 1951600150, 809001400, 339600110,
                 1622049154, 1099600250, 8563000110, 2768100205, 3995700435,
                 8861700030, 3303980210, 7731100066, 8146100580, 825069097,
                 3889100029, 9524100196]
})


# ## 2

# In[32]:


joined_df = clients.set_index('house_id').join(houses.set_index('id'), how='inner')
joined_df.head()


# ## 3

# In[34]:


merged_df = clients.merge(houses, left_on='house_id', right_on='id', how='inner')
merged_df.head()


# # Задание 3

# ## 1

# In[41]:


p_bedrooms = houses.pivot_table(index = 'bedrooms', values = 'price', 
                                aggfunc='mean')
average_cost = p_bedrooms.sort_values('price')
average_cost.head()


# ## 2

# In[39]:


p_condition = houses.pivot_table(index = 'condition', values = 'price', 
                                 aggfunc = ['min', 'mean', 'max'])
p_condition.head()


# ## 3

# In[45]:


p_views = houses.pivot_table(index = 'waterfront', columns = 'view', values = 'id',
                             aggfunc = 'count', fill_value = 0)
p_views.head()


# In[ ]:




