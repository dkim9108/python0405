#class1.py
class Person:
    #클래스에 소속된 멤버변수(주로데이터를 공유) static 키워드 별도로X
    num_person=0
    def __init__(self):
        #인스턴스 멤버변수는 여기서 초기화
        self.name = "default name"
        Person.num_person += 1
    def print(self):
        print("My name is {0}".format(self.name))

#인스턴스 생성
p1 = Person()
p2 = Person()
print("인스턴스 갯수: {0}".format(Person.num_person))

#런타임(실행시간)시에 멤버 변수 추가(동적언어는 가능)
#디자인타임(코딩, 개발...)
Person.title = "new title"
print(Person.title)
print(p1.title)
print(p2.title)
