# Defining multiple classes
class A:
    def method(self):
        return "Method from class A"


class B(A):
    def method(self):
        return "Method from class B"


class C(A):
    def method(self):
        return "Method from class C"


class D(B, C):
    pass


# Creating an object of class D
d = D()
print(d.method())  # Outputs: Method from class B

# Printing the MRO
print(
    D.mro())  # Outputs: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
