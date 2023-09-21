from unittest import TestCase
from levelup.position import point

class TestPosition(TestCase):
    def test_init(self):
        position_x
        position_y
        testobj = point(position_x,position_y)
        self.assertEqual(position_x, testobj.position_x)
        self.assertEqual(position_y, testobj.position_y)
        self.assertIsNotNone(testobj.coordinates)
