#!/usr/bin/env python
# coding: utf-8

# ### 판다스 프로파일링(Pandas-Profiing)
# 
# - 방대한 양의 데이터를 가진 데이터프레임을 .profile_report()라는 한 줄의 명령으로 탐색하는 패키지

# In[1]:


import pandas as pd
import pandas_profiling
import os


# In[3]:


os.chdir('C:/Users/User/OneDrive/바탕 화면')


# In[5]:


data = pd.read_csv('spam.csv', encoding= 'latin1''')


# In[6]:


data[:5]


# 리포트 생성하기

# In[ ]:


pr = data.profile_report()  #프로파일링 결과 리포트를 pr에 저장
#data.profile_report() -> 결과 바로 보기


# In[9]:


pr


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




