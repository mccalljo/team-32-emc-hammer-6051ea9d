from unittest import TestCase
from levelup.position import Position


class TestPosition(TestCase):
    def test_init(self):
        x_coordinate = 0
        y_coordinate = 1
        testobj = Position(x_coordinate, y_coordinate)
        self.assertIsNotNone(testobj)
  