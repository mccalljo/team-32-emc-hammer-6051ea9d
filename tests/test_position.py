from unittest import TestCase
from levelup.position import position

class TestPosition(TestCase):
    def test_init(self):
        position_x = 0
        position_y = 0
        testobj = position(position_x,position_y)
        self.assertEqual(position_x, position_y, testobj.name)