import pandas as pd

#파일 불러오기
df = pd.read_excel('C:/Users/User/OneDrive/바탕 화면/데이터실무\/datasalon-master/02_개정판/4_Tourists_Event/files/kto_total.xlsx')
df.head()

from matplotlib import font_manager, rc
import platform 

if platform.system() == 'Windows': 
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else: 
    print('Check your OS system')

import matplotlib.pyplot as plt

condition = (df['국적'] =='중국')
df_filter = df[condition]
df_filter.head()

#시계열 그래프 그리기1
plt.plot(df_filter['기준연월'], df_filter['관광'])
plt.show()


# 예제 4-46 시계열 그래프 그리기 2
## 그래프 크기 조절 
plt.figure(figsize = (12, 4))

## 그래프 내용 설정 
plt.plot(df_filter['기준연월'], df_filter['관광'])

## 그래프 타이틀, X축, Y축 이름 달기 
plt.title('중국 국적의 관광객 추이')
plt.xlabel('기준년연월')
plt.ylabel('관광객수')

## x 축 눈금 값 설정 
plt.xticks(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01', '2020-01'])

## 그래프 표현하기 
plt.show()

#상위리스트 5개국
cntry_list = ['중국', '일본', '대만', '미국', '홍콩']


for cntry in cntry_list:
    condition = (df['국적'] ==cntry)
    df_filter = df[condition]

    plt.figure(figsize = (12,4))

    plt.plot(df_filter['기준연월'], df_filter['관광'])

    plt.title('{} 국적의 관광객 추이'.format(cntry))
    plt.xlabel('기준연월일')
    plt.ylabel('관광객수')
    
    plt.xticks(['2010-01', '2011-01', '2012-01', '2013-01', '2014-01', '2015-01', '2016-01', '2017-01', '2018-01', '2019-01', '2020-01'])

    plt.show()