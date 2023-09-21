import random

class GameMap:
    
    number_positions = 100
    
    def __init__(self):
        self.current_position = (0, 0)  # Set initial position to (0, 0)
        self.move_count = 0

    def generate_starting_position(self):
        # This method is no longer used, as we set the initial position to (0, 0)
        pass

    def generate_starting_position(self):
        x = random.randint(0, 9)  # Replace 0 and 9 with your desired range
        y = random.randint(0, 9)  # Replace 0 and 9 with your desired range
        return (x, y)
    
    def calculate_position(self, position: tuple, direction):
        x, y = position  # Unpack the current position
        if direction == "up":
            y += 1
        elif direction == "down":
            y -= 1
        elif direction == "left":
            x -= 1
        elif direction == "right":
            x += 1

        # Check if the new position is valid (you can add validation logic here)

        return (x, y)

    def is_position_valid(self, position: tuple):
        x, y = position
        # Check if the coordinates are within the valid range for your game
        return 0 <= x < 10 and 0 <= y < 10  # Replace 10 with your actual range

    def get_current_position(self):  # Renamed the method to get_current_position
        return self.current_position  # This method returns the current position

    def get_total_positions(self) -> int:
        return self.number_positions
