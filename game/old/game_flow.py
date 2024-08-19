from owner import System, Player
import utils

class GameFlow:
    def __init__(self):
        self.owners = []
        self.current_day = 0

    def start_game(self):
        self.setup_owners()
        self.start_game()

    def setup_owners(self):
        # Initialize owners
        # Add system owner
        system_owner = System.setup_system()
        self.owners.append(system_owner)

        # Add player owner
        print("Welcome to Zero Game!")
        player_name = input("Enter your name: ")
        player_owner = Player.setup_player(name=player_name, is_human=True)
        self.owners.append(player_owner)
        
        # Add AI Opponents
        print(f"Welcome, {player_name}! How many Opponents would you like to play against? (1-3)")
        num_opponents = int(input())
        for i in range(num_opponents):
            opponent_name = utils.generate_name()
            opponent_owner = Player.setup_player(name=opponent_name, is_human=False)
            self.owners.append(opponent_owner)

    def start_of_day(self):
        self.current_day += 1
        print(f"Day {self.current_day} has begun.")
        # Additional start of day logic

    def character_engagement_phase(self):
        # Character engagement logic
        pass

    def tick_clocks(self):
        # Advance clocks and resolve opportunities
        pass

    def end_of_day(self):
        # Wrap up the day and prepare for the next one
        pass