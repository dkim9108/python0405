#web2.py
import urllib.request
from bs4 import BeautifulSoup

#웹서버에 요청해서 결과물을 문자열로 받기
#패키지명.모듈명.함수명
data = urllib.request.urlopen('http://comic.naver.com/webtoon/list.nhn?titleId=20853&weekday=fri')
#검색이 용이한 객체
soup = BeautifulSoup(data,"html.parser")

# <td class = "title">
#     <a href="/webtoon/detail.nhn?titleId=20853&no=49&weekday=fri" onclick="nclk_v2(event,'lst.title','20853','49')">마음의 소리 49화 <지혜></a>
# </td>