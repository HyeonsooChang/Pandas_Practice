import os
import pandas as pd

os.chdir('C:/Users/User/OneDrive/바탕 화면/데이터실무/datasalon-master/02_개정판/2_Data_Analysis_Basic/files')

sample_1 = pd.read_excel('sample_1.xlsx', 
                        header = 1, 
                        skipfooter = 2, 
                        usecols = 'A:C')
sample_1.head(3)

sample_1
#칼럼 선택
sample_1['입국객수']
#칼럼 추가
sample_1['기준년월'] = '2019-12'
sample_1

#데이터 필터링
#필터링 실습 1
condition = (sample_1['성별'] == '남성')
condition

sample_1[condition]

#필터링 실습 2
condition = (sample_1['입국객수'] >= 150000)
sample_1[condition]

#필터링 실습 3 (and)
condition = (sample_1['입국객수'] >= 150000) & (sample_1['성별'] == '남성')

#코드의 가독성 높이기
condition = (sample_1['입국객수'] >= 150000) \
    & (sample_1['성별'] == '남성')
sample_1[condition]

#필터링 실습 4 (or)
condition = (sample_1['입국객수'] >= 150000) \
    | (sample_1['성별'] == '남성')
sample_1[condition]

#간단히 표시 #isin()함수는 찾고싶은 값 추출
condition = sample_1['국적코드'].isin(['A01', 'A18'])
condition
sample_1[condition]

#찾고 싶은 값 이외의 것들
sample_1[condition==False]

# 데이터 통합

code_master = pd.read_excel('sample_codemaster.xlsx')
code_master

#데이터 옆으로 통합(left 조건)
sample_1_code = pd.merge(left=sample_1, right=code_master,how='left', left_on='국적코드', right_on='국적코드')

sample_1_code

#데이터 통합(아래로) - 시계열 데이터에 주로 사용됨.
sample_2 = pd.read_excel('sample_2.xlsx', header=1,
                         skipfooter=2, usecols='A:C')

sample_2['기준연월'] = '2019-12'

sample_2_code = pd.merge(left=sample_2,
                         right=code_master, how='left',
                         left_on='국적코드', right_on='국적코드')

sample_2_code
sample_1_code

sample = sample_1_code.append(sample_2_code, ignore_index= True)
sample


#피봇 테이블 활용
sample_pivot = sample.pivot_table(values='입국객수',
                                  index='국적명', columns='기준년월', aggfunc='mean')
sample_pivot
