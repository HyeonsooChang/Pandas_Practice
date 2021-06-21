import pandas as pd
import os

os.chdir('C:/Users/User/OneDrive/바탕 화면/youtube_training')

df1 = pd.read_excel('Data05.xlsx')
#불러오는 단계에서 1행을 skip 해버리기
df1 = pd.read_excel('Data05.xlsx', skiprows=1)
df1.columns
df1.shape

df2 = df1.iloc[:, 8:-2]
#transpose 함수 사용
df1.iloc[:, 8:-2].T

#stack하면 series형태로 변환/ 컬럼들이 index값으로 들어간다
df2.stack()
#dateframe으로 변경
pd.DataFrame(df2.stack())

pd.DataFrame(df2.stack()).reset_index().iloc[1:]

#키값을 고려한 처리

df3 = df1.iloc[:, 6:-2].drop(columns = ['Unnamed: 7', '판매'])
df3.set_index(['제품명']).stack()

df3.set_index(['제품명']).stack()
pd.DataFrame(df3.set_index(['제품명']).stack())
df4 = pd.DataFrame(df3.set_index(['제품명']).stack()).reset_index()

#칼럼명 바꾸기
df5 = df4.rename(columns = {'level_1': '날짜명', 0 : '재고량'})
df1.columns
#df1(원본데이터)와 합치기
df6 = df1[['카테고리명', '자재그룹', '제품코드', '자재그룹명', '제품명','안전재고', ' 분류']]

df7 = pd.merge(df6, df5, how = 'right')
df7.to_excel('total_data.xlsx')