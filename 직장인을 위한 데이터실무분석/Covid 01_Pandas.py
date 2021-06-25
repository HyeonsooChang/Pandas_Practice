import pandas as pd
import os

os.chdir('C:/Users/User/OneDrive/바탕 화면/데이터실무/datasalon-master/02_개정판/4_Tourists_Event/files')

kto_201901 = pd.read_excel('kto_201901.xlsx',
                           header=1, usecols='A:G', skipfooter= 4)
kto_201901.head()
kto_201901.tail()

#데이터 전처리
kto_201901.info()
kto_201901.describe()

#각 칼럼에서 0인 부분을 필터링
condition = (kto_201901['관광'] == 0) \
    | (kto_201901['상용'] == 0) \
    | (kto_201901['공용'] == 0) \
    | (kto_201901['유학/연수'] == 0)

kto_201901[condition]

#기준년월 칼럼 생성
kto_201901['기준년월'] = '2019-01'
kto_201901.head()

#unique() 함수 활용
kto_201901['국적'].unique()

#대륙 목록 만들기
continents_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙', '교포소계']
continents_list

#대륙 목록에 해당하는 값 제외
condition = (kto_201901.국적.isin(continents_list) == False)
kto_201901_country = kto_201901[condition]
kto_201901_country['국적'].unique()

kto_201901_country.head()

#인덱스 재설정
kto_201901_country_newindex = kto_201901_country.reset_index(drop=True)
kto_201901_country_newindex.head()

#대륙 칼럼값 만들기
continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['오세아니아']*3 \
+ ['아프리카']*2 + ['기타대륙'] + ['교포']
print(continents)

#대륙칼럼 생성
kto_201901_country_newindex['대륙'] = continents
kto_201901_country_newindex.head()

#관광객비율(%) 칼럼 생성
kto_201901_country_newindex['관광객비율(%)'] = round(kto_201901_country_newindex['관광'] / kto_201901_country_newindex['계'] * 100, 1)
kto_201901_country_newindex.head()

#pivot_table()함수 활용
kto_201901_country_newindex.pivot_table(values='관광객비율(%)', index='대륙', aggfunc='mean')

#중국 국적만 필터링
condition = (kto_201901_country_newindex['국적'] == '중국')
kto_201901_country_newindex[condition]

#기준년월별로 전체 외국인 관광객 대비 국적별 관광객 비율 살펴보기
tourist_sum = sum(kto_201901_country_newindex['관광'])
tourist_sum

#전체비율(%) 칼럼 생성
kto_201901_country_newindex['전체비율(%)'] = round(kto_201901_country_newindex['관광']/ tourist_sum * 100,1)
kto_201901_country_newindex
