import unittest

# Unittest test
class MyTest(unittest.TestCase):
    def test_method1(self):
        actual = 1
        expected = 1
        self.assertEquals(actual, expected)

    def test_method2(self):
        actual = 1
        expected = 2
        self.assertNotEquals(actual, expected)