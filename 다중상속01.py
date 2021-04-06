
class Tiger:
    def jump(self):
        print("호랑이 점프")

class Lion:
    def bite(self):
        print("사자 물어뜯기")
    def cry(self):
        print("사자 으르르르릉~")
class Liger(Lion,Tiger):
    def play(self):
        print("라이거와 놀기")


l = Liger()
l.cry()
print("내부에 상속 순서 튜플: {0}".format(Liger.__mro__))        
