import unittest
from parens import balanced

class TestBalancedParens(unittest.TestCase):

    def test_case1(self):
        self.assertTrue(
            balanced('((())())()')
        )

    def test_case2(self):
        self.assertEqual(
            balanced(')()('), 0
        )

    def test_case3(self):
        self.assertEqual(
            balanced('())'), 2
        )

if __name__ == '__main__':
    unittest.main()
