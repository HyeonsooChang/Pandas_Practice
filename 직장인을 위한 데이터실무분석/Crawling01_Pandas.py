#크롬드라이버 실행
from selenium import webdriver
driver = webdriver.Chrome('C:/Users/User/OneDrive/바탕 화면/workspace/chromedriver.exe')

#URL 접속
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)

#웹페이지의 HTML 다운로드
from bs4 import BeautifulSoup
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#100개의 노래 태그 찾기
songs = soup.select('table > tbody > tr')
print(len(songs))
print(songs[0])

#한 개의 곡 정보 지정하기
song = songs[0]

#곡 제목 찾기 a는 태그명
title = song.select('a')
len(title)

#곡 제목 찾기 2/ 원하는 정보의 태그를 사용하는 다른 정보들이 많기 때문에
title = song.select('span > a')
len(title)

#곡 제목 찾기 3
title = song.select('div.ellipsis.rank01 > span > a')
len(title)

#곡 제목 가져오기
title = song.select('div.ellipsis.rank01 > span > a')[0].text
title

#가수 찾기
singer = song.select('div.ellipsis.rank02 > a')
len(singer)
#가수 정보 가져오기
singer = song.select('div.ellipsis.rank02 > a')[0].text
singer

#멜론 100위 노래순위 정보 가져오기
for song in songs:
    title = song.select('div.ellipsis.rank01 > span > a')[0].text
    singer = song.select('div.ellipsis.rank02 > a')[0].text
    print(title, singer, sep ='|')


#멜론 상위 100곡 크롤링(selenium만 활용)
driver = webdriver.Chrome('C:/Users/User/OneDrive/바탕 화면/workspace/chromedriver.exe')
url = 'http://www.melon.com/chart/index.htm'
driver.get(url)

songs = driver.find_elements_by_css_selector('table> tbody >tr')
for song in songs:
    title = song.find_elements_by_css_selector('div.ellipsis.rank01 > span > a')[0].text
    singer = song.find_elements_by_css_selector('div.ellipsis.rank02 > a')[0].text
    print(title, singer, sep ='|')
