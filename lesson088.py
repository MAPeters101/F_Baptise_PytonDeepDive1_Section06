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



