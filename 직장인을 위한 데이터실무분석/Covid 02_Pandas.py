import pandas as pd

def create_kto_data(yy,mm):
    #1. 불러올 엑셀 파일 경로 지정
    file_path = 'C:/Users/User/OneDrive/바탕 화면/데이터실무\/datasalon-master/02_개정판/4_Tourists_Event/files/kto_{}{}.xlsx'.format(yy,mm)

    #2. 엑셀 파일 불러오기
    df = pd.read_excel(file_path, header = 1, skipfooter= 4, usecols= 'A:G')

    #3. "기준년월" 칼럼 추가
    df['기준연월'] = '{}-{}'.format(yy,mm)

    #4. "국적" 칼럼에서 대륙 제거하고 국가만 남기기
    ignore_list = ['아시아주', '미주', '구주', '대양주', '아프리카주', '기타대륙', '교포소계']
    condition = (df['국적'].isin(ignore_list) == False)
    df_country = df[condition].reset_index(drop=True)

    #5. "대륙" 칼럼 추가
    continents = ['아시아']*25 + ['아메리카']*5 + ['유럽']*23 + ['대양주']*3 + ['아프리카']*2 + ['기타대륙'] + ['교포']   
    df_country['대륙'] = continents 

    #6. 국가별 "관광객비율(%)" 컬럼 추가
    df_country['관광객비율(%)'] = round(df_country.관광 / df_country.계 * 100, 1) 

    #7. "전체비율(%)" 컬럼 추가
    tourist_sum = sum(df_country['관광'])
    df_country['전체비율(%)'] = round(df_country['관광'] / tourist_sum * 100, 1)
    
    # 8.결과 출력
    return(df_country)

kto_test = create_kto_data(2018,12)
kto_test.head()