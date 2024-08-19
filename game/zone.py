import random
from element import Element

class Zone:
    name = ""
    type = ""
    elements = []

    # Assumes all elements are cards
    @classmethod
    def setup_deck(cls, name, _elements=[], shuffle=True):
        cls.name = name
        cls.type = "deck"
        for element in _elements:
            _ = Element.setup_card(element)
            cls.elements.append(_)
        
        if shuffle:
            random.shuffle(cls.elements)
        return cls
    
    # Currently only supports card and pawn play areas
    @classmethod
    def setup_play_area(cls, name, _elements=[]):
        cls.name = name
        cls.type = "play_area"
        for element in _elements:
            if element.type == "card":
                _ = Element.setup_card(element)
            else:
                _ = Element.setup_pawn()
            cls.elements.append(_)
        return cls

    @classmethod
    def setup_discard(cls, name):
        cls.name = name
        cls.type = "discard"
        return cls


    # Assumes all elements are cards
    @classmethod
    def setup_hand(cls, name, _elements=[]):
        cls.name = name
        cls.type = "hand"
        for element in _elements:
            _ = Element.setup_card(element)
            cls.elements.append(_)
        return cls

    # Assumes all elements are tokens
    @classmethod
    def setup_pool(cls, name, token_type, starting_amount=0):
        cls.name = name
        cls.type = "pool"
        cls.elements = [Element.setup_token(token_type, starting_amount)]
        return cls