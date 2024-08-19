import random

def generate_player_name():
        # Generate a random name using a set of syllables
        syllables = ["ka", "zu", "mi", "ra", "shi", "ta", "na", "mo", "ki", "sa", "ri", "no", "ha", "yo", "ma", "ne", "ko", "se", "lu", "pa"]
        number_of_names = random.randint(1, 3)
        name = ''.join(
            ''.join(random.choice(syllables) for _ in range(random.randint(1, 4))).capitalize()
            for _ in range(number_of_names)
        )
        return name