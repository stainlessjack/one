from resources import Token, Resource
from character import Character

class Player:
    def __init__(self, name, is_human=False):
        self.name = name
        self.hand = []  # List of Resource instances
        self.tokens = {
            'Gold': 0,
            'Prestige': 0
        }
        self.characters = []  # List of Character instances
        self.opportunities = []  # Opportunities currently engaged
        self.starting_character_count = 3
        self.is_human = is_human

    def select_opportunity(self, available_opportunities):
        # Allow the player to select an opportunity to engage
        pass

    def engage_opportunity(self, opportunity):
        # Engage a selected opportunity
        pass

    def resolve_opportunity(self, opportunity):
        # Resolve an opportunity the player engaged in
        pass


    def setup_characters(self):
        # Initialize 3 random characters for the player
        for i in range(self.starting_character_count):
            character = Character.generate_random_character()
            self.characters.append(character)

