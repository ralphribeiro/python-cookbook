from itertools import permutations, combinations, combinations_with_replacement


items = ['a', 'b', 'c']

for p in permutations(items):
    print(p)
print('-'*10)

for p in permutations(items, 2):
    print(p)
print('-'*10)

for c in combinations(items, 3):
    print(c)
print('-'*10)

for c in combinations(items, 2):
    print(c)
print('-'*10)

for c in combinations(items, 1):
    print(c)
print('-'*10)

for c in combinations_with_replacement(items, 3):
    print(c)
print('-'*10)
