#map file
from dataclasses import dataclass

@dataclass
class pirate_map
    name = "Bermuda Triangle"

    def __init__(self, map_name):
        self.name = map_name

class pirate_map_cell:
    x: int
    y: int
    terrain: str

# Create a 10x10 map with default terrain "Water"
map = [[pirate_map_cell(x, y, "Water") for x in range(10)] for y in range(10)]

# Accessing a cell's terrain type (e.g., row 2, column 3)
terrain_type = map[2][3].terrain
print(f"Terrain at (2, 3): {terrain_type}")
