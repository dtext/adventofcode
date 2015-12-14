import unittest
import script as s


class MyTestCase(unittest.TestCase):

    def test_nice(self):
        self.assertTrue(s.matchesrules("ugknbfddgicrmopn", s.patterns1))
        self.assertTrue(s.matchesrules("aaa", s.patterns1))

    def test_naughty(self):
        self.assertFalse(s.matchesrules("jchzalrnumimnmhp", s.patterns1))
        self.assertFalse(s.matchesrules("haegwjzuvuyypxyu", s.patterns1))
        self.assertFalse(s.matchesrules("dvszwmarrgswjxmb", s.patterns1))

    def test_nice2(self):
        self.assertTrue(s.matchesrules("qjhvhtzxzqqjkmpb", s.patterns2))
        self.assertTrue(s.matchesrules("xxyxx", s.patterns2))

    def test_naughty2(self):
        self.assertFalse(s.matchesrules("uurcxstgmygtbstg", s.patterns2))
        self.assertFalse(s.matchesrules("ieodomkazucvgmuy", s.patterns2))

if __name__ == '__main__':
    unittest.main()
