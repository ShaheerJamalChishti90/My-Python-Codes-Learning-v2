class A:
    def method(self):
        print("A")

class B(A): #This is a Child Class of its Upper Class A
    def method(self):
        print("B")
        super().method()

class C(A): #This is a Child Class of its Upper Class A
    def method(self):
        print("C")
        super().method()

class D(B, C): #This is a Child Class of its Upper Class B and C
    def method(self):
        print("D")
        super().method()

d = C()
d.method()
print(D.mro())

 