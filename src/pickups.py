
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
        super().__init__("key", 100, "K")
class Chest(Item):
    def __init__(self):
        super().__init__("chest",100,"C")

pickups = [
    Item("carrot", 20, "C"),
    Item("apple",20,"A"),
    Item("strawberry",20,"S"),
    Item("cherry", 20, "CH"),
    Item("watermelon",20, "W"),
    Item("radish", 10,"R"),
    Item("cucumber",10,"CU"),
    Item("meatball",30,"M"),
    Item ("spade", 0 , "S") # spade för att gräva
 ]


def randomize(grid):
    items = pickups + [Trap() for _ in range(3)] + [Key(), Chest()]
    for item in items:
        while True:
            # slumpa en position tills vi hittar en som är ledig
            x = grid.get_random_x()
            y = grid.get_random_y()
            if grid.is_empty(x, y):
                grid.set(x, y, item)
                break  # avbryt while-loopen, fortsätt med nästa varv i for-loopen
    return len(items) - 3 # exkluderar fällor
