from __future__ import absolute_import
import unittest

"""
Given two strings, write a method to decide if one is a permutation of the other

2017-01-14 Michael Palarya
"""


def check_permutation1(s1, s2):
    """
    pythonic solution, without an additional data structure
    """
    return len(s1) == len(s2) and sorted(s1) == sorted(s2)


def check_permutation2(s1, s2):
    """
    C-like solution
    """
    total_uniques = 2**8
    lst = [0] * total_uniques

    for c1 in s1:
        lst[ord(c1)] += 1
    for c2 in s2:
        lst[ord(c2)] -= 1

    if set(lst) == set([0]):
        return True
    return False


class Test(unittest.TestCase):
    # (string, expected-result)
    tests = [
        ("", "", True),
        (" ", " ", True),
        ("  ", "  ", True),
        ("  ", " ", False),
        ("  ", " ", False),
        ("qwertyuiop[]", "q]w[eprotiyu", True),
        ("abc", "abcd", False),
        ("abc", "abd", False),
        ("hey you", "heyyo u", True),
    ]

    functions = [
        check_permutation1,
        check_permutation2,
    ]

    def test_all(self):
        for f in self.functions:
            for s1, s2, expected_result in self.tests:
                self.assertEqual(f(s1, s2), expected_result)


if __name__ == "__main__":
    unittest.main()
