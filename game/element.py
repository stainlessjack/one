import random
import utils

class Element:
    name = ""
    type = ""

class Token(Element):
    amount = 0

    @classmethod
    def setup_token(cls, name, amount):
        cls.name = name
        cls.type = "token"
        cls.amount = amount
        return cls

class Pawn(Element):
    traits = {"physical": 0, "mental": 0, "social": 0}
    energy = 0
    moves = []

    @classmethod
    def setup_pawn(cls):
        cls.name = utils.generate_character_name()
        cls.type = "pawn"
        
        
        # Give each trait a 1, then add 1 to a random trait 6 times
        cls.traits = {'physical': 1, 'mental': 1, 'social': 1}
        for i in range(6):
            cls.traits[random.choice(['physical', 'mental', 'social'])] += 1

        # 3. select 3 moves from the vanilla move list based on the trait values
        import json

        with open('data/starting_moves.json', 'r') as file:
            moves = json.load(file)

        selected_moves = []
        for trait, value in cls.traits.items():
            # Find the move with the highest power for the given trait value
            best_move = max(
                (move for move in moves if move['power'].get(trait.lower(), 0) <= value),
                key=lambda move: move['power'].get(trait.lower(), 0),
                default=None
            )
            if best_move:
                selected_moves.append(best_move)

        cls.moves = selected_moves
        return cls
    
class Card(Element):
    subtype = ""
    power = 0
    cost = 0
    description = ""

    @classmethod
    def setup_card(cls):
        return cls
