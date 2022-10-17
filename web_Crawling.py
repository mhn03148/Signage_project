from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://see.knu.ac.kr/content/board/notice.html')#웹페이지를 열어줌
driver.implicitly_wait(3)#3초안에 웹페이지를 load 하면 바로 넘어가거나 3초를 기다림.
driver.find_element(By.XPATH,r'//*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[1]/td[2]/a').click()#해당 게시물을 클릭한다.
driver.find_element(By.TAG_NAME,'body').send_keys(Keys.PAGE_DOWN)#pagedown키를 누른만큼 스크롤을 내린다.
element = driver.find_element(By.CLASS_NAME,'contentview')#캡쳐할 영역을 지정한다.
element_png = element.screenshot_as_png#캡쳐하는 코드
with open('test.png','wb') as file:
    file.write(element_png)
driver.back()#뒤로가기 역할
driver.find_element(By.XPATH,r'//*[@id="content"]/div/div/div[2]/div[2]/table/tbody/tr[2]/td[2]/a').click()
element = driver.find_element(By.CLASS_NAME,'contentview')
element_png1 = element.screenshot_as_png
with open('test1.png','wb') as file:
    file.write(element_png1)

