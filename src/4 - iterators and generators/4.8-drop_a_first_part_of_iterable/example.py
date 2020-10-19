from itertools import dropwhile
from os.path import dirname, abspath, join

p = dirname(abspath(__file__))

with open(join(p, 'some_text.txt')) as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# or

with open(join(p, 'some_text.txt')) as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
