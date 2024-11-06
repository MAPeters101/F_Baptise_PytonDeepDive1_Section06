#help(print)

def my_func(a, b=1):
    # Some comment
    #'Some comment'
    """returns a * b

    some additional docs here.

    Inputs:


    Outputs:
    """

    return a * b

help(my_func)
print('='*30)
print(my_func.__doc__)


print('-'*10)

def my_func2(a: 'Annotation for a',
             b: 'Annotation for b' = 1) -> 'Something with a long annotation':
    """Documentation for my_func2"""
    return a * b

help(my_func2)

print(my_func2.__doc__)
print(my_func2.__annotations__)
print('+'*10)


x = 3
y = 5
def my_func3(a: 'some character', b=max(x,y)) -> 'character a repeated ' + str(max(x,y)) + ' times':
    print(b)
    return a * max(x, y)

print(my_func3('a'))
print(my_func3.__annotations__)

x = 10
print(my_func('a'))
print(my_func3.__annotations__)
print('='*20)
def my_func4(a: str,
            b: 'int > 0' = 1,
            *args: 'some extra positional args',
            k1: 'keyword-only arg 1',
            k2: 'keyword-only arg 2' = 100,
            **kwargs: 'some extra keyword-only args') -> 'something':
    print(a, b, args, k1, k2, kwargs)

help(my_func4)
print(my_func4.__annotations__)


my_func4(1, 2, 3, 4, 5, k1=10, k3=300, k4=400)



