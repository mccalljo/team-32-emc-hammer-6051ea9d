from unittest import TestCase
from levelup.position import point

class TestPosition(TestCase):
    def test_init(self):
        position_x = 0
        position_y = 0
        testobj = point(position_x,position_y)
        self.assertEqual(position_x, testobj.position_x)
        self.assertEqual(position_y, testobj.position_y)
        self.assertIsNotNone(testobj.coordinates)

    """
    def test_maxpos(self):
        position_x_max = 9
        position_y_max = 9  
        testObj = point()
        self.assertEqual(position_x_max, testObj.position_x_max)
        self.assertEqual(position_y_max, testObj.position_y_max)      

    def test_minpos(self):
        position_x_min = 0
        position_y_min = 0          
        testObj = point()
        self.assertEqual(position_x_min, testObj.position_x_min)
        self.assertEqual(position_y_min, testObj.position_y_min)  
    """   