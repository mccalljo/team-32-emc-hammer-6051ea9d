from unittest import TestCase
from levelup.character import Character


class TestCharacterInitWithName(TestCase):
    
    ARBITRARY_NAME = "MyName"

    def test_init(self):
        testobj = Character(self.ARBITRARY_NAME)
        self.assertEqual(self.ARBITRARY_NAME, testobj.name)





