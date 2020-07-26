import unittest
from mumbling import mumble


class MumblingTestCase(unittest.TestCase):

    def test_framework_is_working(self):
        self.assertEqual(True, True)

    def test_mumble_empty_string(self):
        self.assertEqual(mumble(""), "")

    def test_mumble_single_string(self):
        self.assertEqual(mumble("a"), "A")

    def test_mumbles_abc(self):
        self.assertEqual(mumble("abC"), "A-Bb-Ccc")

    def test_mumbles_abcd(self):
        self.assertEqual(mumble("aBCd"), "A-Bb-Ccc-Dddd")

    def test_mumbles_qwerty(self):
        self.assertEqual(mumble("QWERTY"), "Q-Ww-Eee-Rrrr-Ttttt-Yyyyyy")


if __name__ == '__main__':
    unittest.main()
