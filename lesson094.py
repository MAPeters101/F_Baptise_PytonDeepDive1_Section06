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
