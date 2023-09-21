from unittest import TestCase
from levelup.position import Positions
class TestPositions(TestCase):
    def test_init(self):
        position_x = 0
        position_y = 0
        testobj = Positions(position_x,position_y)
        self.assertEqual(position_x, testobj.position_x)
        self.assertEqual(position_y, testobj.position_y)
        self.assertIsNotNone(testobj)

