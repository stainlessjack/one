from zone import Zone

class Owner:
    def __init__(self, name, owner_type, is_human):
        self.name = name
        self.owner_type = owner_type
        self.is_human = is_human
        self.zones = []

class System(Owner):
    @classmethod
    def setup_system(cls):
        system_owner = cls(name="System", owner_type="system", is_human=False)
        # Setup the system's zones
        system_owner.zones.append(Zone.create_zone("Day Deck", "card"))
        system_owner.zones.append(Zone.create_zone("World Opportunities", "card"))
        system_owner.zones.append(Zone.create_zone("Graveyard", "element"))
        system_owner.zones.append(Zone.create_zone("Market Deck", "card"))
        system_owner.zones.append(Zone.create_zone("Market Opportunities", "card"))
        system_owner.zones.append(Zone.create_zone("Workyard Deck", "card"))
        system_owner.zones.append(Zone.create_zone("Workyard Opportunities", "card"))
        return system_owner

class Player(Owner):
    @classmethod
    def setup_player(cls, name, is_human):
        player_owner = cls(name=name, owner_type="player", is_human=is_human)
        # Setup the player's zones
        player_owner.zones.append(Zone.create_zone("Characters", "pawn"))
        player_owner.zones.append(Zone.create_zone("Hand", "card"))
        player_owner.zones.append(Zone.create_zone("Opportunities", "card"))
        player_owner.zones.append(Zone.create_zone("Resources", "card"))
        player_owner.zones.append(Zone.create_zone("Gold", "token"))
        player_owner.zones.append(Zone.create_zone("Prestige", "token"))
        return player_owner