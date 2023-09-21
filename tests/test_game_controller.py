from unittest import TestCase
from levelup.controller import GameController
from levelup.controller import Direction

class TestGameController(TestCase):
    def test_init(self):
        testObj = GameController()
        assert testObj.status != None


