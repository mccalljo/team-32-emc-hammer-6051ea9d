
from unittest import TestCase
from levelup.map import Map

class TestGameMap(TestCase):
    def test_get_position(self):        
        test_object  = Map()
        result = test_object.get_position()
        assert( result == (0, 0))        

    def test_calculate_position(self):
        test_object = Map()
        result = test_object.calculate_position((3,3), "North")
        assert  result == (3, 4)
        

    def test_is_position_valid(self):
        test_object = Map()
        result = test_object.is_position_valid((4,4))
        assert result

    def test_get_starting_position(self):
        test_object = Map()
        result = test_object.get_starting_position()
        assert result[0] in range(0,10) and result[1] in range(0,10)
        pass