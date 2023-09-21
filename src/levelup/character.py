
from levelup.direction import Direction
from levelup.map import Map

class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name

    def getName():
        pass

    def move(self, direction :Direction) -> None:
        self.current_position = self.map.calculate_new_postion(
            self.current_position, direction)

    def enter_map(self, map :Map):
        self.map = map
        self.current_position = self.map.starting_position

