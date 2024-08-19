class Element:
    def __init__(self, name):
        self.name = name

class Token(Element):
    def __init__(self, name, amount):
        super().__init__(name)
        self.amount = amount

class Pawn(Element):
    def __init__(self, name):
        super().__init__(name)

class Card(Element):
    def __init__(self, name):
        super().__init__(name)

class Dice(Element):
    def __init__(self, name, sides):
        super().__init__(name)
        self.sides = sides