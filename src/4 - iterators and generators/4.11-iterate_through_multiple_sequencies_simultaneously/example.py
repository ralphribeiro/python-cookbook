from itertools import zip_longest

xpts = [1, 2, 3, 4, 6, 7, 8]
ypts = [9, 10, 11, 12, 13, 14]

for x, y in zip(xpts, ypts):
    print(x, y)


a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
b = [3, 5, 6, 7]

for i in zip(a, b):
    print(i)


for i in zip_longest(a, b):
    print(i)
