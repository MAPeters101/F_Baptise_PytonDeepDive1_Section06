l = [5, 8, 6, 10, 9]
_max = lambda x, y: x if x > y else y
print(_max(3, 4))
print(_max(10, 2))
print()

def max_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _max(result, x)
    return result

print(max_sequence(l))

_min = lambda x, y: x if x < y else y
print(_min(3, 4))
print(_min(10, 2))
print()

def min_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _min(result, x)
    return result

print(min_sequence(l))
print()

_add = lambda x, y: x + y
print(_add(3, 4))
print(_add(10, 2))
print()

def add_sequence(sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = _add(result, x)
    return result

print(add_sequence(l))
print()

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print(_reduce(_max, l))
print(_reduce(_min, l))
print(_reduce(_add, l))
print()

#print(_reduce(_add, {1,2,3,4,5}))

from functools import reduce

print(reduce(_max, l))
print(reduce(_min, l))
print(reduce(_add, l))
print()

print(reduce(_max, {1,2,3,4,5}))
print(reduce(_min, {1,2,3,4,5}))
print(reduce(_add, {1,2,3,4,5}))
print()

print(min(l))
print(max(l))
print(sum(l))
print(min({1,2,3,4,5}))
print(max({1,2,3,4,5}))
print(sum({1,2,3,4,5}))
print()

s = {True, 1, 0, None}
print(all(s))

s2 = {True, 1, 's'}
print(all(s2))
print(bool(True) and bool(1) and bool('s'))
print()

print(any(s))
print(any(s2))
