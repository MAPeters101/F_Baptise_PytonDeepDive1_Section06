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

def apply_func(x, fn):
    return fn(x)

print(apply_func(3, sq))

print()

print(apply_func(5, lambda x: x**2))
print(apply_func(5, lambda x: x**3))

def apply_func2(fn, *args, **kwargs):
    return fn(*args, **kwargs)

print(apply_func2(sq, 3))
print(apply_func2(lambda x: x**2, 3))
print(apply_func2(lambda x, y: x + y, 1, 2))
print(apply_func2(lambda x, *, y: x + y, 1, y=4))
print(apply_func2(lambda *args: sum(args), 1, 2, 3, 4, 5))
print(apply_func2(sum, (1, 2, 3, 4, 5)))
print(sum((1, 2, 3, 4, 5, 6)))







