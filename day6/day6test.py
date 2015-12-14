import unittest
import script as s


class MyTestCase(unittest.TestCase):
    def test_parse(self):
        self.assertTupleEqual(s.parse("toggle 936,774 through 937,775"), ((936, 774), (937, 775), "toggle"))
        self.assertTupleEqual(s.parse("turn off 116,843 through 533,934"), ((116, 843), (533, 934), "turn off"))
        self.assertTupleEqual(s.parse("turn on 950,906 through 986,993"), ((950, 906), (986, 993), "turn on"))

    def test_cmd(self):
        self.assertFalse(s.cmd_fn["toggle"](True))
        self.assertTrue(s.cmd_fn["toggle"](False))
        self.assertFalse(s.cmd_fn["turn off"](True))
        self.assertFalse(s.cmd_fn["turn off"](False))
        self.assertTrue(s.cmd_fn["turn on"](True))
        self.assertTrue(s.cmd_fn["turn on"](False))


if __name__ == '__main__':
    unittest.main()
