from selenium import webdriver
driver = webdriver.Chrome('C:/Users/User/OneDrive/바탕 화면/workspace/chromedriver.exe')

import time
#인스타그램 접속하기
driver.get('http://www.instagram.com')
time.sleep(2)

#인스타그램 검색결과 URL을 만드는 함수
def insta_searching(word):
    url = 'http://www.instagram.com/explore/tags/' + word
    return url

#검색 결과 페이지 접속하기
word = '제주도맛집'
url = insta_searching(word)
driver.get(url)

#HTML에서 첫 번째 게시글 찾아 클릭하기
def select_first(driver):
    first = driver.find_element_by_css_selector("div._9AhH0")
    first.click()
    time.sleep(3)

select_first(driver)

#게시글 정보 가져오기

import re
from bs4 import BeautifulSoup
import unicodedata

def get_content(driver):
    # ① 현재 페이지 html 정보 가져오기
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    # ② 본문 내용 가져오기
    try:
        content = soup.select('div.C4VMK > span')[0].text
        content = unicodedata.normalize('NFC', content) 
    except:
        content = ' '
    # ③ 본문 내용에서 해시태그 가져오기(정규식 활용)
    tags = re.findall(r'#[^\s#,\\]+', content)  
    # ④ 작성일자 정보 가져오기
    date = soup.select('time._1o9PC.Nzb55')[0]['datetime'][:10]
    # ⑤ 좋아요 수 가져오기
    try:
        like = soup.select('div.Nm9Fw > button')[0].text[4:-1]   
    except:
        like = 0
    # ⑥ 위치정보 가져오기
    try: 
        place = soup.select('div.M30cS')[0].text
        place = unicodedata.normalize('NFC', place)
    except:
        place = ''
    # ⑦ 수집한 정보 저장하기
    data = [content, date, like, place, tags]
    return data

get_content(driver)

#다음 게시글 열기
def move_next(driver):
    
    right = driver.find_element_by_css_selector ('a.coreSpriteRightPaginationArrow')
    right.click()
    time.sleep(3)

move_next(driver)