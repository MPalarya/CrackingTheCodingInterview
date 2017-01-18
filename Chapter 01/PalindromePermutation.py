from __future__ import absolute_import
import unittest

"""
Given a string, write a function to check if it is a permutation of a palindrome.
For example: Tact Coa is a palindrome permutation (taco cat, atco cta, etc.)

2017-01-17 Michael Palarya
"""


def palindrome_permutation1(s):
    minn = ord('a')
    maxx = ord('z')
    parity_lst = [0] * (maxx - minn)
    for c in s:
        c_ = ord(c.lower())
        if c_ > maxx or c_ < minn:
            continue
        parity_lst[c_ - minn] ^= 1

    return parity_lst.count(1) <= 1


class Test(unittest.TestCase):
    # (string, expected-result)
    tests = [
        ("Tact Coa", True),
        (" ", True),
        ("", True),
        ("A a bBc", True),
        ("A a bB", True),
        ("A a bBcdef", False),
        ("A a bBcde", False),
        ("A a bBcd", False),
        ("gA a bB", True),
        ("ghA a bB", False),
        ("ghiA a bB", False),
    ]

    functions = [
        palindrome_permutation1,
    ]

    def test_all(self):
        for f in self.functions:
            for s, expected_result in self.tests:
                self.assertEqual(f(s), expected_result)

if __name__ == "__main__":
    unittest.main()
