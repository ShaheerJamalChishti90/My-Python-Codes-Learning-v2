class A:
    def method(self):
        print("Method from A")

class B(A):
    def method(self):
        print("Method from B")

class C(A):
    def method(self):
        print("Method from C")

class D(B, C):
    pass

# Create an instance of D
d = D()
d.method()  # This will call the method from B
print(D.__mro__)