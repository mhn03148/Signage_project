# crawling
url_see = 'https://see.knu.ac.kr/content/board/notice.html' #접속하는 url 주소
key_list_see = ['안전', '등록', '교직', '수업', '학생', ''] #공지 제목 태그 리스트
selector_see = '#content > div > div > div.board_list > div.board_body > table > tbody > tr:nth-child(%s) > td.left > a'

# image
img_size = (1600, 1200)
tag_size = 100
tag_start = [20, 20]
contents_size = 60
contents_start = [tag_start[0], tag_start[1]+tag_size]
