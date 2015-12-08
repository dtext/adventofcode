__author__ = 'dt'

import unittest
import script


class MyTestCase(unittest.TestCase):

    def test_nice(self):
        self.assertTrue(script.matchesrules("ugknbfddgicrmopn"))
        self.assertTrue(script.matchesrules("aaa"))

    def test_naughty(self):
        self.assertFalse(script.matchesrules("jchzalrnumimnmhp"))
        self.assertFalse(script.matchesrules("haegwjzuvuyypxyu"))
        self.assertFalse(script.matchesrules("dvszwmarrgswjxmb"))


if __name__ == '__main__':
    unittest.main()
