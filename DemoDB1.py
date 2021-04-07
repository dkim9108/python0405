#DemoDB1.py
#SQLite를 사용하는 데모(로컬 데이터베이스)

import sqlite3
#처음에는 데이터베이스 파일(또는 메모리)생성
con = sqlite3.connect(":memory:")
#SQL구뭉늘 실행하는 것은 대부분 cursor객체
cur=con.cursor()
#저장소(테이블)만들기: 테이블 스키마(뼈대)
cur.execute("create table PhoneBook(Name text, PhoneNum text)")
#1건 검색
cur.execute("insert into PhoneBook values('derick', '010=111');")

#입력 파라메터 처리
name = "gildong"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook values(?,?);",(name, phoneNumber))
#다중의 레코드(행,row)를 입력받는 경우
datalist=(("tom","010-123"),("dsp","010-567"))
cur.executemany("insert into PhoneBook values (?,?);", datalist)


#검색
cur.execute(("select * from PhoneBook;"))
# for row in cur:
#         print(row)

print(cur.fetchone())

print("----fetchmany(2)----")
print(cur.fetchmany(2))
print("-----fetchall()-----")
print(cur.fetchall())

cur.execute("select *from PhoneBook;")
result = cur.fetchone()
print(result[0])
print(result[1])
#2차원 행열 데이터 [행][열]
print("----다중행----")
result = cur.fetchall()
print(result[0][0])
print(result[0][1])