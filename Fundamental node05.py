import requests
import os

os.chdir('C:/Users/User/OneDrive/바탕 화면/dsads')

import pandas as pd

df = pd.read_csv("kospi.csv")
df.head(2)

df['Date'] = pd.to_datetime(df["Date"])

df.isna().sum()

#Pandas의 dropna 함수를 사용해서 Nan 값의 결측치를 삭제
print("삭제 전 데이터의 길이", len(df))
df = df.dropna(axis = 0).reset_index(drop=True)
print("삭제 후 데이터의 길이", len(df))
df.isna().sum()

#데이터를 그래프로 그려 확인하기
import matplotlib.pyplot as plt
from matplotlib.pylab import rcParams
plt.rcParams["figure.figsize"] = (10,5)
# Line Graph by matplotlib with wide-form DataFrame
plt.plot(df.Date, df.Close, marker='s', color='r')
plt.plot(df.Date, df.High, marker='o', color='g')
plt.plot(df.Date, df.Low, marker='*', color='b')
plt.plot(df.Date, df.Open, marker='+', color='y')
plt.title('KOSPI ', fontsize=20)
plt.ylabel('Stock', fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.legend(['Close', 'High', 'Low', 'Open'], fontsize=12, loc='best')
plt.show()

#이상한 데이터 탐색
df.loc[df.Low>df.High]

df.loc[df.Date == '2020-05-06', 'Low'] = 1903
df.loc[df.Low>df.High]

# 평균이 0이고, 표준편차가 1인 정규분포를 그립니다.
%matplotlib inline
from scipy.stats import norm
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-5, 5, 0.001)
y = norm.pdf(x,0,1)

fig, ax = plt.subplots(figsize=(9,6))
ax.fill_between(x,y,0, alpha=0.3, color='b')
ax.set_xlim([-4,4])
ax.set_title('normal distribution')
plt.show()

fig, ax = plt.subplots(figsize=(9,6))
_ = plt.hist(df.Close, 100, density=True, alpha=0.75)

from statsmodels.stats.weightstats import ztest
_, p = ztest(df.Close)
print(p)