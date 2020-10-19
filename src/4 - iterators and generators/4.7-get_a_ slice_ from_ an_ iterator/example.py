from itertools import islice


def count(n):
    while True:
        yield n
        n += 1


c = count(0)

for x in islice(c, 10, 20):
    print(x)
