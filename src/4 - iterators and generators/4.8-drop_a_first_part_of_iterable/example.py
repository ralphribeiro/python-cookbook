from itertools import dropwhile


with open('some_text.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# or

with open('some_text.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')
