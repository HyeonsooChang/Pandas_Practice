#벅스 사이트에 접속하기
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/User/OneDrive/바탕 화면/workspace/chromedriver.exe')

#URL 접속
url = 'http://music.bugs.co.kr/chart'
driver.get(url)

#웹페이지의 HTML 다운로드
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#tr태그로 곡 정보 찾기 1
songs = soup.select('tr')
print(len(songs))

#tr태그로 곡 정보 찾기 3
songs = soup.select('table > tbody > tr')
print(len(songs))

songs = soup.select('table > tbody > tr')
print(len(songs))

songs = soup.select('table.byChart > tbody > tr')
print(len(songs))

#songs 태그 중 첫번째 태그 출력하기
print(songs[0])

#한 개의 곡 정보 지정하기
song = songs[0]

#벅스 사이트에서 곡 제목 찾기1
title = song.select('a')
len(title)

#벅스 사이트에서 곡 제목 찾기2
title = song.select('p > a')
len(title)

#벅스 사이트에서 곡 제목 찾기3
title = song.select('p.title > a')
len(title)

#벅스 사이트에서 곡 제목 텍스트 출력하기
title = song.select('p.title > a')[0].text
title

#가수 이름 텍스트 출력하기
singer = song.select('p.artist > a')[0].text
singer

#벅스 100위 노래 순위 가져오기
songs = soup.select('table.byChart > tbody > tr')

for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    print(title, singer, sep = '|')

#반복문을 이요해 곡과 가수명을 song_data에 저장하기
song_data =[]
songs = soup.select('table.byChart > tbody > tr')
rank = 1
for song in songs:
    title = song.select('p.title > a')[0].text
    singer = song.select('p.artist > a')[0].text
    song_data.append(['Bugs', rank, title, singer])
    rank = rank + 1

import pandas as pd
columns = ['서비스', '순위', '타이틀', '가수']
pd_data = pd.DataFrame(song_data, columns = columns)
pd_data.head()

