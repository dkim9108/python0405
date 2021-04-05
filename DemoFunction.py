#DemoFunction.py
#함수를 정의
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b

#호출
print(add(3,4))
print(sub(5,2))
print(mul(5,2))
print(div(5,3))
print("========================")

#가변형과 불변형(int, float, 복소수, 튜플, 문자열)
a = 1.2
print(id(a))
a = 2.3
print(id(a)) #불변형은 주소값이 변함, 왜냐면 새로불러오는거라서!
print("=======가변형 예시=======") #가변형은 안바뀜. 
lst = ["red", "blue"]
print(id(lst))
lst.append("white")
print(id(lst))

print("====전역변수, 지역변수====")
x=5
def func(a):
    return a+x

def func2(a):
    x=1
    return a+x

print(func(1))
print(func2(1))