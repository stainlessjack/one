import random

class Character:
    def __init__(self, name='Nobody', trait_values={'Physical': 0, 'Mental': 0, 'Social': 0}, starting_moves=[]):
        self.name = name
        self.trait_values = trait_values
        self.energy_pool = 6
        self.starting_moves = starting_moves

    def engage(self, opportunity):
        # Engage a character with an opportunity
        pass

    def reset_energy(self):
        # Reset energy at the end of the day
        self.energy_pool = 6

    @classmethod
    def generate_random_character(cls):
        # Generate a random character
        # 1. generate a random name using a set of syllables
        syllables = ["ka", "zu", "mi", "ra", "shi", "ta", "na", "mo", "ki", "sa", "ri", "no", "ha", "yo", "ma", "ne", "ko", "se", "lu", "pa"]
        number_of_names = random.randint(1, 3)
        for i in range(number_of_names):
            number_of_syllables = random.randint(1, 4)
            name = ''.join(random.choice(syllables) for _ in range(number_of_syllables)).capitalize()

        # 2. give each trait a 1, then add 1 to a random trait 6 times
        trait_values = {'Physical': 1, 'Mental': 1, 'Social': 1}
        for i in range(6):
            trait_values[random.choice(['Physical', 'Mental', 'Social'])] += 1

        # 3. select 3 moves from the vanilla move list based on the trait values
        import json

        with open('data/vanilla_moves.json', 'r') as file:
            moves = json.load(file)

        selected_moves = []
        for trait, value in trait_values.items():
            # Find the move with the highest power for the given trait value
            best_move = max(
                (move for move in moves if move['power'].get(trait.lower(), 0) <= value),
                key=lambda move: move['power'].get(trait.lower(), 0),
                default=None
            )
            if best_move:
                selected_moves.append(best_move)

        # 4. return the character
        return cls(name, trait_values, selected_moves)