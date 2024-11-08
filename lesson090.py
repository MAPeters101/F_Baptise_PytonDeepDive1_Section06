def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(3))
print(fact(4))
print()

print(map(fact, range(6)))
results = map(fact, range(6))
print(results)
for x in results:
    print(x)
print('-'*10)

for x in results:
    print(x)
print('-'*10)

results = list(map(fact, range(6)))
print(results)
print(results)
print('='*30)


l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
results = list(map(lambda x, y: x+y, l1, l2))
print(results)

l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
t1 = 100, 200, 300, 400
results = list(map(lambda x, y, z: x+y+z, l1, l2, t1))
print(results)

print('1'*20)
l1 = [1, 2, 3, 4, 5]
l2 = [10, 20, 30]
t1 = 100, 200, 300, 400
results = map(lambda x, y: x+y, l1, l2, t1)
print(results)
# for x in results:
#     print(x)
print('2'*20)

x = range(5)
print(x)

for i in x:
    print(i)

for i in x:
    print(i)

print(list(filter(lambda x: x%3 == 0, range(25))))
print(filter(None, [1, 0, 4, 'a', '', None, True, False]))
print(list(filter(None, [1, 0, 4, 'a', '', None, True, False])))
print()

l1 = [1, 2, 3, 4]
l2 = [10, 20, 30, 40]
l3 = 'python'
results = zip(l1, l2, l3)
print(results)
print('3-'*10)
for x in results:
    print(x)
for x in results:
    print(x)
print('4-'*10)
print()

results = list(zip(l1, l2, l3))
print(results)
print('3-'*10)
for x in results:
    print(x)
for x in results:
    print(x)
print('4-'*10)
print()

result = list(zip(range(10000), 'python'))
print(result)
print('='*50)


l = range(10)
print(list(l))
print(list(map(fact, l)))
print()

results = [fact(n) for n in range(10)]
print(results)
print()

results = (fact(n) for n in range(10))
print(results)
print('5'*10)
print()
for x in results:
    print(x)

print()
for x in results:
    print(x)
print('-'*20)

results = list((fact(n) for n in range(10)))
print(results)
print('5'*10)
print()
for x in results:
    print(x)

print()
for x in results:
    print(x)
print('-+'*20)

l1 = [1, 2, 3, 4, 5, 6]
l2 = [10, 20, 30, 40]
print(list(map(lambda x, y: x+y, l1, l2)))

print([x+y for x, y in zip(l1, l2)])
print()

print(list(filter(lambda x: x%2==0, map(lambda x, y: x+y, l1, l2))))
print()

print([x+y for x, y in zip(l1, l2) if (x+y)%2==0])
print()

results = (x+y for x, y in zip(l1, l2) if (x+y)%2==0)
print(results)
print(list(results))
print()


