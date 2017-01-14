from __future__ import absolute_import
import unittest

"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

2017-01-14 Michael Palarya
"""


def is_unique1(s):
    """
    pythonic solution
    """
    return len(s) == len(set(s))


def is_unique2(s):
    """
    simple solution using c-like arrays
    also possible with bitwise operations and a long instead of using a list
    """
    total_uniques = 2**8  # all possible bytes(chars)
    if len(s) > total_uniques:
        return False  # pigeonhole principle

    lst = [False] * total_uniques
    for c in s:
        o = ord(c)
        if lst[o]:
            return False
        lst[o] = True
    return True


def is_unique3(s):
    """
    without using data structures
    """
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            if s[i] == s[j]:
                return False
    return True


class Test(unittest.TestCase):
    # (string, expected-result)
    tests = [
        ("", True),
        (" ", True),
        ("  ", False),
        ('a', True),
        ('aa', False),
        ('ab', True),
        ('qwertyuiop[]', True),
        (' qwertyuiop[] ', False)
    ]

    functions = [
        is_unique1,
        is_unique2,
        is_unique3,
    ]

    def test_all(self):
        for f in self.functions:
            for s, expected_result in self.tests:
                self.assertEqual(f(s), expected_result)

if __name__ == "__main__":
    unittest.main()
