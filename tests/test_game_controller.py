from unittest import TestCase
from levelup.controller import GameController

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None

    def test_controller_creates_character(self):
        testObj = GameController()
        result = testObj.create_character("mickey mouse")
        self.assertEqual(testObj.character.name, "mickey mouse")
