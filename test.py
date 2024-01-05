import time
class Bla:
    def __init__(self, name, age):
        self.name = name
        self.age = age

bla1 = Bla("lol", 42)
print(bla1)
bla2 = Bla("rofl", 9000)
print(bla2)
blas = [bla1, bla2]
print(blas)
print(bla1.name)
print(bla2.name)
del blas[0]
print(blas)
print(bla1)