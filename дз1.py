#!/usr/bin/env python
# coding: utf-8

# ## Задание 2

# In[5]:


def stock_total(fruits):
    total = 0
    for v in fruits.values():
        total += v
    return total


# In[6]:


fruits = {"яблоки": 10, "персики": 20, "груши": 15, "манго": 5}


# In[7]:


stock_total(fruits)


# ## Задание 3

# In[8]:


ad_expenses = [100, 125, -90, 345, 655, -1, 0, 200]


# In[12]:


ad_expenses_final = [i if i > 0 else 0 for i in ad_expenses]
ad_expenses_final


# In[13]:


sum(ad_expenses_final)


# Мне кажется, что, вероятнее всего, отрицательные числа занесены по ошибке, когда там должны были быть положительные. Тогда получается немножко по-другому:

# In[14]:


ad_expenses_final2 = [abs(i) for i in ad_expenses]
ad_expenses_final2


# In[15]:


sum(ad_expenses_final2)


# ## Задание 4

# ### 1

# In[22]:


dates = ['2021-09-14', '2021-12-15', '2021-09-08', '2021-12-05', '2021-10-09', '2021-09-30', '2021-12-22', '2021-11-29', '2021-12-24', '2021-11-26', '2021-10-27', '2021-12-18', '2021-11-09', '2021-11-23', '2021-09-27', '2021-10-02', '2021-12-27', '2021-09-20', '2021-12-13', '2021-11-01', '2021-11-09', '2021-12-06', '2021-12-08', '2021-10-09', '2021-10-31', '2021-09-30', '2021-11-09', '2021-12-13', '2021-10-26', '2021-12-09']
prices = [1270, 8413, 9028, 3703, 5739, 4095, 295, 4944, 5723, 3701, 4471, 651, 7037, 4274, 6275, 4988, 6930, 2971, 6592, 2004, 2822, 519, 3406, 2732, 5015, 2008, 316, 6333, 5700, 2887]


# In[116]:


profits_nov = sum([prices[i] for i in range(len(dates)) if dates[i].startswith('2021-11')])
profits_nov


# In[127]:


def profits_month(dates: str, profits: int) -> {str, int}:
    profits = {}
    for i in range(len(dates)):
        month = dates[i][5:7]
        if month not in profits:
            profits[month] = prices[i]
        else:
            profits[month] += prices[i]
    return profits


# In[128]:


profits_month(dates, prices)


# In[ ]:




