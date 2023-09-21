import random
import unittest
from levelup.gamemap import GameMap

class TestGameMap(unittest.TestCase):

    def setUp(self):
        self.game_map = GameMap()

    def test_get_position(self):        
        result = self.game_map.current_position
        self.assertEqual(result, (0, 0))

    def test_calculate_position(self):
        result = self.game_map.calculate_position((3, 3), "up")  # Use "up" instead of "North"
        self.assertEqual(result, (3, 4))

    def test_is_position_valid(self):
        result = self.game_map.is_position_valid((4, 4))
        self.assertTrue(result)

    def test_get_starting_position(self):
        result = self.game_map.generate_starting_position()  # Use generate_starting_position instead
        x, y = result
        self.assertTrue(0 <= x < 10)
        self.assertTrue(0 <= y < 10)

if __name__ == '__main__':
    unittest.main()
