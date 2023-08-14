import unittest
from main import Foo


class FooTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(Foo(15) + 3, 18)
        self.assertEqual(Foo(3) + 13, 16)
        foo = Foo(10)
        self.assertEqual(foo+10, 20)
        self.assertEqual(foo.x, 10)

    def test_fact(self):
        self.assertEqual(Foo(3).factorial(), 6)

print('all passed')