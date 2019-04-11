class A:
    def method(self):
        print("This method belongs to class A")

class B(A):
    def method(self):
        print("This method belongs to class B")

class C(A):
    def method(self):
        print("This method belongs to class C")

class D(B,C): # The class that is called first will be the over written method
    pass

d = D()
d.method()
