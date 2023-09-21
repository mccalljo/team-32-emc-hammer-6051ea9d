import string

class Character:
    name = ""

    def __init__(self, character_name):
        self.name = character_name

    def getName(self) -> string:
        return self.name
    
    def move(self,direction: string):
        
        pass
