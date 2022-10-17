import requests
from bs4 import BeautifulSoup
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/a
#*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a
#*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[5]/td[2]/a
#//*[@id="content"]/div/div/div[1]/table/tbody/tr[4]/td
url = 'https://see.knu.ac.kr/content/board/notice.html'

response = requests.get(url)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://see.knu.ac.kr/content/board/notice.html')#웹페이지를 열어줌
driver.implicitly_wait(3)#3초안에 웹페이지를 load 하면 바로 넘어가거나 3초를 기다림.
driver.find_element(By.XPATH,r'//*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/a').click()#해당 게시물을 클릭한다.
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)
element = driver.find_element(By.CLASS_NAME,'contentview')
element_png = element.screenshot_as_png
with open('test.png','wb') as file:
    file.write(element_png)
driver.back()
driver.find_element(By.XPATH,r'//*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
element = driver.find_element(By.CLASS_NAME,'contentview')
element_png1 = element.screenshot_as_png
with open('test1.png','wb') as file:
    file.write(element_png1)

if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')#한글 가져올때,깨질떄, utf-8로 설정해줘야 함
    title = soup.select_one('#content > div > div > div.board_list > div.board_body > table > tbody > tr:nth-child(5) > td.left > a')
    # content > div > div > div.board_list > div.board_body > table > tbody > tr:nth-child(6) > td.left > a

    for i in range(1,10):
        title = soup.select_one('#content > div > div > div.board_list > div.board_body > table > tbody > tr:nth-child('+str(i)+') > td.left > a')
        print(title.get_text())

else :
    print(response.status_code)
