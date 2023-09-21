import math

class point:
    position_x: int = 0
    position_y: int = 0
    position_x_min: int = 0
    position_y_min: int = 0
    position_x_max: int = 9
    position_y_max: int = 9

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        pointcoordinates = point(position_x, position_y)
