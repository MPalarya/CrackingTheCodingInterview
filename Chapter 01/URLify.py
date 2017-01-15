from __future__ import absolute_import
import unittest

"""
Write a method to replace all spaces in a string with '%20'.

2017-01-15 Michael Palarya
"""


def urlify1(s, length):
    """
    pythonic solution
    """
    return "%20".join(s.split())


def urlify2(s, length):
    """
    simple solution by creating a new string
    """
    # ignore ending spaces
    for i in range(length-1, -1, -1):
        if s[i] != " ":
            length = i+1
            break

    res = ""
    skipped_left_spaces = False
    replaced_i = -1
    for i in range(length):
        if s[i] != " ":
            res += s[i]
            skipped_left_spaces = True
        elif skipped_left_spaces:
            if i-1 != replaced_i:
                res += "%20"
            replaced_i = i
    return res


class Test(unittest.TestCase):
    # (string, expected-result)
    tests = [
        ("", ""),
        (" ", ""),
        ("          ", ""),
        ("a", "a"),
        ("   a    ", "a"),
        ("a a", "a%20a"),
        ("     a      a       ", "a%20a"),
    ]

    functions = [
        urlify1,
        urlify2,
    ]

    def test_all(self):
        for f in self.functions:
            for s, expected_result in self.tests:
                self.assertEqual(f(s, len(s)), expected_result)

if __name__ == "__main__":
    unittest.main()
