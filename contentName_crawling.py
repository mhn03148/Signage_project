import requests
from bs4 import BeautifulSoup

def crawling():
    url = 'https://see.knu.ac.kr/content/board/notice.html'
    response = requests.get(url)

    content_dic = {}

    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')#한글 가져올때,깨질떄, utf-8로 설정해줘야 함
        key_list = ['안전', '[학생]', '등록', '교직', '수업','']
        for i in range(1,35):
            title = soup.select_one('#content > div > div > div.board_list > div.board_body > table > tbody > tr:nth-child('+str(i)+') > td.left > a')

            for j in range(len(key_list)):
                if key_list[j] in title.get_text().strip():
                    if key_list[j] == '':
                        if content_dic.get("기타", -1) == -1:
                            content_dic["기타"] = [title.get_text().strip()]
                        else:
                            content_dic["기타"].append(title.get_text().strip())
                    if content_dic.get(key_list[j], -1) == -1:
                        content_dic[key_list[j]] = [title.get_text().strip()]
                    else:
                        content_dic[key_list[j]].append(title.get_text().strip())
                    break

        return content_dic
    else:
        print(response.status_code)
crawling()
