# Example of iterating of fixed-size records
#
# The file 'data.bin' contains 32-byte fixed size records
# that consist of a 4-digit number followed by a 28-byte string.

from functools import partial
from os.path import abspath, dirname, join


RECORD_SIZE = 32
p = dirname(abspath(__file__))


with open(join(p, 'data.bin'), 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print(r)
