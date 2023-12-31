from unittest import TestCase
from levelup.character import Character
from levelup.controller import Direction

class TestCharacterInitWithName(TestCase):
    def test_init(self):
        ARBITRARY_NAME = "Capt Dork"
        testobj = Character(ARBITRARY_NAME)
        self.assertEqual(ARBITRARY_NAME, testobj.name)

    def test_get_name(self):
        ARBITRARY_NAME = "Capt John McCall"
        testobj = Character(ARBITRARY_NAME)
        result = testobj.getName()
        self.assertEqual(ARBITRARY_NAME, result)

    def test_move(self):
        ARBITRARY_NAME = "Sailing the high seas"
        testobj = Character(ARBITRARY_NAME)
        result = testobj.move(Direction.WEST)
        
