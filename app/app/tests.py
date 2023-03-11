from django.test import SimpleTestCase
from app import calc

class SimpleAdd(SimpleTestCase):
    def test_add(self):
        res = calc.add(5,6)

        self.assertEqual(res, 11)

    def test_sub(self):
        res = calc.sub(5,6)

        self.assertEqual(res, 1)