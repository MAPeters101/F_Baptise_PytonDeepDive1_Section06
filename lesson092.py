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

