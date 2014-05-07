# -*- coding: utf-8 -*-
#
# transform - a method that takes an array of characters
# it reverse the array and uppercases all vowels except 'a'
# and it lowercases all consonants except 'z'
#
#
# Run the test cases by:
# python -m unittest transform
#

import unittest
import timeit
import resource


def transform(data):
    transformed_data = []
    for x in data:
        if x in ['e', 'i', 'o', 'u', 'E', 'I', 'O', 'U']:
            x = x.upper()
        elif x > 'A' and x < 'Z':
            x = x.lower()
        transformed_data.insert(0, x)
    return transformed_data


class TransformTests(unittest.TestCase):

    def _execute_test(self, dataset):
        for data in dataset:
            input, expected, msg = data
            result = transform(input)
            self.assertEqual(result, expected, msg)
            print('Passed transform({input})'.format(input=input))

    # Functional tests
    def test_functional(self):
        data = [
            (['A', 'a', 'Z', 'z'], ['z', 'Z', 'a', 'A'], 'lists must match'),
            ('EIOUeiou', ['U', 'O', 'I', 'E', 'U', 'O', 'I', 'E'], 'lists must match'),
            ('bcdfghjklmnpqrstvwxy', ['y', 'x', 'w', 'v', 't', 's', 'r', 'q', 'p', 'n', 'm', 'l', 'k', 'j', 'h', 'g',
                                      'f', 'd', 'c', 'b'], 'lists must match'),
            ('BCDFGHJKLMNPQRSTVWXY', ['y', 'x', 'w', 'v', 't', 's', 'r', 'q', 'p', 'n', 'm', 'l', 'k', 'j', 'h', 'g',
                                      'f', 'd', 'c', 'b'], 'lists must match'),
            ('0123456789', ['9', '8', '7', '6', '5', '4', '3', '2', '1', '0'], 'lists must match'),
        ]
        self._execute_test(data)

    # Unicode tests, more test data can be added.
    # This test case fails, as the method doesn't handle unicode.
    def test_unicode(self):
        data = [
            ('会意字會意字', ['字', '意', '會', '字', '意', '会'], 'unicode not handleded'),
        ]
        self._execute_test(data)

    # Special characters test, more test data can be added.
    def test_special_chars(self):
        data = [
            ('~!#$%^&*_+=-', ['-', '=', '+', '_', '*', '&', '^', '%', '$', '#', '!', '~'], 'lists must match'),
        ]
        self._execute_test(data)

    # Special Case of Blank, any other special cases can go here.
    def test_special_cases(self):
        data = [
            ('', [], 'lists must match'),  # Blank Input
        ]
        self._execute_test(data)

    # Negative inputs: dictionary object and Tuples: Method should complain of input not being an array as defined.
    # These tests fail right now, since the method does not raise any exceptions.
    def test_negative_input(self):
        self.assertRaises(Exception, transform, data={'a': 1, 'b': 2, 'c': 3})
        self.assertRaises(Exception, transform, data=('a', 1, '*'))

    # Method called in xtest_performance
    def _performance_test(self):
        data = [i for i in range(10000)]
        transform(data)

    # Uncomment the next line to skip this long running Performance timing and resource test
    # @unittest.skip("Skipping Performance and Resource Usage tests")
    def test_performance(self):
        begin = resource.getrusage(resource.RUSAGE_SELF)
        result = timeit.timeit(self._performance_test, number=1000)
        print('1000 iterations {result} seconds'.format(result=result))
        end = resource.getrusage(resource.RUSAGE_SELF)
        print('Memory usage: {diff} kb'.format(diff=end.ru_maxrss - begin.ru_maxrss))
