# Method Resolution Order (MRO)

## What is MRO?
MRO stands for **Method Resolution Order** and determines the order in which base classes are searched when calling a method. MRO is important in multiple inheritance, where a class can inherit from more than one parent class.

### Key points:
- MRO determines the order in which classes are searched for methods.
- In Python, the MRO can be accessed using the mro() method or __mro__ attribute.
- The MRO follows the C3 Linearization algorithm in Python.
### Example:
```python
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

d = D()
print(d.method())  # Outputs: Method from class B
print(D.mro())     # Outputs: [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
```