import unittest
import leapyear

class TestName(unittest.TestCase):
    def test1(self):
        self.assertEqual(leapyear.is_leap(2000), True)

    def test2(self):
        self.assertEqual(leapyear.is_leap(2100), False)

    def test3(self):
        self.assertEqual(leapyear.is_leap(1998), False)

if __name__ == '__main__':
    unittest.main(verbosity=2)