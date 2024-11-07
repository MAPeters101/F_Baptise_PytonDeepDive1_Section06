print(callable(print))

result = print('hello')
print(result)

l = [1, 2, 3]
print(callable(l.append))

result = l.append(4)
print(l)
print(result)

s = 'abc'
print(callable(s.upper))
print(callable(s.upper()))
result = s.upper()
print(result)

from decimal import Decimal
print(callable(Decimal))
a = Decimal('10.5')
print(a)
print(type(a))
print(callable(a))
print('='*20)

class MyClass:
    def __init__(self, x=0):
        print('initializing....')
        self.counter = x

print(callable(MyClass))
a = MyClass(100)
print(a.counter)
print(callable(a))
print('='*20)

class MyClass2:
    def __init__(self, x=0):
        print('initializing....')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter...')
        self.counter += x

b = MyClass2()
MyClass2.__call__(b, 10)
print(b.counter)
print(callable(b))
b()
b(100)
print(b.counter)

print(type(MyClass))
print(type(Decimal))

