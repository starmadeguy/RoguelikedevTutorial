from typing import Tuple, List


class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int]):
        self.x = x
        self.y = y
        self.char = char
        self.color = color

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy

class InteractableEntity(Entity):
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int], function):
        super().__init__(x, y, char, color)
        self.function = function

    def execute (self, args: List):
        self.function(args)

class Lever(InteractableEntity):
    def __init__(self, x: int, y: int, char: str, color: Tuple[int, int, int], function):
        super().__init__(x, y, char, color, function)