#web.py
#from 패키지명 import 모듈명
from bs4 import BeautifulSoup

#페이지를 로딩 (HTM>문서를 읽어오리고 유니코드 지정)
page = open("c:\\work2\\test01.html","rt",encoding="utf-8").read()
#검색이 용이한 객체 생성
soup = BeautifulSoup(page, "html.parser")
#print(soup.prettify())
#<P>를 모두 검색. 리스트 형식으로 리턴
#print( soup.find_all("p"))
#print( soup.find("p"))
#print(soup.find_all("p", class_="outer-text"))
#특정 id속성검색
#print(soup.find(id="first"))
#<a>태그가져오기
#print(soup.find_all("b"))

#tag를 제거하고 내부 문자열(컨텐츠만)
#<p>컨텐츠</p>
for tag in soup.find_all("p"):
    #앞뒤에 공백문자를 제거
    print(tag.text.strip())