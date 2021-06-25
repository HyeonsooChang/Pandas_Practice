import pandas as pd
import matplotlib.pyplot as plt

from matplotlib import font_manager, rc
import platform
if platform.system() == 'Windows':
    path = 'c:/Windows/Fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname = path).get_name()
    rc('font', family = font_name)
elif platform.system() == 'Darwin':
    rc('font', family = 'AppleGothic')
else:
    print('Check your OS system')

df = pd.read_excel('C:/Users/User/OneDrive/바탕 화면/workspace/Pandas/Pandas_Practice/직장인을 위한 데이터실무분석/youtube_rank.xlsx')
df.head()
df.tail()

df['subscriber'][0:10]
df['subscriber'].str.replace('만', '0000')[0:10]

#replaced_subscriber 시리즈 문자열 변경하기
df['replaced_subscriber'] = df['subscriber'].str.replace('만', '0000')
df.head()

df.info()
#시리즈 데이터 타입 변환하기
df['replaced_subscriber'] = df['replaced_subscriber'].astype('int')
df.info()

#카테고리 별 구독자 수, 채널 수 피봇테이블 생성하기
pivot_df = df.pivot_table(index = 'category', values = 'replaced_subscriber', aggfunc= ['sum', 'count'])
pivot_df.head()

#데이터프레임의 칼럼명 변경하기
pivot_df.columns = ['subscriber_sum', 'category_count']
pivot_df.head()

#데이터프레임의 인덱스 초기화하기
pivot_df = pivot_df.reset_index()
pivot_df.head()

#데이터프레임을 내림차순 정렬하기
pivot_df = pivot_df.sort_values(by = 'subscriber_sum', ascending= False)
pivot_df.head()

#카테고리별 구독자 수 시각화하기
plt.figure(figsize = (30,10))
plt.pie(pivot_df['subscriber_sum'], labels=pivot_df['category'], autopct='%1.1f%%')
plt.show()

#카테고리별 채널 수 시각화하기
pivot_df = pivot_df.sort_values(by = 'category_count', ascending= False)
plt.figure(figsize = (30,10))
plt.pie(pivot_df['category_count'], labels = pivot_df['category'], autopct='%1.1f%%')