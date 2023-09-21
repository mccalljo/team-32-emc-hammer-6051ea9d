import random

class Map:
    number_positions = 100
    
    def __init__(self): 
        pass

    def get_starting_position(self):
        return (0,1)
        pass
    
    def get_position(self):
        return (0,0)
        pass

    def calculate_position(self, position: tuple, direction ):
        return (3,4)
        pass

    def is_position_valid(self, position: tuple):
        vaildator = range(0, 10)
        return all([position for x in vaildator])
        

    def get_total_positions(self) -> int:
        return cls.number_positions
        pass