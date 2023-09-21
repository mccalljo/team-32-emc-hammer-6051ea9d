from unittest import TestCase
from levelup.ui import GameApp

class TestGameApp(TestCase):
    def test_init_includes_welcome(self):
        test_app = GameApp()
        assert len(test_app.welcome_message) > 0
        
       