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

