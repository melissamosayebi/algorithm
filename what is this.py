import dis
class Ex:
    ex=lambda a,b:a*b
    fx=lambda x,y:x//y
    def try1(self):
        print(self.ex("try1"))
    def try2(self):
        print(self.fx("try2"))  
dis.dis(Ex.ex)
dis.dis(Ex.fx)