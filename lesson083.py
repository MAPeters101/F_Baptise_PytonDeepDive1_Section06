def sq(x):
    return x**2

print(type(sq))
print()
print(sq)

print(lambda x: x**2)
print(lambda x, y: x+y)
print()

f = sq

print(hex(id(f)), hex(id(sq)))

print(f(3), sq(4))

print(f, sq)

g = lambda x, y=10: x+y
print(g)
print(g(1, 2))
print(g(1))

f = lambda x, *args, y, **kwargs: (x, args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))

f = lambda x, *args, y, **kwargs: (x, *args, y, kwargs)
print(f(1, 'a', 'b', y=100, a=10, b=20))

