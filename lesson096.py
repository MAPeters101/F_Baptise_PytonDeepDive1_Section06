import operator

print(1+2)
print(operator.add(1, 2))
print(operator.mul(2, 3))
print(operator.truediv(3,2))
print(operator.floordiv(13,2))
print(13 // 2)
print('-'*70)

from functools import reduce

print(reduce(lambda x, y: x*y, [1,2,3,4]))
print(reduce(operator.mul, [1,2,3,4]))
print()

print(operator.lt(10, 3))
print(operator.is_('abc', 'def'))
print(operator.is_('abc', 'abc'))
print()
print(operator.truth([]))
print(operator.truth([1]))
print('='*80)

my_list = [1, 2, 3, 4]
print(my_list[1])
print(operator.getitem(my_list, 1))
print()

my_list[1] = 100
print(my_list)
print(operator.getitem(my_list, 1))
print()

del my_list[3]
print(my_list)
print('+'*50)

my_list = [1, 2, 3, 4]
operator.setitem(my_list, 1, 100)
print(my_list)

operator.delitem(my_list, 3)
print(my_list)

print()








