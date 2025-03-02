import random

class Item:
    """Representerar saker man kan plocka upp."""
    def __init__(self, name, value=10, symbol="?"):
        self.name = name
        self.value = value
        self.symbol = symbol

    def __str__(self):
        return self.symbol

# trap class för att slumpa ut fällor
class Trap(Item):
    def __init__(self):
        super().__init__("trap", -10, "T")
class Key (Item):
    def __init__(self):
        super().__init__("key", 0, "K")
class Chest(Item):
    def __init__(self):
        super().__init__("chest",100,"C")

pickups = [
    Item("carrot", 20, "CA"),
    Item("apple", 20, "A"),
    Item("strawberry", 20, "ST"),
    Item("cherry", 20, "CH"),
    Item("watermelon", 20, "W"),
    Item("radish", 10, "R"),
    Item("cucumber", 10, "CU"),
    Item("meatball", 30, "M"),
    Item("spade", 0, "S")  # spade för att gräva
]

def randomize(grid, num_keys=1):
    if not all(hasattr(grid, attr) for attr in ["get_random_x", "get_random_y", "is_empty", "set"]):
        raise AttributeError("Grid object lacks required methods.")

    items = pickups.copy()

    for _ in range (num_keys):
        items.append(Key())
        items.append(Chest())

    traps = [Trap() for _ in range(3)]
    items.extend(traps)

    for item in items:
        while True:
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break
    return len(items) - len(traps)  # Exkludera fällor
