import requests
from bs4 import BeautifulSoup


url = 'https://see.knu.ac.kr/content/board/notice.html'
response = requests.get(url)
content_name=[]
content_dic = {}

if response.status_code == 200:
    html = response.content
    soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')#한글 가져올때,깨질떄, utf-8로 설정해줘야 함

    for i in range(1,35):
        title = soup.select_one('#content > div > div > div.board_list > div.board_body > table > tbody > tr:nth-child('+str(i)+') > td.left > a')
        content_name.append(title.get_text().strip())
        if ('안전' in title.get_text().strip()):
            if content_dic.get("안전", -1) == -1:
                content_dic["안전"] = [title.get_text().strip()]
            else:
                content_dic["안전"].append(title.get_text().strip())
        else:
            if content_dic.get("기타", -1) == -1:
                content_dic["기타"] = [title.get_text().strip()]
            else:
                content_dic["기타"].append(title.get_text().strip())

    print(content_dic)
else :
    print(response.status_code)