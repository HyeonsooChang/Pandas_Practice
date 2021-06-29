
#크롤링 결과 중 해시태그 불러오기
import pandas as pd
raw_total = pd.read_excel('C:/Users/User/OneDrive/바탕 화면/데이터실무/datasalon-master/02_개정판/5_Jeju_Hotplace/files/1_crawling_raw.xlsx')
raw_total['tags'][:3]


#해시태그를 통합저장
tags_total = []

for tags in raw_total['tags']:
    tags_list= tags[2:-2].split("', '")
    for tag in tags_list:
        tags_total.append(tag)

#빈도수 집계(Counter)
from collections import Counter
tag_counts = Counter(tags_total)

#가장 많이 사용된 해시태그 확인
tag_counts.most_common(50)

#데이터 정제
STOPWORDS = ['#일상', '#선팔', '#제주도', '#jeju', '#반영구', '#제주자연눈썹',
'#서귀포눈썹문신', '#제주눈썹문신', '#소통', '#맞팔']

tag_total_selected = []
for tag in tags_total:
    if tag not in STOPWORDS:
        tag_total_selected.append(tag)

tag_counts_selected = Counter(tag_total_selected)
tag_counts_selected.most_common(50)


#시각화 라이브러리 임포트 및 글꼴 설정
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import font_manager, rc
import sys

if sys.platform in ["win32", "win64"]:
    font_name = "malgun gothic"
elif sys.platform == "darwin":
    font_name = "AppleGothic"

rc('font',family=font_name)

#데이터 준비
tag_counts_df = pd.DataFrame(tag_counts_selected.most_common(30))
tag_counts_df.columns = ['tags', 'counts']

#막대 차트 그리기
plt.figure(figsize= (10,10))
sns.barplot(x = 'counts', y = 'tags', data = tag_counts_df)

#워드 클라우드 라이브러리 불러오기
import matplotlib.pyplot as plt
from wordcloud import WordCloud    # 에러시  ! pip install wordcloud 실행
import platform

if platform.system() == 'Windows':   #윈도우의 경우
    font_path = "c:/Windows/Fonts/malgun.ttf"
elif platform.system() == "Darwin":   #Mac 의 경우
    font_path = "/Users/$USER/Library/Fonts/AppleGothic.ttf"

# 예제 5-23 워드클라우드 만들기
wordcloud=WordCloud(font_path= font_path, 
                    background_color="white",
                    max_words=100,
                    relative_scaling= 0.3,
                    width = 800,
                    height = 400
                 ).generate_from_frequencies(tag_counts_selected)  
plt.figure(figsize=(15,10))
plt.imshow(wordcloud)
plt.axis('off')
plt.savefig('C:/Users/User/OneDrive/바탕 화면/workspace/Pandas/Pandas_Practice/직장인을 위한 데이터실무분석/2_tag-wordcloud.png')