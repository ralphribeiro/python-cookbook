from os.path import abspath, dirname, join


p = dirname(abspath(__file__))

# Example of iterating over lines of a file with an extra lineno attribute


def parse_data(filename):
    with open(filename, 'rt') as f:
        for lineno, line in enumerate(f, 1):
            fields = line.split()
            try:
                count = int(fields[1])
            except ValueError as e:
                print(f'Line {lineno}: Parse error: {e}')


parse_data(join(p, 'sample.dat'))
