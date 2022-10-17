import requests
from bs4 import BeautifulSoup
import config

def crawling():
    url = config.url_see
    selector = config.selector_see
    key_list = config.key_list_see
    response = requests.get(url)
    content_dic = {}

    if response.status_code == 200:
        html = response.content
        soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')#한글 가져올때,깨질떄, utf-8로 설정해줘야 함
        for i in range(1,35):
            title = soup.select_one(selector %str(i))
            for j in range(len(key_list)):
                if key_list[j] in title.get_text().strip():
                    if content_dic.get(key_list[j], -1) == -1:
                        content_dic[key_list[j]] = [title.get_text().strip()]
                    else:
                        content_dic[key_list[j]].append(title.get_text().strip())
                    break
        content_dic['기타'] = content_dic['']
        del content_dic['']
        return content_dic
    else:
        return content_dic

