from functools import partial

def my_func(a, b, c):
    print(a, b, c)

my_func(10, 20, 30)

def f(x, y):
    return my_func(10, x, y)

f(20, 30)
f(100, 200)

g = lambda x, y: my_func(10, x, y)
g(100, 200)

h = partial(my_func, 10)
h(20, 30)
h = partial(my_func, 10, 20)
h(30)
#h(10, 20)
print()

def my_func1(a, b, *args, k1, k2, **kwargs):
    print(a, b, args, k1, k2, kwargs)

my_func1(10, 20, 100, 200, k1='a', k2='b', k3=1000, k4=2000)
print()

def h(x, *vars, kw, **kwvars):
    return my_func1(10, x, *vars, k1='a',k2=kw, **kwvars)

h(20, 10, 20, kw='b', k3=1000, k4=2000)

h = partial(my_func1, 10, k1='a')

h(20, 100, 200, k2='b', k3=1000, k4=2000)
print()


def pow(base, exponent):
    return base ** exponent

sq = partial(pow, 2)
print(sq(10))

sq = partial(pow, exponent=2)
print(sq(5))

cu = partial(pow, exponent=3)
print(cu(5))
print(cu(base=5))
print(cu(5, exponent=2))
print()

a=2
sq=partial(pow,exponent=a)
print(sq(5))
a=3
print(sq(5))
print()

def my_func(a, b):
    print(a, b)

a = [1, 2]
f = partial(my_func, a)
f(100)
a.append(3)
print(a)
f(100)
print('-'*20)

origin = (0,0)
l = [(1, 1), (0, 2), (-3, 2), (0,0), (10, 10)]

dist2= lambda a, b: (a[0] - b[0])**2 + (a[1] - b[1])**2
print(dist2((1,1), origin))

print(sorted(l))
#print(sorted(l), key=dist2(e, origin))
f = partial(dist2, origin)
print(f((1,1)))
print(sorted(l, key=f))
print()

f = lambda x: dist2(origin, x)
print(sorted(l, key=f))
print()

print(sorted(l, key=lambda x: dist2(origin, x)))
print()

print(sorted(l, key=partial(dist2, origin)))
print()



