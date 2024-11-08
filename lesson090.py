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

