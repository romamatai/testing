#!/usr/bin/env python

# learn about itertools and chain function provided by it.

from itertools import chain

class Base(object):
    def __iter__(self):
        return iter({'a': 1, 'b': 2, 'z': 26}.items())


class Child(Base):
    def __iter__(self):
        i = super(Child, self).__iter__()
        i2 = iter({'c': 3, 'd': 4, 'y': 25}.items())
        return chain(i, i2)

if __name__ == "__main__":
    print dict(Child())

