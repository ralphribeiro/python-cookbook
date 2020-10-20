# example.py
#
# Various samples of reading CSV files

from collections import namedtuple
import csv
from os.path import abspath, dirname, join

p = dirname(abspath(__file__))

# (a) Reading as tuples

print('Reading as tuples:')
with open(join(p, 'stocks.csv')) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # process row
        print('    ', row)

# (b) Reading as namedtuples

print('Reading as namedtuples')
with open(join(p, 'stocks.csv')) as f:
    f_csv = csv.reader(f)
    Row = namedtuple('Row', next(f_csv))
    for r in f_csv:
        row = Row(*r)
        # Process row
        print('    ', row)


# (c) Reading as dictionaries

print('Reading as dicts')
with open(join(p, 'stocks.csv')) as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        # process row
        print('    ', row)

# (d) Reading into tuples with type conversion

print('Reading into named tuples with type conversion')

col_types = [str, float, str, str, float, int]
with open(join(p, 'stocks.csv')) as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for row in f_csv:
        # Apply conversions to the row items
        row = tuple(convert(value) for convert, value in zip(col_types, row))
        print(row)

# (e) Converting selected dict fields

print('Reading as dicts with type conversion')

field_types = [('Price', float),
               ('Change', float),
               ('Volume', int)]

with open(join(p, 'stocks.csv')) as f:
    for row in csv.DictReader(f):
        row.update((key, conversion(row[key]))
                   for key, conversion in field_types)
        print(row)