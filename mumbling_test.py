import unittest
from mumbling import mumble


class MumblingTestCase(unittest.TestCase):

    def test_framework_is_working(self):
        self.assertEqual(True, True)

    def test_mumble_empty_string(self):
        self.assertEqual(mumble(""), "")

    def test_mumble_single_string(self):
        self.assertEqual(mumble("a"), "A")


if __name__ == '__main__':
    unittest.main()
