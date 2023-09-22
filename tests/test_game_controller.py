from unittest import TestCase
from levelup.controller import GameController
from fake_character import FakeCharacter
from levelup.direction import Direction

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None

    def test_controller_creates_character(self):
        testObj = GameController()
        result = testObj.create_character("Captain Kidd")
        self.assertEqual(testObj.character.name, "Captain Kidd")

    def test_start_game_creates_map_and_enters_char(self):
        testobj = GameController()
        arbitrary_name = "ARBITRARY"
        fake_char = FakeCharacter(arbitrary_name)
        testobj.character = fake_char

        testobj.start_game()
         