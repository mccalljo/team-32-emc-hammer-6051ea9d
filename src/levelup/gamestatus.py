class GameStatus:
    DEFAULT_NAME="DEFAULTNAME"
    running: bool = False
    character_name: str = DEFAULT_NAME
    # NOTE - Game status will have this as a tuple. The Position should probably be in a class
    current_position: tuple = (-100,-100)
    move_count: int = 0
   
   