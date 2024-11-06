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
def my_func3(a):
    return a * max(x, y)

print(my_func3('a'))



