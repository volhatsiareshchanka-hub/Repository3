# 2.4. Порядок разрешения методов (MRO)

class A:
    def who_am_i(self):
        print("I am A")

class B(A):
    def who_am_i(self):
        print("I am B")

class C(A):
    def who_am_i(self):
        print("I am C")

class D(B, C):
    pass

d = D()
d.who_am_i()       # B (по MRO)
print(D.mro())
