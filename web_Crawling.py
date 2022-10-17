import requests
from bs4 import BeautifulSoup


url = 'https://see.knu.ac.kr/content/board/notice.html'

response = requests.get(url)


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
