# -*- 생성자와 소멸자 -*-
import sys

class MyClass:
    def __init__(self, value):
        self.value = value
        print("Instace is created! value = ", value)
    # 소멸자 유명무실 -> 내가 신경쓰지 않아도 GC로 알아서 됨. 파이썬이 알아서 처리.
    def __del__(self):
        print("Instance is deleted!")

#인스턴스 생성
d = MyClass(5)
# d_copy = d #무조건 참조 복사
print("참조 횟수: {0}".format(sys.getrefcount(d)))
del d_copy
del d

print("전체코드 실행 종료")