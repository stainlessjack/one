from owner import Owner
import utils

class GameFlow:
    owners = []
    current_day = 0

    @classmethod
    def setup_game(cls):
        # Setup the System Owner
        print("Welcome to Zero Game!")
        system_owner = Owner.setup_system()
        cls.owners.append(system_owner)
        
        # Setup the Player Owner (Human)
        player_name = input("Enter your name: ")
        player_owner = Owner.setup_player(player_name, is_human=True)
        cls.owners.append(player_owner)

        # Setup the Player Owner(s) (AI)
        num_ai_players = int(input("How many opponents would you like to play against? "))
        for i in range(num_ai_players):
            player_name = utils.generate_player_name()
            ai_owner = Owner.setup_player(player_name, is_human=False)
            cls.owners.append(ai_owner)
        
        return cls


    def start_game(self):
        # Start by listing the players in the game
        print(f"Good luck {self.owners[1].name}! Your opponents in this game include:")
        for owner in self.owners[2:]:
            print(owner.name)
        
        while True:
            self.day_loop()

    def day_loop(self):
        pass