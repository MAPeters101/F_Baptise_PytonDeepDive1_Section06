# dummy code
i = 100

# TODO: Fix this function
# currently does nothing, but should do ....
def my_func(a: "mandatory positional",
            b: "optional positional" = 1,
            c=2,
            *args: "Add extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs: "Provide extra kw-only here") -> "Does nothing":
    """
    This function does nothing but does have various parameters
    and annotations.
    :param a:
    :param b:
    :param c:
    :param args:
    :param kw1:
    :param kw2:
    :param kw3:
    :param kwargs:
    :return:
    """
    i = 10
    j = 20
    a = i + j
    return a


print(my_func.__doc__)
print(my_func.__annotations__)


my_func.short_description = "this is a function that does nothing much"

print(my_func.short_description)
print(dir(my_func))
print(my_func.__name__)

print(hex(id(my_func)))
def func_call(f):
    print(hex(id(f)))
    print(f.__name__)

func_call(my_func)
print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print()
print(dir(my_func.__code__))
print(dir(my_func))
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)
print(my_func.__code__.co_argcount)

print()
print()
print('-'*20)
import inspect
from inspect import isfunction, ismethod, isroutine

a = 10
print(isfunction(a))
print(isfunction(my_func))
print(ismethod(my_func))

class MyClass:
    def f(self):
        pass

print(isfunction(MyClass.f))

my_obj = MyClass()
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print(isroutine(my_obj.f))
print(isroutine(MyClass.f))
print('='*20)

print(inspect.getsource(my_func))
print(inspect.getmodule(my_func))
print(inspect.getmodule(print))
print()
import math
print(inspect.getmodule(math.sin))
print(inspect.getcomments(my_func))
print(my_func.__annotations__)
print(inspect.signature(my_func).return_annotation)

sig = inspect.signature(my_func)
print(sig)
print(sig.parameters)

for k, v in sig.parameters.items():
    print(k, v)

for k, v in sig.parameters.items():
    print(dir(v))

for k, v in sig.parameters.items():
    print(k, type(v))

for k, param in sig.parameters.items():
    print('Key:', k)
    print('Name:', param.name)
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind:', param.kind)
    print('-'*20)

for param in sig.parameters.values():
    print('Name:', param.name)
    print('Default:', param.default)
    print('Annotation:', param.annotation)
    print('Kind:', param.kind)
    print('-'*20)

help(divmod)
print(divmod(4,3))
#print(divmod(x=3, y=4))
print('='*30)
for param in inspect.signature(divmod).parameters.values():
    print(param.kind)